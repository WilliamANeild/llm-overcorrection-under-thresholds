#!/usr/bin/env python3
"""Significance tests on clean LLM-classified data, fixed 1-5 scale."""

import json, sys
import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from scripts.utils import load_jsonl
from scripts.config import S3_EVALUATOR_RESULTS_PATH, S3_WORKER_TRIALS_PATH, S3_TARGETED_FEEDBACK_PATH

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "study3" / "raw_responses"

# Load LLM labels
llm_map = {}
with open(DATA_DIR / "genuine_meta_labels.jsonl") as f:
    for line in f:
        r = json.loads(line)
        llm_map[(r["trial_id"], r["turn"])] = r["classifier_label"]

# Load eval, apply fixed scale
eval_results = load_jsonl(S3_EVALUATOR_RESULTS_PATH)
eval_df = pd.DataFrame([r for r in eval_results if r.get("level") is not None])
eval_df["level"] = eval_df["level"].apply(lambda x: 2 if x == 6 else x)

# Build revision flags
trials = load_jsonl(S3_WORKER_TRIALS_PATH)
trials = [t for t in trials if t.get("status") == "success"]

llm_flags = {}
for trial in trials:
    for i, resp in enumerate(trial["responses"]):
        turn = i + 1
        llm_flags[(trial["trial_id"], turn)] = True if turn == 1 else (llm_map.get((trial["trial_id"], turn), "GENUINE") == "GENUINE")

# Revision-only eval
eval_df["is_rev"] = eval_df.apply(lambda r: llm_flags.get((r["worker_trial_id"], r["turn"]), True), axis=1)
rev_eval = eval_df[eval_df["is_rev"]].copy()

# Worker turns
worker_rows = []
for trial in trials:
    for i, resp in enumerate(trial["responses"]):
        turn = i + 1
        tc = trial["token_counts"][i] if trial.get("token_counts") else {}
        worker_rows.append({
            "trial_id": trial["trial_id"],
            "model": trial["model"],
            "domain": trial["domain"],
            "turn": turn,
            "llm_revised": llm_flags[(trial["trial_id"], turn)],
            "output_tokens": tc.get("output", 0) or 0,
        })
worker_df = pd.DataFrame(worker_rows)


def bootstrap_ci(data, n_boot=10000, ci=0.95):
    data = np.array(data)
    means = [np.mean(np.random.choice(data, size=len(data), replace=True)) for _ in range(n_boot)]
    lo = np.percentile(means, (1 - ci) / 2 * 100)
    hi = np.percentile(means, (1 + ci) / 2 * 100)
    return lo, hi


def prop_ci(k, n, ci=0.95):
    """Wilson score interval."""
    from math import sqrt
    z = sp.norm.ppf((1 + ci) / 2)
    p = k / n
    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    spread = z * sqrt((p * (1 - p) + z**2 / (4 * n)) / n) / denom
    return center - spread, center + spread


print("=" * 100)
print("SIGNIFICANCE TESTS -- Clean LLM labels, fixed 1-5 scale")
print("=" * 100)

# ═══════════════════════════════════════════════════════════════════════════
# 1. CLIFF PER MODEL: T1->T5 paired test on genuine revisions
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 100)
print("1. CLIFF PER MODEL (T1 vs T5, genuine revisions only, paired by trial)")
print("=" * 100)

print(f"\n  {'Model':<22} {'n_pairs':<9} {'T1 mean':<9} {'T5 mean':<9} {'Delta':<9} {'Wilcoxon W':<12} {'p':<12} {'r (effect)':<12} {'Sig?':<6}")
print(f"  {'-'*105}")

