"""Generate the blind evaluator experiment matrix (Study 3).

For each (model, scenario, domain) combination, produces a cell with:
- task_prompt: the raw scenario text (no threshold appended)
- domain: writing, code, or analysis
- Metadata: scenario_id, scenario_label

No thresholds are used in Study 3 (Studies 1-2 covered threshold effects).
The working model gets up to 5 turns: initial output + 4 "Can this be improved?" probes.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.config import (
    BLIND_EVAL_MATRIX_PATH,
    BLIND_EVAL_MAX_TURNS,
    BLIND_EVAL_SCENARIOS_PATH,
    BLIND_EVAL_WORKING_PROBE,
)
from scripts.utils import load_json, save_json


def generate_matrix() -> list[dict]:
    scenarios_config = load_json(BLIND_EVAL_SCENARIOS_PATH)

    # Flatten all domains into a single list
    all_scenarios = []
    for domain in ["writing", "code", "analysis"]:
        for scenario in scenarios_config[domain]:
            all_scenarios.append(scenario)

    matrix = []
    for scenario in all_scenarios:
        cell = {
            "scenario_id": scenario["id"],
            "scenario_label": scenario["label"],
            "domain": scenario["domain"],
            "task_prompt": scenario["scenario_text"],
            "working_probes": [BLIND_EVAL_WORKING_PROBE] * (BLIND_EVAL_MAX_TURNS - 1),
            "max_turns": BLIND_EVAL_MAX_TURNS,
        }
        matrix.append(cell)

    return matrix


def main():
    matrix = generate_matrix()
    save_json(matrix, BLIND_EVAL_MATRIX_PATH)

    domains = {}
    for cell in matrix:
        domains[cell["domain"]] = domains.get(cell["domain"], 0) + 1

    print(f"Generated {len(matrix)} cells:")
    for domain, count in sorted(domains.items()):
        print(f"  {domain}: {count} tasks")
    print(f"Saved to {BLIND_EVAL_MATRIX_PATH}")


if __name__ == "__main__":
    main()
