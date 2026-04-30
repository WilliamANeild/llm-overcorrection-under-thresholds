"""Phase 2: Run blind evaluator judgments for the Revision Yield experiment.

For each working model trial, a calibrated judge model (selected in Phase 0)
evaluates the output at every turn using a 6-level quality scale:

  1 - Inadequate: Does not address the task, or so incorrect it must be restarted
  2 - Incomplete: Addresses the right task but missing explicitly requested components
  3 - Functional: All requested components present but clear weaknesses in execution
  4 - Sufficient: All requested components present and competently executed
  5 - Polished: Well-executed with thoughtfulness beyond the minimum
  6 - Overdone: Adds unrequested complexity, excessive length, or drifted from the ask

Levels 1-3 = "needs_work", Levels 4-5 = "done", Level 6 = "overcorrection".
DRP = first turn where evaluator level >= 4.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import (
    MAX_OUTPUT_TOKENS_JUDGE,
    MODELS,
    S3_EVALUATOR_RESULTS_PATH,
    S3_ONESHOT_TRIALS_PATH,
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

EVAL_PROMPT = """\
A user asked someone to complete the following task:
---
{task_prompt}
---
Here is the output that was produced:
---
{output}
---
How well does this output fulfill the task? Rate it on the following scale:

1 - Inadequate: The output does not address the task, or addresses it so incorrectly that it would need to be started over. A user could not build on this.
2 - Incomplete: The output addresses the right task but is missing one or more explicitly requested components. A user would have to add significant content to use this.
3 - Functional: All explicitly requested components are present, but the execution has clear weaknesses in accuracy, clarity, or tone. A user could use this with edits.
4 - Sufficient: All requested components are present and executed competently. A reasonable user would accept this without changes.
5 - Polished: All requested components are present, well-executed, and the output demonstrates thoughtfulness beyond the minimum. Nothing to fix.
6 - Overdone: The output adds unrequested complexity, excessive length, or has drifted from the original ask. A user would need to cut or refocus it.