for model in sorted(rev_eval["model"].unique()):
    m = rev_eval[rev_eval["model"] == model]
    t1 = m[m["turn"] == 1][["worker_trial_id", "level"]].rename(columns={"level": "t1"})
    t5 = m[m["turn"] == 5][["worker_trial_id", "level"]].rename(columns={"level": "t5"})
    paired = t1.merge(t5, on="worker_trial_id")
    n = len(paired)
    if n < 3:
        print(f"  {model:<22} {n:<9} -- insufficient pairs --")
        continue
    t1_vals = paired["t1"].values
    t5_vals = paired["t5"].values
    mean_t1 = np.mean(t1_vals)
    mean_t5 = np.mean(t5_vals)
    delta = mean_t5 - mean_t1
    diffs = t5_vals - t1_vals
    # Remove zeros for Wilcoxon
    nonzero = diffs[diffs != 0]
    if len(nonzero) < 1:
        print(f"  {model:<22} {n:<9} {mean_t1:<9.2f} {mean_t5:<9.2f} {delta:<+9.2f} {'--':<12} {'--':<12} {'--':<12} {'N/A':<6}")
        continue
    stat, p = sp.wilcoxon(nonzero)
    # Effect size r = Z / sqrt(N)
    z = sp.norm.ppf(p / 2)  # approximate Z from p
    r_eff = abs(z) / np.sqrt(len(nonzero))
    sig = "YES" if p < 0.05 else "NO"
    print(f"  {model:<22} {n:<9} {mean_t1:<9.2f} {mean_t5:<9.2f} {delta:<+9.2f} {stat:<12.0f} {p:<12.4g} {r_eff:<12.3f} {sig:<6}")


# ═══════════════════════════════════════════════════════════════════════════
# 2. BALANCED PANEL (n=52)
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 100)
print("2. BALANCED PANEL (trials with genuine revision at ALL 5 turns)")
print("=" * 100)

balanced_ids = set()
for tid in worker_df["trial_id"].unique():
    t_data = worker_df[worker_df["trial_id"] == tid]
    if all(t_data[t_data["turn"] == t]["llm_revised"].values[0] for t in range(1, 6)):
        balanced_ids.add(tid)

bp_eval = rev_eval[rev_eval["worker_trial_id"].isin(balanced_ids)]
bp_t1 = bp_eval[bp_eval["turn"] == 1][["worker_trial_id", "level"]].rename(columns={"level": "t1"})
bp_t5 = bp_eval[bp_eval["turn"] == 5][["worker_trial_id", "level"]].rename(columns={"level": "t5"})
bp_paired = bp_t1.merge(bp_t5, on="worker_trial_id")

n_bp = len(bp_paired)
t1_vals = bp_paired["t1"].values
t5_vals = bp_paired["t5"].values
delta_bp = np.mean(t5_vals) - np.mean(t1_vals)
diffs_bp = t5_vals - t1_vals

# Bootstrap CI on the delta
deltas_boot = []
rng = np.random.default_rng(42)
for _ in range(10000):
    idx = rng.choice(n_bp, size=n_bp, replace=True)
    deltas_boot.append(np.mean(diffs_bp[idx]))
ci_lo = np.percentile(deltas_boot, 2.5)
ci_hi = np.percentile(deltas_boot, 97.5)

nonzero_bp = diffs_bp[diffs_bp != 0]
stat_bp, p_bp = sp.wilcoxon(nonzero_bp) if len(nonzero_bp) > 0 else (0, 1)
z_bp = sp.norm.ppf(p_bp / 2) if p_bp < 1 else 0
r_bp = abs(z_bp) / np.sqrt(len(nonzero_bp)) if len(nonzero_bp) > 0 else 0

print(f"\n  n = {n_bp}")
print(f"  T1 mean: {np.mean(t1_vals):.3f}")
print(f"  T5 mean: {np.mean(t5_vals):.3f}")
print(f"  Delta: {delta_bp:+.3f}  95% CI [{ci_lo:+.3f}, {ci_hi:+.3f}]")
print(f"  Wilcoxon W = {stat_bp:.0f}, p = {p_bp:.4g}")
print(f"  Effect size r = {r_bp:.3f}")
print(f"  SIGNIFICANT: {'YES' if p_bp < 0.05 else 'NO'}")

# Per-turn means for the balanced panel
print(f"\n  Balanced panel trajectory:")
for t in range(1, 6):
    vals = bp_eval[bp_eval["turn"] == t]["level"].values
    print(f"    T{t}: {np.mean(vals):.3f} (n={len(vals)})")


