"""
Deep Scenario Effects Analysis
==============================
Computes scenario-level statistical tests for the LLM overcorrection study:
1. Kruskal-Wallis on overcorrection across scenarios (pooled + per-model)
2. Pairwise Mann-Whitney with Bonferroni correction
3. Model x Scenario interaction
4. Scenario x Threshold interaction
5. Formality classification analysis
6. Response length (len_delta) by scenario
7. Revision gate by scenario (chi-squared)

Writes findings to data/analysis/deep_scenario_effects.md
"""

import os
import sys
import warnings
from itertools import combinations

import numpy as np
import pandas as pd
from scipy import stats

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCORED = os.path.join(ROOT, "data", "processed", "scored_trials.csv")
LENGTH = os.path.join(ROOT, "data", "analysis", "scored_with_length.csv")
OUTPUT = os.path.join(ROOT, "data", "analysis", "deep_scenario_effects.md")

# ── Load data ────────────────────────────────────────────────────────────────
df = pd.read_csv(SCORED)
df_len = pd.read_csv(LENGTH)

print(f"Scored trials: {len(df)} rows, {df['scenario_id'].nunique()} scenarios, {df['model'].nunique()} models")
print(f"Length-augmented: {len(df_len)} rows")
print(f"Scenarios: {sorted(df['scenario_id'].unique())}")
print(f"Models: {sorted(df['model'].unique())}")
print(f"Threshold levels: {sorted(df['threshold_level'].unique())}")
print()

scenarios = sorted(df["scenario_id"].unique())
models = sorted(df["model"].unique())

# ── Helpers ──────────────────────────────────────────────────────────────────
def effect_size_eta_squared_kw(H, n, k):
    """Eta-squared for Kruskal-Wallis: (H - k + 1) / (n - k)"""
    return (H - k + 1) / (n - k)

def rank_biserial(u, n1, n2):
    """Rank-biserial correlation r = 1 - 2U/(n1*n2)"""
    return 1 - (2 * u) / (n1 * n2)

md_lines = []  # accumulate markdown output

def section(title):
    md_lines.append(f"\n## {title}\n")
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}")

def finding(text):
    md_lines.append(f"**{text}**\n")
    print(f"  >> {text}")

def detail(text):
    md_lines.append(f"{text}\n")
    print(f"     {text}")

def table(headers, rows):
    md_lines.append("| " + " | ".join(headers) + " |")
    md_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        md_lines.append("| " + " | ".join(str(c) for c in row) + " |")
    md_lines.append("")

# ══════════════════════════════════════════════════════════════════════════════
# 1. Kruskal-Wallis: overcorrection across 5 scenarios
# ══════════════════════════════════════════════════════════════════════════════
section("1. Kruskal-Wallis: Overcorrection Across Scenarios")

# Pooled
groups = [df.loc[df["scenario_id"] == s, "overcorrection"].values for s in scenarios]
H_pooled, p_pooled = stats.kruskal(*groups)
n_total = sum(len(g) for g in groups)
eta2_pooled = effect_size_eta_squared_kw(H_pooled, n_total, len(scenarios))

finding(f"Pooled Kruskal-Wallis: H({len(scenarios)-1}) = {H_pooled:.3f}, p = {p_pooled:.6f}, eta^2 = {eta2_pooled:.4f}")

desc_rows = []
for s in scenarios:
    vals = df.loc[df["scenario_id"] == s, "overcorrection"]
    desc_rows.append([s, f"{vals.mean():.3f}", f"{vals.median():.1f}", f"{vals.std():.3f}", str(len(vals))])
table(["Scenario", "Mean OC", "Median OC", "SD", "N"], desc_rows)

detail(f"Interpretation: {'Significant' if p_pooled < 0.05 else 'Non-significant'} differences in overcorrection across the five scenarios "
       f"(p = {p_pooled:.6f}). Effect size eta^2 = {eta2_pooled:.4f} ({'small' if eta2_pooled < 0.06 else 'medium' if eta2_pooled < 0.14 else 'large'}).")

