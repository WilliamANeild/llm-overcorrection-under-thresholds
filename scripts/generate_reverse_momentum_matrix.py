"""Generate the reverse momentum experiment prompt matrix.

One round of affirming feedback ("This looks great, no changes needed")
before the evaluative probe. Tests whether positive priming suppresses
revision below the cold baseline.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.config import (
    AFFIRMING_PROBE,
    EVALUATIVE_PROBE,
    MOMENTUM_THRESHOLDS,
    REVERSE_MOMENTUM_MATRIX_PATH,
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
                turn1_prompt = build_turn1_prompt(
                    scenario["scenario_text"], thresh["text"]
                )
                cell = {
                    "scenario_id": scenario["id"],
                    "scenario_label": scenario["label"],
                    "framing": framing,
                    "threshold_level": thresh["level"],
                    "threshold_text": thresh["text"],
                    "dose": -1,  # negative dose = reverse momentum
                    "turn1_prompt": turn1_prompt,
                    "intermediate_probes": [AFFIRMING_PROBE],
                    "final_probe": EVALUATIVE_PROBE,
                }
                matrix.append(cell)

    return matrix


def main():
    matrix = generate_matrix()
    save_json(matrix, REVERSE_MOMENTUM_MATRIX_PATH)
    print(f"Generated {len(matrix)} cells")
    print(f"Saved to {REVERSE_MOMENTUM_MATRIX_PATH}")


if __name__ == "__main__":
    main()
