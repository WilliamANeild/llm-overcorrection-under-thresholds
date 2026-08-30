#!/usr/bin/env python3
"""Recompute all metrics that depend on the revision/meta split, using LLM classifier labels.
Compare old (keyword) vs new (LLM) values.

Does NOT modify any .tex files. Report only.
"""

import json, sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import numpy as np
import pandas as pd
from scipy import stats as sp_stats

from scripts.config import (
    S3_EVALUATOR_RESULTS_PATH,
    S3_WORKER_TRIALS_PATH,
    S3_TARGETED_FEEDBACK_PATH,
    S3_REVERSIBILITY_RESULTS_PATH,
    S3_SELF_REFLECTION_PATH,
)
from scripts.utils import load_jsonl

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "study3" / "raw_responses"
LLM_LABELS = DATA_DIR / "genuine_meta_labels.jsonl"

# ── Load LLM labels ──
llm_label_map = {}  # (trial_id, turn) -> "GENUINE" or "META"
with open(LLM_LABELS) as f:
    for line in f:
        r = json.loads(line)
        llm_label_map[(r["trial_id"], r["turn"])] = r["classifier_label"]

# ── Old keyword classifier (copied from analyze.py) ──
def classify_revision_keyword(response):
    if not response or len(response.strip()) < 5:
        return False
    strong_decline = [
        "keep this as my final", "this is my final version",
        "i'd like to keep this", "i would like to keep this",
        "keep this as the final", "i'll keep this", "i will keep this",
        "happy with this version", "this version is ready",
        "no changes needed", "no improvements needed",
        "no further changes", "no further improvements",
        "no revisions needed", "nothing to improve",
        "nothing i would change", "i wouldn't change",
        "i don't think any changes", "don't see any need",
    ]
    weak_decline = [
        "looks good as is", "looks good as-is", "looks good",
        "already well", "already good", "ready to use",
        "ready as is", "ready as-is", "satisfied with",
        "meets the requirements", "the output is complete",
        "this is complete", "complete as is", "is ready",
        "is done", "i agree", "well done", "no need",
        "i think it's good", "i think this is good",
        "i think it looks good", "no, i think",
        "i'm satisfied", "final version", "no changes",
    ]
    head = response[:300].lower()
    for phrase in strong_decline:
        if phrase in head:
            return False
    if len(response) < 500:
        response_lower = response.lower()
        for phrase in weak_decline:
            if phrase in response_lower:
                return False
    return True


# ── Load data ──
trials = load_jsonl(S3_WORKER_TRIALS_PATH)
trials = [t for t in trials if t.get("status") == "success"]

eval_results = load_jsonl(S3_EVALUATOR_RESULTS_PATH)
eval_df = pd.DataFrame([r for r in eval_results if r.get("level") is not None])

# Apply fixed scale: Level 6 -> 2
eval_df["level"] = eval_df["level"].apply(lambda x: 2 if x == 6 else x)

# Build worker turns with BOTH classifiers
worker_rows = []
for trial in trials:
    for turn_idx, response in enumerate(trial["responses"]):
        turn = turn_idx + 1
        token_info = trial["token_counts"][turn_idx] if trial.get("token_counts") else {}
        kw_revised = True if turn == 1 else classify_revision_keyword(response)
        llm_revised = True if turn == 1 else (llm_label_map.get((trial["trial_id"], turn), "GENUINE") == "GENUINE")
        worker_rows.append({
            "trial_id": trial["trial_id"],
            "model": trial["model"],
            "domain": trial["domain"],
            "turn": turn,
            "kw_revised": kw_revised,
            "llm_revised": llm_revised,
            "output_tokens": token_info.get("output", 0) or 0,
            "response_length": len(response),
        })
worker_df = pd.DataFrame(worker_rows)

# Build revision flags for eval filtering
kw_flags = {}
llm_flags = {}
for trial in trials:
    for turn_idx, response in enumerate(trial["responses"]):
        turn = turn_idx + 1
        kw_flags[(trial["trial_id"], turn)] = True if turn == 1 else classify_revision_keyword(response)
        llm_flags[(trial["trial_id"], turn)] = True if turn == 1 else (llm_label_map.get((trial["trial_id"], turn), "GENUINE") == "GENUINE")


def get_rev_eval(flags):
    df = eval_df.copy()
    df["is_rev"] = df.apply(lambda r: flags.get((r["worker_trial_id"], r["turn"]), True), axis=1)
    return df[df["is_rev"]].drop(columns=["is_rev"])


