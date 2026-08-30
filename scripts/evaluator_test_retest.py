"""Evaluator Test-Retest Reliability Script.

Measures the stability of blind evaluator judgments by re-running the same
evaluator prompt on a random sample of Study 3 outputs and comparing new
scores to the originals.

Reports:
  - Cohen's kappa (linear-weighted)
  - Pearson correlation
  - Exact agreement %
  - 1-off agreement %

Usage:
    # Full run (requires ANTHROPIC_API_KEY environment variable)
    python scripts/evaluator_test_retest.py

    # Dry run (prints what would be sent, no API calls)
    python scripts/evaluator_test_retest.py --dry-run

    # Custom sample size
    python scripts/evaluator_test_retest.py --n-samples 100

    # Use a specific random seed for reproducibility
    python scripts/evaluator_test_retest.py --seed 42

Environment Variables:
    ANTHROPIC_API_KEY - Required for API calls (not needed for --dry-run)
"""

import argparse
import json
import os
import random
import sys
import time
from pathlib import Path

import anthropic
import numpy as np
from scipy import stats
from sklearn.metrics import cohen_kappa_score
from tqdm import tqdm

# Project paths
ROOT = Path(__file__).resolve().parent.parent
S3_DIR = ROOT / "data" / "study3"
EVALUATOR_RESULTS_PATH = S3_DIR / "raw_responses" / "evaluator_results.jsonl"
WORKER_TRIALS_PATH = S3_DIR / "raw_responses" / "worker_trials.jsonl"
OUTPUT_PATH = S3_DIR / "analysis" / "test_retest_results.json"

# Evaluator model
EVALUATOR_MODEL = "claude-sonnet-4-20250514"

# The same blind evaluator prompt used in Phase 2 (phase2_evaluator.py)
EVAL_PROMPT = """\
A user asked someone to complete the following task:
---
{task_prompt}
---
Here is the output that was produced:
---
{output}
---
How well does this output fulfill the task? Rate it on the following scale:

1 - Inadequate: The output does not address the task, or addresses it so incorrectly that it would need to be started over. A user could not build on this.
2 - Incomplete: The output addresses the right task but is missing one or more explicitly requested components. A user would have to add significant content to use this.
3 - Functional: All explicitly requested components are present, but the execution has clear weaknesses in accuracy, clarity, or tone. A user could use this with edits.
4 - Sufficient: All requested components are present and executed competently. A reasonable user would accept this without changes.
5 - Polished: All requested components are present, well-executed, and the output demonstrates thoughtfulness beyond the minimum. Nothing to fix.
6 - Overdone: The output adds unrequested complexity, excessive length, or has drifted from the original ask. A user would need to cut or refocus it.

Respond with ONLY a JSON object:
{{"level": 1-6, "rationale": "one sentence explaining your rating"}}"""


def load_jsonl(path: Path) -> list[dict]:
    """Load a JSONL file into a list of dicts."""
    records = []
    if not path.exists():
        return records
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def parse_evaluator_response(text: str) -> dict | None:
    """Parse evaluator JSON response, handling markdown fences and think tags."""
    import re
    text = text.strip()
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        text = "\n".join(lines)
    try:
        data = json.loads(text)
        if "level" in data:
            level = int(data["level"])
            if 1 <= level <= 6:
                return {"level": level, "rationale": data.get("rationale", "")}
    except (json.JSONDecodeError, ValueError, KeyError):
        pass
    return None


def select_samples(n_samples: int, seed: int) -> list[dict]:
    """Select n random evaluator results that have valid levels and matching worker data."""
    rng = random.Random(seed)

    # Load evaluator results (only those with valid levels)
    eval_results = load_jsonl(EVALUATOR_RESULTS_PATH)
    valid_evals = [r for r in eval_results if r.get("level") is not None]

    if not valid_evals:
        print("ERROR: No valid evaluator results found.")
        sys.exit(1)

    # Load worker trials to get outputs
    worker_trials = load_jsonl(WORKER_TRIALS_PATH)
    worker_map = {t["trial_id"]: t for t in worker_trials if t.get("status") == "success"}

    # Build samples with full context
    samples = []
    for ev in valid_evals:
        wt = worker_map.get(ev["worker_trial_id"])
        if wt is None:
            continue
        turn_idx = ev["turn"] - 1
        if turn_idx < 0 or turn_idx >= len(wt.get("responses", [])):
            continue
        output = wt["responses"][turn_idx]
        # Skip meta-responses (empty or very short)
        if not output or len(output.strip()) < 20:
            continue
        samples.append({
            "eval_id": ev["eval_id"],
            "worker_trial_id": ev["worker_trial_id"],
            "task_prompt": wt["task_prompt"],
            "output": output,
            "original_level": ev["level"],
            "model": ev["model"],
            "domain": ev["domain"],
            "turn": ev["turn"],
        })

    if len(samples) < n_samples:
        print(f"WARNING: Only {len(samples)} valid samples available (requested {n_samples})")
        n_samples = len(samples)

    selected = rng.sample(samples, n_samples)
    return selected


