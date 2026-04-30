"""Shared utilities for the experiment pipeline."""

import json
import os
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from scripts.config import MAX_RETRIES, METADATA_PATH, RATE_LIMIT_SECONDS, RETRY_BACKOFF_BASE

load_dotenv()

# ── Running cost tracker ──
# Per-token pricing (output tokens, USD) as of 2025
_TOKEN_PRICES = {
    "gpt-4o-2024-11-20": {"input": 2.50 / 1_000_000, "output": 10.0 / 1_000_000},
    "claude-sonnet-4-20250514": {"input": 3.0 / 1_000_000, "output": 15.0 / 1_000_000},
    "gemini-2.5-flash-preview-04-17": {"input": 0.15 / 1_000_000, "output": 0.60 / 1_000_000},
    "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo": {"input": 0.88 / 1_000_000, "output": 0.88 / 1_000_000},
    "mistralai/Mistral-Large-Instruct-2407": {"input": 2.0 / 1_000_000, "output": 6.0 / 1_000_000},
    "Qwen/Qwen2.5-72B-Instruct-Turbo": {"input": 0.90 / 1_000_000, "output": 0.90 / 1_000_000},
}
_cumulative_cost = {"total": 0.0, "by_model": {}}


def track_cost(model_id: str, input_tokens: int | None, output_tokens: int | None):
    """Accumulate running cost for a single API call."""
    prices = _TOKEN_PRICES.get(model_id)
    if not prices:
        return
    cost = (input_tokens or 0) * prices["input"] + (output_tokens or 0) * prices["output"]
    _cumulative_cost["total"] += cost
    _cumulative_cost["by_model"][model_id] = _cumulative_cost["by_model"].get(model_id, 0.0) + cost


def get_cumulative_cost() -> dict:
    """Return running cost summary."""
    return {
        "total_usd": round(_cumulative_cost["total"], 4),
        "by_model": {k: round(v, 4) for k, v in _cumulative_cost["by_model"].items()},
    }


def print_cost_summary():
    """Print current cumulative cost to stdout."""
    costs = get_cumulative_cost()
    print(f"\n  Running cost: ${costs['total_usd']:.4f}")
    for model, cost in sorted(costs["by_model"].items()):
        print(f"    {model}: ${cost:.4f}")


# ── JSON / JSONL helpers ──

def load_json(path: Path) -> dict | list:
    with open(path) as f:
        return json.load(f)