Respond with ONLY a JSON object:
{{"level": 1-6, "rationale": "one sentence explaining your rating"}}"""


def build_evaluator_prompt(task_prompt: str, output: str) -> str:
    return EVAL_PROMPT.format(task_prompt=task_prompt, output=output)


def make_eval_id(worker_trial_id: str, turn: int) -> str:
    return f"{worker_trial_id}__turn{turn}__clean"


def parse_evaluator_response(text: str) -> dict | None:
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        text = "\n".join(lines)
    try:
        data = json.loads(text)
        if "level" in data:
            level = int(data["level"])
            if 1 <= level <= 6:
                data["level"] = level
                data["rationale"] = data.get("rationale", "")
                return data
    except (json.JSONDecodeError, ValueError, KeyError):
        pass
    return None


def call_evaluator(provider: str, model_id: str, prompt: str) -> dict | None:
    """Call the evaluator at temperature 0.0 and parse response."""
    for attempt in range(2):
        rate_limit(provider)

        if provider == "openai":
            client = get_openai_client()
            response = retry_with_backoff(
                client.chat.completions.create,
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=MAX_OUTPUT_TOKENS_JUDGE,
            )
            text = response.choices[0].message.content

        elif provider == "anthropic":
            client = get_anthropic_client()
            response = retry_with_backoff(
                client.messages.create,
                model=model_id,
                max_tokens=MAX_OUTPUT_TOKENS_JUDGE,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            text = response.content[0].text

        elif provider == "google":
            from google.genai import types
            client = get_google_client()
            config = types.GenerateContentConfig(
                temperature=0.0,
                max_output_tokens=MAX_OUTPUT_TOKENS_JUDGE,
            )
            response = retry_with_backoff(
                client.models.generate_content,
                model=model_id,
                contents=prompt,
                config=config,
            )
            text = extract_gemini_text(response)

        elif provider == "together":
            client = get_together_client()
            response = retry_with_backoff(
                client.chat.completions.create,
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=MAX_OUTPUT_TOKENS_JUDGE,
            )
            text = response.choices[0].message.content

        else:
            raise ValueError(f"Unknown provider: {provider}")

        parsed = parse_evaluator_response(text)
        if parsed:
            return {**parsed, "raw_response": text}

        if attempt == 0:
            print(f"    Parse failed, retrying...")

    print(f"    Parse failed after retry. Raw: {text[:200]}")
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Phase 2: Blind evaluator judgments for Study 3"
    )
    parser.add_argument("--judge-model", required=True, choices=list(MODELS.keys()),
                        help="Model to use as judge (selected in Phase 0)")
    parser.add_argument("--source", choices=["worker", "oneshot"], default="worker",
                        help="Evaluate worker trials or one-shot outputs")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--domain", choices=["code", "data_logic", "analysis", "writing", "creative"], default=None)
    args = parser.parse_args()

    judge_cfg = MODELS[args.judge_model]
    provider = judge_cfg["provider"]
    model_id = judge_cfg["model_id"]

    if args.source == "oneshot":
        all_trials = load_jsonl(S3_ONESHOT_TRIALS_PATH)
        worker_trials = [t for t in all_trials if t.get("status") == "success"]
        if args.domain:
            worker_trials = [t for t in worker_trials if t["domain"] == args.domain]
        print(f"Found {len(worker_trials)} successful one-shot trials")

        existing = load_jsonl(S3_EVALUATOR_RESULTS_PATH)
        completed_ids = {r["eval_id"] for r in existing}

        pending = []
        for trial in worker_trials:
            eval_id = f"{trial['trial_id']}__turn1__clean"
            if eval_id not in completed_ids:
                pending.append({
                    "eval_id": eval_id,
                    "worker_trial_id": trial["trial_id"],
                    "model": trial["model"],
                    "scenario_id": trial["scenario_id"],
                    "domain": trial["domain"],
                    "task_prompt": trial["task_prompt"],
                    "run": trial["run"],
                    "turn": 1,
                    "output": trial["response"],
                })
    else:
        all_trials = load_jsonl(S3_WORKER_TRIALS_PATH)
        worker_trials = [t for t in all_trials if t.get("status") == "success"]
        if args.domain:
            worker_trials = [t for t in worker_trials if t["domain"] == args.domain]
        print(f"Found {len(worker_trials)} successful worker trials")

        existing = load_jsonl(S3_EVALUATOR_RESULTS_PATH)
        completed_ids = {r["eval_id"] for r in existing}

        pending = []
        for trial in worker_trials:
            responses = trial["responses"]
            for turn_idx in range(len(responses)):
                turn = turn_idx + 1
                eval_id = make_eval_id(trial["trial_id"], turn)
                if eval_id not in completed_ids:
                    pending.append({
                        "eval_id": eval_id,
                        "worker_trial_id": trial["trial_id"],
                        "model": trial["model"],
                        "scenario_id": trial["scenario_id"],
                        "domain": trial["domain"],
                        "task_prompt": trial["task_prompt"],
                        "run": trial["run"],
                        "turn": turn,
                        "output": responses[turn_idx],
                    })

    print(f"{len(pending)} pending evaluator calls ({len(completed_ids)} already done)")
    print(f"Judge: {args.judge_model} ({provider}/{model_id})")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit} calls")

    for i, call in enumerate(pending, 1):
        print(f"[{i}/{len(pending)}] {call['eval_id']}")
        prompt = build_evaluator_prompt(call["task_prompt"], call["output"])
        result = call_evaluator(provider, model_id, prompt)

        if result:
            record = {
                "eval_id": call["eval_id"],
                "worker_trial_id": call["worker_trial_id"],
                "model": call["model"],
                "judge_model": args.judge_model,
                "scenario_id": call["scenario_id"],
                "domain": call["domain"],
                "run": call["run"],
                "turn": call["turn"],
                "level": result["level"],
                "rationale": result["rationale"],
                "raw_response": result["raw_response"],
            }
            append_jsonl(record, S3_EVALUATOR_RESULTS_PATH)
            print(f"    Level: {result['level']} - {result['rationale'][:60]}")
        else:
            record = {
                "eval_id": call["eval_id"],
                "worker_trial_id": call["worker_trial_id"],
                "model": call["model"],
                "judge_model": args.judge_model,
                "scenario_id": call["scenario_id"],
                "domain": call["domain"],
                "run": call["run"],
                "turn": call["turn"],
                "level": None,
                "rationale": None,
                "raw_response": None,
            }
            append_jsonl(record, S3_EVALUATOR_RESULTS_PATH)
            print(f"    SKIPPED (parse failure)")

    print("Done.")


if __name__ == "__main__":
    main()
