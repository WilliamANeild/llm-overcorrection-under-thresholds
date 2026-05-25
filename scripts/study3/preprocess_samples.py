"""Preprocess annotation samples: classify response types and strip preambles.

Uses Claude Sonnet to classify each sample as one of:
  - pure_content:     Model just writes the deliverable
  - preamble_content: Preamble like "Here's a revised version:" then content
  - hedged_meta:      Hedges/offers to revise without producing content
  - pure_meta:        Just commentary, no content at all

Preamble+content samples have preambles stripped. Meta samples are removed
from the annotation queue. Outputs a clean samples.json for the annotator UI
and a classification report.

Usage:
    python -m scripts.study3.preprocess_samples [--dry-run]
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from dotenv import load_dotenv

load_dotenv()

SAMPLES_PATH = (
    Path(__file__).resolve().parent.parent.parent
    / "annotator-ui"
    / "public"
    / "samples.json"
)
REPORT_PATH = (
    Path(__file__).resolve().parent.parent.parent
    / "data"
    / "study3"
    / "raw_responses"
    / "sample_classifications.json"
)

CLASSIFICATION_PROMPT = """\
You are classifying AI-generated responses for a research study.

Given a TASK PROMPT and the MODEL OUTPUT, classify the output into exactly one category:

1. "pure_content" - The model directly produces the requested deliverable (summary, email, code, analysis, etc.) with no preamble or meta-commentary.

2. "preamble_content" - The model starts with a preamble (e.g. "Certainly! Here's a revised version:", "Here's a concise summary:", "I'd like to revise it to...") and then produces the actual deliverable. The preamble is conversational wrapper around real content.

3. "hedged_meta" - The model comments on the task, offers to revise, asks for preferences, or hedges without actually producing the requested deliverable. Examples: "The current version is solid, but I'd be happy to revise if you have feedback...", "I'm ready to finalize or revise based on your preferences. Would you like to: 1. Keep it as-is 2. Make it more data-driven..."

4. "pure_meta" - The model only provides brief commentary with no content at all. Examples: "This looks great. Ready to use.", "This version looks solid and meets all the requirements."

IMPORTANT RULES:
- If the response contains ANY substantial deliverable content (even after a long preamble), classify as "preamble_content" or "pure_content".
- "hedged_meta" responses may contain short illustrative snippets or option menus, but they do NOT constitute a full deliverable.
- When in doubt between hedged_meta and preamble_content, ask: "Could a user copy-paste a usable deliverable from this response?" If yes -> preamble_content. If no -> hedged_meta.

For "preamble_content" responses, also extract the content portion (everything after the preamble). Find the natural boundary where the preamble ends and the actual deliverable begins.

Respond with a JSON object:
{
  "classification": "pure_content" | "preamble_content" | "hedged_meta" | "pure_meta",
  "reasoning": "One sentence explaining your classification",
  "cleaned_output": "For preamble_content only: the output with preamble removed. For all other types: null"
}

TASK PROMPT:
%s

