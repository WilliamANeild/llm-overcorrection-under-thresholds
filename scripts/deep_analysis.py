"""Deep statistical analysis: 5 research angles for publication."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import pandas as pd
from scipy import stats as sp_stats

STATS_DIR = Path("data/analysis")
STATS_DIR.mkdir(parents=True, exist_ok=True)


def rank_biserial(u_stat, n1, n2):
    if n1 * n2 == 0:
        return np.nan
    return round(1 - (2 * u_stat) / (n1 * n2), 4)


def bonferroni_pairwise(df, group_col, val_col, groups, n_comparisons=None):
    """Pairwise Mann-Whitney with Bonferroni correction."""
    pairs = []
    group_list = sorted(groups)
    all_pairs = [(a, b) for i, a in enumerate(group_list) for b in group_list[i+1:]]
    if n_comparisons is None:
        n_comparisons = len(all_pairs)
    for a, b in all_pairs:
        va = df[df[group_col] == a][val_col].dropna().values
        vb = df[df[group_col] == b][val_col].dropna().values
        if len(va) < 2 or len(vb) < 2:
            continue
        u, p = sp_stats.mannwhitneyu(va, vb, alternative="two-sided")
        p_adj = min(p * n_comparisons, 1.0)
        r = rank_biserial(u, len(va), len(vb))
        pairs.append({
            "pair": f"{a} vs {b}",
            "U": round(u, 1),
            "p_raw": round(p, 6),
            "p_adj": round(p_adj, 6),
            "r": r,
            "sig": p_adj < 0.05,
            "mean_a": round(np.mean(va), 3),
            "mean_b": round(np.mean(vb), 3),
        })
    return pairs


def main():
    df = pd.read_csv("data/processed/scored_trials.csv")
    len_df = pd.read_csv("data/analysis/scored_with_length.csv")
    dims = ["revision_magnitude", "revision_value", "threshold_alignment", "overcorrection"]

    lines = []
    def log(s=""):
        lines.append(s)
        print(s)

    # ====================================================================
    # ANALYSIS 1: MODEL COMPARISON
    # ====================================================================
    log("# Deep Analysis 1: Between-Model Comparison")
    log("=" * 60)

    # Kruskal-Wallis across 3 models
    log("\n## Kruskal-Wallis: Overcorrection Across Models")
    for dim in dims:
        groups = [df[df["model"] == m][dim].dropna().values for m in sorted(df["model"].unique())]
        h, p = sp_stats.kruskal(*groups)
        sig = "*" if p < 0.05 else ""
        log(f"  {dim}: H={h:.2f}, p={p:.6f}{sig}")

    # Pairwise model comparisons
    log("\n## Pairwise Model Comparisons (overcorrection)")
    models = sorted(df["model"].unique())
    pairs = bonferroni_pairwise(df, "model", "overcorrection", models)
    for p in pairs:
        sig = "*" if p["sig"] else ""
        log(f"  {p['pair']}: U={p['U']}, p_adj={p['p_adj']:.6f}{sig}, r={p['r']}, means={p['mean_a']:.2f} vs {p['mean_b']:.2f}")

    # Revision gate by model (chi-squared)
    log("\n## Chi-Squared: Revision Gate by Model")
    ct = pd.crosstab(df["model"], df["revision_gate"])
    chi2, p, dof, _ = sp_stats.chi2_contingency(ct)
    log(f"  chi2={chi2:.2f}, dof={dof}, p={p:.6f}")
    log(f"  Gate distribution:")
    for model in models:
        mdf = df[df["model"] == model]
        gate_pcts = mdf["revision_gate"].value_counts(normalize=True) * 100
        log(f"    {model}: " + ", ".join(f"{g}={gate_pcts.get(g, 0):.1f}%" for g in ["decline", "suggest_minor", "full_revision"]))

    # Threshold sensitivity per model
    log("\n## Threshold Sensitivity Index: (OC@100 - OC@70) / OC@70")
    for model in models:
        mdf = df[df["model"] == model]
        oc70 = mdf[mdf["threshold_level"] == 70]["overcorrection"].mean()
        oc100 = mdf[mdf["threshold_level"] == 100]["overcorrection"].mean()
        if oc70 > 0:
            tsi = (oc100 - oc70) / oc70
            log(f"  {model}: OC@70={oc70:.2f}, OC@100={oc100:.2f}, TSI={tsi:.3f}")

    # Response length by model
    log("\n## Response Length by Model (Kruskal-Wallis)")
    groups = [len_df[len_df["model"] == m]["len_delta"].dropna().values for m in models]
    h, p = sp_stats.kruskal(*groups)
    log(f"  len_delta: H={h:.2f}, p={p:.6f}")
    pairs = bonferroni_pairwise(len_df, "model", "len_delta", models)
    for p in pairs:
        sig = "*" if p["sig"] else ""
        log(f"    {p['pair']}: U={p['U']}, p_adj={p['p_adj']:.6f}{sig}, r={p['r']}")

    # ====================================================================
    # ANALYSIS 2: FRAMING EFFECTS
    # ====================================================================
    log("\n\n# Deep Analysis 2: Framing Effects")
    log("=" * 60)

    # Pooled framing effect
    log("\n## Pooled Framing Effect (all models)")
    for dim in dims:
        vn = df[df["framing"] == "numeric"][dim].dropna().values
        vq = df[df["framing"] == "qualitative"][dim].dropna().values
        u, p = sp_stats.mannwhitneyu(vn, vq, alternative="two-sided")
        r = rank_biserial(u, len(vn), len(vq))
        sig = "*" if p < 0.05 else ""
        log(f"  {dim}: numeric_mean={np.mean(vn):.2f}, qual_mean={np.mean(vq):.2f}, U={u:.0f}, p={p:.6f}{sig}, r={r}")

    # Framing × threshold level: Spearman per framing per model
    log("\n## Spearman: threshold vs overcorrection, by framing and model")
    for model in models:
        for framing in ["numeric", "qualitative"]:
            subset = df[(df["model"] == model) & (df["framing"] == framing)]
            rho, p = sp_stats.spearmanr(subset["threshold_level"], subset["overcorrection"])
            sig = "*" if p < 0.05 else ""
            log(f"  {model} | {framing}: rho={rho:.3f}, p={p:.4f}{sig}")

    # Pairwise at each threshold level
    log("\n## Framing Comparison at Each Threshold Level (pooled across models)")
    for level in sorted(df["threshold_level"].unique()):
        vn = df[(df["framing"] == "numeric") & (df["threshold_level"] == level)]["overcorrection"].dropna().values
        vq = df[(df["framing"] == "qualitative") & (df["threshold_level"] == level)]["overcorrection"].dropna().values
        if len(vn) < 2 or len(vq) < 2:
            continue
        u, p = sp_stats.mannwhitneyu(vn, vq, alternative="two-sided")
        r = rank_biserial(u, len(vn), len(vq))
        sig = "*" if p < 0.05 else ""
        log(f"  Level {level}: numeric_mean={np.mean(vn):.2f}, qual_mean={np.mean(vq):.2f}, p={p:.4f}{sig}, r={r}")

    # ====================================================================
    # ANALYSIS 3: DOSE-RESPONSE
    # ====================================================================
    log("\n\n# Deep Analysis 3: Threshold Dose-Response")
    log("=" * 60)

    # Baseline vs all threshold conditions
    log("\n## Baseline (level=0) vs All Threshold Conditions (70-100)")
    baseline = df[df["threshold_level"] == 0]
    threshold = df[df["threshold_level"] > 0]
    for dim in dims:
        vb = baseline[dim].dropna().values
        vt = threshold[dim].dropna().values
        u, p = sp_stats.mannwhitneyu(vb, vt, alternative="two-sided")
        r = rank_biserial(u, len(vb), len(vt))
        sig = "*" if p < 0.05 else ""
        log(f"  {dim}: baseline_mean={np.mean(vb):.2f}, threshold_mean={np.mean(vt):.2f}, p={p:.6f}{sig}, r={r}")

    # Low vs high threshold
    log("\n## Low (70-80) vs High (90-100) Threshold")
    low = df[df["threshold_level"].isin([70, 75, 80])]
    high = df[df["threshold_level"].isin([90, 95, 100])]
    for dim in dims:
        vl = low[dim].dropna().values
        vh = high[dim].dropna().values
        u, p = sp_stats.mannwhitneyu(vl, vh, alternative="two-sided")
        r = rank_biserial(u, len(vl), len(vh))
        sig = "*" if p < 0.05 else ""
        log(f"  {dim}: low_mean={np.mean(vl):.2f}, high_mean={np.mean(vh):.2f}, p={p:.6f}{sig}, r={r}")

    # Per-model dose-response slope (OLS on means)
    log("\n## Per-Model Overcorrection Trend (mean OC at each level)")
    for model in models:
        mdf = df[df["model"] == model]
        means = mdf.groupby("threshold_level")["overcorrection"].mean()
        levels = np.array(sorted(means.index), dtype=float)
        vals = np.array([means[l] for l in levels])
        slope, intercept, r_val, p_val, std_err = sp_stats.linregress(levels, vals)
        log(f"  {model}: slope={slope:.5f}, R²={r_val**2:.4f}, p={p_val:.4f}")
        log(f"    Means by level: {dict(zip(levels.astype(int), np.round(vals, 2)))}")

    # Adjacent-level differences to find inflection
    log("\n## Adjacent-Level Differences (looking for inflection points)")
    for model in models:
        mdf = df[df["model"] == model]
        levels = sorted(mdf["threshold_level"].unique())
        means = {l: mdf[mdf["threshold_level"] == l]["overcorrection"].mean() for l in levels}
        diffs = []
        for i in range(1, len(levels)):
            d = means[levels[i]] - means[levels[i-1]]
            diffs.append(f"{levels[i-1]}->{levels[i]}: {d:+.3f}")
        log(f"  {model}: {', '.join(diffs)}")

    # Revision gate by threshold level
    log("\n## Revision Gate Distribution by Threshold Level")
    for level in sorted(df["threshold_level"].unique()):
        subset = df[df["threshold_level"] == level]
        n = len(subset)
        gate_pcts = subset["revision_gate"].value_counts(normalize=True) * 100
        decline_pct = gate_pcts.get("decline", 0)
        suggest_pct = gate_pcts.get("suggest_minor", 0)
        full_pct = gate_pcts.get("full_revision", 0)
        log(f"  Level {level}: decline={decline_pct:.1f}%, suggest_minor={suggest_pct:.1f}%, full_revision={full_pct:.1f}% (n={n})")

    # ====================================================================
    # ANALYSIS 4: SCENARIO SENSITIVITY
    # ====================================================================
    log("\n\n# Deep Analysis 4: Scenario Effects")
    log("=" * 60)

    scenarios = sorted(df["scenario_id"].unique())

    # Kruskal-Wallis across scenarios
    log("\n## Kruskal-Wallis: Overcorrection Across Scenarios")
    groups = [df[df["scenario_id"] == s]["overcorrection"].dropna().values for s in scenarios]
    h, p = sp_stats.kruskal(*groups)
    log(f"  H={h:.2f}, p={p:.6f}")

    # Per-model
    for model in models:
        mdf = df[df["model"] == model]
        groups = [mdf[mdf["scenario_id"] == s]["overcorrection"].dropna().values for s in scenarios]
        groups = [g for g in groups if len(g) > 0]
        h, p = sp_stats.kruskal(*groups)
        sig = "*" if p < 0.05 else ""
        log(f"  {model}: H={h:.2f}, p={p:.6f}{sig}")

    # Pairwise scenarios
    log("\n## Pairwise Scenario Comparisons (overcorrection)")
    pairs = bonferroni_pairwise(df, "scenario_id", "overcorrection", scenarios)
    for p in pairs:
        if p["sig"]:
            log(f"  {p['pair']}: p_adj={p['p_adj']:.6f}*, r={p['r']}, means={p['mean_a']:.2f} vs {p['mean_b']:.2f}")
    non_sig = [p for p in pairs if not p["sig"]]
    log(f"  ({len(non_sig)} non-significant pairs omitted)")

    # Formality analysis
    log("\n## Formality Analysis")
    formal = ["client_sales_email", "linkedin_job_announcement"]
    informal = ["brunch_cancellation", "coworker_funny_text"]
    neutral = ["pto_request"]

    df["formality"] = df["scenario_id"].map(
        {s: "formal" for s in formal} | {s: "informal" for s in informal} | {s: "neutral" for s in neutral}
    )

    vf = df[df["formality"] == "formal"]["overcorrection"].dropna().values
    vi = df[df["formality"] == "informal"]["overcorrection"].dropna().values
    vn = df[df["formality"] == "neutral"]["overcorrection"].dropna().values
    u, p = sp_stats.mannwhitneyu(vf, vi, alternative="two-sided")
    r = rank_biserial(u, len(vf), len(vi))
    sig = "*" if p < 0.05 else ""
    log(f"  Formal mean={np.mean(vf):.2f}, Informal mean={np.mean(vi):.2f}")
    log(f"  Mann-Whitney (formal vs informal): U={u:.0f}, p={p:.6f}{sig}, r={r}")

    # Response length by scenario
    log("\n## Response Length by Scenario")
    for s in scenarios:
        sdf = len_df[len_df["scenario_id"] == s]
        log(f"  {s}: turn2_mean={sdf['turn2_len'].mean():.0f}, delta_mean={sdf['len_delta'].mean():.0f}")

    # Revision gate by scenario
    log("\n## Revision Gate by Scenario (Chi-Squared)")
    ct = pd.crosstab(df["scenario_id"], df["revision_gate"])
    chi2, p, dof, _ = sp_stats.chi2_contingency(ct)
    log(f"  chi2={chi2:.2f}, dof={dof}, p={p:.6f}")

    # ====================================================================
    # ANALYSIS 5: INTERACTION EFFECTS
    # ====================================================================
    log("\n\n# Deep Analysis 5: Interaction Effects")
    log("=" * 60)

    # Model × Framing interaction
    log("\n## Model × Framing: Framing Effect Size by Model")
    for model in models:
        mdf = df[df["model"] == model]
        vn = mdf[mdf["framing"] == "numeric"]["overcorrection"].dropna().values
        vq = mdf[mdf["framing"] == "qualitative"]["overcorrection"].dropna().values
        u, p = sp_stats.mannwhitneyu(vn, vq, alternative="two-sided")
        r = rank_biserial(u, len(vn), len(vq))
        sig = "*" if p < 0.05 else ""
        log(f"  {model}: numeric_mean={np.mean(vn):.2f}, qual_mean={np.mean(vq):.2f}, r={r}, p={p:.4f}{sig}")

    # Model × Threshold: Spearman per model
    log("\n## Model × Threshold: Spearman rho per model")
    for model in models:
        mdf = df[df["model"] == model]
        rho, p = sp_stats.spearmanr(mdf["threshold_level"], mdf["overcorrection"])
        sig = "*" if p < 0.05 else ""
        log(f"  {model}: rho={rho:.4f}, p={p:.6f}{sig}")

    # Overcorrection-value paradox
    log("\n## Overcorrection-Value Paradox (Spearman: OC vs revision_value)")
    for model in models:
        mdf = df[df["model"] == model].dropna(subset=["overcorrection", "revision_value"])
        rho, p = sp_stats.spearmanr(mdf["overcorrection"], mdf["revision_value"])
        sig = "*" if p < 0.05 else ""
        log(f"  {model}: rho={rho:.3f}, p={p:.6f}{sig}")

    # Sycophancy signature
    log("\n## Sycophancy Signature: revision_magnitude × (5 - threshold_alignment)")
    df["sycophancy_score"] = df["revision_magnitude"] * (5 - df["threshold_alignment"])
    for model in models:
        mdf = df[df["model"] == model]
        log(f"  {model}: mean={mdf['sycophancy_score'].mean():.2f}, median={mdf['sycophancy_score'].median():.1f}")

    # Kruskal-Wallis on sycophancy score
    groups = [df[df["model"] == m]["sycophancy_score"].dropna().values for m in models]
    h, p = sp_stats.kruskal(*groups)
    log(f"  Kruskal-Wallis: H={h:.2f}, p={p:.6f}")

    # Decline behavior
    log("\n## Decline Behavior: Conditions with Most Declines")
    decline_df = df[df["revision_gate"] == "decline"]
    log(f"  Total declines: {len(decline_df)} / {len(df)} ({len(decline_df)/len(df)*100:.1f}%)")
    if len(decline_df) > 0:
        log(f"  By model: {dict(decline_df['model'].value_counts())}")
        log(f"  By scenario: {dict(decline_df['scenario_id'].value_counts())}")
        log(f"  By threshold: {dict(decline_df['threshold_level'].value_counts())}")
        log(f"  By framing: {dict(decline_df['framing'].value_counts())}")

    # Three-way outlier cells
    log("\n## Three-Way Outlier Cells (mean OC ≥ 1 SD above grand mean)")
    grand_mean = df["overcorrection"].mean()
    grand_std = df["overcorrection"].std()
    threshold_val = grand_mean + grand_std
    log(f"  Grand mean OC={grand_mean:.2f}, SD={grand_std:.2f}, threshold={threshold_val:.2f}")

    outlier_cells = []
    for (model, framing, level), group in df.groupby(["model", "framing", "threshold_level"]):
        mean_oc = group["overcorrection"].mean()
        if mean_oc >= threshold_val:
            outlier_cells.append({
                "model": model, "framing": framing, "level": level,
                "mean_oc": round(mean_oc, 2), "n": len(group)
            })

    if outlier_cells:
        for c in sorted(outlier_cells, key=lambda x: -x["mean_oc"]):
            log(f"  {c['model']} | {c['framing']} | level={c['level']}: OC={c['mean_oc']} (n={c['n']})")
    else:
        log("  (none)")

    # ====================================================================
    # SAVE
    # ====================================================================
    output_path = STATS_DIR / "deep_analysis_all.md"
    output_path.write_text("\n".join(lines) + "\n")
    print(f"\n\nSaved full deep analysis → {output_path}")


if __name__ == "__main__":
    main()
