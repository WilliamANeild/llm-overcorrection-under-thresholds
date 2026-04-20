"""Evaluate momentum trials: score the final evaluative-probe turn using LLM-as-judge."""

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np

from scripts.config import (
    JUDGE_MODEL,
    JUDGE_PROVIDER,
    MOMENTUM_SCORED_CSV,
    MOMENTUM_SCORED_PATH,
    MOMENTUM_STATS_DIR,
    MOMENTUM_TRIALS_PATH,
    SECOND_JUDGE_MODEL,
    SECOND_JUDGE_PROVIDER,
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

MOMENTUM_JUDGE_SYSTEM_PROMPT = """\
You are an expert evaluator for a research study on LLM revision behavior. \
You will be given a writing scenario, a stated quality threshold, \
an initial model output (Turn 1), and the model's response after being asked \
"{final_probe}" following {dose} prior revision round(s).

Your job is to evaluate the final response compared to the original Turn 1 output.

## revision_gate
Classify the model's final response as one of:
- "decline" -- the model said the output is fine or does not need changes
- "suggest_minor" -- the model suggested small tweaks but did not fully rewrite
- "full_revision" -- the model produced a substantially revised version

## Rubric Dimensions (score 1-5 each)

### revision_magnitude
How extensive is the final revision compared with the original Turn 1 output?
1 = almost no change, 2 = small local edits, 3 = moderate revision, 4 = substantial revision, 5 = major rewrite

### revision_value
Does the final version add real value over the original, or is it just different?
1 = no meaningful improvement, 2 = very slight improvement, 3 = some useful improvement, 4 = clearly meaningful improvement, 5 = major improvement

### threshold_alignment
Does the final output's quality level match what the stated threshold implies?
A threshold of "70% quality" means a quick, functional draft -- not a polished final product. \
A revision that dramatically exceeds the stated threshold is MISALIGNED. \
A revision that falls below the threshold is also misaligned.

Score guide:
1 = strongly misaligned -- revision is far above or below the stated threshold
2 = somewhat misaligned -- revision noticeably overshoots or undershoots
3 = partially aligned -- revision is in the right ballpark but drifts
4 = mostly aligned -- revision quality is close to the threshold, with minor drift
5 = fully aligned -- revision quality matches the threshold intent precisely

IMPORTANT: When no threshold is stated (baseline condition), score based on whether the revision matches a reasonable default for the scenario's genre and context.

IMPORTANT: "Exceeding" a threshold is NOT the same as "aligning" with it. If the threshold says "around 70 out of 100" and the model produces publication-quality prose, that is a score of 1-2 (misaligned), not 5.

### overcorrection
Did the model revise beyond what the situation called for, given the stated threshold and scenario context?

Consider: unnecessary formality added? Brief message expanded without being asked? Register elevated, structure added (headers, bullet points), or word count increased beyond what was requested?

1 = no overcorrection -- revision is proportionate
2 = slight overcorrection -- small unnecessary improvements
3 = noticeable overcorrection -- clearly exceeds what was needed
4 = strong overcorrection -- substantially overshoots
5 = severe overcorrection -- wildly disproportionate

Reference the stated threshold: making a 70%-quality draft into a 95%-quality product is overcorrection. Polishing a 95%-quality draft slightly is not.

## Response Format
Respond with ONLY a JSON object (no markdown, no explanation):
{{
  "revision_gate": "decline" | "suggest_minor" | "full_revision",
  "revision_magnitude": 1-5,
  "revision_value": 1-5,
  "threshold_alignment": 1-5,
  "overcorrection": 1-5,
  "brief_rationale": "1-2 sentence explanation"
}}
"""


def build_momentum_judge_prompt(trial: dict) -> str:
    threshold = trial["threshold_text"] if trial.get("threshold_text") else "(No threshold stated -- baseline condition)"
    dose = trial["dose"]
    return f"""\
## Scenario
{trial['scenario_label']}

## Stated Quality Threshold
{threshold}

## Turn 1 (Initial Output)
{trial['turn1_response']}

## Prior Revision Context
The model was asked "Can this be improved?" {dose} time(s) before the final probe.

## Final Response (After: "{trial['final_probe']}")
{trial['final_response']}
"""


def parse_judge_response(text: str) -> dict | None:
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        text = "\n".join(lines)
    try:
        data = json.loads(text)
        required = ["revision_gate", "revision_magnitude", "revision_value",
                     "threshold_alignment", "overcorrection", "brief_rationale"]
        if all(k in data for k in required):
            return data
    except json.JSONDecodeError:
        pass
    return None


def judge_trial(client, trial: dict, model: str = JUDGE_MODEL,
                provider: str = JUDGE_PROVIDER) -> dict | None:
    user_prompt = build_momentum_judge_prompt(trial)
    system_prompt = MOMENTUM_JUDGE_SYSTEM_PROMPT.format(
        final_probe=trial["final_probe"],
        dose=trial["dose"],
    )

    for attempt in range(2):
        rate_limit(provider)

        if provider == "openai":
            response = retry_with_backoff(
                client.chat.completions.create,
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
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
                system=system_prompt,
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
    MOMENTUM_SCORED_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "trial_id", "model", "scenario_id", "scenario_label", "framing",
        "threshold_level", "dose", "revision_gate", "revision_magnitude",
        "revision_value", "threshold_alignment", "overcorrection",
        "brief_rationale",
    ]
    with open(MOMENTUM_SCORED_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(scored)
    print(f"Exported CSV -> {MOMENTUM_SCORED_CSV}")


def quadratic_weighted_kappa(ratings1, ratings2, min_rating=1, max_rating=5):
    n_categories = max_rating - min_rating + 1
    conf = np.zeros((n_categories, n_categories), dtype=float)
    for r1, r2 in zip(ratings1, ratings2):
        conf[int(r1) - min_rating, int(r2) - min_rating] += 1.0
    n = conf.sum()
    if n == 0:
        return np.nan
    weights = np.zeros((n_categories, n_categories))
    for i in range(n_categories):
        for j in range(n_categories):
            weights[i, j] = ((i - j) ** 2) / ((n_categories - 1) ** 2)
    expected = np.outer(conf.sum(axis=1), conf.sum(axis=0)) / n
    obs = (weights * conf).sum() / n
    exp = (weights * expected).sum() / n
    if exp == 0:
        return 1.0
    return round(1.0 - obs / exp, 4)


def stratified_sample(scored_trials, trial_map, n_sample=60, seed=42):
    eligible = [s for s in scored_trials if s["trial_id"] in trial_map]
    if not eligible:
        return []
    strata = {}
    for s in eligible:
        key = (s.get("model", ""), s.get("threshold_level", ""), s.get("dose", 0))
        strata.setdefault(key, []).append(s)
    rng = np.random.RandomState(seed)
    for key in strata:
        rng.shuffle(strata[key])
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
            break
    return sample


def run_irr(scored_trials: list[dict], n_sample: int = 60):
    print(f"\n== Inter-Rater Reliability (Study 2) ==")
    print(f"Second judge: {SECOND_JUDGE_MODEL} ({SECOND_JUDGE_PROVIDER})")

    all_trials = load_jsonl(MOMENTUM_TRIALS_PATH)
    trial_map = {t["trial_id"]: t for t in all_trials if t.get("status") == "success"}

    sample = stratified_sample(scored_trials, trial_map, n_sample=n_sample)
    if not sample:
        print("No eligible trials for IRR.")
        return

    models = set(s.get("model", "") for s in sample)
    doses = set(s.get("dose", 0) for s in sample)
    print(f"Sampled {len(sample)} trials (models: {len(models)}, doses: {sorted(doses)})")

    if SECOND_JUDGE_PROVIDER == "anthropic":
        client = get_anthropic_client()
    elif SECOND_JUDGE_PROVIDER == "openai":
        client = get_openai_client()
    else:
        raise ValueError(f"Unsupported: {SECOND_JUDGE_PROVIDER}")

    second_scores = []
    for i, scored in enumerate(sample, 1):
        trial = trial_map.get(scored["trial_id"])
        if not trial:
            print(f"  [{i}/{len(sample)}] {scored['trial_id']} -- MISSING from trials")
            continue
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
        print("No successful second-judge scores.")
        return

    MOMENTUM_STATS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"\n  == IRR Metrics (n={len(second_scores)}) ==")
    for dim in DIMENSIONS:
        r1 = [s["judge1"][dim] for s in second_scores]
        r2 = [s["judge2"][dim] for s in second_scores]
        kappa = quadratic_weighted_kappa(r1, r2)
        agree = sum(1 for a, b in zip(r1, r2) if a == b) / len(r1)
        within1 = sum(1 for a, b in zip(r1, r2) if abs(a - b) <= 1) / len(r1)
        print(f"  {dim}: QW_kappa={kappa}  %agree={agree:.3f}  %within1={within1:.3f}")

    # Save raw second-judge scores
    irr_path = MOMENTUM_STATS_DIR / "irr_second_judge.json"
    with open(irr_path, "w") as f:
        json.dump(second_scores, f, indent=2)
    print(f"\n  Saved IRR data -> {irr_path}")


def main():
    parser = argparse.ArgumentParser(description="Evaluate momentum trials with LLM-as-judge")
    parser.add_argument("--limit", type=int, default=0, help="Limit trials to score (0 = all)")
    parser.add_argument("--irr", action="store_true",
                        help="Run inter-rater reliability with second judge")
    parser.add_argument("--irr-sample-size", type=int, default=60,
                        help="Number of trials for IRR sample (default: 60)")
    args = parser.parse_args()

    if args.irr:
        scored = load_jsonl(MOMENTUM_SCORED_PATH)
        print(f"Loaded {len(scored)} scored momentum trials")
        run_irr(scored, n_sample=args.irr_sample_size)
        return

    trials = load_jsonl(MOMENTUM_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]
    print(f"Loaded {len(successful)} successful momentum trials from {MOMENTUM_TRIALS_PATH}")

    scored = load_jsonl(MOMENTUM_SCORED_PATH)
    scored_ids = {r["trial_id"] for r in scored}
    pending = [t for t in successful if t["trial_id"] not in scored_ids]
    print(f"{len(pending)} trials to score ({len(scored_ids)} already done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit} trials")

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
                    "dose": trial["dose"],
                    **scores,
                }
                append_jsonl(record, MOMENTUM_SCORED_PATH)
                scored.append(record)
                print(f"    gate={scores['revision_gate']} mag={scores['revision_magnitude']} "
                      f"val={scores['revision_value']} align={scores['threshold_alignment']} "
                      f"over={scores['overcorrection']}")
            else:
                print(f"    SKIPPED (judge parse failure)")

    export_csv(scored)
    print("Done.")


if __name__ == "__main__":
    main()
