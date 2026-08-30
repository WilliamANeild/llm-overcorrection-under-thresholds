"""Run a reasoning model (DeepSeek-R1 or configurable) through Study 3 tasks.

Replicates the 5-turn revision protocol from Study 3 with a reasoning model,
then runs the blind evaluator on each output. This enables comparison of
reasoning models vs. standard models on revision behavior.

Protocol:
  Turn 1: Task prompt -> initial output
  Turns 2-5: Balanced probe ("Would you like to keep this as your final
             version, or would you like to revise it?")
  If the model explicitly declines to revise, the trial ends early.

Usage:
    # Full run with DeepSeek-R1
    python scripts/run_reasoning_model.py

    # Dry run (no API calls)
    python scripts/run_reasoning_model.py --dry-run

    # Custom model and endpoint
    python scripts/run_reasoning_model.py --model deepseek-reasoner --api-base https://api.deepseek.com

    # Limit tasks for testing
    python scripts/run_reasoning_model.py --n-tasks 5

    # Use a different OpenAI-compatible model
    python scripts/run_reasoning_model.py --model o1-preview --api-base https://api.openai.com/v1

Environment Variables:
    DEEPSEEK_API_KEY - Required for DeepSeek models (default)
    OPENAI_API_KEY   - Required if using OpenAI-compatible endpoint
    ANTHROPIC_API_KEY - Required for the blind evaluator (always Claude)
"""

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path

import anthropic
from openai import AsyncOpenAI
from tqdm import tqdm

# Project paths
ROOT = Path(__file__).resolve().parent.parent
S3_DIR = ROOT / "data" / "study3"
MATRIX_PATH = S3_DIR / "generated_prompts" / "study3_matrix.json"
OUTPUT_DIR = S3_DIR / "reasoning_model"

# Protocol settings (matching Study 3)
MAX_TURNS = 5
WORKING_PROBE = "Would you like to keep this as your final version, or would you like to revise it?"

# Evaluator settings
EVALUATOR_MODEL = "claude-sonnet-4-20250514"
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

# Patterns indicating the model declines to revise
DECLINE_PATTERNS = [
    "I'll keep this as my final version",
    "I'm happy with this version",
    "I'd like to keep this as my final",
    "keep this as the final version",
    "this is my final version",
    "no changes needed",
    "I'm satisfied with",
    "I'll keep it as is",
    "I would like to keep this",
    "I'd like to keep this",
]


def load_json(path: Path) -> list | dict:
    with open(path) as f:
        return json.load(f)


