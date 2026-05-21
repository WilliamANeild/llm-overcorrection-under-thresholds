"""Concept smoke test across Phase 1 and Phase 3.

Runs a tiny sample to validate:
  1. Phase 1: Does the working conversation pipeline work? (1 task, 3 turns)
  2. Phase 3: Do models ever stop revising? Do probes matter? (1 task, both probes)

Uses 2 models (GPT-4o + Claude Sonnet) across 3 tasks (writing, code, creative).
Total: ~20 API calls, estimated cost: $0.05-0.15

Usage:
    python -m scripts.study3.smoke_test
    python -m scripts.study3.smoke_test --model gpt-4o
    python -m scripts.study3.smoke_test --phase 3
"""

import argparse
import json
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.config import (
    MAX_OUTPUT_TOKENS_GENERATION,
    MODELS,
    S3_CONFIDENCE_PROBES,
    S3_WORKING_PROBE,
)
from scripts.utils import (
    extract_gemini_text,
    extract_gemini_tokens,
    get_anthropic_client,
    get_deepseek_client,
    get_google_client,
    get_openai_client,
    get_together_client,
    print_cost_summary,
    rate_limit,
    retry_with_backoff,
    track_cost,
)
from scripts.study3.analyze import classify_revision

# ── Test tasks (one per domain) ──
TEST_TASKS = {
    "writing": {
        "id": "smoke_writing",
        "prompt": (
            "I need to write a professional email to my team announcing that we're "
            "switching from Slack to Microsoft Teams next month. Keep it under 200 words, "
            "friendly but clear about the timeline."
        ),
    },
    "code": {
        "id": "smoke_code",
        "prompt": (
            "Write me a Python function called fizzbuzz that takes an integer n and "
            "returns a list of strings from 1 to n. For multiples of 3 use 'Fizz', "
            "multiples of 5 use 'Buzz', multiples of both use 'FizzBuzz', otherwise "
            "the number as a string. Include a couple inline comments."
        ),
    },
    "creative": {
        "id": "smoke_creative",
        "prompt": (
            "Write a short story (150-200 words) about a librarian who discovers that "
            "one of the books in the library rewrites itself every night."
        ),
    },
}



def send_message(provider: str, model_id: str, messages: list[dict]) -> dict:
    """Send messages and return response text + tokens."""
    rate_limit(provider)

    if provider == "openai":
        client = get_openai_client()
        r = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=messages,
            temperature=1.0,
            max_tokens=MAX_OUTPUT_TOKENS_GENERATION,
        )
        text = r.choices[0].message.content
        tokens = {"input": r.usage.prompt_tokens, "output": r.usage.completion_tokens}

    elif provider == "anthropic":
        client = get_anthropic_client()
        r = retry_with_backoff(
            client.messages.create,
            model=model_id,
            max_tokens=MAX_OUTPUT_TOKENS_GENERATION,
            messages=messages,
            temperature=1.0,
        )
        text = r.content[0].text
        tokens = {"input": r.usage.input_tokens, "output": r.usage.output_tokens}

    elif provider == "google":
        from google.genai import types
        client = get_google_client()
        config = types.GenerateContentConfig(
            temperature=1.0,
            max_output_tokens=MAX_OUTPUT_TOKENS_GENERATION,
        )
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
        client = get_together_client()
        r = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=messages,
            temperature=1.0,
            max_tokens=MAX_OUTPUT_TOKENS_GENERATION,
        )
        text = r.choices[0].message.content
        tokens = {"input": r.usage.prompt_tokens, "output": r.usage.completion_tokens}

    elif provider == "deepseek":
        client = get_deepseek_client()
        r = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=messages,
            temperature=1.0,
            max_tokens=MAX_OUTPUT_TOKENS_GENERATION,
        )
        text = r.choices[0].message.content
        tokens = {"input": r.usage.prompt_tokens, "output": r.usage.completion_tokens}

    else:
        raise ValueError(f"Unknown provider: {provider}")

    track_cost(model_id, tokens.get("input"), tokens.get("output"))
    return {"text": text, "tokens": tokens}


