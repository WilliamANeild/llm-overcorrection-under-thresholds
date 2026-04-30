"""Export calibration samples as JSON for the annotator web UI.

Usage:
    python -m scripts.study3.export_for_annotation

Reads the calibration_samples.json from Phase 0 and writes a cleaned version
that the annotator UI can load directly. Model identity is stripped so raters
are blind to which model produced each output.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import S3_JUDGE_CALIBRATION_PATH
from scripts.utils import load_json

def main():
    cal_path = S3_JUDGE_CALIBRATION_PATH.parent / "calibration_samples.json"
    if not cal_path.exists():
        print(f"No calibration samples found at {cal_path}")
        print("Run: python -m scripts.study3.phase0_judge_calibration --step extract")
        return

    samples = load_json(cal_path)

    # Strip model identity (blind evaluation) and keep only what annotators need
    export = []
    for s in samples:
        export.append({
            "sample_id": s["sample_id"],
            "domain": s["domain"],
            "turn": s["turn"],
            "task_prompt": s["task_prompt"],
            "output": s["output"],
        })

    out_path = Path(__file__).resolve().parent.parent.parent / "annotator-ui" / "public" / "samples.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(export, f, indent=2)

    print(f"Exported {len(export)} blinded samples to {out_path}")
    print("Annotators can load this file in the web UI.")


if __name__ == "__main__":
    main()
