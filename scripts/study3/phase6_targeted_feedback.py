"""Phase 5 (Targeted Feedback): Test for the Revision Yield experiment.

RQ7: When the blind evaluator says output genuinely needs work (level 1-3),
does specific critique produce better revisions than generic probing?

Flow:
1. Load Phase 2 evaluator results where level <= 2
2. Ask the evaluator to provide a specific critique
3. Give a fresh model instance: task + output + critique -> targeted revision
4. Blind-evaluate the targeted revision using the same 4-level scale
5. Compare quality to the working model's next-turn generic revision (from Phase 1)
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import (
    MAX_OUTPUT_TOKENS_GENERATION,
    MAX_OUTPUT_TOKENS_JUDGE,
    MODELS,
    S3_EVALUATOR_RESULTS_PATH,
    S3_TARGETED_FEEDBACK_PATH,
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

CRITIQUE_PROMPT = """\
A user asked for the following task:

---
{task_prompt}
---

Here is the output that was produced:

---
{output}
---

You previously judged this output as needing more work. Please provide a specific, actionable critique explaining exactly what needs to be improved. Be concrete about what is missing, wrong, or could be better.

Respond with ONLY a JSON object:
{{"critique": "your specific feedback here"}}"""

TARGETED_REVISION_PROMPT = """\
A user asked for the following task:

---
{task_prompt}
---

Here is a previous attempt at this task:

---
{output}
---

A reviewer provided this feedback:

---
{critique}
---

Please produce an improved version that addresses the reviewer's feedback. Output only the revised version, nothing else."""

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


def parse_json_response(text: str) -> dict | None:
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        text = "\n".join(lines)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def call_model(provider: str, model_id: str, prompt: str, temperature: float = 0.0,
               max_tokens: int = MAX_OUTPUT_TOKENS_JUDGE) -> str | None:
    rate_limit(provider)

    if provider == "openai":
        client = get_openai_client()
        r = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return r.choices[0].message.content

    elif provider == "anthropic":
        client = get_anthropic_client()
        r = retry_with_backoff(
            client.messages.create,
            model=model_id,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        return r.content[0].text

    elif provider == "google":
        from google.genai import types
        client = get_google_client()
        config = types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
        )
        r = retry_with_backoff(
            client.models.generate_content,
            model=model_id,
            contents=prompt,
            config=config,
        )
        return extract_gemini_text(r)

    elif provider == "together":
        client = get_together_client()
        r = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return r.choices[0].message.content

    return None


def main():
    parser = argparse.ArgumentParser(
        description="Phase 5: Targeted feedback test for Study 3"
    )
    parser.add_argument("--model", required=True, choices=list(MODELS.keys()))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-turn", type=int, default=3,
                        help="Only process evaluator level 1-2 results up to this turn")
    args = parser.parse_args()

    model_cfg = MODELS[args.model]
    provider = model_cfg["provider"]
    model_id = model_cfg["model_id"]

    # Load Phase 2 evaluator results: level 1-2 (needs work)
    eval_results = load_jsonl(S3_EVALUATOR_RESULTS_PATH)
    needs_work = [
        r for r in eval_results
        if r["model"] == args.model
        and r.get("level") is not None
        and r["level"] <= 3
        and r["turn"] <= args.max_turn
    ]
    print(f"Found {len(needs_work)} level 1-3 evaluator results for {args.model} (turns 1-{args.max_turn})")

    # Load worker trials for reference
    worker_trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    worker_map = {t["trial_id"]: t for t in worker_trials if t.get("status") == "success"}

    # Skip completed
    existing = load_jsonl(S3_TARGETED_FEEDBACK_PATH)
    completed = {r["source_eval_id"] for r in existing}

    pending = [r for r in needs_work if r["eval_id"] not in completed]
    print(f"{len(pending)} pending targeted feedback calls ({len(completed)} done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit}")

    for i, eval_result in enumerate(pending, 1):
        source_eval_id = eval_result["eval_id"]
        worker_trial_id = eval_result["worker_trial_id"]
        turn = eval_result["turn"]

        print(f"[{i}/{len(pending)}] {source_eval_id}")

        worker_trial = worker_map.get(worker_trial_id)
        if not worker_trial:
            print(f"  SKIP: worker trial not found")
            continue

        output = worker_trial["responses"][turn - 1]
        task_prompt = worker_trial["task_prompt"]

        # Step 1: Get specific critique
        critique_prompt = CRITIQUE_PROMPT.format(task_prompt=task_prompt, output=output)
        critique_text = call_model(provider, model_id, critique_prompt, temperature=0.0)
        if not critique_text:
            print(f"  SKIP: critique call failed")
            continue

        critique_data = parse_json_response(critique_text)
        critique = critique_data.get("critique", critique_text) if critique_data else critique_text

        # Step 2: Fresh instance produces targeted revision
        revision_prompt = TARGETED_REVISION_PROMPT.format(
            task_prompt=task_prompt, output=output, critique=critique
        )
        targeted_revision = call_model(provider, model_id, revision_prompt, temperature=1.0,
                                       max_tokens=MAX_OUTPUT_TOKENS_GENERATION)
        if not targeted_revision:
            print(f"  SKIP: targeted revision call failed")
            continue

        # Step 3: Blind-evaluate the targeted revision
        eval_prompt = EVAL_PROMPT.format(task_prompt=task_prompt, output=targeted_revision)
        eval_text = call_model(provider, model_id, eval_prompt, temperature=0.0)
        targeted_eval = parse_json_response(eval_text) if eval_text else None
        targeted_level = targeted_eval.get("level") if targeted_eval else None

        # Get the generic next-turn revision quality for comparison
        generic_next_level = None
        if turn < len(worker_trial["responses"]):
            generic_output = worker_trial["responses"][turn]
            generic_eval_prompt = EVAL_PROMPT.format(task_prompt=task_prompt, output=generic_output)
            generic_eval_text = call_model(provider, model_id, generic_eval_prompt, temperature=0.0)
            generic_eval = parse_json_response(generic_eval_text) if generic_eval_text else None
            generic_next_level = generic_eval.get("level") if generic_eval else None

        record = {
            "source_eval_id": source_eval_id,
            "worker_trial_id": worker_trial_id,
            "model": args.model,
            "scenario_id": eval_result["scenario_id"],
            "domain": eval_result["domain"],
            "turn": turn,
            "critique": critique,
            "targeted_revision": targeted_revision,
            "targeted_level": targeted_level,
            "generic_next_level": generic_next_level,
            "level_delta": (
                (targeted_level - generic_next_level)
                if targeted_level is not None and generic_next_level is not None
                else None
            ),
        }
        append_jsonl(record, S3_TARGETED_FEEDBACK_PATH)

        print(f"  Targeted level: {targeted_level}, Generic next level: {generic_next_level}, Delta: {record['level_delta']}")

    print("Done.")


if __name__ == "__main__":
    main()
