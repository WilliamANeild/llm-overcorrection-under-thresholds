"""Phase 4: Reversibility Test for the Revision Yield experiment.

For each completed worker trial, a fresh instance of the same model sees BOTH
the turn-1 output and turn-5 output (randomized order, blinded) and picks which
one better fulfills the original task.

RQ11: If the model prefers turn-1 over turn-5, it's admitting its own revisions
made things worse.
"""

import argparse
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import (
    MODELS,
    S3_REVERSIBILITY_RESULTS_PATH,
    S3_WORKER_TRIALS_PATH,
)
from scripts.utils import (
    append_jsonl,
    get_anthropic_client,
    get_google_client,
    get_openai_client,
    load_jsonl,
    rate_limit,
    retry_with_backoff,
)

COMPARISON_PROMPT = """\
A user asked for the following task to be completed:

---
{task_prompt}
---

Two different outputs were produced. Please evaluate which one better fulfills the task.

OUTPUT A:
---
{output_a}
---

OUTPUT B:
---
{output_b}
---

Which output better fulfills the original task? Consider completeness, appropriateness, tone, and quality.

Respond with ONLY a JSON object:
{{"choice": "A" or "B" or "tie", "reason": "one sentence explanation"}}"""


def make_result_id(worker_trial_id: str) -> str:
    return f"s3_reverse__{worker_trial_id}"


def parse_comparison_response(text: str) -> dict | None:
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        text = "\n".join(lines)
    try:
        data = json.loads(text)
        if "choice" in data:
            choice = data["choice"].strip().upper()
            if choice in ("A", "B", "TIE"):
                data["choice"] = choice
                return data
    except (json.JSONDecodeError, ValueError):
        pass
    return None


def call_comparison(provider: str, model_id: str, prompt: str) -> dict | None:
    for attempt in range(2):
        rate_limit(provider)

        if provider == "openai":
            client = get_openai_client()
            r = retry_with_backoff(
                client.chat.completions.create,
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            text = r.choices[0].message.content

        elif provider == "anthropic":
            client = get_anthropic_client()
            r = retry_with_backoff(
                client.messages.create,
                model=model_id,
                max_tokens=256,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            text = r.content[0].text

        elif provider == "google":
            from google.genai import types
            client = get_google_client()
            config = types.GenerateContentConfig(temperature=0.0)
            r = retry_with_backoff(
                client.models.generate_content,
                model=model_id,
                contents=prompt,
                config=config,
            )
            text = r.text

        else:
            raise ValueError(f"Unknown provider: {provider}")

        parsed = parse_comparison_response(text)
        if parsed:
            return {**parsed, "raw_response": text}

        if attempt == 0:
            print(f"    Parse failed, retrying...")

    return None


def main():
    parser = argparse.ArgumentParser(
        description="Phase 4: Reversibility test for Study 3"
    )
    parser.add_argument("--model", required=True, choices=list(MODELS.keys()))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    model_cfg = MODELS[args.model]
    provider = model_cfg["provider"]
    model_id = model_cfg["model_id"]

    # Load worker trials that have 5 turns
    all_trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    worker_trials = [
        t for t in all_trials
        if t.get("status") == "success"
        and t["model"] == args.model
        and len(t.get("responses", [])) >= 5
    ]
    print(f"Found {len(worker_trials)} completed 5-turn trials for {args.model}")

    # Skip completed
    existing = load_jsonl(S3_REVERSIBILITY_RESULTS_PATH)
    completed = {r["result_id"] for r in existing}

    pending = []
    for trial in worker_trials:
        result_id = make_result_id(trial["trial_id"])
        if result_id not in completed:
            pending.append(trial)

    print(f"{len(pending)} pending comparisons ({len(completed)} done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit}")

    for i, trial in enumerate(pending, 1):
        result_id = make_result_id(trial["trial_id"])
        print(f"[{i}/{len(pending)}] {result_id}")

        turn1_output = trial["responses"][0]
        turn5_output = trial["responses"][4]

        # Randomize position to control for order bias
        if rng.random() < 0.5:
            output_a, output_b = turn1_output, turn5_output
            turn1_position = "A"
        else:
            output_a, output_b = turn5_output, turn1_output
            turn1_position = "B"

        prompt = COMPARISON_PROMPT.format(
            task_prompt=trial["task_prompt"],
            output_a=output_a,
            output_b=output_b,
        )

        result = call_comparison(provider, model_id, prompt)

        if result:
            # Map choice back to turn preference
            if result["choice"] == "TIE":
                prefers_turn1 = None
            elif result["choice"] == turn1_position:
                prefers_turn1 = True
            else:
                prefers_turn1 = False

            record = {
                "result_id": result_id,
                "worker_trial_id": trial["trial_id"],
                "model": args.model,
                "scenario_id": trial["scenario_id"],
                "domain": trial["domain"],
                "run": trial["run"],
                "turn1_position": turn1_position,
                "raw_choice": result["choice"],
                "prefers_turn1": prefers_turn1,
                "reason": result.get("reason", ""),
                "raw_response": result["raw_response"],
            }
            append_jsonl(record, S3_REVERSIBILITY_RESULTS_PATH)
            pref = "TURN 1" if prefers_turn1 else ("TURN 5" if prefers_turn1 is False else "TIE")
            print(f"    Prefers: {pref} ({result.get('reason', '')[:60]})")
        else:
            record = {
                "result_id": result_id,
                "worker_trial_id": trial["trial_id"],
                "model": args.model,
                "scenario_id": trial["scenario_id"],
                "domain": trial["domain"],
                "run": trial["run"],
                "turn1_position": turn1_position,
                "raw_choice": None,
                "prefers_turn1": None,
                "reason": None,
                "raw_response": None,
            }
            append_jsonl(record, S3_REVERSIBILITY_RESULTS_PATH)
            print(f"    SKIPPED (parse failure)")

    print("Done.")


if __name__ == "__main__":
    main()
