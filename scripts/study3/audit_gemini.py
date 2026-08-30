#!/usr/bin/env python3
"""Audit Gemini's LLM classifier labels."""

import json, sys, random
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import numpy as np
from scipy import stats as sp

from scripts.utils import load_jsonl
from scripts.config import S3_EVALUATOR_RESULTS_PATH, S3_WORKER_TRIALS_PATH

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "study3" / "raw_responses"

# Load LLM labels
llm_labels = {}
with open(DATA_DIR / "genuine_meta_labels.jsonl") as f:
    for line in f:
        r = json.loads(line)
        llm_labels[(r["trial_id"], r["turn"])] = r

# Load full response text
trials = load_jsonl(S3_WORKER_TRIALS_PATH)
trials = [t for t in trials if t.get("status") == "success"]

gemini_trials = [t for t in trials if t["model"] == "gemini-2.5-flash"]
print(f"Gemini trials: {len(gemini_trials)}")

# Build full text map
full_text = {}
for trial in gemini_trials:
    for i, resp in enumerate(trial["responses"]):
        full_text[(trial["trial_id"], i + 1)] = resp

# Load eval
eval_results = load_jsonl(S3_EVALUATOR_RESULTS_PATH)
eval_df = {(r["worker_trial_id"], r["turn"]): r for r in eval_results if r.get("level") is not None}

# ═══════════════════════════════════════════════════════════════════════════
# 1. GENUINE vs META counts by turn
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("1. GEMINI GENUINE vs META by turn")
print("=" * 80)

gemini_post_t1 = []
for trial in gemini_trials:
    for turn in [2, 3, 4, 5]:
        key = (trial["trial_id"], turn)
        label_info = llm_labels.get(key, {})
        gemini_post_t1.append({
            "trial_id": trial["trial_id"],
            "turn": turn,
            "label": label_info.get("classifier_label", "MISSING"),
            "reason": label_info.get("reason", ""),
            "keyword_label": label_info.get("keyword_label", ""),
        })

print(f"\n  {'Turn':<6} {'GENUINE':<10} {'META':<10} {'Total':<10}")
print(f"  {'-'*36}")
for t in [2, 3, 4, 5]:
    t_rows = [r for r in gemini_post_t1 if r["turn"] == t]
    gen = sum(1 for r in t_rows if r["label"] == "GENUINE")
    meta = sum(1 for r in t_rows if r["label"] == "META")
    print(f"  T{t:<5} {gen:<10} {meta:<10} {len(t_rows):<10}")

total_gen = sum(1 for r in gemini_post_t1 if r["label"] == "GENUINE")
total_meta = sum(1 for r in gemini_post_t1 if r["label"] == "META")
print(f"  {'All':<6} {total_gen:<10} {total_meta:<10} {len(gemini_post_t1):<10}")

# ═══════════════════════════════════════════════════════════════════════════
# 2. ALL Gemini GENUINE turns -- full text
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print(f"2. ALL GEMINI GENUINE TURNS ({total_gen} total) -- full text")
print("=" * 80)

genuine_rows = [r for r in gemini_post_t1 if r["label"] == "GENUINE"]
for i, r in enumerate(genuine_rows, 1):
    text = full_text.get((r["trial_id"], r["turn"]), "(not found)")
    reason = r["reason"]
    level_info = eval_df.get((r["trial_id"], r["turn"]))
    level = level_info["level"] if level_info else "?"
    print(f"\n  --- GENUINE #{i} ---")
    print(f"  trial={r['trial_id']} | T{r['turn']} | eval_level={level} | keyword={r['keyword_label']}")
    print(f"  Reason: {reason}")
    print(f"  TEXT ({len(text)} chars):")
    print(text[:3000])
    if len(text) > 3000:
        print(f"  [... truncated, {len(text)} total chars]")
    print(f"  --- END #{i} ---")

# ═══════════════════════════════════════════════════════════════════════════
# 3. Random 15 Gemini META turns -- full text + reason
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("3. RANDOM 15 GEMINI META TURNS -- full text + reason")
print("=" * 80)

meta_rows = [r for r in gemini_post_t1 if r["label"] == "META"]
random.seed(20260609)
sample_meta = random.sample(meta_rows, min(15, len(meta_rows)))

for i, r in enumerate(sample_meta, 1):
    text = full_text.get((r["trial_id"], r["turn"]), "(not found)")
    reason = r["reason"]
    level_info = eval_df.get((r["trial_id"], r["turn"]))
    level = level_info["level"] if level_info else "?"
    print(f"\n  --- META #{i} ---")
    print(f"  trial={r['trial_id']} | T{r['turn']} | eval_level={level} | keyword={r['keyword_label']}")
    print(f"  Reason: {reason}")
    print(f"  TEXT ({len(text)} chars):")
    print(text[:2000])
    if len(text) > 2000:
        print(f"  [... truncated, {len(text)} total chars]")
    print(f"  --- END #{i} ---")

