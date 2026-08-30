#!/usr/bin/env python3
"""Strip meta-commentary from ALL 3,600 outputs and rescore changed ones.

Produces stripped_rescore_full.jsonl with one record per (trial_id, turn):
  - trial_id, turn, model, domain, task_prompt
  - orig_score (from evaluator_results.jsonl, 6->2 recoded)
  - stripped_score (rescored on stripped text, 6->2 recoded; = orig_score if text unchanged)
  - chars_removed (0 if unchanged)
  - was_rescored (bool)
"""

import json, re, sys, time, os
from pathlib import Path
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

DATA = Path(__file__).resolve().parents[2] / "data" / "study3" / "raw_responses"
OUT_PATH = DATA / "stripped_rescore_full.jsonl"

# ── Stripping (same patterns as strip_meta_commentary.py) ──

PREAMBLE_META = [
    r"(?:i'?d like to|let me|i'?ll|i want to)\s+(?:revise|make|take|offer|give|try|refine|polish|tighten)",
    r"here'?s (?:the|my|a|an|another) (?:revised|improved|updated|final|slightly|new|definitive)",
    r"(?:sure|okay|alright|absolutely)[,!.]?\s+here",
    r"(?:looking|look) (?:back|at (?:it|this|my))",
    r"(?:after|upon) (?:review|re-?reading|careful review|reflection)",
    r"(?:i've|i have) reviewed",
    r"thank(?:s| you) for (?:the|asking|checking|your|this)",
    r"(?:great|good) (?:question|prompt)",
    r"actually,? let me",
    r"considering the response",
    r"(?:this is a )?(?:very )?(?:solid|strong|great|good|excellent) (?:implementation|version|set|start|draft|point)",
    r"you'?re right to ask",
    r"since you(?:'re| are| repeated| asked|'ve)",
    r"i (?:think|believe) (?:i can|we can|it could|the|this|there's)",
    r"i can make (?:some|a few|one|minor)",
    r"(?:after|upon) re-?reading",
    r"i understand (?:the|your|you're)",
    r"i'?m (?:satisfied|happy|confident) with",
    r"(?:the|this) (?:version|response|output|code|email|post|analysis) (?:is|can be|meets|works)",
]
POSTAMBLE_META = [
    r"let me know (?:if|what|how|whether)",
    r"hope this helps",
    r"feel free to",
    r"(?:happy|glad|ready) to (?:help|assist|revise|adjust|make|answer)",
    r"(?:if you'?d like|would you like|if you want) (?:any|me to|further|more|to|a)",
    r"(?:i'?m|we'?re) (?:here|available|happy) (?:to|if)",
    r"(?:just )?let me know",
    r"(?:what do you think|how does (?:this|that) (?:sound|look|work))",
    r"(?:otherwise|if not),? (?:this|it|we|you|consider|go ahead)",
    r"(?:i believe|i think|i'?m confident) (?:this|it|the) (?:version|is|meets|works|feels)",
    r"(?:ready to|you can) (?:use|go|send|share|present|submit)",
    r"(?:i'?ve|i have) made (?:some|minor|a few)",
    r"(?:do you|would you) (?:want|like|need) (?:me to|any)",
    r"(?:this is|consider this|go ahead).{0,30}(?:final|done|ready|yours)",
    r"if (?:this|that) works for you",
    r"(?:if you|you can) (?:have|need|want) any (?:questions|concerns|feedback)",
    r"(?:congratulations|best of luck|good luck)",
    r"please let me know",
]
CONTENT_SIGNALS = [
    r"```", r"^\s*[-*]\s+\*\*", r"^\s*\d+\.\s", r"^\s*#{1,4}\s",
    r"\bdef\s+\w+\(", r"\bfunction\s+\w+\(", r"\bclass\s+\w+",
    r"^\s*\|.*\|", r"Subject:", r"^(?:Hi|Dear|Hello)\s+\w+",
    r"\$\d+", r"\d+%", r"(?:domestic|international|express)",
]

def is_meta_paragraph(text, patterns):
    text_lower = text.strip().lower()
    if len(text_lower) < 5: return False
    for sig in CONTENT_SIGNALS:
        if re.search(sig, text, re.MULTILINE | re.IGNORECASE): return False
    for pat in patterns:
        if re.search(pat, text_lower): return True
    return False

def strip_text(text):
    if not text or len(text.strip()) < 50: return text
    parts = re.split(r"(\n\n+|\n---+\n)", text)
    strip_front = 0
    i = 0
    while i < len(parts):
        part = parts[i].strip()
        if not part or re.match(r"^---+$", part): i += 1; continue
        if is_meta_paragraph(part, PREAMBLE_META):
            strip_front = i + 1
            if i + 1 < len(parts) and not parts[i+1].strip(): strip_front = i + 2
            i += 1
        else: break
        i += 1
    strip_back = len(parts)
    i = len(parts) - 1
    while i >= strip_front:
        part = parts[i].strip()
        if not part or re.match(r"^---+$", part): i -= 1; continue
        if is_meta_paragraph(part, POSTAMBLE_META):
            strip_back = i
            if i - 1 >= strip_front and not parts[i-1].strip(): strip_back = i - 1
            i -= 1
        else: break
        i -= 1
    kept = parts[strip_front:strip_back]
    result = "".join(kept).strip()
    if len(result) < len(text.strip()) * 0.3: return text.strip()
    return result if result else text.strip()