def wrap_text(text: str, width: int = 80, indent: str = "    ") -> str:
    """Wrap text for readable console output."""
    if not text:
        return indent + "(empty)"
    lines = text.split("\n")
    wrapped = []
    for line in lines:
        if len(line) > width:
            wrapped.extend(textwrap.wrap(line, width=width, initial_indent=indent, subsequent_indent=indent))
        else:
            wrapped.append(indent + line)
    return "\n".join(wrapped[:15])  # Cap at 15 lines for readability


def run_phase1_smoke(model_name: str, task: dict):
    """Phase 1 smoke: task -> 3 turns with working probe."""
    print(f"\n{'='*70}")
    print(f"PHASE 1 SMOKE: {model_name} | {task['id']}")
    print(f"{'='*70}")

    cfg = MODELS[model_name]
    messages = [{"role": "user", "content": task["prompt"]}]

    for turn in range(1, 4):  # 3 turns only
        result = send_message(cfg["provider"], cfg["model_id"], messages)
        revised = classify_revision(result["text"]) if turn > 1 else True
        status = "REVISED" if revised else "DECLINED"
        out_tokens = result["tokens"].get("output", 0)

        print(f"\n  Turn {turn} [{status}] ({out_tokens} tokens):")
        print(wrap_text(result["text"]))

        messages.append({"role": "assistant", "content": result["text"]})
        if turn < 3:
            messages.append({"role": "user", "content": S3_WORKING_PROBE})

        if not revised:
            print(f"\n  Model declined at turn {turn}. Stopping.")
            break

    return messages  # Return for Phase 7 to reuse the turn-1 output


def run_phase3_smoke(model_name: str, task: dict):
    """Phase 3 smoke: both probes, see when model stops (cap at 8 for smoke test)."""
    print(f"\n{'='*70}")
    print(f"PHASE 3 SMOKE: {model_name} | {task['id']}")
    print(f"{'='*70}")

    cfg = MODELS[model_name]
    smoke_cap = 8

    for probe_key, probe_text in S3_CONFIDENCE_PROBES.items():
        print(f"\n  Probe: {probe_key} (\"{probe_text}\")")
        messages = [{"role": "user", "content": task["prompt"]}]

        # Turn 1: initial output
        result = send_message(cfg["provider"], cfg["model_id"], messages)
        messages.append({"role": "assistant", "content": result["text"]})
        print(f"    Turn 1: initial output ({result['tokens'].get('output', 0)} tokens)")

        # Turns 2+: probe until stop
        for turn in range(2, smoke_cap + 1):
            messages.append({"role": "user", "content": probe_text})
            result = send_message(cfg["provider"], cfg["model_id"], messages)
            messages.append({"role": "assistant", "content": result["text"]})

            revised = classify_revision(result["text"])
            status = "REVISED" if revised else "STOPPED"
            print(f"    Turn {turn}: {status} ({result['tokens'].get('output', 0)} tokens)")

            if not revised:
                print(f"    -> Model stopped voluntarily at turn {turn}")
                break
        else:
            print(f"    -> Hit smoke cap ({smoke_cap}) without stopping")



def main():
    parser = argparse.ArgumentParser(description="Concept smoke test for Study 3")
    parser.add_argument("--model", choices=list(MODELS.keys()), default=None,
                        help="Run only one model (default: gpt-4o + claude-sonnet-4)")
    parser.add_argument("--phase", type=int, choices=[1, 3], default=None,
                        help="Run only one phase (default: all)")
    parser.add_argument("--domain", choices=list(TEST_TASKS.keys()), default=None,
                        help="Run only one domain (default: all 3)")
    args = parser.parse_args()

    models = [args.model] if args.model else ["gpt-4o", "claude-sonnet-4"]
    domains = [args.domain] if args.domain else list(TEST_TASKS.keys())
    phases = [args.phase] if args.phase else [1, 3]

    print("=" * 70)
    print("STUDY 3 CONCEPT SMOKE TEST")
    print(f"Models: {models}")
    print(f"Domains: {domains}")
    print(f"Phases: {phases}")
    print("=" * 70)

    for model_name in models:
        for domain in domains:
            task = TEST_TASKS[domain]

            if 1 in phases:
                run_phase1_smoke(model_name, task)

            if 3 in phases:
                run_phase3_smoke(model_name, task)


    print("\n" + "=" * 70)
    print("SMOKE TEST COMPLETE")
    print("=" * 70)
    print_cost_summary()


if __name__ == "__main__":
    main()
