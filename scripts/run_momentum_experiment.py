"""Run the momentum experiment: multi-turn conversations with leading probes
followed by an evaluative probe."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.config import MODELS, MOMENTUM_MATRIX_PATH, MOMENTUM_TRIALS_PATH, RUNS_PER_CELL
from scripts.utils import (
    append_jsonl,
    chat_n_turns,
    load_json,
    load_jsonl,
    log_experiment_metadata,
)


def make_momentum_trial_id(model: str, scenario_id: str, framing: str,
                           level: int, dose: int, run: int) -> str:
    return f"{model}__{scenario_id}__{framing}__{level}__momentum_d{dose}__run{run}"


def build_trial_list(matrix: list[dict], model_name: str) -> list[dict]:
    model_cfg = MODELS[model_name]
    trials = []
    for cell in matrix:
        for run in range(1, RUNS_PER_CELL + 1):
            trial_id = make_momentum_trial_id(
                model_name,
                cell["scenario_id"],
                cell["framing"],
                cell["threshold_level"],
                cell["dose"],
                run,
            )
            # Build full prompt sequence: turn1 + intermediate leading probes + final evaluative
            prompts = [cell["turn1_prompt"]] + cell["intermediate_probes"] + [cell["final_probe"]]
            trials.append({
                "trial_id": trial_id,
                "model": model_name,
                "provider": model_cfg["provider"],
                "model_id": model_cfg["model_id"],
                "run": run,
                "prompts": prompts,
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
    try:
        result = chat_n_turns(
            provider=trial["provider"],
            model_id=trial["model_id"],
            prompts=trial["prompts"],
        )
        responses = result["responses"]
        return {
            "trial_id": trial["trial_id"],
            "model": trial["model"],
            "scenario_id": trial["scenario_id"],
            "scenario_label": trial["scenario_label"],
            "framing": trial["framing"],
            "threshold_level": trial["threshold_level"],
            "threshold_text": trial["threshold_text"],
            "dose": trial["dose"],
            "run": trial["run"],
            "prompts": trial["prompts"],
            "responses": responses,
            "turn1_response": responses[0],
            "final_response": responses[-1],
            "final_probe": trial["final_probe"],
            "n_turns": len(responses),
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
            "dose": trial["dose"],
            "run": trial["run"],
            "prompts": trial["prompts"],
            "responses": None,
            "turn1_response": None,
            "final_response": None,
            "final_probe": trial["final_probe"],
            "n_turns": 0,
            "status": "error",
            "error": str(e),
        }


def main():
    parser = argparse.ArgumentParser(description="Run momentum experiment trials")
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
    parser.add_argument(
        "--dose",
        type=int,
        default=None,
        choices=[1, 2, 3],
        help="Only run trials for a specific dose level",
    )
    args = parser.parse_args()

    matrix = load_json(MOMENTUM_MATRIX_PATH)
    model_cfg = MODELS[args.model]
    log_experiment_metadata(args.model, model_cfg["model_id"])
    all_trials = build_trial_list(matrix, args.model)

    if args.dose is not None:
        all_trials = [t for t in all_trials if t["dose"] == args.dose]

    completed = get_completed_ids(MOMENTUM_TRIALS_PATH)

    if args.retry_errors:
        failed = get_failed_ids(MOMENTUM_TRIALS_PATH)
        pending = [t for t in all_trials if t["trial_id"] in failed and t["trial_id"] not in completed]
        print(f"Retrying {len(pending)} failed momentum trials for {args.model}")
    else:
        pending = [t for t in all_trials if t["trial_id"] not in completed]
        print(f"{len(pending)} pending momentum trials for {args.model} ({len(completed)} already done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit} trials")

    for i, trial in enumerate(pending, 1):
        print(f"[{i}/{len(pending)}] {trial['trial_id']} (dose={trial['dose']}, {len(trial['prompts'])} turns)")
        result = run_trial(trial)
        append_jsonl(result, MOMENTUM_TRIALS_PATH)

        if result["status"] == "error":
            print(f"  ERROR: {result['error']}")
        else:
            final_len = len(result['final_response']) if result['final_response'] else 0
            print(f"  OK ({result['n_turns']} turns, {final_len} chars in final)")

    print("Done.")


if __name__ == "__main__":
    main()