print("=" * 80)
print("RECOMPUTATION: OLD (keyword) vs NEW (LLM classifier)")
print("Fixed 1-5 scale (Level 6 recoded to 2)")
print("=" * 80)


# ═══════════════════════════════════════════════════════════════════════════
# 1. REVISION RATE BY TURN
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("1. REVISION RATE BY TURN (T2-T5)")
print("=" * 80)

post_t1 = worker_df[worker_df["turn"] >= 2]

print(f"\n  {'Turn':<6} {'OLD (keyword)':<20} {'NEW (LLM)':<20} {'Delta':<10}")
print(f"  {'-'*56}")
for t in [2, 3, 4, 5]:
    t_data = post_t1[post_t1["turn"] == t]
    old_rate = t_data["kw_revised"].mean()
    new_rate = t_data["llm_revised"].mean()
    delta = new_rate - old_rate
    print(f"  T{t:<5} {old_rate:.1%}{'':<14} {new_rate:.1%}{'':<14} {delta:+.1%}")

old_overall = post_t1["kw_revised"].mean()
new_overall = post_t1["llm_revised"].mean()
print(f"  {'All':<6} {old_overall:.1%}{'':<14} {new_overall:.1%}{'':<14} {new_overall - old_overall:+.1%}")

print("\n  By model:")
print(f"  {'Model':<22} {'OLD overall':<14} {'NEW overall':<14} {'Delta':<10}")
print(f"  {'-'*60}")
for model in sorted(post_t1["model"].unique()):
    m_data = post_t1[post_t1["model"] == model]
    old_r = m_data["kw_revised"].mean()
    new_r = m_data["llm_revised"].mean()
    print(f"  {model:<22} {old_r:.1%}{'':<8} {new_r:.1%}{'':<8} {new_r - old_r:+.1%}")


# ═══════════════════════════════════════════════════════════════════════════
# 2. REVISION-DESPITE-SUFFICIENCY
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("2. REVISION-DESPITE-SUFFICIENCY")
print("=" * 80)

eval_match = eval_df[["worker_trial_id", "turn", "level"]].copy()
eval_match = eval_match.rename(columns={"worker_trial_id": "trial_id", "turn": "eval_turn"})
eval_match["next_turn"] = eval_match["eval_turn"] + 1

worker_next = worker_df[worker_df["turn"] >= 2][["trial_id", "turn", "kw_revised", "llm_revised"]].copy()
worker_next = worker_next.rename(columns={"turn": "next_turn"})

merged = eval_match.merge(worker_next, on=["trial_id", "next_turn"], how="inner")
done_at_t = merged[merged["level"] >= 4]

old_cases = done_at_t[done_at_t["kw_revised"] == True]
new_cases = done_at_t[done_at_t["llm_revised"] == True]

old_rate = len(old_cases) / len(done_at_t) if len(done_at_t) > 0 else 0
new_rate = len(new_cases) / len(done_at_t) if len(done_at_t) > 0 else 0

print(f"\n  Evaluator says done (level >= 4): {len(done_at_t)} cases")
print(f"  OLD (keyword): {len(old_cases)}/{len(done_at_t)} ({old_rate:.1%}) revise anyway")
print(f"  NEW (LLM):     {len(new_cases)}/{len(done_at_t)} ({new_rate:.1%}) revise anyway")
print(f"  Delta: {new_rate - old_rate:+.1%}")

print("\n  By turn:")
for t in sorted(done_at_t["eval_turn"].unique()):
    t_done = done_at_t[done_at_t["eval_turn"] == t]
    old_t = t_done[t_done["kw_revised"] == True]
    new_t = t_done[t_done["llm_revised"] == True]
    old_r = len(old_t) / len(t_done) if len(t_done) > 0 else 0
    new_r = len(new_t) / len(t_done) if len(t_done) > 0 else 0
    print(f"    T{int(t)}->T{int(t)+1}: OLD {len(old_t)}/{len(t_done)} ({old_r:.1%}) | NEW {len(new_t)}/{len(t_done)} ({new_r:.1%})")


# ═══════════════════════════════════════════════════════════════════════════
# 3. REVISION TAX
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("3. REVISION TAX")
print("=" * 80)