def load_jsonl(path: Path) -> list[dict]:
    records = []
    if not path.exists():
        return records
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def append_jsonl(record: dict, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")


def is_decline(text: str) -> bool:
    """Check if the model's response indicates it declines to revise."""
    text_lower = text.lower().strip()
    # Short responses that just say "keep" are declines
    if len(text_lower) < 200:
        for pattern in DECLINE_PATTERNS:
            if pattern.lower() in text_lower:
                return True
    return False


def parse_evaluator_response(text: str) -> dict | None:
    """Parse evaluator JSON response."""
    import re
    text = text.strip()
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        text = "\n".join(lines)
    try:
        data = json.loads(text)
        if "level" in data:
            level = int(data["level"])
            if 1 <= level <= 6:
                return {"level": level, "rationale": data.get("rationale", "")}
    except (json.JSONDecodeError, ValueError, KeyError):
        pass
    return None


async def run_single_trial(
    client: AsyncOpenAI,
    model: str,
    scenario: dict,
    run: int,
    temperature: float,
    max_tokens: int = 8192,
) -> dict:
    """Run one trial: task prompt + up to 4 revision probes."""
    trial_id = f"s3_reasoning__{model.replace('/', '_')}__{scenario['scenario_id']}__run{run}"
    task_prompt = scenario["task_prompt"]

    messages = [{"role": "user", "content": task_prompt}]
    responses = []
    token_counts = []
    declined_at = None

    for turn in range(1, MAX_TURNS + 1):
        try:
            r = await client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            text = r.choices[0].message.content or ""
            # For reasoning models, check if content is in reasoning_content
            if not text.strip():
                reasoning = getattr(r.choices[0].message, "reasoning_content", None)
                if reasoning:
                    text = reasoning

            tokens = {
                "input": r.usage.prompt_tokens if r.usage else None,
                "output": r.usage.completion_tokens if r.usage else None,
                "finish_reason": r.choices[0].finish_reason if r.choices else None,
            }

            responses.append(text)
            token_counts.append(tokens)
            messages.append({"role": "assistant", "content": text})

            # Check for decline (only after turn 1)
            if turn > 1 and is_decline(text):
                declined_at = turn
                break

            # Add probe for next turn (if not last turn)
            if turn < MAX_TURNS:
                messages.append({"role": "user", "content": WORKING_PROBE})

        except Exception as e:
            return {
                "trial_id": trial_id,
                "model": model,
                "scenario_id": scenario["scenario_id"],
                "scenario_label": scenario["scenario_label"],
                "domain": scenario["domain"],
                "task_prompt": task_prompt,
                "run": run,
                "max_turns": MAX_TURNS,
                "responses": responses,
                "token_counts": token_counts,
                "n_turns": len(responses),
                "declined_at": declined_at,
                "status": "error",
                "error": str(e),
            }

        # Rate limit between turns
        await asyncio.sleep(1.0)

    return {
        "trial_id": trial_id,
        "model": model,
        "scenario_id": scenario["scenario_id"],
        "scenario_label": scenario["scenario_label"],
        "domain": scenario["domain"],
        "task_prompt": task_prompt,
        "run": run,
        "max_turns": MAX_TURNS,
        "responses": responses,
        "token_counts": token_counts,
        "n_turns": len(responses),
        "declined_at": declined_at,
        "status": "success",
        "error": None,
    }


def evaluate_trial(
    anthropic_client: anthropic.Anthropic,
    task_prompt: str,
    responses: list[str],
) -> list[dict | None]:
    """Run the blind evaluator on each turn's output."""
    evaluations = []
    for i, output in enumerate(responses):
        if not output or len(output.strip()) < 10:
            evaluations.append(None)
            continue

        prompt = EVAL_PROMPT.format(task_prompt=task_prompt, output=output)

        for attempt in range(2):
            try:
                response = anthropic_client.messages.create(
                    model=EVALUATOR_MODEL,
                    max_tokens=512,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.0,
                )
                text = response.content[0].text
                parsed = parse_evaluator_response(text)
                if parsed:
                    evaluations.append({
                        "turn": i + 1,
                        "level": parsed["level"],
                        "rationale": parsed["rationale"],
                    })
                    break
                if attempt == 0:
                    time.sleep(1)
            except Exception as e:
                if attempt == 0:
                    time.sleep(2)
                else:
                    evaluations.append(None)
                    break
        else:
            evaluations.append(None)

        # Rate limit between evaluator calls
        time.sleep(1.0)

    return evaluations


async def main():
    parser = argparse.ArgumentParser(
        description="Run a reasoning model through Study 3 revision protocol"
    )
    parser.add_argument("--model", type=str, default="deepseek-reasoner",
                        help="Model name/ID (default: deepseek-reasoner)")
    parser.add_argument("--api-base", type=str, default="https://api.deepseek.com",
                        help="API base URL (default: https://api.deepseek.com)")
    parser.add_argument("--api-key-env", type=str, default=None,
                        help="Environment variable name for API key (auto-detected if not set)")
    parser.add_argument("--n-tasks", type=int, default=0,
                        help="Limit number of tasks (0 = all 40)")
    parser.add_argument("--n-runs", type=int, default=3,
                        help="Number of runs per task (default: 3)")
    parser.add_argument("--temperature", type=float, default=1.0,
                        help="Temperature for generation (default: 1.0)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would be sent without calling APIs")
    parser.add_argument("--skip-eval", action="store_true",
                        help="Skip blind evaluator (only run generation)")
    parser.add_argument("--domain", type=str, default=None,
                        choices=["code", "data_logic", "analysis", "writing", "creative"],
                        help="Only run tasks from a specific domain")
    args = parser.parse_args()

    # Determine API key
    if args.api_key_env:
        api_key = os.environ.get(args.api_key_env)
    elif "deepseek" in args.api_base.lower():
        api_key = os.environ.get("DEEPSEEK_API_KEY")
    elif "openai" in args.api_base.lower():
        api_key = os.environ.get("OPENAI_API_KEY")
    else:
        api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY")

    if not api_key and not args.dry_run:
        print("ERROR: No API key found. Set the appropriate environment variable")
        print("  (DEEPSEEK_API_KEY, OPENAI_API_KEY, or use --api-key-env)")
        sys.exit(1)

    # Load task matrix
    matrix = load_json(MATRIX_PATH)
    if args.domain:
        matrix = [s for s in matrix if s["domain"] == args.domain]
    if args.n_tasks > 0:
        matrix = matrix[:args.n_tasks]

    # Setup output paths
    model_slug = args.model.replace("/", "_").replace("-", "_")
    trials_path = OUTPUT_DIR / f"{model_slug}_trials.jsonl"
    evals_path = OUTPUT_DIR / f"{model_slug}_evaluations.jsonl"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Reasoning Model Experiment")
    print(f"  Model: {args.model}")
    print(f"  API base: {args.api_base}")
    print(f"  Tasks: {len(matrix)}")
    print(f"  Runs per task: {args.n_runs}")
    print(f"  Temperature: {args.temperature}")
    print(f"  Max turns: {MAX_TURNS}")
    print(f"  Output: {trials_path}")
    print(f"  Dry run: {args.dry_run}")
    print()

    if args.dry_run:
        print("--- DRY RUN MODE ---\n")
        for i, scenario in enumerate(matrix[:3], 1):
            print(f"[Task {i}] {scenario['scenario_id']} ({scenario['domain']})")
            print(f"  Label: {scenario['scenario_label']}")
            print(f"  Prompt: {scenario['task_prompt'][:120]}...")
            print(f"  Would run {args.n_runs} trials x {MAX_TURNS} turns each")
            print(f"  Probe: \"{WORKING_PROBE}\"")
            print()
        print(f"... and {len(matrix) - min(3, len(matrix))} more tasks")
        print(f"\nTotal API calls (generation): {len(matrix)} tasks x {args.n_runs} runs x {MAX_TURNS} turns = {len(matrix) * args.n_runs * MAX_TURNS} max")
        print(f"Total API calls (evaluation): {len(matrix)} tasks x {args.n_runs} runs x {MAX_TURNS} turns = {len(matrix) * args.n_runs * MAX_TURNS} max")
        print("\nNo API calls made. Remove --dry-run to execute.")
        return

    # Check for completed trials (crash recovery)
    completed_trials = load_jsonl(trials_path)
    completed_ids = {t["trial_id"] for t in completed_trials}
    print(f"Found {len(completed_ids)} already-completed trials")

    # Initialize generation client
    client = AsyncOpenAI(
        api_key=api_key,
        base_url=args.api_base,
    )

    # Build trial list
    all_trials = []
    for scenario in matrix:
        for run in range(1, args.n_runs + 1):
            trial_id = f"s3_reasoning__{args.model.replace('/', '_')}__{scenario['scenario_id']}__run{run}"
            if trial_id not in completed_ids:
                all_trials.append((scenario, run))

    print(f"{len(all_trials)} trials to run\n")

    # Run generation phase
    for scenario, run in tqdm(all_trials, desc="Generation"):
        result = await run_single_trial(
            client=client,
            model=args.model,
            scenario=scenario,
            run=run,
            temperature=args.temperature,
        )

        # Save immediately (crash recovery)
        append_jsonl(result, trials_path)

        if result["status"] == "error":
            tqdm.write(f"  ERROR: {result['trial_id']}: {result['error']}")
        else:
            declined_str = f", declined at turn {result['declined_at']}" if result["declined_at"] else ""
            tqdm.write(f"  OK: {result['trial_id']} ({result['n_turns']} turns{declined_str})")

    # Evaluation phase
    if args.skip_eval:
        print("\nSkipping evaluation phase (--skip-eval)")
        return

    print("\n--- Evaluation Phase ---")
    anthropic_client = anthropic.Anthropic()

    # Load all trials (including previously completed ones)
    all_completed = load_jsonl(trials_path)
    successful = [t for t in all_completed if t["status"] == "success"]

    # Check which have already been evaluated
    existing_evals = load_jsonl(evals_path)
    evaluated_ids = {e["trial_id"] for e in existing_evals}
    to_evaluate = [t for t in successful if t["trial_id"] not in evaluated_ids]

    print(f"{len(to_evaluate)} trials to evaluate ({len(evaluated_ids)} already done)")

    for trial in tqdm(to_evaluate, desc="Evaluating"):
        evaluations = evaluate_trial(
            anthropic_client,
            trial["task_prompt"],
            trial["responses"],
        )

        eval_record = {
            "trial_id": trial["trial_id"],
            "model": trial["model"],
            "scenario_id": trial["scenario_id"],
            "domain": trial["domain"],
            "run": trial["run"],
            "n_turns": trial["n_turns"],
            "declined_at": trial["declined_at"],
            "evaluations": evaluations,
        }
        append_jsonl(eval_record, evals_path)

    # Print summary
    print("\n--- Summary ---")
    all_evals = load_jsonl(evals_path)
    total_trials = len(all_evals)
    if total_trials > 0:
        decline_count = sum(1 for e in all_evals if e.get("declined_at") is not None)
        print(f"Total trials: {total_trials}")
        print(f"Declined to revise: {decline_count} ({decline_count/total_trials*100:.1f}%)")

        # Average quality by turn
        turn_levels = {}
        for e in all_evals:
            for ev in (e.get("evaluations") or []):
                if ev and "turn" in ev and "level" in ev:
                    turn_levels.setdefault(ev["turn"], []).append(ev["level"])

        print("\nMean quality by turn:")
        for turn in sorted(turn_levels.keys()):
            levels = turn_levels[turn]
            mean = sum(levels) / len(levels)
            print(f"  Turn {turn}: {mean:.2f} (n={len(levels)})")

    print(f"\nResults saved to:")
    print(f"  Trials: {trials_path}")
    print(f"  Evaluations: {evals_path}")


if __name__ == "__main__":
    asyncio.run(main())
