"""Phase 6 (Self-Reflection): For the Revision Yield experiment.

RQ14: Can the model identify its own overcorrection?

Protocol: Load Phase 1 conversations, append a 6th turn with a self-reflection
probe, send the full context at temperature 0.0, and parse the recommended turn.

Probe:
  Looking back at all your versions across this conversation, which one would
  you recommend the user actually use? Reply with ONLY a JSON object:
  {"recommended_turn": 1-5, "reason": "one sentence explanation"}
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import (
    MAX_OUTPUT_TOKENS_JUDGE,
    MODELS,
    S3_SELF_REFLECTION_PATH,
    S3_SELF_REFLECTION_PROBE,
    S3_WORKER_TRIALS_PATH,
)
from scripts.utils import (
    append_jsonl,
    extract_gemini_text,
    get_anthropic_client,
    get_google_client,
    get_openai_client,
    get_together_client,
    load_jsonl,
    rate_limit,
    retry_with_backoff,
)


def make_result_id(worker_trial_id: str) -> str:
    return f"s3_reflect__{worker_trial_id}"


def parse_reflection_response(text: str) -> dict | None:
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        text = "\n".join(lines)
    try:
        data = json.loads(text)
        if "recommended_turn" in data:
            turn = int(data["recommended_turn"])
            if 1 <= turn <= 5:
                return {
                    "recommended_turn": turn,
                    "reason": data.get("reason", ""),
                }
    except (json.JSONDecodeError, ValueError):
        pass
    return None


def call_reflection(provider: str, model_id: str, messages: list[dict]) -> dict | None:
    """Send the full conversation + reflection probe and parse response."""
    for attempt in range(2):
        rate_limit(provider)

        if provider == "openai":
            client = get_openai_client()
            r = retry_with_backoff(
                client.chat.completions.create,
                model=model_id,
                messages=messages,
                temperature=0.0,
                max_tokens=MAX_OUTPUT_TOKENS_JUDGE,
            )
            text = r.choices[0].message.content

        elif provider == "anthropic":
            client = get_anthropic_client()
            r = retry_with_backoff(
                client.messages.create,
                model=model_id,
                max_tokens=MAX_OUTPUT_TOKENS_JUDGE,
                messages=messages,
                temperature=0.0,
            )
            text = r.content[0].text

        elif provider == "google":
            from google.genai import types
            client = get_google_client()
            config = types.GenerateContentConfig(
                temperature=0.0,
                max_output_tokens=MAX_OUTPUT_TOKENS_JUDGE,
            )
            # Convert messages to Google format
            contents = []
            for msg in messages:
                role = "model" if msg["role"] == "assistant" else "user"
                contents.append({"role": role, "parts": [{"text": msg["content"]}]})
            r = retry_with_backoff(
                client.models.generate_content,
                model=model_id,
                contents=contents,
                config=config,
            )
            text = extract_gemini_text(r)

        elif provider == "together":
            client = get_together_client()
            r = retry_with_backoff(
                client.chat.completions.create,
                model=model_id,
                messages=messages,
                temperature=0.0,
                max_tokens=MAX_OUTPUT_TOKENS_JUDGE,
            )
            text = r.choices[0].message.content

        else:
            raise ValueError(f"Unknown provider: {provider}")

        parsed = parse_reflection_response(text)
        if parsed:
            return {**parsed, "raw_response": text}

        if attempt == 0:
            print(f"    Parse failed, retrying...")

    print(f"    Parse failed after retry. Raw: {text[:200]}")
    return None


def rebuild_conversation(trial: dict) -> list[dict]:
    """Rebuild the multi-turn conversation as a message list."""
    messages = []
    prompts = trial["prompts"]
    responses = trial["responses"]

    for i in range(len(responses)):
        messages.append({"role": "user", "content": prompts[i]})
        messages.append({"role": "assistant", "content": responses[i]})

    # Append the reflection probe as the final user turn
    messages.append({"role": "user", "content": S3_SELF_REFLECTION_PROBE})
    return messages


def main():
    parser = argparse.ArgumentParser(
        description="Phase 6: Self-reflection test for Study 3"
    )
    parser.add_argument("--model", required=True, choices=list(MODELS.keys()))
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    model_cfg = MODELS[args.model]
    provider = model_cfg["provider"]
    model_id = model_cfg["model_id"]

    # Load worker trials with all 5 turns
    all_trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    worker_trials = [
        t for t in all_trials
        if t.get("status") == "success"
        and t["model"] == args.model
        and len(t.get("responses", [])) >= 5
    ]
    print(f"Found {len(worker_trials)} completed 5-turn trials for {args.model}")

    # Skip completed
    existing = load_jsonl(S3_SELF_REFLECTION_PATH)
    completed = {r["result_id"] for r in existing}

    pending = []
    for trial in worker_trials:
        result_id = make_result_id(trial["trial_id"])
        if result_id not in completed:
            pending.append(trial)

    print(f"{len(pending)} pending reflections ({len(completed)} done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit}")

    for i, trial in enumerate(pending, 1):
        result_id = make_result_id(trial["trial_id"])
        print(f"[{i}/{len(pending)}] {result_id}")

        messages = rebuild_conversation(trial)
        result = call_reflection(provider, model_id, messages)

        if result:
            record = {
                "result_id": result_id,
                "worker_trial_id": trial["trial_id"],
                "model": args.model,
                "scenario_id": trial["scenario_id"],
                "domain": trial["domain"],
                "run": trial["run"],
                "recommended_turn": result["recommended_turn"],
                "reason": result["reason"],
                "raw_response": result["raw_response"],
            }
            append_jsonl(record, S3_SELF_REFLECTION_PATH)
            print(f"    Recommends turn {result['recommended_turn']}: {result['reason'][:60]}")
        else:
            record = {
                "result_id": result_id,
                "worker_trial_id": trial["trial_id"],
                "model": args.model,
                "scenario_id": trial["scenario_id"],
                "domain": trial["domain"],
                "run": trial["run"],
                "recommended_turn": None,
                "reason": None,
                "raw_response": None,
            }
            append_jsonl(record, S3_SELF_REFLECTION_PATH)
            print(f"    SKIPPED (parse failure)")

    print("Done.")


if __name__ == "__main__":
    main()
