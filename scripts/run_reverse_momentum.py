"""Run the reverse momentum experiment: affirming feedback before evaluative probe."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.config import (
    MODELS,
    REVERSE_MOMENTUM_MATRIX_PATH,
    REVERSE_MOMENTUM_TRIALS_PATH,
    RUNS_PER_CELL,
)
from scripts.utils import (
    append_jsonl,
    chat_n_turns,
    load_json,
    load_jsonl,
    log_experiment_metadata,
)


def make_trial_id(model: str, scenario_id: str, framing: str,
                  level: int, run: int) -> str:
    return f"{model}__{scenario_id}__{framing}__{level}__reverse_d1__run{run}"


def build_trial_list(matrix: list[dict], model_name: str) -> list[dict]:
    model_cfg = MODELS[model_name]
    trials = []
    for cell in matrix:
        for run in range(1, RUNS_PER_CELL + 1):
            trial_id = make_trial_id(
                model_name, cell["scenario_id"], cell["framing"],
                cell["threshold_level"], run,
            )
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
    parser = argparse.ArgumentParser(description="Run reverse momentum experiment")
    parser.add_argument("--model", required=True, choices=list(MODELS.keys()))
    parser.add_argument("--retry-errors", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    matrix = load_json(REVERSE_MOMENTUM_MATRIX_PATH)
    model_cfg = MODELS[args.model]
    log_experiment_metadata(args.model, model_cfg["model_id"])
    all_trials = build_trial_list(matrix, args.model)

    completed = get_completed_ids(REVERSE_MOMENTUM_TRIALS_PATH)

    if args.retry_errors:
        failed = {r["trial_id"] for r in load_jsonl(REVERSE_MOMENTUM_TRIALS_PATH)
                  if r.get("status") == "error"} - completed
        pending = [t for t in all_trials if t["trial_id"] in failed]
        print(f"Retrying {len(pending)} failed trials for {args.model}")
    else:
        pending = [t for t in all_trials if t["trial_id"] not in completed]
        print(f"{len(pending)} pending trials for {args.model} ({len(completed)} done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit} trials")

    for i, trial in enumerate(pending, 1):
        print(f"[{i}/{len(pending)}] {trial['trial_id']}")
        result = run_trial(trial)
        append_jsonl(result, REVERSE_MOMENTUM_TRIALS_PATH)
        if result["status"] == "error":
            print(f"  ERROR: {result['error']}")
        else:
            final_len = len(result['final_response']) if result['final_response'] else 0
            print(f"  OK ({result['n_turns']} turns, {final_len} chars in final)")

    print("Done.")


if __name__ == "__main__":
    main()
