"""Generate the prompt matrix from scenarios, thresholds, and probe types."""

import sys
from pathlib import Path

# Allow running as script
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.config import SCENARIOS_PATH, THRESHOLDS_PATH, PROMPT_MATRIX_PATH, FRAMINGS
from scripts.utils import load_json, save_json


def generate_matrix() -> list[dict]:
    scenarios = load_json(SCENARIOS_PATH)
    thresholds = load_json(THRESHOLDS_PATH)
    probe_types = thresholds["probe_types"]  # {"leading": "Can this be improved?", "neutral": "..."}

    cells = []
    for scenario in scenarios:
        for framing in FRAMINGS:
            for threshold in thresholds[framing]:
                for probe_name, probe_text in probe_types.items():
                    if threshold["text"]:
                        turn1 = f"{scenario['scenario_text']}\n\n{threshold['text']}"
                    else:
                        turn1 = scenario["scenario_text"]
                    cell = {
                        "scenario_id": scenario["id"],
                        "scenario_label": scenario["label"],
                        "framing": framing,
                        "threshold_level": threshold["level"],
                        "threshold_text": threshold["text"],
                        "probe_type": probe_name,
                        "turn1_prompt": turn1,
                        "turn2_prompt": probe_text,
                    }
                    cells.append(cell)

    return cells


def main():
    cells = generate_matrix()
    save_json(cells, PROMPT_MATRIX_PATH)
    print(f"Generated {len(cells)} cells → {PROMPT_MATRIX_PATH}")

    # Quick sanity check
    framings = set(c["framing"] for c in cells)
    levels = set(c["threshold_level"] for c in cells)
    scenarios = set(c["scenario_id"] for c in cells)
    probes = set(c["probe_type"] for c in cells)
    print(f"  Scenarios: {len(scenarios)}, Framings: {len(framings)}, "
          f"Levels: {len(levels)}, Probe types: {len(probes)}")


if __name__ == "__main__":
    main()