def call_evaluator(client: anthropic.Anthropic, task_prompt: str, output: str) -> dict | None:
    """Call the evaluator model and parse response."""
    prompt = EVAL_PROMPT.format(task_prompt=task_prompt, output=output)

    for attempt in range(2):
        try:
            response = client.messages.create(
                model=EVALUATOR_MODEL,
                max_tokens=512,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            text = response.content[0].text
            parsed = parse_evaluator_response(text)
            if parsed:
                return parsed
            if attempt == 0:
                time.sleep(1)
        except Exception as e:
            if attempt == 0:
                print(f"  API error: {e}, retrying...")
                time.sleep(2)
            else:
                print(f"  API error on retry: {e}")
                return None
    return None


def compute_metrics(original: list[int], retest: list[int]) -> dict:
    """Compute agreement metrics between original and retest scores."""
    original_arr = np.array(original)
    retest_arr = np.array(retest)
    n = len(original)

    # Cohen's kappa (linear weighted for ordinal scale)
    kappa = cohen_kappa_score(original, retest, weights="linear")

    # Pearson correlation
    pearson_r, pearson_p = stats.pearsonr(original_arr, retest_arr)

    # Exact agreement
    exact_match = int(np.sum(original_arr == retest_arr))
    exact_pct = exact_match / n * 100

    # 1-off agreement (within 1 level)
    one_off = int(np.sum(np.abs(original_arr - retest_arr) <= 1))
    one_off_pct = one_off / n * 100

    # Additional descriptive stats
    mean_diff = float(np.mean(retest_arr - original_arr))
    abs_mean_diff = float(np.mean(np.abs(retest_arr - original_arr)))

    return {
        "n": n,
        "cohens_kappa_linear": round(kappa, 4),
        "pearson_r": round(pearson_r, 4),
        "pearson_p": pearson_p,
        "exact_agreement_n": exact_match,
        "exact_agreement_pct": round(exact_pct, 2),
        "one_off_agreement_n": one_off,
        "one_off_agreement_pct": round(one_off_pct, 2),
        "mean_difference": round(mean_diff, 4),
        "mean_absolute_difference": round(abs_mean_diff, 4),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Test-retest reliability of the blind evaluator (Study 3)"
    )
    parser.add_argument("--n-samples", type=int, default=50,
                        help="Number of random samples to re-evaluate (default: 50)")
    parser.add_argument("--seed", type=int, default=2024,
                        help="Random seed for sample selection (default: 2024)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would be sent without calling the API")
    args = parser.parse_args()

    print(f"Evaluator Test-Retest Reliability")
    print(f"  Model: {EVALUATOR_MODEL}")
    print(f"  Samples: {args.n_samples}")
    print(f"  Seed: {args.seed}")
    print(f"  Dry run: {args.dry_run}")
    print()

    # Select samples
    samples = select_samples(args.n_samples, args.seed)
    print(f"Selected {len(samples)} samples for re-evaluation")

    if args.dry_run:
        print("\n--- DRY RUN MODE ---")
        for i, s in enumerate(samples[:3], 1):
            prompt = EVAL_PROMPT.format(task_prompt=s["task_prompt"], output=s["output"])
            print(f"\n[Sample {i}] eval_id={s['eval_id']}")
            print(f"  Model: {s['model']}, Domain: {s['domain']}, Turn: {s['turn']}")
            print(f"  Original level: {s['original_level']}")
            print(f"  Prompt length: {len(prompt)} chars")
            print(f"  First 200 chars of prompt:\n    {prompt[:200]}...")
        print(f"\n... and {len(samples) - 3} more samples")
        print("\nNo API calls made. Remove --dry-run to execute.")
        return

    # Initialize client
    client = anthropic.Anthropic()

    # Run re-evaluations
    original_levels = []
    retest_levels = []
    detailed_results = []

    print("\nRunning re-evaluations...")
    for sample in tqdm(samples, desc="Evaluating"):
        result = call_evaluator(client, sample["task_prompt"], sample["output"])

        if result is None:
            print(f"  SKIP: {sample['eval_id']} (parse failure)")
            continue

        original_levels.append(sample["original_level"])
        retest_levels.append(result["level"])
        detailed_results.append({
            "eval_id": sample["eval_id"],
            "model": sample["model"],
            "domain": sample["domain"],
            "turn": sample["turn"],
            "original_level": sample["original_level"],
            "retest_level": result["level"],
            "retest_rationale": result["rationale"],
            "difference": result["level"] - sample["original_level"],
        })

        # Rate limit: 1 request per second
        time.sleep(1.0)

    if len(original_levels) < 5:
        print("ERROR: Too few successful re-evaluations to compute metrics.")
        sys.exit(1)

    # Compute metrics
    metrics = compute_metrics(original_levels, retest_levels)

    # Print results
    print(f"\n{'='*60}")
    print(f"TEST-RETEST RESULTS (n={metrics['n']})")
    print(f"{'='*60}")
    print(f"  Cohen's kappa (linear):   {metrics['cohens_kappa_linear']:.4f}")
    print(f"  Pearson r:                {metrics['pearson_r']:.4f} (p={metrics['pearson_p']:.2e})")
    print(f"  Exact agreement:          {metrics['exact_agreement_n']}/{metrics['n']} ({metrics['exact_agreement_pct']:.1f}%)")
    print(f"  1-off agreement:          {metrics['one_off_agreement_n']}/{metrics['n']} ({metrics['one_off_agreement_pct']:.1f}%)")
    print(f"  Mean difference (re-orig):{metrics['mean_difference']:+.4f}")
    print(f"  Mean |difference|:        {metrics['mean_absolute_difference']:.4f}")
    print(f"{'='*60}")

    # Save results
    output_data = {
        "evaluator_model": EVALUATOR_MODEL,
        "n_samples_requested": args.n_samples,
        "n_samples_evaluated": metrics["n"],
        "seed": args.seed,
        "metrics": metrics,
        "detailed_results": detailed_results,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output_data, f, indent=2)
    print(f"\nResults saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
