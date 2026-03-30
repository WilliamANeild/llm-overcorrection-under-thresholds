"""Run the experiment: expand prompt matrix into trials and execute two-turn conversations."""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.config import MODELS, PROMPT_MATRIX_PATH, TRIALS_PATH, RUNS_PER_CELL
from scripts.utils import load_json, load_jsonl, append_jsonl, make_trial_id, chat_two_turns, log_experiment_metadata


def build_trial_list(matrix: list[dict], model_name: str) -> list[dict]:
    """Expand the prompt matrix into individual trials for a given model."""
    model_cfg = MODELS[model_name]
    trials = []
    for cell in matrix:
        for run in range(1, RUNS_PER_CELL + 1):
            trial_id = make_trial_id(
                model_name,
                cell["scenario_id"],
                cell["framing"],
                cell["threshold_level"],
                run,
            )
            trials.append({
                "trial_id": trial_id,
                "model": model_name,
                "provider": model_cfg["provider"],
                "model_id": model_cfg["model_id"],
                "run": run,
                **cell,
            })
    return trials


def get_completed_ids(path: Path) -> set[str]:
    records = load_jsonl(path)
    return {r["trial_id"] for r in records if r.get("status") == "success"}


def get_failed_ids(path: Path) -> set[str]:
    records = load_jsonl(path)
    return {r["trial_id"] for r in records if r.get("status") == "error"}


def run_trial(trial: dict) -> dict:
    """Execute a single trial and return the result record."""
    try:
        result = chat_two_turns(
            provider=trial["provider"],
            model_id=trial["model_id"],
            turn1_prompt=trial["turn1_prompt"],
            turn2_prompt=trial["turn2_prompt"],
        )
        return {
            "trial_id": trial["trial_id"],
            "model": trial["model"],
            "scenario_id": trial["scenario_id"],
            "scenario_label": trial["scenario_label"],
            "framing": trial["framing"],
            "threshold_level": trial["threshold_level"],
            "threshold_text": trial["threshold_text"],
            "run": trial["run"],
            "turn1_prompt": trial["turn1_prompt"],
            "turn2_prompt": trial["turn2_prompt"],
            "turn1_response": result["turn1_response"],
            "turn2_response": result["turn2_response"],
            "status": "success",
            "error": None,
        }
    except Exception as e:
        return {
            "trial_id": trial["trial_id"],
            "model": trial["model"],
            "scenario_id": trial["scenario_id"],
            "scenario_label": trial["scenario_label"],
            "framing": trial["framing"],
            "threshold_level": trial["threshold_level"],
            "threshold_text": trial["threshold_text"],
            "run": trial["run"],
            "turn1_prompt": trial["turn1_prompt"],
            "turn2_prompt": trial["turn2_prompt"],
            "turn1_response": None,
            "turn2_response": None,
            "status": "error",
            "error": str(e),
        }


def main():
    parser = argparse.ArgumentParser(description="Run experiment trials")
    parser.add_argument(
        "--model",
        required=True,
        choices=list(MODELS.keys()),
        help="Which model to run",
    )
    parser.add_argument(
        "--retry-errors",
        action="store_true",
        help="Re-run previously failed trials",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Limit number of trials to run (0 = all)",
    )
    args = parser.parse_args()

    matrix = load_json(PROMPT_MATRIX_PATH)
    model_cfg = MODELS[args.model]
    log_experiment_metadata(args.model, model_cfg["model_id"])
    all_trials = build_trial_list(matrix, args.model)

    completed = get_completed_ids(TRIALS_PATH)

    if args.retry_errors:
        failed = get_failed_ids(TRIALS_PATH)
        pending = [t for t in all_trials if t["trial_id"] in failed]
        print(f"Retrying {len(pending)} failed trials for {args.model}")
    else:
        pending = [t for t in all_trials if t["trial_id"] not in completed]
        print(f"{len(pending)} pending trials for {args.model} ({len(completed)} already done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit} trials")

    for i, trial in enumerate(pending, 1):
        print(f"[{i}/{len(pending)}] {trial['trial_id']}")
        result = run_trial(trial)
        append_jsonl(result, TRIALS_PATH)

        if result["status"] == "error":
            print(f"  ERROR: {result['error']}")
        else:
            print(f"  OK ({len(result['turn2_response'])} chars in turn 2)")

    print("Done.")


if __name__ == "__main__":
    main()
