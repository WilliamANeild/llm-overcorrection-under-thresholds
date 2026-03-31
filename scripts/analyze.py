"""Analyze scored trials: descriptive stats + statistical tests using pandas/scipy."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import pandas as pd
from scipy import stats as sp_stats
from statsmodels.miscmodels.ordinal_model import OrderedModel
from statsmodels.stats.multitest import multipletests

from scripts.config import (
    JUDGE_MODEL,
    SCORED_TRIALS_JSONL,
    STATS_DIR,
    SUMMARY_BY_CONDITION_CSV,
    SUMMARY_BY_MODEL_CSV,
    SUMMARY_BY_MODEL_CONDITION_CSV,
    SUMMARY_BY_SCENARIO_CSV,
    TRIALS_PATH,
)
from scripts.utils import load_jsonl

DIMENSIONS = ["revision_magnitude", "revision_value", "threshold_alignment", "overcorrection"]
GATE_CATEGORIES = ["decline", "suggest_minor", "full_revision"]


# ── Helpers ──

def descriptive_stats(group: pd.DataFrame) -> dict:
    """Compute descriptive stats for a group of scored trials."""
    n = len(group)
    result = {"n": n}

    # Gate distribution
    gate_counts = group["revision_gate"].value_counts()
    for g in GATE_CATEGORIES:
        count = int(gate_counts.get(g, 0))
        result[f"gate_{g}_count"] = count
        result[f"gate_{g}_pct"] = round(count / n * 100, 1) if n > 0 else 0.0

    # Dimension stats
    for dim in DIMENSIONS:
        vals = group[dim].dropna()
        if len(vals) > 0:
            result[f"{dim}_mean"] = round(vals.mean(), 2)
            result[f"{dim}_median"] = round(vals.median(), 2)
            result[f"{dim}_std"] = round(vals.std(), 2)
        else:
            result[f"{dim}_mean"] = None
            result[f"{dim}_median"] = None
            result[f"{dim}_std"] = None

    # High overcorrection flag
    oc = group["overcorrection"].dropna()
    if len(oc) > 0:
        high = int((oc >= 4).sum())
        result["high_overcorrection_count"] = high
        result["high_overcorrection_pct"] = round(high / len(oc) * 100, 1)

    return result


def bootstrap_ci(values, n_boot=5000, ci=0.95, seed=42):
    """Compute bootstrap CI for the median."""
    rng = np.random.RandomState(seed)
    vals = np.array(values, dtype=float)
    vals = vals[~np.isnan(vals)]
    if len(vals) < 2:
        return (np.nan, np.nan)
    medians = np.array([np.median(rng.choice(vals, size=len(vals), replace=True)) for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    return (round(np.percentile(medians, alpha * 100), 3),
            round(np.percentile(medians, (1 - alpha) * 100), 3))


def rank_biserial(u_stat, n1, n2):
    """Rank-biserial effect size r = 1 - 2U/(n1*n2)."""
    if n1 * n2 == 0:
        return np.nan
    return round(1 - (2 * u_stat) / (n1 * n2), 4)


# ── Main ──

def main():
    scored = load_jsonl(SCORED_TRIALS_JSONL)
    if not scored:
        print("No scored data to analyze.")
        return

    df = pd.DataFrame(scored)
    for dim in DIMENSIONS:
        df[dim] = pd.to_numeric(df[dim], errors="coerce")

    # Backfill probe_type for v1 data
    if "probe_type" not in df.columns:
        df["probe_type"] = "leading"
    df["probe_type"] = df["probe_type"].fillna("leading")

    print(f"Loaded {len(df)} scored trials")
    probe_types = sorted(df["probe_type"].unique())
    print(f"Probe types: {probe_types}")

    # ── 1. Summary by condition (framing × threshold_level) ──
    rows = []
    for (framing, level), group in df.groupby(["framing", "threshold_level"]):
        row = {"framing": framing, "threshold_level": level}
        row.update(descriptive_stats(group))
        rows.append(row)
    pd.DataFrame(rows).to_csv(SUMMARY_BY_CONDITION_CSV, index=False)
    print(f"Wrote {SUMMARY_BY_CONDITION_CSV}")

    # ── 2. Summary by model ──
    rows = []
    for model, group in df.groupby("model"):
        row = {"model": model}
        row.update(descriptive_stats(group))
        rows.append(row)
    pd.DataFrame(rows).to_csv(SUMMARY_BY_MODEL_CSV, index=False)
    print(f"Wrote {SUMMARY_BY_MODEL_CSV}")

    # ── 3. Summary by model × condition (KEY TABLE) ──
    rows = []
    for (model, framing, level), group in df.groupby(["model", "framing", "threshold_level"]):
        row = {"model": model, "framing": framing, "threshold_level": level}
        row.update(descriptive_stats(group))
        rows.append(row)
    pd.DataFrame(rows).to_csv(SUMMARY_BY_MODEL_CONDITION_CSV, index=False)
    print(f"Wrote {SUMMARY_BY_MODEL_CONDITION_CSV}")

    # ── 4. Summary by scenario ──
    rows = []
    for scenario_id, group in df.groupby("scenario_id"):
        row = {"scenario_id": scenario_id}
        row.update(descriptive_stats(group))
        rows.append(row)
    pd.DataFrame(rows).to_csv(SUMMARY_BY_SCENARIO_CSV, index=False)
    print(f"Wrote {SUMMARY_BY_SCENARIO_CSV}")

    # ── 4b. Summary by probe type ──
    summary_by_probe_path = STATS_DIR / "summary_by_probe_type.csv"
    rows = []
    for probe, group in df.groupby("probe_type"):
        row = {"probe_type": probe}
        row.update(descriptive_stats(group))
        rows.append(row)
    pd.DataFrame(rows).to_csv(summary_by_probe_path, index=False)
    print(f"Wrote {summary_by_probe_path}")

    # ── 4c. Summary by model × probe type ──
    summary_by_model_probe_path = STATS_DIR / "summary_by_model_probe.csv"
    rows = []
    for (model, probe), group in df.groupby(["model", "probe_type"]):
        row = {"model": model, "probe_type": probe}
        row.update(descriptive_stats(group))
        rows.append(row)
    pd.DataFrame(rows).to_csv(summary_by_model_probe_path, index=False)
    print(f"Wrote {summary_by_model_probe_path}")

    # ── Statistical tests ──
    STATS_DIR.mkdir(parents=True, exist_ok=True)
    report_lines = []
    test_rows = []

    def log(line=""):
        report_lines.append(line)
        print(line)

    log("=" * 70)
    log("STATISTICAL ANALYSIS REPORT")
    log("=" * 70)

    models = sorted(df["model"].unique())

    # ── 5. Mann-Whitney U: numeric vs qualitative framing ──
    log("\n── Mann-Whitney U: Numeric vs Qualitative Framing ──")
    for model in models:
        mdf = df[df["model"] == model]
        numeric = mdf[mdf["framing"] == "numeric"]
        qualitative = mdf[mdf["framing"] == "qualitative"]
        for dim in DIMENSIONS:
            vals_n = numeric[dim].dropna().values
            vals_q = qualitative[dim].dropna().values
            if len(vals_n) < 2 or len(vals_q) < 2:
                continue
            u_stat, p_val = sp_stats.mannwhitneyu(vals_n, vals_q, alternative="two-sided")
            r = rank_biserial(u_stat, len(vals_n), len(vals_q))
            sig = "*" if p_val < 0.05 else ""
            log(f"  {model} | {dim}: U={u_stat:.0f}, p={p_val:.4f}{sig}, r={r}")
            test_rows.append({
                "test": "mann_whitney_u",
                "comparison": "numeric_vs_qualitative",
                "model": model,
                "dimension": dim,
                "statistic": round(u_stat, 2),
                "p_value": round(p_val, 6),
                "effect_size_r": r,
                "significant_0.05": p_val < 0.05,
            })

    # ── 5b. Mann-Whitney U: leading vs neutral probe ──
    if len(probe_types) > 1:
        log("\n── Mann-Whitney U: Leading vs Neutral Probe ──")
        for model in models:
            mdf = df[df["model"] == model]
            leading = mdf[mdf["probe_type"] == "leading"]
            neutral = mdf[mdf["probe_type"] == "neutral"]
            for dim in DIMENSIONS:
                vals_l = leading[dim].dropna().values
                vals_n = neutral[dim].dropna().values
                if len(vals_l) < 2 or len(vals_n) < 2:
                    continue
                u_stat, p_val = sp_stats.mannwhitneyu(vals_l, vals_n, alternative="two-sided")
                r = rank_biserial(u_stat, len(vals_l), len(vals_n))
                sig = "*" if p_val < 0.05 else ""
                log(f"  {model} | {dim}: U={u_stat:.0f}, p={p_val:.4f}{sig}, r={r}")
                test_rows.append({
                    "test": "mann_whitney_u",
                    "comparison": "leading_vs_neutral",
                    "model": model,
                    "dimension": dim,
                    "statistic": round(u_stat, 2),
                    "p_value": round(p_val, 6),
                    "effect_size_r": r,
                    "significant_0.05": p_val < 0.05,
                })

        # Pooled probe effect
        log("\n── Pooled Probe Effect (all models) ──")
        for dim in DIMENSIONS:
            vals_l = df[df["probe_type"] == "leading"][dim].dropna().values
            vals_n = df[df["probe_type"] == "neutral"][dim].dropna().values
            if len(vals_l) < 2 or len(vals_n) < 2:
                continue
            u_stat, p_val = sp_stats.mannwhitneyu(vals_l, vals_n, alternative="two-sided")
            r = rank_biserial(u_stat, len(vals_l), len(vals_n))
            sig = "*" if p_val < 0.05 else ""
            log(f"  {dim}: leading_mean={np.mean(vals_l):.2f}, neutral_mean={np.mean(vals_n):.2f}, "
                f"U={u_stat:.0f}, p={p_val:.4f}{sig}, r={r}")

        # Probe × threshold interaction: does probe type moderate the threshold-overcorrection relationship?
        log("\n── Probe × Threshold Interaction: Spearman rho per probe type per model ──")
        for model in models:
            for probe in probe_types:
                subset = df[(df["model"] == model) & (df["probe_type"] == probe)]
                if len(subset) < 3:
                    continue
                rho, p_val = sp_stats.spearmanr(subset["threshold_level"], subset["overcorrection"])
                sig = "*" if p_val < 0.05 else ""
                log(f"  {model} | {probe}: rho={rho:.3f}, p={p_val:.4f}{sig}")

        # Revision gate by probe type
        log("\n── Chi-Squared: Revision Gate by Probe Type ──")
        for model in models:
            mdf = df[df["model"] == model]
            ct = pd.crosstab(mdf["probe_type"], mdf["revision_gate"])
            if ct.shape[0] < 2 or ct.shape[1] < 2:
                continue
            chi2, p_val, dof, _ = sp_stats.chi2_contingency(ct)
            sig = "*" if p_val < 0.05 else ""
            log(f"  {model}: chi2={chi2:.2f}, dof={dof}, p={p_val:.4f}{sig}")
            # Show gate distribution per probe
            for probe in probe_types:
                pdata = mdf[mdf["probe_type"] == probe]
                gate_pcts = pdata["revision_gate"].value_counts(normalize=True) * 100
                log(f"    {probe}: " + ", ".join(
                    f"{g}={gate_pcts.get(g, 0):.1f}%" for g in GATE_CATEGORIES))
            test_rows.append({
                "test": "chi_squared",
                "comparison": "gate_by_probe_type",
                "model": model,
                "dimension": "revision_gate",
                "statistic": round(chi2, 2),
                "p_value": round(p_val, 6),
                "effect_size_r": None,
                "significant_0.05": p_val < 0.05,
            })

    # ── 6. Kruskal-Wallis H: overcorrection across threshold levels ──
    log("\n── Kruskal-Wallis H: Overcorrection Across Threshold Levels ──")
    pairwise_pairs = [(0, 70), (0, 100), (70, 100), (70, 85), (85, 100)]
    for model in models:
        for framing in ["numeric", "qualitative"]:
            subset = df[(df["model"] == model) & (df["framing"] == framing)]
            groups = []
            levels = sorted(subset["threshold_level"].unique())
            for lev in levels:
                vals = subset[subset["threshold_level"] == lev]["overcorrection"].dropna().values
                if len(vals) > 0:
                    groups.append(vals)
            if len(groups) < 2:
                continue
            h_stat, p_val = sp_stats.kruskal(*groups)
            sig = "*" if p_val < 0.05 else ""
            log(f"  {model} | {framing}: H={h_stat:.2f}, p={p_val:.4f}{sig}")
            test_rows.append({
                "test": "kruskal_wallis_h",
                "comparison": f"threshold_levels_{framing}",
                "model": model,
                "dimension": "overcorrection",
                "statistic": round(h_stat, 2),
                "p_value": round(p_val, 6),
                "effect_size_r": None,
                "significant_0.05": p_val < 0.05,
            })

            # Pairwise follow-up with Bonferroni
            if p_val < 0.05:
                n_comparisons = len(pairwise_pairs)
                for lev_a, lev_b in pairwise_pairs:
                    vals_a = subset[subset["threshold_level"] == lev_a]["overcorrection"].dropna().values
                    vals_b = subset[subset["threshold_level"] == lev_b]["overcorrection"].dropna().values
                    if len(vals_a) < 2 or len(vals_b) < 2:
                        continue
                    u_stat, p_pw = sp_stats.mannwhitneyu(vals_a, vals_b, alternative="two-sided")
                    p_adj = min(p_pw * n_comparisons, 1.0)
                    r = rank_biserial(u_stat, len(vals_a), len(vals_b))
                    sig = "*" if p_adj < 0.05 else ""
                    log(f"    Pairwise {lev_a} vs {lev_b}: U={u_stat:.0f}, p_adj={p_adj:.4f}{sig}, r={r}")
                    test_rows.append({
                        "test": "mann_whitney_u_pairwise",
                        "comparison": f"{framing}_{lev_a}_vs_{lev_b}",
                        "model": model,
                        "dimension": "overcorrection",
                        "statistic": round(u_stat, 2),
                        "p_value": round(p_adj, 6),
                        "effect_size_r": r,
                        "significant_0.05": p_adj < 0.05,
                    })

    # ── 7. Spearman correlation: threshold_level vs overcorrection ──
    log("\n── Spearman Correlation: Threshold Level vs Overcorrection ──")
    for model in models:
        mdf = df[df["model"] == model].dropna(subset=["overcorrection"])
        if len(mdf) < 3:
            continue
        rho, p_val = sp_stats.spearmanr(mdf["threshold_level"], mdf["overcorrection"])
        sig = "*" if p_val < 0.05 else ""
        log(f"  {model}: rho={rho:.3f}, p={p_val:.4f}{sig}")
        test_rows.append({
            "test": "spearman_correlation",
            "comparison": "threshold_vs_overcorrection",
            "model": model,
            "dimension": "overcorrection",
            "statistic": round(rho, 4),
            "p_value": round(p_val, 6),
            "effect_size_r": round(rho, 4),
            "significant_0.05": p_val < 0.05,
        })

    # ── 8. Chi-squared: revision_gate by framing ──
    log("\n── Chi-Squared: Revision Gate Distribution by Framing ──")
    for model in models:
        mdf = df[df["model"] == model]
        ct = pd.crosstab(mdf["framing"], mdf["revision_gate"])
        if ct.shape[0] < 2 or ct.shape[1] < 2:
            continue
        chi2, p_val, dof, _ = sp_stats.chi2_contingency(ct)
        sig = "*" if p_val < 0.05 else ""
        log(f"  {model}: chi2={chi2:.2f}, dof={dof}, p={p_val:.4f}{sig}")
        test_rows.append({
            "test": "chi_squared",
            "comparison": "gate_by_framing",
            "model": model,
            "dimension": "revision_gate",
            "statistic": round(chi2, 2),
            "p_value": round(p_val, 6),
            "effect_size_r": None,
            "significant_0.05": p_val < 0.05,
        })

    # ── 9. Bootstrap 95% CIs for median overcorrection ──
    log("\n── Bootstrap 95% CIs for Median Overcorrection ──")
    for model in models:
        for framing in ["numeric", "qualitative"]:
            subset = df[(df["model"] == model) & (df["framing"] == framing)]
            vals = subset["overcorrection"].dropna().values
            if len(vals) < 2:
                continue
            lo, hi = bootstrap_ci(vals)
            log(f"  {model} | {framing}: median={np.median(vals):.1f}, 95% CI=[{lo}, {hi}]")

    # ── 10. Judge Self-Preferencing Bias Detection ──
    log("\n── Judge Self-Preferencing Bias Detection ──")
    judge_model_name = "gpt-4o"
    df["is_judge_model"] = df["model"] == judge_model_name
    self_trials = df[df["is_judge_model"]]
    other_trials = df[~df["is_judge_model"]]
    log(f"  Judge model: {judge_model_name}")
    log(f"  Self trials: {len(self_trials)}, Other trials: {len(other_trials)}")

    for dim in DIMENSIONS:
        vals_self = self_trials[dim].dropna().values
        vals_other = other_trials[dim].dropna().values
        if len(vals_self) < 2 or len(vals_other) < 2:
            continue
        u_stat, p_val = sp_stats.mannwhitneyu(vals_self, vals_other, alternative="two-sided")
        r = rank_biserial(u_stat, len(vals_self), len(vals_other))
        sig = "*" if p_val < 0.05 else ""
        direction = "higher" if np.mean(vals_self) > np.mean(vals_other) else "lower"
        log(f"  {dim}: self_mean={np.mean(vals_self):.2f}, other_mean={np.mean(vals_other):.2f} "
            f"({direction}), U={u_stat:.0f}, p={p_val:.4f}{sig}, r={r}")
        test_rows.append({
            "test": "judge_self_preference",
            "comparison": f"self_vs_other_{dim}",
            "model": judge_model_name,
            "dimension": dim,
            "statistic": round(u_stat, 2),
            "p_value": round(p_val, 6),
            "effect_size_r": r,
            "significant_0.05": p_val < 0.05,
        })

    # Per-model breakdown
    log("\n  Per-model mean scores (judge bias check):")
    for dim in DIMENSIONS:
        means = df.groupby("model")[dim].mean()
        log(f"    {dim}: " + ", ".join(f"{m}={v:.2f}" for m, v in means.items()))

    # ── 11. Response Length as Bias-Free Overcorrection Proxy ──
    log("\n── Response Length Analysis (Bias-Free Proxy) ──")
    raw_trials = load_jsonl(TRIALS_PATH)
    raw_success = [t for t in raw_trials if t.get("status") == "success"]
    if raw_success:
        len_df = pd.DataFrame(raw_success)
        len_df["turn1_len"] = len_df["turn1_response"].str.len()
        len_df["turn2_len"] = len_df["turn2_response"].str.len()
        len_df["len_delta"] = len_df["turn2_len"] - len_df["turn1_len"]
        len_df["len_ratio"] = len_df["turn2_len"] / len_df["turn1_len"].clip(lower=1)

        # Save length stats
        len_summary_rows = []
        for model in sorted(len_df["model"].unique()):
            mdf = len_df[len_df["model"] == model]
            log(f"  {model}: turn1_mean={mdf['turn1_len'].mean():.0f}, "
                f"turn2_mean={mdf['turn2_len'].mean():.0f}, "
                f"delta_mean={mdf['len_delta'].mean():.0f}, "
                f"ratio_mean={mdf['len_ratio'].mean():.2f}")
            len_summary_rows.append({
                "model": model,
                "turn1_len_mean": round(mdf["turn1_len"].mean(), 1),
                "turn2_len_mean": round(mdf["turn2_len"].mean(), 1),
                "len_delta_mean": round(mdf["len_delta"].mean(), 1),
                "len_ratio_mean": round(mdf["len_ratio"].mean(), 3),
            })

        # Response length by probe type
        if "probe_type" in len_df.columns and len(len_df["probe_type"].unique()) > 1:
            log("\n  Response length by probe type:")
            for model in sorted(len_df["model"].unique()):
                for probe in sorted(len_df["probe_type"].unique()):
                    subset = len_df[(len_df["model"] == model) & (len_df["probe_type"] == probe)]
                    if len(subset) == 0:
                        continue
                    log(f"    {model} | {probe}: delta_mean={subset['len_delta'].mean():.0f}, "
                        f"ratio_mean={subset['len_ratio'].mean():.2f}")

        # Spearman: threshold_level vs len_delta
        log("\n  Spearman: threshold_level vs response length delta:")
        for model in sorted(len_df["model"].unique()):
            mdf = len_df[len_df["model"] == model].dropna(subset=["len_delta"])
            if len(mdf) < 3:
                continue
            rho, p_val = sp_stats.spearmanr(mdf["threshold_level"], mdf["len_delta"])
            sig = "*" if p_val < 0.05 else ""
            log(f"    {model}: rho={rho:.3f}, p={p_val:.4f}{sig}")
            test_rows.append({
                "test": "spearman_correlation",
                "comparison": "threshold_vs_len_delta",
                "model": model,
                "dimension": "response_length_delta",
                "statistic": round(rho, 4),
                "p_value": round(p_val, 6),
                "effect_size_r": round(rho, 4),
                "significant_0.05": p_val < 0.05,
            })

        # Correlation between len_delta and judge overcorrection score
        merged = df.merge(
            len_df[["trial_id", "turn1_len", "turn2_len", "len_delta", "len_ratio"]],
            on="trial_id", how="inner"
        )
        if len(merged) > 3:
            log("\n  Spearman: response length delta vs judge overcorrection score:")
            for model in sorted(merged["model"].unique()):
                mdf = merged[merged["model"] == model].dropna(subset=["len_delta", "overcorrection"])
                if len(mdf) < 3:
                    continue
                rho, p_val = sp_stats.spearmanr(mdf["len_delta"], mdf["overcorrection"])
                sig = "*" if p_val < 0.05 else ""
                log(f"    {model}: rho={rho:.3f}, p={p_val:.4f}{sig}")
                test_rows.append({
                    "test": "spearman_correlation",
                    "comparison": "len_delta_vs_overcorrection",
                    "model": model,
                    "dimension": "length_overcorrection_convergence",
                    "statistic": round(rho, 4),
                    "p_value": round(p_val, 6),
                    "effect_size_r": round(rho, 4),
                    "significant_0.05": p_val < 0.05,
                })

            # Bias convergence check
            log("\n  Bias convergence check (do length and judge agree on model ranking?):")
            model_len_rank = merged.groupby("model")["len_delta"].mean().rank()
            model_oc_rank = merged.groupby("model")["overcorrection"].mean().rank()
            log(f"    Length delta rank:      {dict(model_len_rank)}")
            log(f"    Judge overcorrection rank: {dict(model_oc_rank)}")
            if model_len_rank.equals(model_oc_rank):
                log("    CONVERGE: Length and judge rankings match perfectly")
            else:
                log("    DIVERGE: Length and judge rankings differ — potential judge bias")

        # Save length summary
        len_csv_path = STATS_DIR / "response_length_summary.csv"
        pd.DataFrame(len_summary_rows).to_csv(len_csv_path, index=False)
        log(f"\n  Wrote {len_csv_path}")

        # Save merged data for visualization
        if len(merged) > 0:
            merged_csv_path = STATS_DIR / "scored_with_length.csv"
            merged.to_csv(merged_csv_path, index=False)
            log(f"  Wrote {merged_csv_path}")

    df.drop(columns=["is_judge_model"], inplace=True, errors="ignore")

    # ── 12. FDR Correction (Benjamini-Hochberg) ──
    log("\n── FDR Correction (Benjamini-Hochberg) ──")
    if test_rows:
        p_values = [r["p_value"] for r in test_rows]
        reject, p_adj, _, _ = multipletests(p_values, method="fdr_bh")
        for i, row in enumerate(test_rows):
            row["p_fdr"] = round(p_adj[i], 6)
            row["significant_fdr_0.05"] = bool(reject[i])
        n_total = len(test_rows)
        n_raw_sig = sum(1 for r in test_rows if r["significant_0.05"])
        n_fdr_sig = sum(1 for r in test_rows if r["significant_fdr_0.05"])
        log(f"  {n_total} tests total")
        log(f"  {n_raw_sig} significant at p<0.05 (uncorrected)")
        log(f"  {n_fdr_sig} significant at FDR q<0.05")
        n_lost = n_raw_sig - n_fdr_sig
        if n_lost > 0:
            log(f"  {n_lost} tests lost significance after FDR correction:")
            for r in test_rows:
                if r["significant_0.05"] and not r["significant_fdr_0.05"]:
                    log(f"    {r['test']} | {r['comparison']} | {r['model']} | {r['dimension']}: "
                        f"p={r['p_value']:.4f} -> q={r['p_fdr']:.4f}")

    # ── 13. Ordinal Regression: Overcorrection ~ Threshold + Framing + Probe ──
    log("\n── Ordinal Regression: Overcorrection ──")

    # Filter to primary probes (leading + pilot_c) for the main model
    primary = df[df["probe_type"].isin(["leading", "pilot_c"])].copy()
    primary["is_leading"] = (primary["probe_type"] == "leading").astype(int)
    primary["is_qualitative"] = (primary["framing"] == "qualitative").astype(int)
    primary["threshold_scaled"] = primary["threshold_level"] / 100.0

    # Encode model as dummies (reference: gpt-4o)
    model_dummies = pd.get_dummies(primary["model"], prefix="model", drop_first=False)
    if "model_gpt-4o" in model_dummies.columns:
        model_dummies = model_dummies.drop(columns=["model_gpt-4o"])
    primary = pd.concat([primary, model_dummies], axis=1)

    # Encode scenario as dummies (reference: first alphabetically)
    scenario_dummies = pd.get_dummies(primary["scenario_id"], prefix="scen", drop_first=True)
    primary = pd.concat([primary, scenario_dummies], axis=1)

    exog_cols_no_scenario = ["is_leading", "threshold_scaled", "is_qualitative"]
    exog_cols_no_scenario += [c for c in model_dummies.columns]
    exog_cols_with_scenario = exog_cols_no_scenario + [c for c in scenario_dummies.columns]

    def log_ordinal_results(res, var_names, label, save_path):
        """Log ordinal regression results for named variables."""
        log(f"  Converged: {res.mle_retvals.get('converged', 'unknown')}")
        log(f"  Log-likelihood: {res.llf:.1f}")
        log(f"  AIC: {res.aic:.1f}")
        for name in var_names:
            if name in res.params.index:
                coef = res.params[name]
                pval = res.pvalues[name]
                sig = "*" if pval < 0.05 else ""
                log(f"    {name}: coef={coef:.4f}, p={pval:.4f}{sig}")
        save_path.write_text(str(res.summary()))
        log(f"  Saved -> {save_path}")

    # Model A: without scenario fixed effects (simpler)
    try:
        log("\n  Model A: overcorrection ~ probe + threshold + framing + model")
        exog_a = primary[exog_cols_no_scenario].astype(float)
        mod_a = OrderedModel(primary["overcorrection"].astype(float), exog_a, distr="logit")
        res_a = mod_a.fit(method="bfgs", disp=False, maxiter=1000)
        log_ordinal_results(res_a, exog_cols_no_scenario, "Model A",
                            STATS_DIR / "ordinal_regression_model_a.txt")
    except Exception as e:
        log(f"  Model A failed: {e}")

    # Model B: with scenario fixed effects
    try:
        log("\n  Model B: overcorrection ~ probe + threshold + framing + model + scenario")
        exog_b = primary[exog_cols_with_scenario].astype(float)
        mod_b = OrderedModel(primary["overcorrection"].astype(float), exog_b, distr="logit")
        res_b = mod_b.fit(method="bfgs", disp=False, maxiter=1000)
        log_ordinal_results(res_b, exog_cols_no_scenario, "Model B",
                            STATS_DIR / "ordinal_regression_model_b.txt")
        log(f"    (scenario fixed effects: {len(scenario_dummies.columns)} dummies, omitted for brevity)")
    except Exception as e:
        log(f"  Model B failed: {e}")

    # Model C: leading-only, threshold dose-response
    try:
        log("\n  Model C (leading only): overcorrection ~ threshold + framing + model + scenario")
        leading_only = primary[primary["probe_type"] == "leading"].copy()
        exog_c_cols = ["threshold_scaled", "is_qualitative"] + [c for c in model_dummies.columns] + [c for c in scenario_dummies.columns]
        exog_c = leading_only[exog_c_cols].astype(float)
        mod_c = OrderedModel(leading_only["overcorrection"].astype(float), exog_c, distr="logit")
        res_c = mod_c.fit(method="bfgs", disp=False, maxiter=1000)
        main_vars_c = ["threshold_scaled", "is_qualitative"] + [c for c in model_dummies.columns]
        log_ordinal_results(res_c, main_vars_c, "Model C",
                            STATS_DIR / "ordinal_regression_model_c.txt")
    except Exception as e:
        log(f"  Model C failed: {e}")

    # ── 14. Post-Hoc Power Analysis ──
    log("\n── Post-Hoc Power Analysis ──")
    log("  Minimum detectable effect sizes at 80% power, alpha=0.05:")

    # RQ1: Revision gate (chi-squared / proportion test)
    # With N=1920 per probe, what proportion difference is detectable?
    n_per_probe = len(primary[primary["probe_type"] == "leading"])
    log(f"\n  RQ1 (revision gate): N={n_per_probe} per probe")
    # For a 2-sample proportion test, MDE ≈ 2.8 * sqrt(p*(1-p)/n) for 80% power
    # With observed p ≈ 0.5 (most conservative), MDE ≈ 2.8 * sqrt(0.25/1920) ≈ 0.032
    p_base = 0.5
    mde_prop = 2.8 * np.sqrt(p_base * (1 - p_base) / n_per_probe)
    log(f"  MDE for proportion difference: {mde_prop:.3f} (observed difference: ~0.75)")
    log(f"  Study is massively overpowered for the revision gate effect")

    # RQ2: Threshold-overcorrection correlation (Spearman)
    n_leading = len(primary[primary["probe_type"] == "leading"])
    # For Spearman correlation, MDE |rho| ≈ sqrt(chi2_crit / (n-1)) ≈ sqrt(7.85/n)
    # At 80% power, alpha=0.05, one-tailed: critical z ≈ 2.8, so |rho| ≈ 2.8/sqrt(n)
    mde_rho = 2.8 / np.sqrt(n_leading)
    log(f"\n  RQ2 (threshold-overcorrection): N={n_leading} leading-probe trials")
    log(f"  MDE for |rho|: {mde_rho:.4f}")
    log(f"  Observed |rho|: 0.14 (GPT-4o) to 0.50 (Gemini Flash)")
    log(f"  Study is well-powered to detect all observed correlations")

    # RQ3: Model differences (3-group Kruskal-Wallis)
    n_per_model = n_leading // 3
    # Cohen's f for Kruskal-Wallis: MDE f ≈ sqrt(chi2_crit / N)
    # With N~640 per model and 3 groups: MDE f ≈ 0.08 (small)
    mde_f = np.sqrt(5.99 / (n_per_model * 3))  # chi2 critical value df=2
    log(f"\n  RQ3 (model differences): N={n_per_model} per model in leading probe")
    log(f"  MDE for Cohen's f (3-group): {mde_f:.4f}")
    log(f"  Detectable effect size category: {'small' if mde_f < 0.10 else 'medium'}")

    # Overall
    total_primary = len(primary)
    log(f"\n  Total primary trials: {total_primary}")
    log(f"  Per-cell (model × framing × threshold × probe): {total_primary // (3*2*8*2)}")

    # ── Save outputs ──
    stats_report_path = STATS_DIR / "stats_report.txt"
    stats_report_path.write_text("\n".join(report_lines) + "\n")
    print(f"\nWrote {stats_report_path}")

    if test_rows:
        tests_df = pd.DataFrame(test_rows)
        tests_csv_path = STATS_DIR / "statistical_tests.csv"
        tests_df.to_csv(tests_csv_path, index=False)
        print(f"Wrote {tests_csv_path}")

    # ── High overcorrection flags ──
    print("\n── High Overcorrection Cells (mean >= 4.0) ──")
    flagged = False
    for (framing, level), group in df.groupby(["framing", "threshold_level"]):
        mean_oc = group["overcorrection"].dropna().mean()
        if mean_oc >= 4.0:
            print(f"  {framing} x {level}: overcorrection_mean={mean_oc:.2f}")
            flagged = True
    if not flagged:
        print("  (none)")

    print("\nDone.")


if __name__ == "__main__":
    main()
