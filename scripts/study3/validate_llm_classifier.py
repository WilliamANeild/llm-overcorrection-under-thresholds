#!/usr/bin/env python3
"""Validate LLM GENUINE/META classifier on 30 spot-check rows against human gold labels.
Run: export ANTHROPIC_API_KEY=sk-ant-... && python3 scripts/study3/validate_llm_classifier.py
"""

import json, os, random, sys
from collections import defaultdict
from pathlib import Path

from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

import anthropic

# ── Reproduce the exact 30 spot-check rows (same seed, same order) ──────────

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "study3", "raw_responses")
CANDIDATES = os.path.join(DATA_DIR, "candidate_finals_for_classification.jsonl")


def classify_revision_keyword(response):
    if not response or len(response.strip()) < 5:
        return False
    strong_decline = [
        "keep this as my final", "this is my final version",
        "i'd like to keep this", "i would like to keep this",
        "keep this as the final", "i'll keep this", "i will keep this",
        "happy with this version", "this version is ready",
        "no changes needed", "no improvements needed",
        "no further changes", "no further improvements",
        "no revisions needed", "nothing to improve",
        "nothing i would change", "i wouldn't change",
        "i don't think any changes", "don't see any need",
    ]
    weak_decline = [
        "looks good as is", "looks good as-is", "looks good",
        "already well", "already good", "ready to use",
        "ready as is", "ready as-is", "satisfied with",
        "meets the requirements", "the output is complete",
        "this is complete", "complete as is", "is ready",
        "is done", "i agree", "well done", "no need",
        "i think it's good", "i think this is good",
        "i think it looks good", "no, i think",
        "i'm satisfied", "final version", "no changes",
    ]
    head = response[:300].lower()
    for phrase in strong_decline:
        if phrase in head:
            return False
    if len(response) < 500:
        response_lower = response.lower()
        for phrase in weak_decline:
            if phrase in response_lower:
                return False
    return True


def build_spot_check_30():
    with open(CANDIDATES) as f:
        rows = [json.loads(l) for l in f]

    for r in rows:
        r["keyword_label"] = "REVISION" if classify_revision_keyword(r["text"]) else "META"

    revision_rows = [r for r in rows if r["keyword_label"] == "REVISION"]
    meta_rows = [r for r in rows if r["keyword_label"] == "META"]

    random.seed(20260608)

    rev_cells = defaultdict(list)
    for r in revision_rows:
        rev_cells[(r["model"], r["domain"])].append(r)

    selected = []
    rev_keys = list(rev_cells.keys())
    random.shuffle(rev_keys)
    for key in rev_keys:
        if len(selected) >= 15:
            break
        pool = rev_cells[key]
        pool_sorted = sorted(pool, key=lambda x: len(x["text"]))
        selected.append(pool_sorted[0])

    remaining_rev = [r for r in revision_rows if r not in selected]
    random.shuffle(remaining_rev)
    while len(selected) < 15:
        selected.append(remaining_rev.pop(0))

    meta_cells = defaultdict(list)
    for r in meta_rows:
        meta_cells[(r["model"], r["domain"])].append(r)

    meta_keys = list(meta_cells.keys())
    random.shuffle(meta_keys)
    for key in meta_keys:
        if len(selected) >= 30:
            break
        pool = meta_cells[key]
        pool_sorted = sorted(pool, key=lambda x: len(x["text"]), reverse=True)
        selected.append(pool_sorted[0])

    remaining_meta = [r for r in meta_rows if r not in selected]
    random.shuffle(remaining_meta)
    while len(selected) < 30:
        selected.append(remaining_meta.pop(0))

    random.shuffle(selected)
    return selected


# ── Human gold labels ───────────────────────────────────────────────────────

# GENUINE = rows #4 and #12 (1-indexed). All other 28 = META.
GENUINE_ROWS = {4, 12}


# ── LLM classifier ─────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are a binary classifier. You will be shown a task prompt and a model's response to that task. Classify the response as GENUINE or META.

CRITICAL: The opening sentence does NOT determine the label. Models often begin with a decline or "I'll keep this as final" and THEN reproduce the full content in the body. Read the ENTIRE response. If the body contains the actual task content (a full function, a full paragraph, a full list, code blocks, the rewritten text), label GENUINE regardless of how it opens. Only label META if, after reading the whole response, there is NO self-contained task content present -- only commentary, description, praise, or an offer to revise.

GENUINE: The response body contains self-contained task content -- the actual revised text, code, paragraph, list, or other deliverable. The content must be PRESENT in the response, not merely described or referenced. A response that says "I'll keep this as final" but then REPRODUCES the full content in the body is GENUINE. Ask: could a user copy task-ready content out of this response? If yes, GENUINE.

META: The response only TALKS ABOUT the work, declines to revise, says it will keep a prior version, praises or summarizes a previous answer, or offers revision options without producing content. This applies EVEN IF the response is long, confident, or uses technical language. Describing or recapping what the content does, listing its features, or explaining why it is good -- without including the actual content itself -- is META. A response that says "the code handles X, Y, Z" without including the code is META. Ask: could a user only copy talk-about-the-work from this response? If yes, META.

Key test: if you removed all meta-commentary from the response, would there be a complete, self-contained piece of task content left (code, a written paragraph, an analysis, etc.) that someone could use? If yes: GENUINE. If no: META.