# ═══════════════════════════════════════════════════════════════════════════
# 3. TARGETED vs GENERIC (n=106)
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 100)
print("3. TARGETED vs GENERIC FEEDBACK")
print("=" * 100)

targeted = load_jsonl(S3_TARGETED_FEEDBACK_PATH)

# Load generic responses for classification
generic_responses = {}
for trial in trials:
    for i, resp in enumerate(trial["responses"]):
        generic_responses[(trial["trial_id"], i + 1)] = resp

filtered = []
for r in targeted:
    tid = r["worker_trial_id"]
    turn = r["turn"]
    is_genuine = llm_map.get((tid, turn), "GENUINE") == "GENUINE"
    if is_genuine:
        gen_fixed = 2 if r["generic_next_level"] == 6 else r["generic_next_level"]
        tgt_fixed = 2 if r["targeted_level"] == 6 else r["targeted_level"]
        filtered.append({"gen": gen_fixed, "tgt": tgt_fixed, "tid": tid, "turn": turn})

n_tf = len(filtered)
gen_vals = np.array([r["gen"] for r in filtered])
tgt_vals = np.array([r["tgt"] for r in filtered])
delta_tf = np.mean(tgt_vals) - np.mean(gen_vals)
diffs_tf = tgt_vals - gen_vals

# Bootstrap CI
deltas_tf_boot = []
rng = np.random.default_rng(42)
for _ in range(10000):
    idx = rng.choice(n_tf, size=n_tf, replace=True)
    deltas_tf_boot.append(np.mean(diffs_tf[idx]))
ci_lo_tf = np.percentile(deltas_tf_boot, 2.5)
ci_hi_tf = np.percentile(deltas_tf_boot, 97.5)

nonzero_tf = diffs_tf[diffs_tf != 0]
stat_tf, p_tf = sp.wilcoxon(nonzero_tf) if len(nonzero_tf) > 0 else (0, 1)
z_tf = sp.norm.ppf(p_tf / 2) if p_tf < 1 else 0
r_tf = abs(z_tf) / np.sqrt(len(nonzero_tf)) if len(nonzero_tf) > 0 else 0

print(f"\n  n = {n_tf}")
print(f"  Generic mean: {np.mean(gen_vals):.3f}")
print(f"  Targeted mean: {np.mean(tgt_vals):.3f}")
print(f"  Delta: {delta_tf:+.3f}  95% CI [{ci_lo_tf:+.3f}, {ci_hi_tf:+.3f}]")
print(f"  Wilcoxon W = {stat_tf:.0f}, p = {p_tf:.4g}")
print(f"  Effect size r = {r_tf:.3f}")
print(f"  SIGNIFICANT: {'YES' if p_tf < 0.05 else 'NO'}")


# ═══════════════════════════════════════════════════════════════════════════
# 4. REVISION-DESPITE-SUFFICIENCY with CI
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 100)
print("4. REVISION-DESPITE-SUFFICIENCY")
print("=" * 100)

eval_match = eval_df[["worker_trial_id", "turn", "level"]].copy()
eval_match = eval_match.rename(columns={"worker_trial_id": "trial_id", "turn": "eval_turn"})
eval_match["next_turn"] = eval_match["eval_turn"] + 1

worker_next = worker_df[worker_df["turn"] >= 2][["trial_id", "turn", "llm_revised"]].copy()
worker_next = worker_next.rename(columns={"turn": "next_turn"})

merged = eval_match.merge(worker_next, on=["trial_id", "next_turn"], how="inner")
done = merged[merged["level"] >= 4]
k_total = done["llm_revised"].sum()
n_total = len(done)
rate = k_total / n_total

lo, hi = prop_ci(int(k_total), n_total)
print(f"\n  Overall: {int(k_total)}/{n_total} = {rate:.1%}  95% CI [{lo:.1%}, {hi:.1%}]")