def compute_cary(level_by_turn, tokens_by_turn, cost_per_token):
    cary = {}
    for t in sorted(level_by_turn.keys()):
        cum_tokens = sum(tokens_by_turn.get(tt, 0) for tt in sorted(level_by_turn.keys()) if tt <= t)
        cary[t] = level_by_turn[t] - cost_per_token * cum_tokens
    return cary

def compute_tax_for_classifier(rev_eval, worker_df_col, col_name):
    """Compute revision tax using a specific classifier's revision flags."""
    results = {}
    for model in sorted(worker_df["model"].unique()):
        m_eval = rev_eval[rev_eval["model"] == model]
        m_worker = worker_df[worker_df["model"] == model]

        level_by_turn = m_eval.groupby("turn")["level"].mean().to_dict()
        tokens_by_turn = m_worker.groupby("turn")["output_tokens"].mean().to_dict()
        turns = sorted(level_by_turn.keys())

        if not turns:
            continue

        full_tokens = sum(tokens_by_turn.get(t, 0) for t in turns)
        cary = compute_cary(level_by_turn, tokens_by_turn, 1e-4)
        t_star = max(cary.keys(), key=lambda t: cary[t]) if cary else 1
        opt_tokens = sum(tokens_by_turn.get(t, 0) for t in turns if t <= t_star)

        tax_pct = ((full_tokens - opt_tokens) / opt_tokens * 100) if opt_tokens > 0 else 0
        waste_frac = ((full_tokens - opt_tokens) / full_tokens * 100) if full_tokens > 0 else 0

        results[model] = {
            "t_star": t_star,
            "tax_pct": tax_pct,
            "waste_frac": waste_frac,
            "opt_tokens": opt_tokens,
            "full_tokens": full_tokens,
        }
    return results

# Interpretation A: meta-responses excluded from quality scoring but their tokens still count in full_tokens
# (This is what the current code does -- worker_df includes ALL turns' tokens)
print("\n  Interpretation A: meta-response tokens COUNT as waste (included in full_tokens)")
print("  (Meta-responses excluded from quality scoring but their output tokens still accumulate)")

old_rev_eval = get_rev_eval(kw_flags)
new_rev_eval = get_rev_eval(llm_flags)

old_tax = compute_tax_for_classifier(old_rev_eval, worker_df, "kw_revised")
new_tax = compute_tax_for_classifier(new_rev_eval, worker_df, "llm_revised")

print(f"\n  {'Model':<22} {'OLD t*':<8} {'NEW t*':<8} {'OLD tax%':<12} {'NEW tax%':<12} {'OLD waste%':<12} {'NEW waste%':<12}")
print(f"  {'-'*88}")
for model in sorted(old_tax.keys()):
    o = old_tax[model]
    n = new_tax[model]
    print(f"  {model:<22} {o['t_star']:<8} {n['t_star']:<8} {o['tax_pct']:<12.1f} {n['tax_pct']:<12.1f} {o['waste_frac']:<12.1f} {n['waste_frac']:<12.1f}")

# Interpretation B: meta-response tokens excluded entirely (only genuine revision tokens count)
print("\n  Interpretation B: meta-response tokens EXCLUDED (only genuine revision turn tokens count)")

def compute_tax_genuine_tokens_only(rev_eval, flags):
    results = {}
    for model in sorted(worker_df["model"].unique()):
        m_eval = rev_eval[rev_eval["model"] == model]
        # Only count tokens from turns where the model produced genuine content
        m_worker_genuine = worker_df[(worker_df["model"] == model)]
        # For token aggregation, only include turns that are genuine revisions (or T1)
        genuine_tokens_by_turn = {}
        for t in range(1, 6):
            t_data = m_worker_genuine[m_worker_genuine["turn"] == t]
            if t == 1:
                genuine_tokens_by_turn[t] = t_data["output_tokens"].mean() if len(t_data) > 0 else 0
            else:
                # Only include tokens from genuine revisions
                t_genuine = t_data[t_data.apply(
                    lambda r: flags.get((r["trial_id"], r["turn"]), True), axis=1
                )]
                genuine_tokens_by_turn[t] = t_genuine["output_tokens"].mean() if len(t_genuine) > 0 else 0

        level_by_turn = m_eval.groupby("turn")["level"].mean().to_dict()
        turns = sorted(level_by_turn.keys())
        if not turns:
            continue

        full_tokens = sum(genuine_tokens_by_turn.get(t, 0) for t in turns)
        cary = compute_cary(level_by_turn, genuine_tokens_by_turn, 1e-4)
        t_star = max(cary.keys(), key=lambda t: cary[t]) if cary else 1
        opt_tokens = sum(genuine_tokens_by_turn.get(t, 0) for t in turns if t <= t_star)

        tax_pct = ((full_tokens - opt_tokens) / opt_tokens * 100) if opt_tokens > 0 else 0
        waste_frac = ((full_tokens - opt_tokens) / full_tokens * 100) if full_tokens > 0 else 0

        results[model] = {
            "t_star": t_star,
            "tax_pct": tax_pct,
            "waste_frac": waste_frac,
        }
    return results