MODEL OUTPUT:
%s"""


def classify_sample(client, sample: dict) -> dict:
    """Classify a single sample using Claude Sonnet."""
    prompt = CLASSIFICATION_PROMPT % (sample["task_prompt"], sample["output"])

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text.strip()

    # Extract JSON from response (handle markdown code blocks)
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()
    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()

    # Try direct parse first; if it fails, find the JSON object boundary
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Find outermost { ... } in the text
    start = text.find("{")
    if start == -1:
        raise ValueError(f"No JSON object found in response: {text[:200]}")
    depth = 0
    in_string = False
    escape_next = False
    end = start
    for i in range(start, len(text)):
        c = text[i]
        if escape_next:
            escape_next = False
            continue
        if c == "\\":
            escape_next = True
            continue
        if c == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                end = i
                break

    return json.loads(text[start : end + 1])


def main():
    parser = argparse.ArgumentParser(description="Preprocess samples for annotation")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Classify but don't overwrite samples.json",
    )
    args = parser.parse_args()

    import anthropic

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    with open(SAMPLES_PATH) as f:
        samples = json.load(f)

    print(f"Classifying {len(samples)} samples with Claude Sonnet...")
    print()

    classifications = []
    for i, sample in enumerate(samples):
        try:
            result = classify_sample(client, sample)
        except Exception as e:
            print(f"  [{i+1}/{len(samples)}] {sample['sample_id']}: ERROR - {e}")
            # Default to keeping the sample on error
            result = {
                "classification": "pure_content",
                "reasoning": f"Classification failed: {e}",
                "cleaned_output": None,
            }

        classifications.append(
            {
                "sample_id": sample["sample_id"],
                "domain": sample["domain"],
                "classification": result["classification"],
                "reasoning": result["reasoning"],
                "cleaned_output": result.get("cleaned_output"),
            }
        )

        label = result["classification"]
        symbol = {
            "pure_content": ".",
            "preamble_content": "P",
            "hedged_meta": "H",
            "pure_meta": "M",
        }.get(label, "?")
        print(
            f"  [{i+1}/{len(samples)}] {sample['sample_id']}: {symbol} {label}",
            end="",
        )
        if label in ("hedged_meta", "pure_meta"):
            print(f"  -- {result['reasoning']}")
        else:
            print()

        # Rate limit: ~1 req/sec to be safe
        if i < len(samples) - 1:
            time.sleep(0.5)

    # Summary
    counts = {}
    for c in classifications:
        counts[c["classification"]] = counts.get(c["classification"], 0) + 1

    print()
    print("Classification summary:")
    for cls, count in sorted(counts.items()):
        pct = count / len(samples) * 100
        print(f"  {cls}: {count} ({pct:.1f}%)")

    meta_ids = {
        c["sample_id"]
        for c in classifications
        if c["classification"] in ("hedged_meta", "pure_meta")
    }
    print(f"\nSamples to remove (meta): {len(meta_ids)}")
    print(
        f"Samples to keep: {len(samples) - len(meta_ids)}"
    )

    # Save classification report
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_PATH, "w") as f:
        json.dump(
            {
                "total_samples": len(samples),
                "counts": counts,
                "classifications": classifications,
            },
            f,
            indent=2,
        )
    print(f"\nClassification report saved to {REPORT_PATH}")

    if args.dry_run:
        print("\n--dry-run: not modifying samples.json")
        return

    # Build clean samples
    clean_samples = []
    preamble_lookup = {
        c["sample_id"]: c["cleaned_output"]
        for c in classifications
        if c["classification"] == "preamble_content" and c["cleaned_output"]
    }

    for sample in samples:
        if sample["sample_id"] in meta_ids:
            continue  # Remove meta samples

        clean_sample = {**sample}
        if sample["sample_id"] in preamble_lookup:
            clean_sample["output"] = preamble_lookup[sample["sample_id"]]

        clean_samples.append(clean_sample)

    # Write clean samples
    with open(SAMPLES_PATH, "w") as f:
        json.dump(clean_samples, f, indent=2)
    print(f"\nWrote {len(clean_samples)} clean samples to {SAMPLES_PATH}")

    # Update assignments to remove meta sample IDs
    assignments_path = SAMPLES_PATH.parent / "assignments.json"
    if assignments_path.exists():
        with open(assignments_path) as f:
            assignments = json.load(f)

        clean_assignments = {}
        for rater, sample_ids in assignments.items():
            clean_assignments[rater] = [
                sid for sid in sample_ids if sid not in meta_ids
            ]

        with open(assignments_path, "w") as f:
            json.dump(clean_assignments, f, indent=2)

        print(f"Updated assignments.json (removed {len(meta_ids)} meta sample IDs)")
        for rater, sids in clean_assignments.items():
            print(f"  {rater}: {len(sids)} samples")

    print("\nDone. Re-deploy with: cd annotator-ui && npx vercel --prod")


if __name__ == "__main__":
    main()
