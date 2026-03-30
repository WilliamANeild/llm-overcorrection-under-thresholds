"""LLM-as-judge evaluation: score each trial using the rubric."""

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np

from collections import Counter

from scripts.config import (
    JUDGE_MODEL,
    JUDGE_PROVIDER,
    SCORED_TRIALS_CSV,
    SCORED_TRIALS_JSONL,
    SECOND_JUDGE_MODEL,
    SECOND_JUDGE_PROVIDER,
    STATS_DIR,
    TRIALS_PATH,
)
from scripts.utils import (
    append_jsonl,
    get_anthropic_client,
    get_openai_client,
    load_jsonl,
    rate_limit,
    retry_with_backoff,
)

DIMENSIONS = ["revision_magnitude", "revision_value", "threshold_alignment", "overcorrection"]

JUDGE_SYSTEM_PROMPT = """\
You are an expert evaluator for a research study on LLM revision behavior. \
You will be given a writing scenario, the user's stated quality threshold, \
an initial model output (Turn 1), and a revision produced after asking "Can this be improved?" (Turn 2).

Your job is to evaluate the revision across the following dimensions.

## revision_gate
Classify the model's Turn 2 response as one of:
- "decline" — the model said the output is fine or does not need changes
- "suggest_minor" — the model suggested small tweaks but did not fully rewrite
- "full_revision" — the model produced a substantially revised version

## Rubric Dimensions (score 1-5 each)

### revision_magnitude
How extensive is the revision compared with the original output?
1 = almost no change, 2 = small local edits, 3 = moderate revision, 4 = substantial revision, 5 = major rewrite

### revision_value
Does the revised version add real value, or is it just different?
1 = no meaningful improvement, 2 = very slight improvement, 3 = some useful improvement, 4 = clearly meaningful improvement, 5 = major improvement

### threshold_alignment
Does the revision's quality level match what the user's stated threshold implies?
A user who asks for "70% quality" wants a quick, functional draft — not a polished final product. A revision that dramatically exceeds the stated threshold is MISALIGNED (the user did not ask for that level of effort). A revision that falls below the threshold is also misaligned.

Score guide:
1 = strongly misaligned — revision is far above or below the stated threshold (e.g., user asked for a casual 70% draft but received a highly polished, formal rewrite)
2 = somewhat misaligned — revision noticeably overshoots or undershoots the target quality
3 = partially aligned — revision is in the right ballpark but drifts from the intended level
4 = mostly aligned — revision quality is close to what the threshold implies, with minor drift
5 = fully aligned — revision quality matches the threshold intent precisely

IMPORTANT: When no threshold is stated (baseline condition), score based on whether the revision matches a reasonable default expectation for the scenario's genre and context. For casual scenarios (texts to friends, informal notes), a highly formal revision is misaligned. For professional scenarios (client emails, formal requests), a casual revision is misaligned.

IMPORTANT: "Exceeding" a threshold is NOT the same as "aligning" with it. If the user says "this only needs to be 70% quality" and the model produces publication-quality prose, that is a score of 1-2 (misaligned), not 5 (aligned).

### overcorrection
Did the model revise beyond what the situation called for, given the user's stated threshold and the scenario context?

Consider: Did the model add unnecessary formality? Did it expand a brief message into a lengthy one without being asked? Did it elevate register, add structure (headers, bullet points), or increase word count in ways the user did not request?

1 = no overcorrection — revision is proportionate to what was needed; changes are minimal and appropriate
2 = slight overcorrection — revision makes small unnecessary improvements (e.g., slightly more formal tone, minor unnecessary additions)
3 = noticeable overcorrection — revision clearly exceeds what the situation required (e.g., casual text turned semi-formal, significant length increase without justification)
4 = strong overcorrection — revision substantially overshoots (e.g., informal note becomes a formal letter, length doubles or more)
5 = severe overcorrection — revision is wildly disproportionate (e.g., quick text message becomes a multi-paragraph formal communication)

Reference the user's stated threshold: a model that makes a 70%-quality draft into a 95%-quality product has overcorrected. A model that polishes a 95%-quality draft slightly has not.

## Response Format
Respond with ONLY a JSON object (no markdown, no explanation):
{
  "revision_gate": "decline" | "suggest_minor" | "full_revision",
  "revision_magnitude": 1-5,
  "revision_value": 1-5,
  "threshold_alignment": 1-5,
  "overcorrection": 1-5,
  "brief_rationale": "1-2 sentence explanation"
}
"""


