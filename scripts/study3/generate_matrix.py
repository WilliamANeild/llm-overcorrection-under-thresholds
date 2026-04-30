"""Generate the Study 3 (Revision Yield) experiment matrix.

Produces a flat list of task cells across all 5 domains (40 tasks total).
No thresholds - Study 3 focuses purely on revision behavior and quality judgment.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import (
    S3_DOMAINS,
    S3_MATRIX_PATH,
    S3_MAX_TURNS,
    S3_SCENARIOS_PATH,
    S3_WORKING_PROBE,
)
from scripts.utils import load_json, save_json


def generate_matrix() -> list[dict]:
    scenarios_config = load_json(S3_SCENARIOS_PATH)

    matrix = []
    for domain in S3_DOMAINS:
        for scenario in scenarios_config[domain]:
            cell = {
                "scenario_id": scenario["id"],
                "scenario_label": scenario["label"],
                "domain": scenario["domain"],
                "task_prompt": scenario["scenario_text"],
                "working_probes": [S3_WORKING_PROBE] * (S3_MAX_TURNS - 1),
                "max_turns": S3_MAX_TURNS,
            }
            matrix.append(cell)

    return matrix


def main():
    S3_MATRIX_PATH.parent.mkdir(parents=True, exist_ok=True)
    matrix = generate_matrix()
    save_json(matrix, S3_MATRIX_PATH)

    domains = {}
    for cell in matrix:
        domains[cell["domain"]] = domains.get(cell["domain"], 0) + 1

    print(f"Generated {len(matrix)} cells:")
    for domain, count in sorted(domains.items()):
        print(f"  {domain}: {count} tasks")
    print(f"\nWith 6 models x 3 runs = {len(matrix) * 6 * 3} total worker trials")
    print(f"Saved to {S3_MATRIX_PATH}")


if __name__ == "__main__":
    main()