# Per-model
detail("")
detail("### Per-Model Kruskal-Wallis")
per_model_rows = []
for m in models:
    sub = df[df["model"] == m]
    grps = [sub.loc[sub["scenario_id"] == s, "overcorrection"].values for s in scenarios]
    H_m, p_m = stats.kruskal(*grps)
    n_m = sum(len(g) for g in grps)
    eta2_m = effect_size_eta_squared_kw(H_m, n_m, len(scenarios))
    per_model_rows.append([m, f"H({len(scenarios)-1}) = {H_m:.3f}", f"p = {p_m:.6f}", f"eta^2 = {eta2_m:.4f}"])
    print(f"  {m}: H = {H_m:.3f}, p = {p_m:.6f}, eta^2 = {eta2_m:.4f}")
table(["Model", "H-statistic", "p-value", "Effect Size"], per_model_rows)

# ══════════════════════════════════════════════════════════════════════════════
# 2. Pairwise Mann-Whitney with Bonferroni
# ══════════════════════════════════════════════════════════════════════════════
section("2. Pairwise Mann-Whitney U with Bonferroni Correction")

pairs = list(combinations(scenarios, 2))
n_comparisons = len(pairs)
pw_rows = []

for s1, s2 in pairs:
    g1 = df.loc[df["scenario_id"] == s1, "overcorrection"].values
    g2 = df.loc[df["scenario_id"] == s2, "overcorrection"].values
    U, p_raw = stats.mannwhitneyu(g1, g2, alternative="two-sided")
    p_adj = min(p_raw * n_comparisons, 1.0)
    r = rank_biserial(U, len(g1), len(g2))
    sig = "***" if p_adj < 0.001 else "**" if p_adj < 0.01 else "*" if p_adj < 0.05 else "ns"
    pw_rows.append([f"{s1} vs {s2}", f"U = {U:.0f}", f"{p_raw:.6f}", f"{p_adj:.6f}", f"r = {r:.3f}", sig])
    if p_adj < 0.05:
        print(f"  {s1} vs {s2}: U={U:.0f}, p_adj={p_adj:.6f}, r={r:.3f} {sig}")

table(["Comparison", "U", "p (raw)", "p (Bonferroni)", "Effect Size (r)", "Sig."], pw_rows)

sig_pairs = [r for r in pw_rows if r[-1] != "ns"]
finding(f"{len(sig_pairs)} of {n_comparisons} pairwise comparisons significant after Bonferroni correction.")
detail("Suggestion: Present as a heatmap of pairwise effect sizes (rank-biserial r) with significance annotations.")

# ══════════════════════════════════════════════════════════════════════════════
# 3. Model × Scenario Interaction
# ══════════════════════════════════════════════════════════════════════════════
section("3. Model x Scenario Interaction")

detail("### Mean Overcorrection by Model x Scenario")
pivot = df.pivot_table(values="overcorrection", index="model", columns="scenario_id", aggfunc="mean")
pivot_rows = []
for m in models:
    row = [m] + [f"{pivot.loc[m, s]:.3f}" for s in scenarios]
    pivot_rows.append(row)
table(["Model"] + scenarios, pivot_rows)

# Friedman-like approach: Kruskal-Wallis on scenarios within each model, compare patterns
# Use a two-way approach: For each scenario, KW across models
detail("### Kruskal-Wallis on Models Within Each Scenario")
ms_rows = []
for s in scenarios:
    sub = df[df["scenario_id"] == s]
    grps = [sub.loc[sub["model"] == m, "overcorrection"].values for m in models]
    H_s, p_s = stats.kruskal(*grps)
    n_s = sum(len(g) for g in grps)
    eta2_s = effect_size_eta_squared_kw(H_s, n_s, len(models))
    ms_rows.append([s, f"H({len(models)-1}) = {H_s:.3f}", f"p = {p_s:.6f}", f"eta^2 = {eta2_s:.4f}"])
    print(f"  {s}: H = {H_s:.3f}, p = {p_s:.6f}")
table(["Scenario", "H-statistic", "p-value", "Effect Size"], ms_rows)