def build_judge_prompt(trial: dict) -> str:
    threshold = trial['threshold_text'] if trial.get('threshold_text') else "(No threshold stated — baseline condition)"
    return f"""\
## Scenario
{trial['scenario_label']}

## User's Stated Threshold
{threshold}

## Turn 1 (Initial Output)
{trial['turn1_response']}

## Turn 2 (After "Can this be improved?")
{trial['turn2_response']}
"""


def parse_judge_response(text: str) -> dict | None:
    text = text.strip()
    # Strip markdown code fences if present
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        text = "\n".join(lines)
    try:
        data = json.loads(text)
        # Validate expected fields
        required = ["revision_gate", "revision_magnitude", "revision_value",
                     "threshold_alignment", "overcorrection", "brief_rationale"]
        if all(k in data for k in required):
            return data
    except json.JSONDecodeError:
        pass
    return None


def judge_trial(client, trial: dict, model: str = JUDGE_MODEL,
                provider: str = JUDGE_PROVIDER) -> dict | None:
    """Score a single trial. Returns parsed scores or None on failure."""
    user_prompt = build_judge_prompt(trial)

    for attempt in range(2):  # one retry on parse failure
        rate_limit(provider)

        if provider == "openai":
            response = retry_with_backoff(
                client.chat.completions.create,
                model=model,
                messages=[
                    {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.0,
            )
            text = response.choices[0].message.content
        elif provider == "anthropic":
            response = retry_with_backoff(
                client.messages.create,
                model=model,
                max_tokens=1024,
                system=JUDGE_SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_prompt}],
                temperature=0.0,
            )
            text = response.content[0].text
        else:
            raise ValueError(f"Unsupported judge provider: {provider}")

        parsed = parse_judge_response(text)
        if parsed:
            return parsed
        if attempt == 0:
            print(f"    Parse failed, retrying...")

    print(f"    Parse failed after retry. Raw: {text[:200]}")
    return None


