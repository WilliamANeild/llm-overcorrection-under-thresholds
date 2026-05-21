"""Phase 3: Model Confidence (Revision Ceiling) for the Revision Yield experiment.

Measures how many times each model will revise with zero additional input before
voluntarily stopping. Unlike Phase 1 (capped at 5 turns), this runs uncapped
until the model declines to revise (up to a safety max of 20 turns).

Two probe conditions are tested:
  A (minimal):  "Is there anything you'd like to change?"
  B (balanced):  Same as Phase 1 probe (for direct comparability)

This is a meta-behavioral study - quality is not measured here. We only care
about when models stop and whether that differs by domain and probe condition.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import (
    MAX_OUTPUT_TOKENS_GENERATION,
    MODELS,
    S3_CONFIDENCE_MAX_TURNS,
    S3_CONFIDENCE_PROBES,
    S3_CONFIDENCE_TRIALS_PATH,
    S3_DOMAINS,
    S3_MATRIX_PATH,
    S3_RUNS_PER_CELL,
)
from scripts.study3.analyze import classify_revision
from scripts.utils import (
    append_jsonl,
    extract_gemini_text,
    extract_gemini_tokens,
    get_anthropic_client,
    get_deepseek_client,
    get_google_client,
    get_openai_client,
    get_together_client,
    load_json,
    load_jsonl,
    log_experiment_metadata,
    print_cost_summary,
    rate_limit,
    retry_with_backoff,
    track_cost,
)


def make_trial_id(model: str, scenario_id: str, probe_key: str, run: int) -> str:
    return f"s3_confidence__{model}__{scenario_id}__{probe_key}__run{run}"


def send_turn(provider: str, model_id: str, messages: list, client=None) -> dict:
    """Send a single turn in an ongoing conversation. Returns response text and tokens."""
    rate_limit(provider)

    if provider == "openai":
        if client is None:
            client = get_openai_client()
        r = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=messages,
            temperature=1.0,
            max_tokens=MAX_OUTPUT_TOKENS_GENERATION,
        )
        text = r.choices[0].message.content
        tokens = {
            "input": r.usage.prompt_tokens if r.usage else None,
            "output": r.usage.completion_tokens if r.usage else None,
        }

    elif provider == "anthropic":
        if client is None:
            client = get_anthropic_client()
        r = retry_with_backoff(
            client.messages.create,
            model=model_id,
            max_tokens=MAX_OUTPUT_TOKENS_GENERATION,
            messages=messages,
            temperature=1.0,
        )
        text = r.content[0].text
        tokens = {
            "input": r.usage.input_tokens if r.usage else None,
            "output": r.usage.output_tokens if r.usage else None,
        }

    elif provider == "google":
        from google.genai import types
        if client is None:
            client = get_google_client()
        config = types.GenerateContentConfig(
            temperature=1.0,
            max_output_tokens=MAX_OUTPUT_TOKENS_GENERATION,
        )
        # Convert messages to Gemini format
        contents = []
        for m in messages:
            role = "model" if m["role"] == "assistant" else "user"
            contents.append({"role": role, "parts": [{"text": m["content"]}]})
        r = retry_with_backoff(
            client.models.generate_content,
            model=model_id,
            contents=contents,
            config=config,
        )
        text = extract_gemini_text(r)
        tokens = extract_gemini_tokens(r)

    elif provider == "together":
        if client is None:
            client = get_together_client()
        r = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=messages,
            temperature=1.0,
            max_tokens=MAX_OUTPUT_TOKENS_GENERATION,
        )
        text = r.choices[0].message.content
        tokens = {
            "input": r.usage.prompt_tokens if r.usage else None,
            "output": r.usage.completion_tokens if r.usage else None,
        }

    elif provider == "deepseek":
        if client is None:
            client = get_deepseek_client()
        r = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=messages,
            temperature=1.0,
            max_tokens=MAX_OUTPUT_TOKENS_GENERATION,
        )
        text = r.choices[0].message.content
        tokens = {
            "input": r.usage.prompt_tokens if r.usage else None,
            "output": r.usage.completion_tokens if r.usage else None,
        }

    else:
        raise ValueError(f"Unknown provider: {provider}")

    track_cost(model_id, tokens.get("input"), tokens.get("output"))
    return {"text": text, "tokens": tokens}


def run_confidence_trial(
    provider: str, model_id: str, task_prompt: str, probe: str
) -> dict:
    """Run a single confidence trial: task -> probe until model stops or hits max."""
    messages = [{"role": "user", "content": task_prompt}]
    responses = []
    token_counts = []
    stopped_voluntarily = False

    # Turn 1: initial output
    result = send_turn(provider, model_id, messages)
    responses.append(result["text"])
    token_counts.append(result["tokens"])
    messages.append({"role": "assistant", "content": result["text"]})

    # Turns 2+: probe until model declines or we hit the safety cap
    for turn in range(2, S3_CONFIDENCE_MAX_TURNS + 1):
        messages.append({"role": "user", "content": probe})
        result = send_turn(provider, model_id, messages)
        responses.append(result["text"])
        token_counts.append(result["tokens"])
        messages.append({"role": "assistant", "content": result["text"]})

        # Check if model declined to revise
        if not classify_revision(result["text"]):
            stopped_voluntarily = True
            break

    return {
        "responses": responses,
        "token_counts": token_counts,
        "n_turns": len(responses),
        "stopped_voluntarily": stopped_voluntarily,
        "stop_turn": len(responses) if stopped_voluntarily else None,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Phase 3: Model confidence (revision ceiling) for Study 3"
    )
    parser.add_argument("--model", required=True, choices=list(MODELS.keys()))
    parser.add_argument("--probe", choices=list(S3_CONFIDENCE_PROBES.keys()), default=None,
                        help="Run only one probe condition (default: both)")
    parser.add_argument("--retry-errors", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--domain", choices=S3_DOMAINS, default=None)
    args = parser.parse_args()

    matrix = load_json(S3_MATRIX_PATH)
    model_cfg = MODELS[args.model]
    log_experiment_metadata(args.model, model_cfg["model_id"])

    if args.domain:
        matrix = [c for c in matrix if c["domain"] == args.domain]

    # Determine which probes to run
    probe_keys = [args.probe] if args.probe else list(S3_CONFIDENCE_PROBES.keys())

    # Build trial list
    trials = []
    for cell in matrix:
        for probe_key in probe_keys:
            for run in range(1, S3_RUNS_PER_CELL + 1):
                trials.append({
                    "trial_id": make_trial_id(args.model, cell["scenario_id"], probe_key, run),
                    "model": args.model,
                    "scenario_id": cell["scenario_id"],
                    "scenario_label": cell["scenario_label"],
                    "domain": cell["domain"],
                    "task_prompt": cell["task_prompt"],
                    "probe_key": probe_key,
                    "probe_text": S3_CONFIDENCE_PROBES[probe_key],
                    "run": run,
                })

    # Skip completed
    existing = load_jsonl(S3_CONFIDENCE_TRIALS_PATH)
    completed = {r["trial_id"] for r in existing if r.get("status") == "success"}

    if args.retry_errors:
        failed = {r["trial_id"] for r in existing if r.get("status") == "error"}
        pending = [t for t in trials if t["trial_id"] in failed and t["trial_id"] not in completed]
        print(f"Retrying {len(pending)} failed trials for {args.model}")
    else:
        pending = [t for t in trials if t["trial_id"] not in completed]
        print(f"{len(pending)} pending confidence trials for {args.model} ({len(completed)} done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit} trials")

    provider = model_cfg["provider"]
    model_id = model_cfg["model_id"]

    for i, trial in enumerate(pending, 1):
        print(f"[{i}/{len(pending)}] {trial['trial_id']} ({trial['domain']}, probe={trial['probe_key']})")

        try:
            result = run_confidence_trial(
                provider, model_id, trial["task_prompt"], trial["probe_text"]
            )
            record = {
                **trial,
                "responses": result["responses"],
                "token_counts": result["token_counts"],
                "n_turns": result["n_turns"],
                "stopped_voluntarily": result["stopped_voluntarily"],
                "stop_turn": result["stop_turn"],
                "status": "success",
                "error": None,
            }
            append_jsonl(record, S3_CONFIDENCE_TRIALS_PATH)
            status = f"stopped at turn {result['stop_turn']}" if result["stopped_voluntarily"] else f"hit cap ({S3_CONFIDENCE_MAX_TURNS})"
            total_out = sum(t.get("output", 0) or 0 for t in result["token_counts"])
            print(f"  OK - {status}, {result['n_turns']} turns, {total_out} output tokens")

        except Exception as e:
            record = {
                **trial,
                "responses": None,
                "token_counts": None,
                "n_turns": 0,
                "stopped_voluntarily": None,
                "stop_turn": None,
                "status": "error",
                "error": str(e),
            }
            append_jsonl(record, S3_CONFIDENCE_TRIALS_PATH)
            print(f"  ERROR: {e}")

    print_cost_summary()
    print("Done.")


if __name__ == "__main__":
    main()