# Compute interaction evidence: variance of model-means across scenarios
model_means = pivot.values  # models x scenarios
grand_mean = df["overcorrection"].mean()
# Interaction: does the model ranking change across scenarios?
ranks_by_scenario = pivot.rank(axis=0)
rank_variance = ranks_by_scenario.var(axis=1)
detail("### Model Rank Variance Across Scenarios (higher = more inconsistent ranking)")
for m in models:
    detail(f"  {m}: rank variance = {rank_variance.loc[m]:.3f}, mean rank = {ranks_by_scenario.loc[m].mean():.2f}")

# Aligned Rank Transform approximation using Scheirer-Ray-Hare
detail("")
detail("### Scheirer-Ray-Hare Test (non-parametric two-way ANOVA approximation)")
# Rank all overcorrection scores
df["oc_rank"] = stats.rankdata(df["overcorrection"])
n_total = len(df)

# SS_total for ranks
grand_rank_mean = df["oc_rank"].mean()
ss_total = ((df["oc_rank"] - grand_rank_mean) ** 2).sum()

# SS for model
model_rank_means = df.groupby("model")["oc_rank"].mean()
model_counts = df.groupby("model")["oc_rank"].count()
ss_model = sum(model_counts[m] * (model_rank_means[m] - grand_rank_mean)**2 for m in models)

# SS for scenario
scen_rank_means = df.groupby("scenario_id")["oc_rank"].mean()
scen_counts = df.groupby("scenario_id")["oc_rank"].count()
ss_scenario = sum(scen_counts[s] * (scen_rank_means[s] - grand_rank_mean)**2 for s in scenarios)

# SS for interaction
cell_means = df.groupby(["model", "scenario_id"])["oc_rank"].mean()
cell_counts = df.groupby(["model", "scenario_id"])["oc_rank"].count()
ss_interaction = 0
for m in models:
    for s in scenarios:
        expected = model_rank_means[m] + scen_rank_means[s] - grand_rank_mean
        n_cell = cell_counts.get((m, s), 0)
        if n_cell > 0:
            ss_interaction += n_cell * (cell_means[(m, s)] - expected)**2

ms_total = ss_total / (n_total - 1)
df_model = len(models) - 1
df_scenario = len(scenarios) - 1
df_interaction = df_model * df_scenario

H_model = ss_model / ms_total
H_scenario = ss_scenario / ms_total
H_interaction = ss_interaction / ms_total

p_model_srh = 1 - stats.chi2.cdf(H_model, df_model)
p_scenario_srh = 1 - stats.chi2.cdf(H_scenario, df_scenario)
p_interaction_srh = 1 - stats.chi2.cdf(H_interaction, df_interaction)

srh_rows = [
    ["Model", f"{df_model}", f"{H_model:.3f}", f"{p_model_srh:.6f}"],
    ["Scenario", f"{df_scenario}", f"{H_scenario:.3f}", f"{p_scenario_srh:.6f}"],
    ["Model x Scenario", f"{df_interaction}", f"{H_interaction:.3f}", f"{p_interaction_srh:.6f}"],
]
table(["Factor", "df", "H", "p-value"], srh_rows)

finding(f"Model x Scenario interaction: H({df_interaction}) = {H_interaction:.3f}, p = {p_interaction_srh:.6f}. "
        f"{'Significant' if p_interaction_srh < 0.05 else 'Non-significant'} interaction — "
        f"{'models differ in how they overcorrect across tasks' if p_interaction_srh < 0.05 else 'models behave similarly across tasks'}.")

detail("Figure suggestion: Grouped bar chart or interaction plot (model x scenario) showing mean overcorrection with 95% CI error bars.")

# Clean up temp column
df.drop(columns=["oc_rank"], inplace=True)

# ══════════════════════════════════════════════════════════════════════════════
# 4. Scenario × Threshold Interaction
# ══════════════════════════════════════════════════════════════════════════════
section("4. Scenario x Threshold Interaction")

thresholds = sorted(df["threshold_level"].unique())

