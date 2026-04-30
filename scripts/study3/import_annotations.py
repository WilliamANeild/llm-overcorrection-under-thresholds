"""Import annotator ratings from the web UI back into the pipeline.

Usage:
    python -m scripts.study3.import_annotations ratings_rater1.csv ratings_rater2.csv [...]

Reads CSV or JSON exports from the annotator UI, computes inter-rater
reliability, and writes the merged human ratings to S3_HUMAN_EVAL_PATH.
"""

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import numpy as np

from scripts.config import S3_HUMAN_EVAL_PATH


def load_ratings_file(path: str) -> list[dict]:
    """Load ratings from CSV or JSON."""
    p = Path(path)
    if p.suffix == ".json":
        with open(p) as f:
            return json.load(f)
    elif p.suffix == ".csv":
        rows = []
        with open(p, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append({
                    "sample_id": row["sample_id"],
                    "level": int(row["level"]),
                    "rationale": row.get("rationale", ""),
                    "rater_id": row.get("rater_id", "unknown"),
                })
        return rows
    else:
        raise ValueError(f"Unsupported file type: {p.suffix}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m scripts.study3.import_annotations file1.csv file2.csv ...")
        sys.exit(1)

    all_ratings = []
    for path in sys.argv[1:]:
        ratings = load_ratings_file(path)
        print(f"Loaded {len(ratings)} ratings from {path}")
        all_ratings.extend(ratings)

    # Group by sample_id
    by_sample: dict[str, list[dict]] = defaultdict(list)
    for r in all_ratings:
        by_sample[r["sample_id"]].append(r)

    print(f"\nTotal unique samples rated: {len(by_sample)}")
    rater_ids = sorted(set(r["rater_id"] for r in all_ratings))
    print(f"Raters: {rater_ids}")

    # Compute inter-rater reliability if 2+ raters
    if len(rater_ids) >= 2:
        # Find samples rated by at least 2 raters
        shared_samples = [sid for sid, ratings in by_sample.items() if len(ratings) >= 2]
        print(f"Samples with 2+ ratings: {len(shared_samples)}")

        if len(shared_samples) >= 10:
            try:
                from sklearn.metrics import cohen_kappa_score

                # Pairwise kappa for first two raters
                r1_id, r2_id = rater_ids[0], rater_ids[1]
                r1_vals, r2_vals = [], []
                for sid in shared_samples:
                    ratings_for_sample = by_sample[sid]
                    r1_rating = next((r for r in ratings_for_sample if r["rater_id"] == r1_id), None)
                    r2_rating = next((r for r in ratings_for_sample if r["rater_id"] == r2_id), None)
                    if r1_rating and r2_rating:
                        r1_vals.append(r1_rating["level"])
                        r2_vals.append(r2_rating["level"])

                if len(r1_vals) >= 10:
                    kappa = cohen_kappa_score(r1_vals, r2_vals, weights="quadratic")
                    print(f"Quadratic weighted kappa ({r1_id} vs {r2_id}): {kappa:.3f}")
                    if kappa < 0.4:
                        print("WARNING: Low agreement. Consider re-calibrating raters.")
                    elif kappa < 0.6:
                        print("NOTE: Moderate agreement. Acceptable but worth monitoring.")
                    else:
                        print("Good agreement.")
            except ImportError:
                print("sklearn not available, skipping kappa computation")

    # Write merged ratings
    S3_HUMAN_EVAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(S3_HUMAN_EVAL_PATH, "w", newline="") as f:
        max_raters = max(len(v) for v in by_sample.values())
        header = ["sample_id", "human_mean", "n_raters"] + [f"rater{i+1}_level" for i in range(max_raters)]
        writer = csv.writer(f)
        writer.writerow(header)

        for sample_id in sorted(by_sample.keys()):
            sample_ratings = by_sample[sample_id]
            levels = [r["level"] for r in sample_ratings]
            mean_level = float(np.mean(levels))
            row = [sample_id, f"{mean_level:.2f}", len(levels)] + levels
            writer.writerow(row)

    print(f"\nWrote {len(by_sample)} merged ratings to {S3_HUMAN_EVAL_PATH}")
    print("Ready for: python -m scripts.study3.phase0_judge_calibration --step select")


if __name__ == "__main__":
    main()