old_tax_b = compute_tax_genuine_tokens_only(old_rev_eval, kw_flags)
new_tax_b = compute_tax_genuine_tokens_only(new_rev_eval, llm_flags)

print(f"\n  {'Model':<22} {'OLD t*':<8} {'NEW t*':<8} {'OLD tax%':<12} {'NEW tax%':<12} {'OLD waste%':<12} {'NEW waste%':<12}")
print(f"  {'-'*88}")
for model in sorted(old_tax_b.keys()):
    o = old_tax_b[model]
    n = new_tax_b[model]
    print(f"  {model:<22} {o['t_star']:<8} {n['t_star']:<8} {o['tax_pct']:<12.1f} {n['tax_pct']:<12.1f} {o['waste_frac']:<12.1f} {n['waste_frac']:<12.1f}")


# ═══════════════════════════════════════════════════════════════════════════
# 4. THE CLIFF (quality trajectories)
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("4. THE CLIFF (quality trajectories)")
print("=" * 80)

print("\n  Pooled revision-only mean quality by turn:")
print(f"  {'Turn':<6} {'OLD (keyword filter)':<22} {'NEW (LLM filter)':<22} {'Delta':<10}")
print(f"  {'-'*60}")

for t in range(1, 6):
    old_mean = old_rev_eval[old_rev_eval["turn"] == t]["level"].mean()
    new_mean = new_rev_eval[new_rev_eval["turn"] == t]["level"].mean()
    old_n = len(old_rev_eval[old_rev_eval["turn"] == t])
    new_n = len(new_rev_eval[new_rev_eval["turn"] == t])
    delta = new_mean - old_mean
    print(f"  T{t:<5} {old_mean:.3f} (n={old_n}){'':<6} {new_mean:.3f} (n={new_n}){'':<6} {delta:+.3f}")

old_t1 = old_rev_eval[old_rev_eval["turn"] == 1]["level"].mean()
old_t5 = old_rev_eval[old_rev_eval["turn"] == 5]["level"].mean()
new_t1 = new_rev_eval[new_rev_eval["turn"] == 1]["level"].mean()
new_t5 = new_rev_eval[new_rev_eval["turn"] == 5]["level"].mean()
print(f"\n  T1->T5 endpoint delta: OLD {old_t5 - old_t1:+.3f} | NEW {new_t5 - new_t1:+.3f}")

# Per-model cliff
print("\n  Per-model T1->T5 (revision-only):")
print(f"  {'Model':<22} {'OLD T1':<8} {'OLD T5':<8} {'OLD delta':<10} {'NEW T1':<8} {'NEW T5':<8} {'NEW delta':<10}")
print(f"  {'-'*78}")
for model in sorted(eval_df["model"].unique()):
    o_m = old_rev_eval[old_rev_eval["model"] == model]
    n_m = new_rev_eval[new_rev_eval["model"] == model]
    o_t1 = o_m[o_m["turn"] == 1]["level"].mean() if len(o_m[o_m["turn"] == 1]) > 0 else float('nan')
    o_t5 = o_m[o_m["turn"] == 5]["level"].mean() if len(o_m[o_m["turn"] == 5]) > 0 else float('nan')
    n_t1 = n_m[n_m["turn"] == 1]["level"].mean() if len(n_m[n_m["turn"] == 1]) > 0 else float('nan')
    n_t5 = n_m[n_m["turn"] == 5]["level"].mean() if len(n_m[n_m["turn"] == 5]) > 0 else float('nan')
    o_d = o_t5 - o_t1 if not (np.isnan(o_t1) or np.isnan(o_t5)) else float('nan')
    n_d = n_t5 - n_t1 if not (np.isnan(n_t1) or np.isnan(n_t5)) else float('nan')
    print(f"  {model:<22} {o_t1:<8.2f} {o_t5:<8.2f} {o_d:<+10.2f} {n_t1:<8.2f} {n_t5:<8.2f} {n_d:<+10.2f}")