detail("### Mean Overcorrection by Scenario x Threshold Level")
pivot_st = df.pivot_table(values="overcorrection", index="scenario_id", columns="threshold_level", aggfunc="mean")
st_rows = []
for s in scenarios:
    row = [s] + [f"{pivot_st.loc[s, t]:.2f}" for t in thresholds]
    st_rows.append(row)
table(["Scenario"] + [str(t) for t in thresholds], st_rows)

# Spearman correlation of threshold vs overcorrection per scenario
detail("### Threshold Sensitivity: Spearman rho (threshold_level ~ overcorrection) per Scenario")
sens_rows = []
for s in scenarios:
    sub = df[df["scenario_id"] == s]
    rho, p_rho = stats.spearmanr(sub["threshold_level"], sub["overcorrection"])
    sens_rows.append([s, f"rho = {rho:.3f}", f"p = {p_rho:.6f}", "***" if p_rho < 0.001 else "**" if p_rho < 0.01 else "*" if p_rho < 0.05 else "ns"])
    print(f"  {s}: rho = {rho:.3f}, p = {p_rho:.6f}")
table(["Scenario", "Spearman rho", "p-value", "Sig."], sens_rows)

# Scheirer-Ray-Hare for Scenario x Threshold
detail("")
detail("### Scheirer-Ray-Hare: Scenario x Threshold Interaction")
df["oc_rank"] = stats.rankdata(df["overcorrection"])
grand_rank_mean = df["oc_rank"].mean()
ss_total = ((df["oc_rank"] - grand_rank_mean) ** 2).sum()
ms_total = ss_total / (len(df) - 1)

scen_rank_means2 = df.groupby("scenario_id")["oc_rank"].mean()
scen_counts2 = df.groupby("scenario_id")["oc_rank"].count()
thresh_rank_means = df.groupby("threshold_level")["oc_rank"].mean()
thresh_counts = df.groupby("threshold_level")["oc_rank"].count()

ss_thresh = sum(thresh_counts[t] * (thresh_rank_means[t] - grand_rank_mean)**2 for t in thresholds)
ss_scen2 = sum(scen_counts2[s] * (scen_rank_means2[s] - grand_rank_mean)**2 for s in scenarios)

cell_means_st = df.groupby(["scenario_id", "threshold_level"])["oc_rank"].mean()
cell_counts_st = df.groupby(["scenario_id", "threshold_level"])["oc_rank"].count()
ss_st_interaction = 0
for s in scenarios:
    for t in thresholds:
        expected = scen_rank_means2[s] + thresh_rank_means[t] - grand_rank_mean
        key = (s, t)
        if key in cell_counts_st:
            n_cell = cell_counts_st[key]
            ss_st_interaction += n_cell * (cell_means_st[key] - expected)**2

df_thresh = len(thresholds) - 1
df_scen2 = len(scenarios) - 1
df_st_int = df_thresh * df_scen2

H_st = ss_st_interaction / ms_total
p_st = 1 - stats.chi2.cdf(H_st, df_st_int)

finding(f"Scenario x Threshold interaction: H({df_st_int}) = {H_st:.3f}, p = {p_st:.6f}. "
        f"{'Significant' if p_st < 0.05 else 'Non-significant'} — "
        f"{'some scenarios are more threshold-sensitive than others' if p_st < 0.05 else 'threshold sensitivity is similar across scenarios'}.")

# Find most/least threshold-sensitive scenario
rho_vals = {}
for s in scenarios:
    sub = df[df["scenario_id"] == s]
    rho, _ = stats.spearmanr(sub["threshold_level"], sub["overcorrection"])
    rho_vals[s] = rho
most_sens = max(rho_vals, key=lambda k: abs(rho_vals[k]))
least_sens = min(rho_vals, key=lambda k: abs(rho_vals[k]))
detail(f"Most threshold-sensitive scenario: {most_sens} (rho = {rho_vals[most_sens]:.3f})")
detail(f"Least threshold-sensitive scenario: {least_sens} (rho = {rho_vals[least_sens]:.3f})")
detail("Figure suggestion: Line plot of mean overcorrection vs threshold level, one line per scenario, with shaded 95% CI bands.")

