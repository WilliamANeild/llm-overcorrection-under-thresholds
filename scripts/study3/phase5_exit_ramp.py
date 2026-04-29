"""Phase 5: Exit Ramp Test for the Revision Yield experiment.

Tests RQ12: Can the revision loop be broken by giving the model explicit
permission to stop?

Structure:
  Turn 1: task prompt -> initial output
  Turn 2: "Can this be improved?" -> revision
  Turn 3: EXIT RAMP probe (gives explicit permission to say "done")
  Turn 4: "Can this be improved?" -> (does it resume revising after the ramp?)
  Turn 5: "Can this be improved?" -> final

Compares to Phase 1 where turn 3 is just "Can this be improved?" again.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import (
    MODELS,
    S3_EXIT_RAMP_PROBE,
    S3_EXIT_RAMP_TRIALS_PATH,
    S3_MATRIX_PATH,
    S3_RUNS_PER_CELL,
    S3_WORKING_PROBE,
)
from scripts.utils import (
    append_jsonl,
    load_json,
    load_jsonl,
    log_experiment_metadata,
)
from scripts.study3.phase1_worker import chat_n_turns_with_tokens


def make_trial_id(model: str, scenario_id: str, run: int) -> str:
    return f"s3_exitramp__{model}__{scenario_id}__run{run}"


def build_exit_ramp_prompts(task_prompt: str) -> list[str]:
    """Build the 5-turn prompt sequence with exit ramp at turn 3."""
    return [
        task_prompt,              # Turn 1: initial task
        S3_WORKING_PROBE,         # Turn 2: "Can this be improved?"
        S3_EXIT_RAMP_PROBE,       # Turn 3: EXIT RAMP (permission to stop)
        S3_WORKING_PROBE,         # Turn 4: back to "Can this be improved?"
        S3_WORKING_PROBE,         # Turn 5: "Can this be improved?"
    ]


def main():
    parser = argparse.ArgumentParser(
        description="Phase 5: Exit ramp test for Study 3"
    )
    parser.add_argument("--model", required=True, choices=list(MODELS.keys()))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--domain", choices=["code", "data_logic", "analysis", "writing", "creative"], default=None)
    parser.add_argument("--retry-errors", action="store_true")
    args = parser.parse_args()

    matrix = load_json(S3_MATRIX_PATH)
    model_cfg = MODELS[args.model]
    log_experiment_metadata(args.model, model_cfg["model_id"])

    if args.domain:
        matrix = [c for c in matrix if c["domain"] == args.domain]

    # Build trial list
    trials = []
    for cell in matrix:
        for run in range(1, S3_RUNS_PER_CELL + 1):
            trial_id = make_trial_id(args.model, cell["scenario_id"], run)
            prompts = build_exit_ramp_prompts(cell["task_prompt"])
            trials.append({
                "trial_id": trial_id,
                "model": args.model,
                "provider": model_cfg["provider"],
                "model_id": model_cfg["model_id"],
                "scenario_id": cell["scenario_id"],
                "scenario_label": cell["scenario_label"],
                "domain": cell["domain"],
                "task_prompt": cell["task_prompt"],
                "run": run,
                "prompts": prompts,
            })

    # Skip completed
    existing = load_jsonl(S3_EXIT_RAMP_TRIALS_PATH)
    completed = {r["trial_id"] for r in existing if r.get("status") == "success"}
    failed = {r["trial_id"] for r in existing if r.get("status") == "error"}

    if args.retry_errors:
        pending = [t for t in trials if t["trial_id"] in failed and t["trial_id"] not in completed]
        print(f"Retrying {len(pending)} failed trials")
    else:
        pending = [t for t in trials if t["trial_id"] not in completed]
        print(f"{len(pending)} pending exit ramp trials for {args.model} ({len(completed)} done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit}")

    for i, trial in enumerate(pending, 1):
        print(f"[{i}/{len(pending)}] {trial['trial_id']} ({trial['domain']})")

        try:
            result = chat_n_turns_with_tokens(
                provider=trial["provider"],
                model_id=trial["model_id"],
                prompts=trial["prompts"],
            )
            record = {
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "scenario_id": trial["scenario_id"],
                "scenario_label": trial["scenario_label"],
                "domain": trial["domain"],
                "task_prompt": trial["task_prompt"],
                "run": trial["run"],
                "prompts": trial["prompts"],
                "responses": result["responses"],
                "token_counts": result["token_counts"],
                "n_turns": len(result["responses"]),
                "status": "success",
                "error": None,
            }
            append_jsonl(record, S3_EXIT_RAMP_TRIALS_PATH)
            # Check if model accepted the exit ramp at turn 3
            t3_response = result["responses"][2] if len(result["responses"]) > 2 else ""
            accepted = not _is_revision(t3_response)
            print(f"  OK - Exit ramp {'ACCEPTED' if accepted else 'IGNORED'}")
        except Exception as e:
            record = {
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "scenario_id": trial["scenario_id"],
                "scenario_label": trial["scenario_label"],
                "domain": trial["domain"],
                "task_prompt": trial["task_prompt"],
                "run": trial["run"],
                "prompts": trial["prompts"],
                "responses": None,
                "token_counts": None,
                "n_turns": 0,
                "status": "error",
                "error": str(e),
            }
            append_jsonl(record, S3_EXIT_RAMP_TRIALS_PATH)
            print(f"  ERROR: {e}")

    print("Done.")


def _is_revision(response: str) -> bool:
    """Quick check if a response is a revision vs accepting the output is done.

    Uses the same phrase list as analyze.classify_revision for consistency.
    """
    from scripts.study3.analyze import classify_revision
    return classify_revision(response)


if __name__ == "__main__":
    main()