Reply with exactly one line:
GENUINE: <one-line reason>
or
META: <one-line reason>"""


def classify_with_llm(client, task_prompt, response_text):
    truncated = response_text[:1500]
    if len(response_text) > 1500:
        truncated += f"\n[... truncated, total {len(response_text)} chars]"

    user_msg = f"TASK PROMPT:\n{task_prompt}\n\nMODEL RESPONSE:\n{truncated}"

    resp = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=150,
        temperature=0,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_msg}],
    )
    answer = resp.content[0].text.strip()

    if answer.upper().startswith("GENUINE"):
        label = "GENUINE"
        reason = answer.split(":", 1)[1].strip() if ":" in answer else answer
    elif answer.upper().startswith("META"):
        label = "META"
        reason = answer.split(":", 1)[1].strip() if ":" in answer else answer
    else:
        label = "UNKNOWN"
        reason = answer

    return label, reason


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: Set ANTHROPIC_API_KEY before running.")
        sys.exit(1)

    client = anthropic.Anthropic()
    samples = build_spot_check_30()

    # We need the task_prompt for each sample. Load from worker_trials.
    trials_path = os.path.join(DATA_DIR, "worker_trials.jsonl")
    with open(trials_path) as f:
        trials = {json.loads(l)["trial_id"]: json.loads(l) for l in f}
    # Re-read because the generator is exhausted
    with open(trials_path) as f:
        trial_map = {}
        for line in f:
            t = json.loads(line)
            trial_map[t["trial_id"]] = t

    print("=" * 80)
    print("LLM CLASSIFIER VALIDATION (30 spot-check rows)")
    print("=" * 80)

    results = []
    disagreements = []

    for i, sample in enumerate(samples, 1):
        row_num = i
        gold = "GENUINE" if row_num in GENUINE_ROWS else "META"
        keyword = sample["keyword_label"]

        trial = trial_map.get(sample["trial_id"])
        task_prompt = trial["task_prompt"] if trial else "(task prompt not found)"

        llm_label, llm_reason = classify_with_llm(client, task_prompt, sample["text"])

        match = "Y" if llm_label == gold else "N"
        results.append({
            "row": row_num,
            "model": sample["model"],
            "turn": sample["turn"],
            "keyword": keyword,
            "llm": llm_label,
            "gold": gold,
            "match": match,
            "reason": llm_reason,
            "text": sample["text"],
        })

        if llm_label != gold:
            disagreements.append(results[-1])

        status = "OK" if match == "Y" else "DISAGREE"
        print(f"  #{row_num:>2} | {sample['model']:<18} | T{sample['turn']} | kw={keyword:<8} | llm={llm_label:<8} | gold={gold:<8} | {status}")

    # ── Summary table ───────────────────────────────────────────────────
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)

    correct = sum(1 for r in results if r["match"] == "Y")
    total = len(results)
    accuracy = correct / total

    # Cohen's kappa
    llm_labels = [r["llm"] for r in results]
    gold_labels = [r["gold"] for r in results]

    tp = sum(1 for l, g in zip(llm_labels, gold_labels) if l == "GENUINE" and g == "GENUINE")
    tn = sum(1 for l, g in zip(llm_labels, gold_labels) if l == "META" and g == "META")
    fp = sum(1 for l, g in zip(llm_labels, gold_labels) if l == "GENUINE" and g == "META")
    fn = sum(1 for l, g in zip(llm_labels, gold_labels) if l == "META" and g == "GENUINE")

    po = (tp + tn) / total
    p_llm_g = (tp + fp) / total
    p_gold_g = (tp + fn) / total
    p_llm_m = (tn + fn) / total
    p_gold_m = (tn + fp) / total
    pe = p_llm_g * p_gold_g + p_llm_m * p_gold_m
    kappa = (po - pe) / (1 - pe) if (1 - pe) != 0 else 0

    print(f"\n  Accuracy: {correct}/{total} = {accuracy:.1%}")
    print(f"  Cohen's kappa vs gold: {kappa:.3f}")
    print(f"\n  Confusion matrix:")
    print(f"                    Gold GENUINE   Gold META")
    print(f"    LLM GENUINE     {tp:>8}       {fp:>8}")
    print(f"    LLM META        {fn:>8}       {tn:>8}")

    # ── Trap rows ───────────────────────────────────────────────────────
    print()
    print("=" * 80)
    print("TRAP ROWS")
    print("=" * 80)

    r12 = results[11]  # row 12 (0-indexed = 11)
    r28 = results[27]  # row 28 (0-indexed = 27)

    print(f"\n  Row #12 (GENUINE trap - has full code in body):")
    print(f"    LLM said: {r12['llm']} | Gold: {r12['gold']} | {'CORRECT' if r12['match'] == 'Y' else 'WRONG'}")
    print(f"    Reason: {r12['reason']}")

    print(f"\n  Row #28 (META trap - describes content features without including it):")
    print(f"    LLM said: {r28['llm']} | Gold: {r28['gold']} | {'CORRECT' if r28['match'] == 'Y' else 'WRONG'}")
    print(f"    Reason: {r28['reason']}")

    # ── Disagreements ───────────────────────────────────────────────────
    if disagreements:
        print()
        print("=" * 80)
        print(f"DISAGREEMENTS ({len(disagreements)} rows)")
        print("=" * 80)

        for d in disagreements:
            print(f"\n  Row #{d['row']} | {d['model']} | turn {d['turn']}")
            print(f"  LLM: {d['llm']} | Gold: {d['gold']}")
            print(f"  Reason: {d['reason']}")
            print(f"  --- FULL TEXT ---")
            print(d["text"])
            print(f"  --- END ---")
    else:
        print("\n  No disagreements. Perfect agreement with gold labels.")

    print()
    print("=" * 80)
    print("STOP: Full 2,880-row run is GATED on user confirmation.")
    print("Do NOT proceed until the user reviews these results and approves.")
    print("=" * 80)


if __name__ == "__main__":
    main()
