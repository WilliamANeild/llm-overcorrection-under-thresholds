"""Phase 3: One-Shot Ceiling Test for the Revision Yield experiment.

For each task, a fresh model instance produces a single "best possible" output.
This tests RQ10: does one-shot match or beat the iterative turn-5 output?

If one-shot quality >= turn-5 quality, iterative revision has zero net value.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import (
    MODELS,
    S3_MATRIX_PATH,
    S3_ONESHOT_INSTRUCTION,
    S3_ONESHOT_TRIALS_PATH,
    S3_RUNS_PER_CELL,
)
from scripts.utils import (
    append_jsonl,
    get_anthropic_client,
    get_google_client,
    get_openai_client,
    get_together_client,
    load_json,
    load_jsonl,
    log_experiment_metadata,
    rate_limit,
    retry_with_backoff,
)


def make_trial_id(model: str, scenario_id: str, run: int) -> str:
    return f"s3_oneshot__{model}__{scenario_id}__run{run}"


def build_oneshot_prompt(task_prompt: str) -> str:
    return f"{task_prompt}\n\n{S3_ONESHOT_INSTRUCTION}"


def call_oneshot(provider: str, model_id: str, prompt: str) -> dict:
    """Single-turn generation at temperature 1.0."""
    rate_limit(provider)

    if provider == "openai":
        client = get_openai_client()
        r = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=1.0,
        )
        text = r.choices[0].message.content
        tokens = {"input": r.usage.prompt_tokens, "output": r.usage.completion_tokens}

    elif provider == "anthropic":
        client = get_anthropic_client()
        r = retry_with_backoff(
            client.messages.create,
            model=model_id,
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
            temperature=1.0,
        )
        text = r.content[0].text
        tokens = {"input": r.usage.input_tokens, "output": r.usage.output_tokens}

    elif provider == "google":
        from google.genai import types
        client = get_google_client()
        config = types.GenerateContentConfig(temperature=1.0)
        r = retry_with_backoff(
            client.models.generate_content,
            model=model_id,
            contents=prompt,
            config=config,
        )
        text = r.text
        tokens = {
            "input": r.usage_metadata.prompt_token_count if hasattr(r, 'usage_metadata') and r.usage_metadata else None,
            "output": r.usage_metadata.candidates_token_count if hasattr(r, 'usage_metadata') and r.usage_metadata else None,
        }

    elif provider == "together":
        client = get_together_client()
        r = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=1.0,
        )
        text = r.choices[0].message.content
        tokens = {"input": r.usage.prompt_tokens, "output": r.usage.completion_tokens}

    else:
        raise ValueError(f"Unknown provider: {provider}")

    return {"response": text, "tokens": tokens}


def main():
    parser = argparse.ArgumentParser(
        description="Phase 3: One-shot ceiling test for Study 3"
    )
    parser.add_argument("--model", required=True, choices=list(MODELS.keys()))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--domain", choices=["code", "data_logic", "analysis", "writing", "creative"], default=None)
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
            trials.append({
                "trial_id": make_trial_id(args.model, cell["scenario_id"], run),
                "model": args.model,
                "scenario_id": cell["scenario_id"],
                "scenario_label": cell["scenario_label"],
                "domain": cell["domain"],
                "task_prompt": cell["task_prompt"],
                "run": run,
            })

    # Skip completed
    existing = load_jsonl(S3_ONESHOT_TRIALS_PATH)
    completed = {r["trial_id"] for r in existing if r.get("status") == "success"}
    pending = [t for t in trials if t["trial_id"] not in completed]

    print(f"{len(pending)} pending one-shot trials for {args.model} ({len(completed)} done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit}")

    provider = model_cfg["provider"]
    model_id = model_cfg["model_id"]

    for i, trial in enumerate(pending, 1):
        print(f"[{i}/{len(pending)}] {trial['trial_id']}")
        prompt = build_oneshot_prompt(trial["task_prompt"])

        try:
            result = call_oneshot(provider, model_id, prompt)
            record = {
                **trial,
                "prompt": prompt,
                "response": result["response"],
                "tokens": result["tokens"],
                "status": "success",
                "error": None,
            }
            append_jsonl(record, S3_ONESHOT_TRIALS_PATH)
            out_tokens = result["tokens"].get("output", 0) or 0
            print(f"  OK ({out_tokens} output tokens)")
        except Exception as e:
            record = {
                **trial,
                "prompt": prompt,
                "response": None,
                "tokens": None,
                "status": "error",
                "error": str(e),
            }
            append_jsonl(record, S3_ONESHOT_TRIALS_PATH)
            print(f"  ERROR: {e}")

    print("Done.")


if __name__ == "__main__":
    main()