# ── Evaluator call (Anthropic only, same as phase2_evaluator.py) ──

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


def call_evaluator(task_prompt: str, output: str) -> int | None:
    """Score stripped output via Claude Sonnet 4, return level (1-6)."""
    import anthropic
    client = anthropic.Anthropic()
    prompt = EVAL_PROMPT.format(task_prompt=task_prompt, output=output)
    for attempt in range(3):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            text = response.content[0].text.strip()
            text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
            if text.startswith("```"):
                lines = text.split("\n")
                lines = [l for l in lines if not l.startswith("```")]
                text = "\n".join(lines)
            data = json.loads(text)
            level = int(data["level"])
            if 1 <= level <= 6:
                return level
        except Exception as e:
            print(f"  Attempt {attempt+1} failed: {e}", file=sys.stderr)
            time.sleep(2 ** attempt)
    return None


# ── Main ──

def main():
    # Load trials
    with open(DATA / "worker_trials.jsonl") as f:
        trials = [json.loads(l) for l in f if l.strip()]
    trials = [t for t in trials if t.get("status") == "success"]

    # Load original evaluator scores
    with open(DATA / "evaluator_results.jsonl") as f:
        evals = [json.loads(l) for l in f if l.strip()]
    eval_map = {}  # (trial_id, turn) -> level
    for e in evals:
        if e.get("level") is not None:
            eval_map[(e["worker_trial_id"], e["turn"])] = e["level"]

    # Load existing results for resume
    done = set()
    if OUT_PATH.exists():
        with open(OUT_PATH) as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    done.add((r["trial_id"], r["turn"]))
        print(f"Resuming: {len(done)} already done")

    # Build work list
    work = []
    for trial in trials:
        for turn_idx, resp in enumerate(trial["responses"]):
            turn = turn_idx + 1
            tid = trial["trial_id"]
            if (tid, turn) in done:
                continue

            orig = resp.strip()
            stripped = strip_text(resp)
            orig_level = eval_map.get((tid, turn))
            if orig_level is None:
                continue

            # 6->2 recode for orig
            orig_recoded = 2 if orig_level == 6 else orig_level

            needs_rescore = (stripped != orig)
            work.append({
                "trial_id": tid,
                "turn": turn,
                "model": trial["model"],
                "domain": trial["domain"],
                "task_prompt": trial["task_prompt"],
                "orig_level_raw": orig_level,
                "orig_score": orig_recoded,
                "stripped_text": stripped if needs_rescore else None,
                "needs_rescore": needs_rescore,
                "chars_removed": len(orig) - len(stripped) if needs_rescore else 0,
            })

    rescore_count = sum(1 for w in work if w["needs_rescore"])
    nochange_count = len(work) - rescore_count
    print(f"Work remaining: {len(work)} total ({rescore_count} need rescore, {nochange_count} unchanged)")

    # Process: write unchanged immediately, rescore changed ones
    out_f = open(OUT_PATH, "a")
    scored = 0
    errors = 0

    for i, item in enumerate(work):
        if not item["needs_rescore"]:
            # No change, stripped_score = orig_score
            record = {
                "trial_id": item["trial_id"],
                "turn": item["turn"],
                "model": item["model"],
                "domain": item["domain"],
                "orig_score": item["orig_score"],
                "orig_level_raw": item["orig_level_raw"],
                "stripped_score": item["orig_score"],
                "stripped_level_raw": item["orig_level_raw"],
                "chars_removed": 0,
                "was_rescored": False,
            }
            out_f.write(json.dumps(record) + "\n")
        else:
            # Need to rescore
            raw_level = call_evaluator(item["task_prompt"], item["stripped_text"])
            if raw_level is None:
                print(f"ERROR: failed to score {item['trial_id']} T{item['turn']}", file=sys.stderr)
                errors += 1
                continue

            stripped_recoded = 2 if raw_level == 6 else raw_level
            record = {
                "trial_id": item["trial_id"],
                "turn": item["turn"],
                "model": item["model"],
                "domain": item["domain"],
                "orig_score": item["orig_score"],
                "orig_level_raw": item["orig_level_raw"],
                "stripped_score": stripped_recoded,
                "stripped_level_raw": raw_level,
                "chars_removed": item["chars_removed"],
                "was_rescored": True,
            }
            out_f.write(json.dumps(record) + "\n")
            scored += 1

            if scored % 50 == 0:
                out_f.flush()
                print(f"  Rescored {scored}/{rescore_count} ({scored/rescore_count*100:.0f}%)")

    out_f.close()
    print(f"\nDone. Rescored: {scored}, Errors: {errors}")
    print(f"Output: {OUT_PATH}")


if __name__ == "__main__":
    main()