# ═══════════════════════════════════════════════════════════════════════════
# 5. OTHER METRICS THAT CONSUMED THE KEYWORD SPLIT
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("5. OTHER METRICS CONSUMING KEYWORD SPLIT")
print("=" * 80)

# 5a. Survival rate (fraction still revising at each turn)
print("\n  5a. SURVIVAL RATE (fraction producing genuine revision at each turn)")
print(f"  {'Turn':<6} {'OLD':<14} {'NEW':<14} {'Delta':<10}")
print(f"  {'-'*44}")
for t in [2, 3, 4, 5]:
    t_data = worker_df[worker_df["turn"] == t]
    old_s = t_data["kw_revised"].mean()
    new_s = t_data["llm_revised"].mean()
    print(f"  T{t:<5} {old_s:.1%}{'':<8} {new_s:.1%}{'':<8} {new_s - old_s:+.1%}")

# 5b. Per-model survival to T5
print("\n  5b. SURVIVAL TO T5 (fraction with genuine revision at T5)")
print(f"  {'Model':<22} {'OLD':<14} {'NEW':<14} {'Delta':<10}")
print(f"  {'-'*60}")
t5_data = worker_df[worker_df["turn"] == 5]
for model in sorted(t5_data["model"].unique()):
    m_t5 = t5_data[t5_data["model"] == model]
    old_s = m_t5["kw_revised"].mean()
    new_s = m_t5["llm_revised"].mean()
    print(f"  {model:<22} {old_s:.1%}{'':<8} {new_s:.1%}{'':<8} {new_s - old_s:+.1%}")

# 5c. Balanced panel size (trials with genuine revisions at ALL 5 turns)
print("\n  5c. BALANCED PANEL (trials with genuine revision at all 5 turns)")
old_balanced = set()
new_balanced = set()
for trial_id in worker_df["trial_id"].unique():
    t_data = worker_df[worker_df["trial_id"] == trial_id]
    if all(t_data[t_data["turn"] == t]["kw_revised"].values[0] for t in range(1, 6)):
        old_balanced.add(trial_id)
    if all(t_data[t_data["turn"] == t]["llm_revised"].values[0] for t in range(1, 6)):
        new_balanced.add(trial_id)
print(f"  OLD: {len(old_balanced)} / 720 ({len(old_balanced)/720*100:.1f}%)")
print(f"  NEW: {len(new_balanced)} / 720 ({len(new_balanced)/720*100:.1f}%)")

# 5d. Balanced panel cliff
if new_balanced:
    print("\n  5d. BALANCED PANEL CLIFF")
    old_bp_eval = old_rev_eval[old_rev_eval["worker_trial_id"].isin(old_balanced)]
    new_bp_eval = new_rev_eval[new_rev_eval["worker_trial_id"].isin(new_balanced)]
    print(f"  {'Turn':<6} {'OLD':<14} {'NEW':<14}")
    print(f"  {'-'*34}")
    for t in range(1, 6):
        o_m = old_bp_eval[old_bp_eval["turn"] == t]["level"].mean()
        n_m = new_bp_eval[new_bp_eval["turn"] == t]["level"].mean()
        print(f"  T{t:<5} {o_m:.3f}{'':<8} {n_m:.3f}")
    o_delta = old_bp_eval[old_bp_eval["turn"] == 5]["level"].mean() - old_bp_eval[old_bp_eval["turn"] == 1]["level"].mean()
    n_delta = new_bp_eval[new_bp_eval["turn"] == 5]["level"].mean() - new_bp_eval[new_bp_eval["turn"] == 1]["level"].mean()
    print(f"  T1->T5 delta: OLD {o_delta:+.3f} | NEW {n_delta:+.3f}")

# 5e. Targeted feedback (depends on meta-response filter for generic baseline)
print("\n  5e. TARGETED FEEDBACK (n changes due to meta-response filter)")
targeted = load_jsonl(S3_TARGETED_FEEDBACK_PATH)
valid_targeted = [r for r in targeted if r.get("targeted_level") is not None and r.get("generic_level") is not None]

# Load generic responses to classify
generic_responses = {}
for trial in trials:
    for turn_idx, response in enumerate(trial["responses"]):
        turn = turn_idx + 1
        generic_responses[(trial["trial_id"], turn)] = response

