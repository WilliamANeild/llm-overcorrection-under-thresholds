"""Phase 1: Run working model conversations for the blind evaluator experiment.

Each trial is a multi-turn conversation:
  Turn 1: task prompt -> initial output
  Turns 2-5: "Can this be improved?" -> revision (or decline)

All outputs at every turn are stored so the blind evaluator can judge each one.
Temperature 1.0 for the working model (matching Studies 1-2).
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.config import (
    BLIND_EVAL_MATRIX_PATH,
    BLIND_EVAL_RUNS_PER_CELL,
    BLIND_EVAL_WORKER_TRIALS_PATH,
    MODELS,
)
from scripts.utils import (
    append_jsonl,
    chat_n_turns,
    load_json,
    load_jsonl,
    log_experiment_metadata,
)


def make_worker_trial_id(model: str, scenario_id: str, run: int) -> str:
    return f"blind_eval__{model}__{scenario_id}__run{run}"


def build_trial_list(matrix: list[dict], model_name: str) -> list[dict]:
    model_cfg = MODELS[model_name]
    trials = []
    for cell in matrix:
        for run in range(1, BLIND_EVAL_RUNS_PER_CELL + 1):
            trial_id = make_worker_trial_id(model_name, cell["scenario_id"], run)
            prompts = [cell["task_prompt"]] + cell["working_probes"]
            trials.append({
                "trial_id": trial_id,
                "model": model_name,
                "provider": model_cfg["provider"],
                "model_id": model_cfg["model_id"],
                "scenario_id": cell["scenario_id"],
                "scenario_label": cell["scenario_label"],
                "domain": cell["domain"],
                "task_prompt": cell["task_prompt"],
                "run": run,
                "max_turns": cell["max_turns"],
                "prompts": prompts,
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
            "domain": trial["domain"],
            "task_prompt": trial["task_prompt"],
            "run": trial["run"],
            "max_turns": trial["max_turns"],
            "prompts": trial["prompts"],
            "responses": responses,
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
            "domain": trial["domain"],
            "task_prompt": trial["task_prompt"],
            "run": trial["run"],
            "max_turns": trial["max_turns"],
            "prompts": trial["prompts"],
            "responses": None,
            "n_turns": 0,
            "status": "error",
            "error": str(e),
        }


def main():
    parser = argparse.ArgumentParser(
        description="Phase 1: Run working model conversations for blind evaluator experiment"
    )
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
        "--domain",
        choices=["writing", "code", "analysis"],
        default=None,
        help="Only run trials for a specific domain",
    )
    args = parser.parse_args()

    matrix = load_json(BLIND_EVAL_MATRIX_PATH)
    model_cfg = MODELS[args.model]
    log_experiment_metadata(args.model, model_cfg["model_id"])
    all_trials = build_trial_list(matrix, args.model)

    if args.domain:
        all_trials = [t for t in all_trials if t["domain"] == args.domain]

    completed = get_completed_ids(BLIND_EVAL_WORKER_TRIALS_PATH)

    if args.retry_errors:
        failed = get_failed_ids(BLIND_EVAL_WORKER_TRIALS_PATH)
        pending = [t for t in all_trials if t["trial_id"] in failed and t["trial_id"] not in completed]
        print(f"Retrying {len(pending)} failed trials for {args.model}")
    else:
        pending = [t for t in all_trials if t["trial_id"] not in completed]
        print(f"{len(pending)} pending worker trials for {args.model} ({len(completed)} already done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit} trials")

    for i, trial in enumerate(pending, 1):
        print(f"[{i}/{len(pending)}] {trial['trial_id']} ({trial['domain']}, {trial['max_turns']} turns)")
        result = run_trial(trial)
        append_jsonl(result, BLIND_EVAL_WORKER_TRIALS_PATH)

        if result["status"] == "error":
            print(f"  ERROR: {result['error']}")
        else:
            print(f"  OK ({result['n_turns']} turns)")
            for t, resp in enumerate(result["responses"], 1):
                preview = resp[:80].replace("\n", " ") if resp else "(empty)"
                print(f"    Turn {t}: {preview}...")

    print("Done.")


if __name__ == "__main__":
    main()
