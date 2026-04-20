"""Generate the momentum experiment prompt matrix.

For each (scenario, framing, threshold, dose) combination, produces a cell with:
- turn1_prompt: scenario + threshold text (same as Study 1)
- intermediate_probes: list of N leading probes
- final_probe: the evaluative probe
- Metadata: dose, scenario_id, framing, threshold_level
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.config import (
    EVALUATIVE_PROBE,
    LEADING_PROBE,
    MOMENTUM_DOSES,
    MOMENTUM_MATRIX_PATH,
    MOMENTUM_THRESHOLDS,
    SCENARIOS_PATH,
    THRESHOLDS_PATH,
)
from scripts.utils import load_json, save_json


def build_turn1_prompt(scenario_text: str, threshold_text: str) -> str:
    if threshold_text:
        return f"{scenario_text} {threshold_text}"
    return scenario_text


def generate_matrix() -> list[dict]:
    scenarios = load_json(SCENARIOS_PATH)
    thresholds_config = load_json(THRESHOLDS_PATH)

    matrix = []

    for scenario in scenarios:
        for framing in ["numeric", "qualitative"]:
            framing_thresholds = thresholds_config[framing]
            for thresh in framing_thresholds:
                if thresh["level"] not in MOMENTUM_THRESHOLDS:
                    continue
                for dose in MOMENTUM_DOSES:
                    turn1_prompt = build_turn1_prompt(
                        scenario["scenario_text"], thresh["text"]
                    )
                    cell = {
                        "scenario_id": scenario["id"],
                        "scenario_label": scenario["label"],
                        "framing": framing,
                        "threshold_level": thresh["level"],
                        "threshold_text": thresh["text"],
                        "dose": dose,
                        "turn1_prompt": turn1_prompt,
                        "intermediate_probes": [LEADING_PROBE] * dose,
                        "final_probe": EVALUATIVE_PROBE,
                    }
                    matrix.append(cell)

    return matrix


def main():
    matrix = generate_matrix()
    save_json(matrix, MOMENTUM_MATRIX_PATH)

    # Verify counts
    n_scenarios = 8
    n_framings = 2
    n_thresholds = len(MOMENTUM_THRESHOLDS)
    n_doses = len(MOMENTUM_DOSES)
    expected = n_scenarios * n_framings * n_thresholds * n_doses
    print(f"Generated {len(matrix)} cells (expected {expected})")
    print(f"  {n_scenarios} scenarios x {n_framings} framings x {n_thresholds} thresholds x {n_doses} doses")
    print(f"Saved to {MOMENTUM_MATRIX_PATH}")


if __name__ == "__main__":
    main()