df.drop(columns=["oc_rank"], inplace=True)

# ══════════════════════════════════════════════════════════════════════════════
# 5. Formality Analysis
# ══════════════════════════════════════════════════════════════════════════════
section("5. Formality Analysis")

formality_map = {
    "client_sales_email": "formal",
    "linkedin_job_announcement": "formal",
    "brunch_cancellation": "informal",
    "coworker_funny_text": "informal",
    "pto_request": "neutral",
}
df["formality"] = df["scenario_id"].map(formality_map)

formal = df.loc[df["formality"] == "formal", "overcorrection"].values
informal = df.loc[df["formality"] == "informal", "overcorrection"].values
neutral = df.loc[df["formality"] == "neutral", "overcorrection"].values

detail("### Descriptive Statistics by Formality")
form_rows = []
for label, arr in [("formal", formal), ("informal", informal), ("neutral", neutral)]:
    form_rows.append([label, f"{np.mean(arr):.3f}", f"{np.median(arr):.1f}", f"{np.std(arr):.3f}", str(len(arr))])
table(["Formality", "Mean OC", "Median OC", "SD", "N"], form_rows)

# Formal vs Informal
U_fi, p_fi = stats.mannwhitneyu(formal, informal, alternative="two-sided")
r_fi = rank_biserial(U_fi, len(formal), len(informal))
finding(f"Formal vs Informal: U = {U_fi:.0f}, p = {p_fi:.6f}, rank-biserial r = {r_fi:.3f}. "
        f"{'Significant difference' if p_fi < 0.05 else 'No significant difference'}.")

# All three: KW
H_form, p_form = stats.kruskal(formal, informal, neutral)
eta2_form = effect_size_eta_squared_kw(H_form, len(formal)+len(informal)+len(neutral), 3)
detail(f"Three-group Kruskal-Wallis: H(2) = {H_form:.3f}, p = {p_form:.6f}, eta^2 = {eta2_form:.4f}")

# Formal vs Informal per model
detail("")
detail("### Formal vs Informal by Model")
fm_rows = []
for m in models:
    sub = df[df["model"] == m]
    f_vals = sub.loc[sub["formality"] == "formal", "overcorrection"].values
    i_vals = sub.loc[sub["formality"] == "informal", "overcorrection"].values
    U_m, p_m = stats.mannwhitneyu(f_vals, i_vals, alternative="two-sided")
    r_m = rank_biserial(U_m, len(f_vals), len(i_vals))
    fm_rows.append([m, f"{np.mean(f_vals):.3f}", f"{np.mean(i_vals):.3f}",
                    f"U = {U_m:.0f}", f"p = {p_m:.6f}", f"r = {r_m:.3f}",
                    "***" if p_m < 0.001 else "**" if p_m < 0.01 else "*" if p_m < 0.05 else "ns"])
    print(f"  {m}: formal={np.mean(f_vals):.3f}, informal={np.mean(i_vals):.3f}, p={p_m:.6f}")
table(["Model", "Mean Formal", "Mean Informal", "U", "p-value", "r", "Sig."], fm_rows)

detail("Interpretation: Formal scenarios involve professionally-coded texts where LLMs may feel more license to 'improve'; informal scenarios have strong personal voice that models may be more reluctant to alter.")
detail("Figure suggestion: Violin plot of overcorrection by formality level, faceted by model.")

df.drop(columns=["formality"], inplace=True)

# ══════════════════════════════════════════════════════════════════════════════
# 6. Response Length (len_delta) by Scenario
# ══════════════════════════════════════════════════════════════════════════════
section("6. Response Length Change (len_delta) by Scenario")

groups_len = [df_len.loc[df_len["scenario_id"] == s, "len_delta"].dropna().values for s in scenarios]
H_len, p_len = stats.kruskal(*groups_len)
n_len = sum(len(g) for g in groups_len)
eta2_len = effect_size_eta_squared_kw(H_len, n_len, len(scenarios))