# ═══════════════════════════════════════════════════════════════════════════
# 4. What IS testable for Gemini
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("4. TESTABLE GEMINI METRICS")
print("=" * 80)

print(f"\n  Overall genuine-revision rate: {total_gen}/{len(gemini_post_t1)} = {total_gen/len(gemini_post_t1)*100:.1f}%")
print(f"  Overall decline rate: {total_meta}/{len(gemini_post_t1)} = {total_meta/len(gemini_post_t1)*100:.1f}%")

# T1->T2 quality delta on trials with genuine T2
genuine_t2_tids = [r["trial_id"] for r in gemini_post_t1 if r["turn"] == 2 and r["label"] == "GENUINE"]
print(f"\n  Trials with genuine T2 revision: {len(genuine_t2_tids)}")

t1_vals = []
t2_vals = []
for tid in genuine_t2_tids:
    e1 = eval_df.get((tid, 1))
    e2 = eval_df.get((tid, 2))
    if e1 and e2:
        l1 = 2 if e1["level"] == 6 else e1["level"]
        l2 = 2 if e2["level"] == 6 else e2["level"]
        t1_vals.append(l1)
        t2_vals.append(l2)

n_paired = len(t1_vals)
print(f"  Paired T1-T2 observations: {n_paired}")

if n_paired >= 3:
    t1_arr = np.array(t1_vals)
    t2_arr = np.array(t2_vals)
    delta = np.mean(t2_arr) - np.mean(t1_arr)
    diffs = t2_arr - t1_arr
    nonzero = diffs[diffs != 0]
    print(f"  T1 mean: {np.mean(t1_arr):.3f}")
    print(f"  T2 mean: {np.mean(t2_arr):.3f}")
    print(f"  Delta: {delta:+.3f}")
    if len(nonzero) >= 1:
        stat, p = sp.wilcoxon(nonzero)
        z = sp.norm.ppf(p / 2) if p < 1 else 0
        r_eff = abs(z) / np.sqrt(len(nonzero)) if len(nonzero) > 0 else 0
        print(f"  Wilcoxon W={stat:.0f}, p={p:.4g}, r={r_eff:.3f}")
        print(f"  SIGNIFICANT: {'YES' if p < 0.05 else 'NO'}")
    else:
        print(f"  All diffs are zero -- no test possible")
    # Show individual pairs
    print(f"\n  Individual T1->T2 pairs:")
    for j, tid in enumerate(genuine_t2_tids):
        if j < len(t1_vals):
            print(f"    {tid}: T1={t1_vals[j]}, T2={t2_vals[j]}, delta={t2_vals[j]-t1_vals[j]:+d}")

# Per-turn genuine revision rate
print(f"\n  Genuine revision rate by turn:")
for t in [2, 3, 4, 5]:
    t_rows = [r for r in gemini_post_t1 if r["turn"] == t]
    gen = sum(1 for r in t_rows if r["label"] == "GENUINE")
    print(f"    T{t}: {gen}/{len(t_rows)} = {gen/len(t_rows)*100:.1f}%")

# How many trials have genuine revisions at ALL turns through T_k?
print(f"\n  Trials with unbroken genuine revision chain:")
for depth in [2, 3, 4, 5]:
    count = 0
    for trial in gemini_trials:
        all_genuine = all(
            llm_labels.get((trial["trial_id"], t), {}).get("classifier_label") == "GENUINE"
            for t in range(2, depth + 1)
        )
        if all_genuine:
            count += 1
    print(f"    Through T{depth}: {count}/{len(gemini_trials)} trials")

# ═══════════════════════════════════════════════════════════════════════════
# 5. DIAGNOSIS
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("5. DIAGNOSIS: untestable or mislabeled?")
print("=" * 80)

print(f"\n  Gemini produces genuine revision at T2 in only {len(genuine_t2_tids)}/{len(gemini_trials)} trials ({len(genuine_t2_tids)/len(gemini_trials)*100:.1f}%)")
print(f"  By T5, only {sum(1 for r in gemini_post_t1 if r['turn']==5 and r['label']=='GENUINE')}/{len(gemini_trials)} trials have a genuine T5 revision")

# Check: of the 8 GENUINE labels, how many does the keyword classifier agree with?
kw_agree = sum(1 for r in genuine_rows if r["keyword_label"] == "REVISION")
kw_disagree = sum(1 for r in genuine_rows if r["keyword_label"] == "META")
print(f"\n  Of {total_gen} GENUINE labels:")
print(f"    Keyword also said REVISION: {kw_agree}")
print(f"    Keyword said META (LLM upgraded): {kw_disagree}")

# Check: of the META labels, how many does keyword agree with?
kw_meta_agree = sum(1 for r in meta_rows if r["keyword_label"] == "META")
kw_meta_disagree = sum(1 for r in meta_rows if r["keyword_label"] == "REVISION")
print(f"\n  Of {total_meta} META labels:")
print(f"    Keyword also said META: {kw_meta_agree}")
print(f"    Keyword said REVISION (LLM downgraded): {kw_meta_disagree}")
