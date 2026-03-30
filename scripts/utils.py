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

def make_trial_id(model: str, scenario_id: str, framing: str, level: int, run: int) -> str:
    return f"{model}__{scenario_id}__{framing}__{level}__run{run}"


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
    for attempt in range(MAX_RETRIES):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                raise
            wait = RETRY_BACKOFF_BASE * (2 ** attempt)
            print(f"  Retry {attempt + 1}/{MAX_RETRIES} after error: {e}. Waiting {wait}s...")
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
        t1 = r1.text

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
        t2 = r2.text
        return {"turn1_response": t1, "turn2_response": t2}

    else:
        raise ValueError(f"Unknown provider: {provider}")