finding(f"Kruskal-Wallis on len_delta: H({len(scenarios)-1}) = {H_len:.3f}, p = {p_len:.6f}, eta^2 = {eta2_len:.4f}")

len_rows = []
for s in scenarios:
    vals = df_len.loc[df_len["scenario_id"] == s, "len_delta"].dropna()
    len_rows.append([s, f"{vals.mean():.1f}", f"{vals.median():.1f}", f"{vals.std():.1f}", str(len(vals))])
table(["Scenario", "Mean len_delta", "Median len_delta", "SD", "N"], len_rows)

# Correlation of len_delta with overcorrection per scenario
detail("### Spearman: len_delta ~ overcorrection by Scenario")
corr_rows = []
for s in scenarios:
    sub = df_len[df_len["scenario_id"] == s].dropna(subset=["len_delta", "overcorrection"])
    rho, p_rho = stats.spearmanr(sub["len_delta"], sub["overcorrection"])
    corr_rows.append([s, f"rho = {rho:.3f}", f"p = {p_rho:.6f}",
                      "***" if p_rho < 0.001 else "**" if p_rho < 0.01 else "*" if p_rho < 0.05 else "ns"])
table(["Scenario", "Spearman rho", "p-value", "Sig."], corr_rows)

detail("Interpretation: Large positive len_delta indicates the model substantially expanded the original text during revision. "
       "Scenarios with higher len_delta may reflect the model adding unsolicited content.")
detail("Figure suggestion: Box plot of len_delta by scenario, with individual data points overlaid (jittered strip plot).")

# ══════════════════════════════════════════════════════════════════════════════
# 7. Revision Gate by Scenario (Chi-Squared)
# ══════════════════════════════════════════════════════════════════════════════
section("7. Revision Gate by Scenario (Chi-Squared)")

ct = pd.crosstab(df["scenario_id"], df["revision_gate"])
chi2, p_chi, dof_chi, expected = stats.chi2_contingency(ct)

finding(f"Chi-squared test: chi2({dof_chi}) = {chi2:.3f}, p = {p_chi:.6f}")

detail("### Observed Counts")
gate_types = sorted(df["revision_gate"].unique())
ct_rows = []
for s in scenarios:
    row = [s] + [str(ct.loc[s, g]) if g in ct.columns else "0" for g in gate_types]
    ct_rows.append(row)
table(["Scenario"] + gate_types, ct_rows)

# Proportions
detail("### Proportion of full_revision by Scenario")
if "full_revision" in ct.columns:
    prop_rows = []
    for s in scenarios:
        total = ct.loc[s].sum()
        full_rev = ct.loc[s, "full_revision"] if "full_revision" in ct.columns else 0
        prop = full_rev / total
        prop_rows.append([s, f"{full_rev}/{total}", f"{prop:.3f}"])
    table(["Scenario", "Count", "Proportion"], prop_rows)

# Cramér's V
k = min(ct.shape)
cramers_v = np.sqrt(chi2 / (n_total * (k - 1))) if k > 1 else 0
detail(f"Cramer's V = {cramers_v:.4f} ({'negligible' if cramers_v < 0.1 else 'small' if cramers_v < 0.3 else 'medium' if cramers_v < 0.5 else 'large'} effect)")
detail("Interpretation: Tests whether models are more likely to gate (decline revision) for certain scenario types.")
detail("Figure suggestion: Stacked bar chart of revision_gate proportions by scenario.")

# ══════════════════════════════════════════════════════════════════════════════
# Write markdown report
# ══════════════════════════════════════════════════════════════════════════════
header = """# Deep Scenario Effects Analysis

> Auto-generated statistical report for the LLM overcorrection study.
> 5 scenarios x 3 models x 2 framings x 8 threshold levels = 1,200 trials.

---
"""

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
with open(OUTPUT, "w") as f:
    f.write(header)
    f.write("\n".join(md_lines))
    f.write("\n")

print(f"\n{'='*70}")
print(f"  Report written to: {OUTPUT}")
print(f"{'='*70}")