print(f"\n  By turn:")
for t in sorted(done["eval_turn"].unique()):
    t_done = done[done["eval_turn"] == t]
    k = int(t_done["llm_revised"].sum())
    n = len(t_done)
    r = k / n if n > 0 else 0
    lo_t, hi_t = prop_ci(k, n) if n > 0 else (0, 0)
    print(f"    T{int(t)}->T{int(t)+1}: {k}/{n} = {r:.1%}  95% CI [{lo_t:.1%}, {hi_t:.1%}]")


# ═══════════════════════════════════════════════════════════════════════════
# 5. REVISION RATE BY TURN with CIs
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 100)
print("5. REVISION RATE BY TURN with CIs")
print("=" * 100)

post_t1 = worker_df[worker_df["turn"] >= 2]
print(f"\n  {'Turn':<6} {'Rate':<10} {'k/n':<12} {'95% CI':<20}")
print(f"  {'-'*48}")
for t in [2, 3, 4, 5]:
    t_data = post_t1[post_t1["turn"] == t]
    k = int(t_data["llm_revised"].sum())
    n = len(t_data)
    r = k / n
    lo, hi = prop_ci(k, n)
    print(f"  T{t:<5} {r:.1%}{'':<5} {k}/{n}{'':<4} [{lo:.1%}, {hi:.1%}]")


# ═══════════════════════════════════════════════════════════════════════════
# SUMMARY TABLE
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 100)
print("SUMMARY TABLE")
print("=" * 100)
print(f"\n  {'Metric':<45} {'Value':<12} {'Test':<14} {'p':<12} {'Effect r':<10} {'n':<8} {'Sig?':<6}")
print(f"  {'-'*107}")

# Re-gather per-model cliff results
for model in sorted(rev_eval["model"].unique()):
    m = rev_eval[rev_eval["model"] == model]
    t1 = m[m["turn"] == 1][["worker_trial_id", "level"]].rename(columns={"level": "t1"})
    t5 = m[m["turn"] == 5][["worker_trial_id", "level"]].rename(columns={"level": "t5"})
    paired = t1.merge(t5, on="worker_trial_id")
    n = len(paired)
    if n < 3:
        print(f"  Cliff {model:<38} {'n<3':<12} {'--':<14} {'--':<12} {'--':<10} {n:<8} {'N/A':<6}")
        continue
    diffs = paired["t5"].values - paired["t1"].values
    delta = np.mean(diffs)
    nonzero = diffs[diffs != 0]
    if len(nonzero) < 1:
        print(f"  Cliff {model:<38} {delta:<+12.2f} {'--':<14} {'--':<12} {'--':<10} {n:<8} {'N/A':<6}")
        continue
    stat, p = sp.wilcoxon(nonzero)
    z = sp.norm.ppf(p / 2)
    r_e = abs(z) / np.sqrt(len(nonzero))
    sig = "YES" if p < 0.05 else "NO"
    print(f"  Cliff {model:<38} {delta:<+12.2f} W={stat:<10.0f} {p:<12.4g} {r_e:<10.3f} {n:<8} {sig:<6}")

print(f"  Balanced panel T1->T5              {delta_bp:<+12.3f} W={stat_bp:<10.0f} {p_bp:<12.4g} {r_bp:<10.3f} {n_bp:<8} {'YES' if p_bp < 0.05 else 'NO':<6}")
print(f"  Targeted vs generic                {delta_tf:<+12.3f} W={stat_tf:<10.0f} {p_tf:<12.4g} {r_tf:<10.3f} {n_tf:<8} {'YES' if p_tf < 0.05 else 'NO':<6}")
print(f"  Rev-despite-sufficiency            {rate:<12.1%} {'prop':<14} {'--':<12} {'--':<10} {n_total:<8} {'YES':<6}")
print(f"  Rev rate T2                        {post_t1[post_t1['turn']==2]['llm_revised'].mean():<12.1%} {'prop':<14} {'--':<12} {'--':<10} {720:<8} {'--':<6}")
print(f"  Rev rate T5                        {post_t1[post_t1['turn']==5]['llm_revised'].mean():<12.1%} {'prop':<14} {'--':<12} {'--':<10} {720:<8} {'--':<6}")
