#!/usr/bin/env python3
"""Audit the revision-despite-sufficiency metric (39.4%) against raw outputs."""

import json, sys, random
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import numpy as np
from scripts.utils import load_jsonl
from scripts.config import S3_EVALUATOR_RESULTS_PATH, S3_WORKER_TRIALS_PATH

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "study3" / "raw_responses"

# Load LLM labels
llm_map = {}
with open(DATA_DIR / "genuine_meta_labels.jsonl") as f:
    for line in f:
        r = json.loads(line)
        llm_map[(r["trial_id"], r["turn"])] = r

# Load eval, fixed scale
eval_results = load_jsonl(S3_EVALUATOR_RESULTS_PATH)
eval_lookup = {}
for r in eval_results:
    if r.get("level") is not None:
        fixed = 2 if r["level"] == 6 else r["level"]
        eval_lookup[(r["worker_trial_id"], r["turn"])] = fixed

# Load full response texts
trials = load_jsonl(S3_WORKER_TRIALS_PATH)
trials = [t for t in trials if t.get("status") == "success"]
full_text = {}
trial_meta = {}
for trial in trials:
    for i, resp in enumerate(trial["responses"]):
        full_text[(trial["trial_id"], i + 1)] = resp
    trial_meta[trial["trial_id"]] = {"model": trial["model"], "domain": trial["domain"]}

# Build the metric: for each (trial, eval_turn) where level >= 4,
# check what happens at eval_turn + 1
cases_true = []   # sufficient AND genuine revision next
cases_false = []  # sufficient AND meta next

for (tid, turn), level in eval_lookup.items():
    if level < 4:
        continue
    next_turn = turn + 1
    if next_turn > 5:
        continue
    llm_info = llm_map.get((tid, next_turn))
    if not llm_info:
        continue
    is_genuine = llm_info["classifier_label"] == "GENUINE"
    meta = trial_meta.get(tid, {})
    case = {
        "trial_id": tid,
        "model": meta.get("model", "?"),
        "domain": meta.get("domain", "?"),
        "eval_turn": turn,
        "eval_level": level,
        "next_turn": next_turn,
        "next_label": llm_info["classifier_label"],
        "next_reason": llm_info.get("reason", ""),
    }
    if is_genuine:
        cases_true.append(case)
    else:
        cases_false.append(case)

total = len(cases_true) + len(cases_false)
rate = len(cases_true) / total if total > 0 else 0

print("=" * 80)
print("AUDIT: Revision-Despite-Sufficiency (39.4%)")
print("=" * 80)

# ── Report 3 first (the breakdown) ──
print(f"\n3. METRIC BREAKDOWN")
print(f"   Sufficient-output turns (level >= 4): {total}")
print(f"   -> Genuine revision next turn: {len(cases_true)} ({len(cases_true)/total*100:.1f}%)")
print(f"   -> Meta-response next turn:    {len(cases_false)} ({len(cases_false)/total*100:.1f}%)")
print(f"   Rate: {rate:.1%}")

# Confirm no double-counting: each (trial_id, eval_turn) should appear once
keys = [(c["trial_id"], c["eval_turn"]) for c in cases_true + cases_false]
print(f"\n   Unique (trial, eval_turn) pairs: {len(set(keys))}")
print(f"   Total cases: {len(keys)}")
print(f"   Double-counted: {len(keys) - len(set(keys))}")

# By eval_turn
print(f"\n   By eval turn:")
for t in [1, 2, 3, 4]:
    t_true = [c for c in cases_true if c["eval_turn"] == t]
    t_false = [c for c in cases_false if c["eval_turn"] == t]
    t_total = len(t_true) + len(t_false)
    t_rate = len(t_true) / t_total if t_total > 0 else 0
    print(f"     T{t}->T{t+1}: {len(t_true)}/{t_total} ({t_rate:.1%}) genuine | {len(t_false)} meta")

# By level
print(f"\n   By prior quality level:")
for lv in [4, 5]:
    lv_true = [c for c in cases_true if c["eval_level"] == lv]
    lv_false = [c for c in cases_false if c["eval_level"] == lv]
    lv_total = len(lv_true) + len(lv_false)
    lv_rate = len(lv_true) / lv_total if lv_total > 0 else 0
    print(f"     Level {lv}: {len(lv_true)}/{lv_total} ({lv_rate:.1%}) genuine")

# By model
print(f"\n   By model:")
for model in sorted(set(c["model"] for c in cases_true + cases_false)):
    m_true = [c for c in cases_true if c["model"] == model]
    m_false = [c for c in cases_false if c["model"] == model]
    m_total = len(m_true) + len(m_false)
    m_rate = len(m_true) / m_total if m_total > 0 else 0
    print(f"     {model:<22} {len(m_true)}/{m_total} ({m_rate:.1%})")

# ── 1. Sample 15 TRUE cases ──
print(f"\n{'=' * 80}")
print(f"1. 15 RANDOM TRUE CASES (sufficient, then genuine revision)")
print(f"{'=' * 80}")

random.seed(20260609)
sample_true = random.sample(cases_true, min(15, len(cases_true)))

for i, c in enumerate(sample_true, 1):
    prior_text = full_text.get((c["trial_id"], c["eval_turn"]), "(not found)")
    next_text = full_text.get((c["trial_id"], c["next_turn"]), "(not found)")
    print(f"\n  --- TRUE #{i} ---")
    print(f"  {c['model']} | {c['domain']} | T{c['eval_turn']}(level={c['eval_level']}) -> T{c['next_turn']}({c['next_label']})")
    print(f"  trial: {c['trial_id']}")
    print(f"  PRIOR OUTPUT (T{c['eval_turn']}, level={c['eval_level']}, {len(prior_text)} chars):")
    print(f"  {prior_text[:600]}")
    if len(prior_text) > 600:
        print(f"  [... +{len(prior_text)-600} chars]")
    print(f"  NEXT OUTPUT (T{c['next_turn']}, {c['next_label']}, {len(next_text)} chars):")
    print(f"  {next_text[:600]}")
    if len(next_text) > 600:
        print(f"  [... +{len(next_text)-600} chars]")
    print(f"  Classifier reason: {c['next_reason']}")
    print(f"  --- END #{i} ---")

# ── 2. Sample 5 FALSE cases ──
print(f"\n{'=' * 80}")
print(f"2. 5 RANDOM FALSE CASES (sufficient, then META decline)")
print(f"{'=' * 80}")

sample_false = random.sample(cases_false, min(5, len(cases_false)))

for i, c in enumerate(sample_false, 1):
    prior_text = full_text.get((c["trial_id"], c["eval_turn"]), "(not found)")
    next_text = full_text.get((c["trial_id"], c["next_turn"]), "(not found)")
    print(f"\n  --- FALSE #{i} ---")
    print(f"  {c['model']} | {c['domain']} | T{c['eval_turn']}(level={c['eval_level']}) -> T{c['next_turn']}({c['next_label']})")
    print(f"  trial: {c['trial_id']}")
    print(f"  PRIOR OUTPUT (T{c['eval_turn']}, level={c['eval_level']}, {len(prior_text)} chars):")
    print(f"  {prior_text[:600]}")
    if len(prior_text) > 600:
        print(f"  [... +{len(prior_text)-600} chars]")
    print(f"  NEXT OUTPUT (T{c['next_turn']}, {c['next_label']}, {len(next_text)} chars):")
    print(f"  {next_text[:600]}")
    if len(next_text) > 600:
        print(f"  [... +{len(next_text)-600} chars]")
    print(f"  Classifier reason: {c['next_reason']}")
    print(f"  --- END #{i} ---")