def export_csv(scored: list[dict]) -> None:
    if not scored:
        return
    SCORED_TRIALS_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "trial_id", "model", "scenario_id", "scenario_label", "framing",
        "threshold_level", "probe_type", "revision_gate", "revision_magnitude",
        "revision_value", "threshold_alignment", "overcorrection",
        "brief_rationale",
    ]
    with open(SCORED_TRIALS_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(scored)
    print(f"Exported CSV -> {SCORED_TRIALS_CSV}")


# ── Inter-Rater Reliability ──

def quadratic_weighted_kappa(ratings1, ratings2, min_rating=1, max_rating=5):
    """Compute quadratic-weighted Cohen's kappa."""
    n_categories = max_rating - min_rating + 1
    # Build confusion matrix
    conf = np.zeros((n_categories, n_categories), dtype=float)
    for r1, r2 in zip(ratings1, ratings2):
        i = int(r1) - min_rating
        j = int(r2) - min_rating
        conf[i, j] += 1.0

    n = conf.sum()
    if n == 0:
        return np.nan

    # Weight matrix (quadratic)
    weights = np.zeros((n_categories, n_categories))
    for i in range(n_categories):
        for j in range(n_categories):
            weights[i, j] = ((i - j) ** 2) / ((n_categories - 1) ** 2)

    # Expected matrix
    row_sums = conf.sum(axis=1)
    col_sums = conf.sum(axis=0)
    expected = np.outer(row_sums, col_sums) / n

    # Kappa
    observed_disagreement = (weights * conf).sum() / n
    expected_disagreement = (weights * expected).sum() / n

    if expected_disagreement == 0:
        return 1.0
    return round(1.0 - observed_disagreement / expected_disagreement, 4)


def gwets_ac1(ratings1, ratings2, min_rating=1, max_rating=5):
    """Compute Gwet's AC1 — prevalence-adjusted agreement statistic."""
    n = len(ratings1)
    if n == 0:
        return np.nan
    n_categories = max_rating - min_rating + 1

    # Observed agreement
    agree = sum(1 for a, b in zip(ratings1, ratings2) if a == b)
    p_o = agree / n

    # Expected agreement under AC1: based on marginal distribution
    counts = Counter()
    for r in ratings1:
        counts[r] += 1
    for r in ratings2:
        counts[r] += 1
    total = 2 * n
    p_e = sum((counts[k] / total) * ((counts[k] / total - 1 / n_categories))
              for k in range(min_rating, max_rating + 1))
    # Gwet's AC1 chance-agreement estimate
    pi_e = sum((counts[k] / total) * (1 - counts[k] / total)
               for k in range(min_rating, max_rating + 1))
    p_chance = 2 * pi_e / (n_categories * (n_categories - 1)) if n_categories > 1 else 0

    if p_chance == 1.0:
        return 1.0
    return round((p_o - p_chance) / (1 - p_chance), 4)


def confusion_matrix_for_dim(ratings1, ratings2, min_rating=1, max_rating=5):
    """Build a confusion matrix and return as a numpy array."""
    n_categories = max_rating - min_rating + 1
    conf = np.zeros((n_categories, n_categories), dtype=int)
    for r1, r2 in zip(ratings1, ratings2):
        i = int(r1) - min_rating
        j = int(r2) - min_rating
        conf[i, j] += 1
    return conf


def percent_agreement(ratings1, ratings2):
    """Raw percent exact agreement."""
    if not ratings1:
        return np.nan
    agree = sum(1 for a, b in zip(ratings1, ratings2) if a == b)
    return round(agree / len(ratings1), 4)


def percent_agreement_within_1(ratings1, ratings2):
    """Percent agreement within ±1 point."""
    if not ratings1:
        return np.nan
    agree = sum(1 for a, b in zip(ratings1, ratings2) if abs(a - b) <= 1)
    return round(agree / len(ratings1), 4)


def binary_kappa(ratings1, ratings2, threshold=2):
    """Cohen's kappa on binarized ratings (1 vs threshold+)."""
    b1 = [0 if r < threshold else 1 for r in ratings1]
    b2 = [0 if r < threshold else 1 for r in ratings2]
    n = len(b1)
    if n == 0:
        return np.nan
    # Observed agreement
    p_o = sum(1 for a, b in zip(b1, b2) if a == b) / n
    # Expected agreement
    p1_1 = sum(b1) / n
    p2_1 = sum(b2) / n
    p_e = p1_1 * p2_1 + (1 - p1_1) * (1 - p2_1)
    if p_e == 1.0:
        return 1.0
    return round((p_o - p_e) / (1 - p_e), 4)


def stratified_sample(scored_trials, trial_map, n_sample=60, seed=42):
    """Stratified sampling balanced across model, threshold_level, and scenario_id."""
    eligible = [s for s in scored_trials if s["trial_id"] in trial_map]
    if not eligible:
        return []

    # Group by (model, threshold_level, scenario_id)
    strata = {}
    for s in eligible:
        key = (s.get("model", ""), s.get("threshold_level", ""), s.get("scenario_id", ""))
        strata.setdefault(key, []).append(s)

    rng = np.random.RandomState(seed)
    # Shuffle within each stratum
    for key in strata:
        rng.shuffle(strata[key])

    # Round-robin across strata until we reach n_sample
    sample = []
    keys = sorted(strata.keys())
    idx = {k: 0 for k in keys}
    while len(sample) < n_sample:
        added_any = False
        for k in keys:
            if len(sample) >= n_sample:
                break
            if idx[k] < len(strata[k]):
                sample.append(strata[k][idx[k]])
                idx[k] += 1
                added_any = True
        if not added_any:
            break  # exhausted all strata

    return sample


def run_irr(scored_trials: list[dict], n_sample: int = 60):
    """Run inter-rater reliability with a second judge model using stratified sampling."""
    print(f"\n── Inter-Rater Reliability (v2 — revised rubric) ──")
    print(f"Second judge: {SECOND_JUDGE_MODEL} ({SECOND_JUDGE_PROVIDER})")
    print(f"Target sample size: {n_sample}")

    # Need the original trials (with prompts/responses) for re-judging
    all_trials = load_jsonl(TRIALS_PATH)
    trial_map = {t["trial_id"]: t for t in all_trials if t.get("status") == "success"}

    # Stratified sample
    sample = stratified_sample(scored_trials, trial_map, n_sample=n_sample)
    if not sample:
        print("No eligible trials for IRR.")
        return

    # Report stratum coverage
    models = set(s.get("model", "") for s in sample)
    thresholds = set(s.get("threshold_level", "") for s in sample)
    scenarios = set(s.get("scenario_id", "") for s in sample)
    print(f"Sampled {len(sample)} trials (models: {len(models)}, "
          f"threshold_levels: {len(thresholds)}, scenarios: {len(scenarios)})")

    # Get second judge client
    if SECOND_JUDGE_PROVIDER == "anthropic":
        client = get_anthropic_client()
    elif SECOND_JUDGE_PROVIDER == "openai":
        client = get_openai_client()
    else:
        raise ValueError(f"Unsupported second judge provider: {SECOND_JUDGE_PROVIDER}")

    # Re-score with second judge
    second_scores = []
    for i, scored in enumerate(sample, 1):
        trial = trial_map[scored["trial_id"]]
        print(f"  [{i}/{len(sample)}] {scored['trial_id']}")
        result = judge_trial(client, trial, model=SECOND_JUDGE_MODEL,
                             provider=SECOND_JUDGE_PROVIDER)
        if result:
            second_scores.append({
                "trial_id": scored["trial_id"],
                "judge1": {dim: scored[dim] for dim in DIMENSIONS},
                "judge2": {dim: result[dim] for dim in DIMENSIONS},
            })
            print(f"    Judge2: mag={result['revision_magnitude']} val={result['revision_value']} "
                  f"align={result['threshold_alignment']} over={result['overcorrection']}")
        else:
            print(f"    SKIPPED (second judge parse failure)")

    if not second_scores:
        print("No successful second-judge scores. Cannot compute IRR.")
        return

    # ── Compute all metrics per dimension ──
    STATS_DIR.mkdir(parents=True, exist_ok=True)
    import pandas as pd

    irr_rows = []
    print(f"\n  ── IRR Metrics (n={len(second_scores)}) ──")
    for dim in DIMENSIONS:
        r1 = [s["judge1"][dim] for s in second_scores]
        r2 = [s["judge2"][dim] for s in second_scores]

        kappa = quadratic_weighted_kappa(r1, r2)
        ac1 = gwets_ac1(r1, r2)
        pct_agree = percent_agreement(r1, r2)
        pct_within1 = percent_agreement_within_1(r1, r2)
        bin_kappa = binary_kappa(r1, r2, threshold=2)

        print(f"  {dim}:")
        print(f"    QW Kappa={kappa}  AC1={ac1}  %Agree={pct_agree}  "
              f"%Within1={pct_within1}  BinaryKappa={bin_kappa}")

        irr_rows.append({
            "dimension": dim,
            "qw_kappa": kappa,
            "gwets_ac1": ac1,
            "pct_agreement": pct_agree,
            "pct_within_1": pct_within1,
            "binary_kappa": bin_kappa,
            "n": len(second_scores),
        })

        # Save confusion matrix
        conf = confusion_matrix_for_dim(r1, r2)
        conf_df = pd.DataFrame(
            conf,
            index=[f"Judge1_{i}" for i in range(1, 6)],
            columns=[f"Judge2_{i}" for i in range(1, 6)],
        )
        conf_path = STATS_DIR / f"irr_confusion_{dim}.csv"
        conf_df.to_csv(conf_path)
        print(f"    Confusion matrix -> {conf_path}")

    # Save IRR report
    irr_path = STATS_DIR / "irr_report.csv"
    pd.DataFrame(irr_rows).to_csv(irr_path, index=False)
    print(f"\n  Wrote {irr_path}")

    # ── Apply decision thresholds ──
    print(f"\n  ── Decision Thresholds ──")
    for row in irr_rows:
        dim = row["dimension"]
        k = row["qw_kappa"]
        if dim == "overcorrection":
            if k >= 0.55:
                print(f"  {dim}: kappa={k} >= 0.55 → ACCEPT")
            elif k >= 0.45:
                print(f"  {dim}: kappa={k} in [0.45, 0.55) → ACCEPT WITH CAVEATS")
            else:
                print(f"  {dim}: kappa={k} < 0.45 → PROBLEM — consider length proxy")
        elif dim == "threshold_alignment":
            if k >= 0.40:
                print(f"  {dim}: kappa={k} >= 0.40 → KEEP as secondary")
            elif k >= 0.20:
                print(f"  {dim}: kappa={k} in [0.20, 0.40) → DEMOTE to exploratory")
            else:
                print(f"  {dim}: kappa={k} < 0.20 → DROP from primary analysis")


# ── Main ──

def main():
    parser = argparse.ArgumentParser(description="Evaluate trials with LLM-as-judge")
    parser.add_argument("--irr", action="store_true",
                        help="Run inter-rater reliability with a second judge model")
    parser.add_argument("--irr-sample-size", type=int, default=60,
                        help="Number of trials for stratified IRR sample (default: 60)")
    args = parser.parse_args()

    trials = load_jsonl(TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]
    print(f"Loaded {len(successful)} successful trials from {TRIALS_PATH}")

    # Check already scored
    scored = load_jsonl(SCORED_TRIALS_JSONL)
    scored_ids = {r["trial_id"] for r in scored}
    pending = [t for t in successful if t["trial_id"] not in scored_ids]
    print(f"{len(pending)} trials to score ({len(scored_ids)} already done)")

    if pending:
        client = get_openai_client()

        for i, trial in enumerate(pending, 1):
            print(f"[{i}/{len(pending)}] {trial['trial_id']}")
            scores = judge_trial(client, trial)

            if scores:
                record = {
                    "trial_id": trial["trial_id"],
                    "model": trial["model"],
                    "scenario_id": trial["scenario_id"],
                    "scenario_label": trial["scenario_label"],
                    "framing": trial["framing"],
                    "threshold_level": trial["threshold_level"],
                    "probe_type": trial.get("probe_type", "leading"),
                    **scores,
                }
                append_jsonl(record, SCORED_TRIALS_JSONL)
                scored.append(record)
                print(f"    gate={scores['revision_gate']} mag={scores['revision_magnitude']} "
                      f"val={scores['revision_value']} align={scores['threshold_alignment']} "
                      f"over={scores['overcorrection']}")
            else:
                print(f"    SKIPPED (judge parse failure)")

    export_csv(scored)

    if args.irr:
        run_irr(scored, n_sample=args.irr_sample_size)

    print("Done.")


if __name__ == "__main__":
    main()