def save_json(data: dict | list, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def append_jsonl(record: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


# ── Trial ID generator ──

def make_trial_id(model: str, scenario_id: str, framing: str, level: int, run: int, probe_type: str = "leading") -> str:
    return f"{model}__{scenario_id}__{framing}__{level}__{probe_type}__run{run}"


# ── Rate limiter ──

_last_call: dict[str, float] = {}


def rate_limit(provider: str) -> None:
    interval = RATE_LIMIT_SECONDS.get(provider, 1.0)
    last = _last_call.get(provider, 0.0)
    elapsed = time.time() - last
    if elapsed < interval:
        time.sleep(interval - elapsed)
    _last_call[provider] = time.time()


# ── Retry wrapper ──

def retry_with_backoff(fn, *args, **kwargs):
    import random
    for attempt in range(MAX_RETRIES):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                raise
            # Longer base wait for 503/capacity errors
            err_str = str(e)
            if "503" in err_str or "UNAVAILABLE" in err_str or "high demand" in err_str:
                wait = 10 * (2 ** attempt) + random.uniform(0, 5)
            else:
                wait = RETRY_BACKOFF_BASE * (2 ** attempt) + random.uniform(0, 1)
            print(f"  Retry {attempt + 1}/{MAX_RETRIES} after error: {e}. Waiting {wait:.0f}s...")
            time.sleep(wait)


# ── API client factory ──

def get_openai_client():
    from openai import OpenAI
    return OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def get_anthropic_client():
    import anthropic
    return anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def get_google_client():
    from google import genai
    return genai.Client(api_key=os.environ["GOOGLE_API_KEY"])


def extract_gemini_text(response) -> str:
    """Safely extract text from a Gemini response, raising on blocked/empty content."""
    if not hasattr(response, 'candidates') or not response.candidates:
        raise ValueError("Gemini returned no candidates")
    candidate = response.candidates[0]
    finish_reason = getattr(candidate, 'finish_reason', None)
    if finish_reason and str(finish_reason) not in ('STOP', 'MAX_TOKENS', 'FinishReason.STOP', 'FinishReason.MAX_TOKENS', '1', '2'):
        raise ValueError(f"Gemini content blocked: finish_reason={finish_reason}")
    text = response.text
    if text is None:
        raise ValueError("Gemini response .text is None (likely safety-filtered)")
    return text


def extract_gemini_tokens(response) -> dict:
    """Safely extract token counts and finish reason from a Gemini response."""
    meta = getattr(response, 'usage_metadata', None)
    finish_reason = None
    if hasattr(response, 'candidates') and response.candidates:
        finish_reason = str(getattr(response.candidates[0], 'finish_reason', None))
    if meta is None:
        return {"input": None, "output": None, "finish_reason": finish_reason}
    return {
        "input": getattr(meta, 'prompt_token_count', None),
        "output": getattr(meta, 'candidates_token_count', None),
        "finish_reason": finish_reason,
    }


def get_together_client():
    from openai import OpenAI
    return OpenAI(
        api_key=os.environ["TOGETHER_API_KEY"],
        base_url="https://api.together.xyz/v1",
    )


# ── Experiment metadata logging ──

def log_experiment_metadata(model_name: str, model_id: str) -> None:
    """Log experiment start metadata to a JSONL file."""
    metadata = {
        "event": "experiment_start",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_name": model_name,
        "model_id": model_id,
        "python_version": sys.version,
        "platform": platform.platform(),
        "note": "temperature=1.0 used for all API calls; API-based LLMs do not support true seed control",
    }
    append_jsonl(metadata, METADATA_PATH)
    print(f"Logged experiment metadata → {METADATA_PATH}")


def chat_two_turns(provider: str, model_id: str, turn1_prompt: str, turn2_prompt: str) -> dict:
    """Send a two-turn conversation and return both responses.

    No system prompt is used (testing default model behavior).
    temperature=1.0 is set explicitly for reproducibility documentation.
    Returns {"turn1_response": str, "turn2_response": str}.
    """
    rate_limit(provider)

    if provider == "openai":
        client = get_openai_client()
        messages = [{"role": "user", "content": turn1_prompt}]
        r1 = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=messages,
            temperature=1.0,
        )
        t1 = r1.choices[0].message.content

        rate_limit(provider)
        messages.append({"role": "assistant", "content": t1})
        messages.append({"role": "user", "content": turn2_prompt})
        r2 = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=messages,
            temperature=1.0,
        )
        t2 = r2.choices[0].message.content
        return {"turn1_response": t1, "turn2_response": t2}

    elif provider == "anthropic":
        client = get_anthropic_client()
        messages = [{"role": "user", "content": turn1_prompt}]
        r1 = retry_with_backoff(
            client.messages.create,
            model=model_id,
            max_tokens=4096,
            messages=messages,
            temperature=1.0,
        )
        t1 = r1.content[0].text

        rate_limit(provider)
        messages.append({"role": "assistant", "content": t1})
        messages.append({"role": "user", "content": turn2_prompt})
        r2 = retry_with_backoff(
            client.messages.create,
            model=model_id,
            max_tokens=4096,
            messages=messages,
            temperature=1.0,
        )
        t2 = r2.content[0].text
        return {"turn1_response": t1, "turn2_response": t2}

    elif provider == "google":
        from google.genai import types

        client = get_google_client()
        config = types.GenerateContentConfig(temperature=1.0)
        r1 = retry_with_backoff(
            client.models.generate_content,
            model=model_id,
            contents=turn1_prompt,
            config=config,
        )
        t1 = extract_gemini_text(r1)

        rate_limit(provider)
        r2 = retry_with_backoff(
            client.models.generate_content,
            model=model_id,
            contents=[
                {"role": "user", "parts": [{"text": turn1_prompt}]},
                {"role": "model", "parts": [{"text": t1}]},
                {"role": "user", "parts": [{"text": turn2_prompt}]},
            ],
            config=config,
        )
        t2 = extract_gemini_text(r2)
        return {"turn1_response": t1, "turn2_response": t2}

    elif provider == "together":
        client = get_together_client()
        messages = [{"role": "user", "content": turn1_prompt}]
        r1 = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=messages,
            temperature=1.0,
        )
        t1 = r1.choices[0].message.content

        rate_limit(provider)
        messages.append({"role": "assistant", "content": t1})
        messages.append({"role": "user", "content": turn2_prompt})
        r2 = retry_with_backoff(
            client.chat.completions.create,
            model=model_id,
            messages=messages,
            temperature=1.0,
        )
        t2 = r2.choices[0].message.content
        return {"turn1_response": t1, "turn2_response": t2}

    else:
        raise ValueError(f"Unknown provider: {provider}")


def chat_n_turns(provider: str, model_id: str, prompts: list[str]) -> dict:
    """Send an N-turn conversation and return all responses.

    No system prompt is used (testing default model behavior).
    temperature=1.0 is set explicitly for reproducibility documentation.
    Returns {"responses": [str, ...]}.
    """
    responses = []

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
            responses.append(text)
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
            responses.append(text)
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
            text = extract_gemini_text(r)
            responses.append(text)
            contents.append({"role": "model", "parts": [{"text": text}]})

    elif provider == "together":
        client = get_together_client()
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
            responses.append(text)
            messages.append({"role": "assistant", "content": text})

    else:
        raise ValueError(f"Unknown provider: {provider}")

    return {"responses": responses}
