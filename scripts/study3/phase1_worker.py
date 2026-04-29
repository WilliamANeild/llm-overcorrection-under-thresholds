"""Phase 1: Run working model conversations for the Revision Yield experiment.

Each trial is a 5-turn conversation:
  Turn 1: task prompt -> initial output
  Turns 2-5: "Can this be improved?" -> revision (or decline)

All outputs at every turn are stored. Token counts are logged per turn.
Temperature 1.0 for the working model (matching Studies 1-2).
"""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import (
    MODELS,
    S3_MATRIX_PATH,
    S3_RUNS_PER_CELL,
    S3_WORKER_TRIALS_PATH,
)
from scripts.utils import (
    append_jsonl,
    load_json,
    load_jsonl,
    log_experiment_metadata,
    rate_limit,
    retry_with_backoff,
    get_openai_client,
    get_anthropic_client,
    get_google_client,
)


def make_trial_id(model: str, scenario_id: str, run: int) -> str:
    return f"s3_worker__{model}__{scenario_id}__run{run}"


def chat_n_turns_with_tokens(provider: str, model_id: str, prompts: list[str]) -> dict:
    """Send an N-turn conversation and return responses with token counts per turn."""
    responses = []
    token_counts = []

    if provider == "openai":
        client = get_openai_client()
        messages = []
        for prompt in prompts:
            rate_limit(provider)
            messages.append({"role": "user", "content": prompt})
            r = retry_with_backoff(
                client.chat.completions.create,
                model=model_id,
                messages=messages,
                temperature=1.0,
            )
            text = r.choices[0].message.content
            tokens = {
                "input": r.usage.prompt_tokens if r.usage else None,
                "output": r.usage.completion_tokens if r.usage else None,
            }
            responses.append(text)
            token_counts.append(tokens)
            messages.append({"role": "assistant", "content": text})

    elif provider == "anthropic":
        client = get_anthropic_client()
        messages = []
        for prompt in prompts:
            rate_limit(provider)
            messages.append({"role": "user", "content": prompt})
            r = retry_with_backoff(
                client.messages.create,
                model=model_id,
                max_tokens=4096,
                messages=messages,
                temperature=1.0,
            )
            text = r.content[0].text
            tokens = {
                "input": r.usage.input_tokens if r.usage else None,
                "output": r.usage.output_tokens if r.usage else None,
            }
            responses.append(text)
            token_counts.append(tokens)
            messages.append({"role": "assistant", "content": text})

    elif provider == "google":
        from google.genai import types
        client = get_google_client()
        config = types.GenerateContentConfig(temperature=1.0)
        contents = []
        for prompt in prompts:
            rate_limit(provider)
            contents.append({"role": "user", "parts": [{"text": prompt}]})
            r = retry_with_backoff(
                client.models.generate_content,
                model=model_id,
                contents=contents,
                config=config,
            )
            text = r.text
            tokens = {
                "input": r.usage_metadata.prompt_token_count if hasattr(r, 'usage_metadata') and r.usage_metadata else None,
                "output": r.usage_metadata.candidates_token_count if hasattr(r, 'usage_metadata') and r.usage_metadata else None,
            }
            responses.append(text)
            token_counts.append(tokens)
            contents.append({"role": "model", "parts": [{"text": text}]})

    else:
        raise ValueError(f"Unknown provider: {provider}")

    return {"responses": responses, "token_counts": token_counts}


def build_trial_list(matrix: list[dict], model_name: str) -> list[dict]:
    model_cfg = MODELS[model_name]
    trials = []
    for cell in matrix:
        for run in range(1, S3_RUNS_PER_CELL + 1):
            trial_id = make_trial_id(model_name, cell["scenario_id"], run)
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
        result = chat_n_turns_with_tokens(
            provider=trial["provider"],
            model_id=trial["model_id"],
            prompts=trial["prompts"],
        )
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
            "responses": result["responses"],
            "token_counts": result["token_counts"],
            "n_turns": len(result["responses"]),
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
            "token_counts": None,
            "n_turns": 0,
            "status": "error",
            "error": str(e),
        }


def main():
    parser = argparse.ArgumentParser(
        description="Phase 1: Run working model conversations for Study 3"
    )
    parser.add_argument("--model", required=True, choices=list(MODELS.keys()))
    parser.add_argument("--retry-errors", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--domain", choices=["code", "data_logic", "analysis", "writing", "creative"], default=None)
    args = parser.parse_args()

    matrix = load_json(S3_MATRIX_PATH)
    model_cfg = MODELS[args.model]
    log_experiment_metadata(args.model, model_cfg["model_id"])
    all_trials = build_trial_list(matrix, args.model)

    if args.domain:
        all_trials = [t for t in all_trials if t["domain"] == args.domain]

    completed = get_completed_ids(S3_WORKER_TRIALS_PATH)

    if args.retry_errors:
        failed = get_failed_ids(S3_WORKER_TRIALS_PATH)
        pending = [t for t in all_trials if t["trial_id"] in failed and t["trial_id"] not in completed]
        print(f"Retrying {len(pending)} failed trials for {args.model}")
    else:
        pending = [t for t in all_trials if t["trial_id"] not in completed]
        print(f"{len(pending)} pending worker trials for {args.model} ({len(completed)} already done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit} trials")

    for i, trial in enumerate(pending, 1):
        print(f"[{i}/{len(pending)}] {trial['trial_id']} ({trial['domain']})")
        result = run_trial(trial)
        append_jsonl(result, S3_WORKER_TRIALS_PATH)

        if result["status"] == "error":
            print(f"  ERROR: {result['error']}")
        else:
            total_out = sum(t.get("output", 0) or 0 for t in result["token_counts"])
            print(f"  OK ({result['n_turns']} turns, {total_out} output tokens)")

    print("Done.")


if __name__ == "__main__":
    main()
