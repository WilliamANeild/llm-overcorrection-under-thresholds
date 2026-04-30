"""Phase 0: Judge Calibration Protocol for the Revision Yield experiment.

Empirically selects the best judge model by comparing all 6 models' ratings
against human ground truth on a stratified calibration sample.

Steps:
  --step extract       Extract stratified calibration sample from pilot data
  --step export-human  Export calibration set for human annotation
  --step import-human  Import human ratings from CSV
  --step model-judges  All 6 models rate the calibration sample
  --step select        Compute correlations, select best judge
"""

import argparse
import csv
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import numpy as np
from scipy import stats as sp_stats

from scripts.config import (
    MODELS,
    S3_HUMAN_EVAL_PATH,
    S3_JUDGE_CALIBRATION_PATH,
    S3_WORKER_TRIALS_PATH,
)
from scripts.utils import (
    append_jsonl,
    get_anthropic_client,
    get_google_client,
    get_openai_client,
    get_together_client,
    load_jsonl,
    rate_limit,
    retry_with_backoff,
    save_json,
)

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


def parse_eval_response(text: str) -> dict | None:
    text = text.strip()
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
    except (json.JSONDecodeError, ValueError):
        pass
    return None


def call_judge(provider: str, model_id: str, prompt: str) -> dict | None:
    for attempt in range(2):
        rate_limit(provider)

        if provider == "openai":
            client = get_openai_client()
            r = retry_with_backoff(
                client.chat.completions.create,
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            text = r.choices[0].message.content

        elif provider == "anthropic":
            client = get_anthropic_client()
            r = retry_with_backoff(
                client.messages.create,
                model=model_id,
                max_tokens=256,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            text = r.content[0].text

        elif provider == "google":
            from google.genai import types
            client = get_google_client()
            config = types.GenerateContentConfig(temperature=0.0)
            r = retry_with_backoff(
                client.models.generate_content,
                model=model_id,
                contents=prompt,
                config=config,
            )
            text = r.text

        elif provider == "together":
            client = get_together_client()
            r = retry_with_backoff(
                client.chat.completions.create,
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            text = r.choices[0].message.content

        else:
            raise ValueError(f"Unknown provider: {provider}")

        parsed = parse_eval_response(text)
        if parsed:
            return {**parsed, "raw_response": text}

        if attempt == 0:
            print(f"    Parse failed, retrying...")

    return None


def step_extract(n_samples: int):
    """Extract a stratified calibration sample from pilot worker trials."""
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]

    if not successful:
        print("No worker trials found. Run pilot Phase 1 first.")
        return

    # Flatten to (task, output, metadata) pairs across all turns and models
    pairs = []
    for trial in successful:
        for turn_idx, response in enumerate(trial["responses"]):
            pairs.append({
                "sample_id": f"{trial['trial_id']}__turn{turn_idx + 1}",
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "domain": trial["domain"],
                "scenario_id": trial["scenario_id"],
                "turn": turn_idx + 1,
                "task_prompt": trial["task_prompt"],
                "output": response,
            })

    print(f"Total (task, output) pairs available: {len(pairs)}")

    # Stratified sampling: balance across domains, turns, and models
    grouped = defaultdict(list)
    for p in pairs:
        key = (p["domain"], p["turn"])
        grouped[key].append(p)

    rng = random.Random(42)
    selected = []
    per_stratum = max(1, n_samples // len(grouped))

    for key in sorted(grouped.keys()):
        stratum = grouped[key]
        rng.shuffle(stratum)
        selected.extend(stratum[:per_stratum])

    # If we need more to reach n_samples, sample from remainder
    selected_ids = {s["sample_id"] for s in selected}
    remaining = [p for p in pairs if p["sample_id"] not in selected_ids]
    rng.shuffle(remaining)
    while len(selected) < n_samples and remaining:
        selected.append(remaining.pop())

    selected = selected[:n_samples]
    print(f"Selected {len(selected)} calibration samples")

    # Domain distribution
    domain_counts = defaultdict(int)
    for s in selected:
        domain_counts[s["domain"]] += 1
    for d, c in sorted(domain_counts.items()):
        print(f"  {d}: {c}")

    # Save calibration set
    cal_path = S3_JUDGE_CALIBRATION_PATH.parent / "calibration_samples.json"
    cal_path.parent.mkdir(parents=True, exist_ok=True)
    save_json(selected, cal_path)
    print(f"Saved calibration samples to {cal_path}")


def step_export_human():
    """Export calibration samples as CSV for human annotation."""
    cal_path = S3_JUDGE_CALIBRATION_PATH.parent / "calibration_samples.json"
    from scripts.utils import load_json
    samples = load_json(cal_path)

    export_path = S3_HUMAN_EVAL_PATH.parent / "human_eval_template.csv"
    export_path.parent.mkdir(parents=True, exist_ok=True)

    with open(export_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["sample_id", "task_prompt", "output", "rater1_level", "rater2_level", "rater3_level"])
        for s in samples:
            writer.writerow([s["sample_id"], s["task_prompt"], s["output"], "", "", ""])

    print(f"Exported {len(samples)} samples to {export_path}")
    print("Have 2-3 raters fill in level columns (1-4 scale), then import with --step import-human")


def step_import_human(file_path: str):
    """Import human ratings from completed CSV."""
    ratings = []
    with open(file_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rater_levels = []
            for key in ["rater1_level", "rater2_level", "rater3_level"]:
                if row.get(key) and row[key].strip():
                    rater_levels.append(int(row[key].strip()))
            if rater_levels:
                ratings.append({
                    "sample_id": row["sample_id"],
                    "rater_levels": rater_levels,
                    "human_mean": float(np.mean(rater_levels)),
                    "n_raters": len(rater_levels),
                })

    # Compute inter-rater reliability if 2+ raters
    if ratings and all(r["n_raters"] >= 2 for r in ratings):
        # Cohen's kappa for first two raters
        r1 = [r["rater_levels"][0] for r in ratings]
        r2 = [r["rater_levels"][1] for r in ratings]
        from sklearn.metrics import cohen_kappa_score
        kappa = cohen_kappa_score(r1, r2, weights="quadratic")
        print(f"Inter-rater reliability (quadratic weighted kappa, raters 1-2): {kappa:.3f}")

    S3_HUMAN_EVAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(S3_HUMAN_EVAL_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["sample_id", "human_mean", "n_raters"] +
                        [f"rater{i+1}_level" for i in range(max(r["n_raters"] for r in ratings))])
        for r in ratings:
            writer.writerow([r["sample_id"], f"{r['human_mean']:.2f}", r["n_raters"]] + r["rater_levels"])

    print(f"Imported {len(ratings)} human ratings to {S3_HUMAN_EVAL_PATH}")


def step_model_judges():
    """All 6 models judge the calibration sample."""
    cal_path = S3_JUDGE_CALIBRATION_PATH.parent / "calibration_samples.json"
    from scripts.utils import load_json
    samples = load_json(cal_path)

    existing = load_jsonl(S3_JUDGE_CALIBRATION_PATH)
    completed_ids = {(r["sample_id"], r["judge_model"]) for r in existing}

    for model_name, model_cfg in MODELS.items():
        provider = model_cfg["provider"]
        model_id = model_cfg["model_id"]
        pending = [s for s in samples if (s["sample_id"], model_name) not in completed_ids]

        print(f"\n{model_name}: {len(pending)} pending ({len(samples) - len(pending)} done)")

        for i, sample in enumerate(pending, 1):
            print(f"  [{i}/{len(pending)}] {sample['sample_id']}")
            prompt = EVAL_PROMPT.format(task_prompt=sample["task_prompt"], output=sample["output"])
            result = call_judge(provider, model_id, prompt)

            record = {
                "sample_id": sample["sample_id"],
                "judge_model": model_name,
                "level": result["level"] if result else None,
                "rationale": result.get("rationale", "") if result else None,
                "raw_response": result.get("raw_response", "") if result else None,
            }
            append_jsonl(record, S3_JUDGE_CALIBRATION_PATH)

            if result:
                print(f"    Level: {result['level']}")
            else:
                print(f"    SKIPPED (parse failure)")

    print("\nAll model judges complete.")


def step_select():
    """Compute correlations with human ratings and select best judge."""
    # Load human ratings
    if not S3_HUMAN_EVAL_PATH.exists():
        print("No human ratings found. Run --step import-human first.")
        return

    human_ratings = {}
    with open(S3_HUMAN_EVAL_PATH, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            human_ratings[row["sample_id"]] = float(row["human_mean"])

    # Load model judge ratings
    judge_results = load_jsonl(S3_JUDGE_CALIBRATION_PATH)
    model_ratings = defaultdict(dict)
    for r in judge_results:
        if r.get("level") is not None:
            model_ratings[r["judge_model"]][r["sample_id"]] = r["level"]

    print("\n== Judge Calibration Results ==\n")
    print(f"{'Model':<20} {'Spearman r':>10} {'p-value':>10} {'QW Kappa':>10} {'N':>5}")
    print("-" * 60)

    results = {}
    for model_name in sorted(model_ratings.keys()):
        ratings = model_ratings[model_name]
        # Align with human ratings
        shared_ids = sorted(set(ratings.keys()) & set(human_ratings.keys()))
        if len(shared_ids) < 10:
            print(f"{model_name:<20} {'insufficient data':>30}")
            continue

        model_vals = [ratings[sid] for sid in shared_ids]
        human_vals = [human_ratings[sid] for sid in shared_ids]

        rho, p = sp_stats.spearmanr(model_vals, human_vals)

        # Quadratic weighted kappa
        try:
            from sklearn.metrics import cohen_kappa_score
            rounded_human = [round(h) for h in human_vals]
            qw_kappa = cohen_kappa_score(model_vals, rounded_human, weights="quadratic")
        except ImportError:
            qw_kappa = float("nan")

        results[model_name] = {"spearman_r": rho, "p_value": p, "qw_kappa": qw_kappa, "n": len(shared_ids)}
        print(f"{model_name:<20} {rho:>10.3f} {p:>10.4f} {qw_kappa:>10.3f} {len(shared_ids):>5}")

    if not results:
        print("\nNo valid results to compare.")
        return

    # Select best judge: highest Spearman r. If tied within 0.02, prefer cheaper (together > google > anthropic > openai)
    cost_rank = {"together": 0, "google": 1, "anthropic": 2, "openai": 3}
    best_model = max(results.keys(), key=lambda m: (results[m]["spearman_r"], -cost_rank.get(MODELS[m]["provider"], 99)))

    best_r = results[best_model]["spearman_r"]
    print(f"\nSelected judge: {best_model} (r = {best_r:.3f})")

    if best_r < 0.5:
        print("WARNING: Best judge has r < 0.5 with human ratings. Consider improving calibration.")
    elif best_r < 0.6:
        print("NOTE: Best judge has r < 0.6. Acceptable but monitor quality.")

    # Save selection
    selection_path = S3_JUDGE_CALIBRATION_PATH.parent / "selected_judge.json"
    save_json({
        "selected_judge": best_model,
        "model_id": MODELS[best_model]["model_id"],
        "provider": MODELS[best_model]["provider"],
        "spearman_r": best_r,
        "all_results": results,
    }, selection_path)
    print(f"Saved judge selection to {selection_path}")
    print(f"\nUse --judge-model {best_model} for Phase 2+")


def main():
    parser = argparse.ArgumentParser(
        description="Phase 0: Judge calibration for Study 3"
    )
    parser.add_argument("--step", required=True,
                        choices=["extract", "export-human", "import-human", "model-judges", "select"])
    parser.add_argument("--n-samples", type=int, default=150,
                        help="Number of calibration samples to extract")
    parser.add_argument("--file", type=str, default=None,
                        help="Path to human ratings CSV (for import-human step)")
    args = parser.parse_args()

    if args.step == "extract":
        step_extract(args.n_samples)
    elif args.step == "export-human":
        step_export_human()
    elif args.step == "import-human":
        if not args.file:
            print("Error: --file required for import-human step")
            sys.exit(1)
        step_import_human(args.file)
    elif args.step == "model-judges":
        step_model_judges()
    elif args.step == "select":
        step_select()


if __name__ == "__main__":
    main()
