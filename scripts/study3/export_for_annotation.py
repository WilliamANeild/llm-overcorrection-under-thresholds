"""Export calibration samples and rater assignments for the annotator web UI.

Usage:
    python -m scripts.study3.export_for_annotation --raters rater1 rater2 rater3

Reads the calibration_samples.json from Phase 0, strips model identity for
blind evaluation, and writes two files to annotator-ui/public/:
  - samples.json: all blinded samples
  - assignments.json: maps each rater ID to their assigned sample IDs

By default each sample is assigned to 2 raters (for inter-rater reliability).
Use --overlap to change this. Samples are distributed evenly across raters,
balanced by domain.
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import S3_JUDGE_CALIBRATION_PATH
from scripts.utils import load_json


def assign_samples(
    samples: list[dict], rater_ids: list[str], overlap: int = 2
) -> dict[str, list[str]]:
    """Assign samples to raters, balanced by domain, with each sample rated by `overlap` raters."""
    # Group by domain for balanced assignment
    by_domain: dict[str, list[str]] = defaultdict(list)
    for s in samples:
        by_domain[s["domain"]].append(s["sample_id"])

    assignments: dict[str, list[str]] = {r: [] for r in rater_ids}
    n_raters = len(rater_ids)

    # For each domain, round-robin assign samples to raters
    for domain in sorted(by_domain.keys()):
        domain_ids = by_domain[domain]
        for i, sample_id in enumerate(domain_ids):
            # Assign this sample to `overlap` raters, cycling through the list
            for j in range(overlap):
                rater_idx = (i * overlap + j) % n_raters
                rater = rater_ids[rater_idx]
                if sample_id not in assignments[rater]:
                    assignments[rater].append(sample_id)

    return assignments


def main():
    parser = argparse.ArgumentParser(
        description="Export calibration samples and assignments for annotator UI"
    )
    parser.add_argument(
        "--raters",
        nargs="+",
        required=True,
        help="Rater IDs (e.g. rater1 rater2 rater3)",
    )
    parser.add_argument(
        "--overlap",
        type=int,
        default=2,
        help="Number of raters per sample (default: 2 for inter-rater reliability)",
    )
    args = parser.parse_args()

    cal_path = S3_JUDGE_CALIBRATION_PATH.parent / "calibration_samples.json"
    if not cal_path.exists():
        print(f"No calibration samples found at {cal_path}")
        print("Run: python -m scripts.study3.phase0_judge_calibration --step extract")
        return

    samples = load_json(cal_path)

    # Strip model identity (blind evaluation)
    export = []
    for s in samples:
        export.append({
            "sample_id": s["sample_id"],
            "domain": s["domain"],
            "turn": s["turn"],
            "task_prompt": s["task_prompt"],
            "output": s["output"],
        })

    rater_ids = [r.lower() for r in args.raters]
    assignments = assign_samples(export, rater_ids, args.overlap)

    # Write files to annotator-ui/public/
    public_dir = Path(__file__).resolve().parent.parent.parent / "annotator-ui" / "public"
    public_dir.mkdir(parents=True, exist_ok=True)

    samples_path = public_dir / "samples.json"
    with open(samples_path, "w") as f:
        json.dump(export, f, indent=2)

    assignments_path = public_dir / "assignments.json"
    with open(assignments_path, "w") as f:
        json.dump(assignments, f, indent=2)

    print(f"Exported {len(export)} blinded samples to {samples_path}")
    print(f"Wrote assignments to {assignments_path}")
    print(f"\nRater assignments ({args.overlap} raters per sample):")
    for rater, sample_ids in assignments.items():
        print(f"  {rater}: {len(sample_ids)} samples")

    # Verify overlap
    sample_coverage: dict[str, int] = defaultdict(int)
    for sample_ids in assignments.values():
        for sid in sample_ids:
            sample_coverage[sid] += 1
    min_cov = min(sample_coverage.values()) if sample_coverage else 0
    max_cov = max(sample_coverage.values()) if sample_coverage else 0
    print(f"\nCoverage: each sample rated by {min_cov}-{max_cov} raters")
    print(f"\nNext: deploy to Vercel with 'vercel --prod' from annotator-ui/")


if __name__ == "__main__":
    main()