old_filtered = []
new_filtered = []
for r in valid_targeted:
    tid = r.get("worker_trial_id", "")
    turn = r.get("turn", 0)
    resp = generic_responses.get((tid, turn), "")
    kw_is_rev = classify_revision_keyword(resp)
    llm_is_rev = llm_label_map.get((tid, turn), "GENUINE") == "GENUINE"
    if kw_is_rev:
        old_filtered.append(r)
    if llm_is_rev:
        new_filtered.append(r)

old_gen_mean = np.mean([r["generic_level"] for r in old_filtered]) if old_filtered else 0
old_tgt_mean = np.mean([r["targeted_level"] for r in old_filtered]) if old_filtered else 0
new_gen_mean = np.mean([r["generic_level"] for r in new_filtered]) if new_filtered else 0
new_tgt_mean = np.mean([r["targeted_level"] for r in new_filtered]) if new_filtered else 0

# Apply fixed scale to targeted feedback levels too
old_gen_fixed = np.mean([2 if r["generic_level"] == 6 else r["generic_level"] for r in old_filtered])
old_tgt_fixed = np.mean([2 if r["targeted_level"] == 6 else r["targeted_level"] for r in old_filtered])
new_gen_fixed = np.mean([2 if r["generic_level"] == 6 else r["generic_level"] for r in new_filtered])
new_tgt_fixed = np.mean([2 if r["targeted_level"] == 6 else r["targeted_level"] for r in new_filtered])

print(f"  OLD (keyword filter): n={len(old_filtered)}, generic={old_gen_fixed:.2f}, targeted={old_tgt_fixed:.2f}, delta={old_tgt_fixed - old_gen_fixed:+.2f}")
print(f"  NEW (LLM filter):     n={len(new_filtered)}, generic={new_gen_fixed:.2f}, targeted={new_tgt_fixed:.2f}, delta={new_tgt_fixed - new_gen_fixed:+.2f}")

# 5f. Content drift metrics (RQ6, RQ12) -- these skip meta-responses inline
# The edit ratio, semantic similarity, word count, instruction adherence all use classify_revision
# inline. Report how many data points change.
print("\n  5f. CONTENT DRIFT / EDIT RATIO (data point count change)")
old_content_n = sum(1 for r in worker_rows if r["turn"] >= 2 and r["kw_revised"])
new_content_n = sum(1 for r in worker_rows if r["turn"] >= 2 and r["llm_revised"])
print(f"  Turns used for content analysis: OLD {old_content_n} | NEW {new_content_n} | Delta {new_content_n - old_content_n}")

# 5g. Reversibility (RQ10) -- uses classify_revision to split revision-only vs meta
print("\n  5g. REVERSIBILITY (T5 revision vs meta split)")
t5_kw_rev = sum(1 for r in worker_rows if r["turn"] == 5 and r["kw_revised"])
t5_llm_rev = sum(1 for r in worker_rows if r["turn"] == 5 and r["llm_revised"])
print(f"  T5 classified as genuine revision: OLD {t5_kw_rev} | NEW {t5_llm_rev}")
print(f"  T5 classified as meta-response:    OLD {720 - t5_kw_rev} | NEW {720 - t5_llm_rev}")

# 5h. Self-reflection (RQ14) -- uses classify_revision for meta-contamination stratification
print("\n  5h. SELF-REFLECTION meta-contamination stratification")
meta_counts_old = {}
meta_counts_new = {}
for trial in trials:
    tid = trial["trial_id"]
    old_mc = sum(1 for i, resp in enumerate(trial["responses"]) if i >= 1 and not classify_revision_keyword(resp))
    new_mc = sum(1 for i in range(1, 5) if llm_label_map.get((tid, i+1), "GENUINE") == "META")
    meta_counts_old[tid] = old_mc
    meta_counts_new[tid] = new_mc

old_dist = defaultdict(int)
new_dist = defaultdict(int)
for v in meta_counts_old.values():
    old_dist[v] += 1
for v in meta_counts_new.values():
    new_dist[v] += 1
print(f"  Meta-responses per trial distribution:")
print(f"  {'Count':<8} {'OLD n_trials':<14} {'NEW n_trials':<14}")
for k in sorted(set(list(old_dist.keys()) + list(new_dist.keys()))):
    print(f"  {k:<8} {old_dist.get(k, 0):<14} {new_dist.get(k, 0):<14}")


print("\n" + "=" * 80)
print("RECOMPUTATION COMPLETE")
print("=" * 80)
