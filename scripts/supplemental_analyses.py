"""Supplemental analyses: ICC, probe x threshold interaction, gate distribution, median overcorrection."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import pandas as pd
from scipy import stats as sp_stats
from statsmodels.miscmodels.ordinal_model import OrderedModel


def compute_icc(data, cell_col, value_col):
    """Compute ICC(1,1) for one-way random effects model."""
    groups = data.groupby(cell_col)[value_col].apply(list)
    groups = groups[groups.apply(len) > 1]

    k_vals = groups.apply(len)
    n_groups = len(groups)

    all_vals = np.concatenate(groups.values)
    grand_mean = np.mean(all_vals)

    group_means = groups.apply(np.mean)
    SSB = sum(k * (gm - grand_mean)**2 for k, gm in zip(k_vals, group_means))
    dfB = n_groups - 1

    SSW = sum(sum((x - gm)**2 for x in g) for g, gm in zip(groups, group_means))
    dfW = sum(k - 1 for k in k_vals)

    MSB = SSB / dfB if dfB > 0 else 0
    MSW = SSW / dfW if dfW > 0 else 0

    k0 = np.mean(k_vals)

    icc = (MSB - MSW) / (MSB + (k0 - 1) * MSW) if (MSB + (k0 - 1) * MSW) != 0 else 0

    return icc, MSB, MSW, n_groups, k0


def main():
    df = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "processed" / "scored_trials.csv")
    dims = ["revision_magnitude", "revision_value", "threshold_alignment", "overcorrection"]
    for dim in dims:
        df[dim] = pd.to_numeric(df[dim], errors="coerce")

    if "probe_type" not in df.columns:
        df["probe_type"] = "leading"
    df["probe_type"] = df["probe_type"].fillna("leading")

    df["run"] = df["trial_id"].str.extract(r'__run(\d+)$').astype(int)
    df["cell"] = df["trial_id"].str.replace(r'__run\d+$', '', regex=True)

    print(f"Total trials: {len(df)}")
    print(f"Unique cells: {df['cell'].nunique()}")
    print(f"Probe types: {sorted(df['probe_type'].unique())}")
    print(f"Revision gate values: {sorted(df['revision_gate'].unique())}")
    print()

    # =================================================================
    # 1. ICC (Intra-Class Correlation) across the 5 runs within each cell
    # =================================================================
    print("=" * 70)
    print("1. ICC (Intra-Class Correlation) -- within-cell variance across 5 runs")
    print("=" * 70)

    for dim in ["overcorrection"] + [d for d in dims if d != "overcorrection"]:
        icc, msb, msw, n_cells, k = compute_icc(df, "cell", dim)
        print(f"  {dim}: ICC(1,1) = {icc:.4f}  (MSB={msb:.4f}, MSW={msw:.4f}, cells={n_cells}, k={k:.1f})")

    print()

    # =================================================================
    # 2. Probe x Threshold interaction in ordinal regression (Model A)
    # =================================================================
    print("=" * 70)
    print("2. Probe x Threshold Interaction in Ordinal Regression (Model A)")
    print("=" * 70)

    primary = df[df["probe_type"].isin(["leading", "pilot_c"])].copy()
    primary["is_leading"] = (primary["probe_type"] == "leading").astype(int)
    primary["is_qualitative"] = (primary["framing"] == "qualitative").astype(int)
    primary["threshold_scaled"] = primary["threshold_level"] / 100.0

    model_dummies = pd.get_dummies(primary["model"], prefix="model", drop_first=False)
    if "model_gpt-4o" in model_dummies.columns:
        model_dummies = model_dummies.drop(columns=["model_gpt-4o"])
    primary = pd.concat([primary, model_dummies], axis=1)

    primary["probe_x_threshold"] = primary["is_leading"] * primary["threshold_scaled"]

    exog_cols = ["is_leading", "threshold_scaled", "is_qualitative", "probe_x_threshold"]
    exog_cols += [c for c in model_dummies.columns]

    try:
        exog = primary[exog_cols].astype(float)
        mod = OrderedModel(primary["overcorrection"].astype(float), exog, distr="logit")
        res = mod.fit(method="bfgs", disp=False, maxiter=1000)

        print(f"  Converged: {res.mle_retvals.get('converged', 'unknown')}")
        print(f"  Log-likelihood: {res.llf:.1f}")
        print(f"  AIC: {res.aic:.1f}")
        print()
        print(f"  {'Variable':<25} {'Coef':>10} {'Std Err':>10} {'p-value':>10}")
        print(f"  {'-'*55}")
        for name in exog_cols:
            if name in res.params.index:
                coef = res.params[name]
                se = res.bse[name]
                pval = res.pvalues[name]
                sig = " *" if pval < 0.05 else ""
                print(f"  {name:<25} {coef:>10.4f} {se:>10.4f} {pval:>10.4f}{sig}")

        print()
        print(f"  INTERACTION TERM (probe_x_threshold):")
        name = "probe_x_threshold"
        coef = res.params[name]
        se = res.bse[name]
        pval = res.pvalues[name]
        print(f"    Coefficient: {coef:.4f}")
        print(f"    Std Error:   {se:.4f}")
        print(f"    p-value:     {pval:.6f}")
        print(f"    Significant: {'Yes' if pval < 0.05 else 'No'} (alpha=0.05)")
    except Exception as e:
        print(f"  Model failed: {e}")
        import traceback
        traceback.print_exc()

    print()

    # =================================================================
    # 3. Three-level gate distribution by probe condition
    # =================================================================
    print("=" * 70)
    print("3. Three-Level Gate Distribution by Probe Condition")
    print("=" * 70)

    all_gates = sorted(df["revision_gate"].unique())
    print(f"  Actual gate values in data: {all_gates}")
    print()

    for probe in sorted(df["probe_type"].unique()):
        subset = df[df["probe_type"] == probe]
        n = len(subset)
        print(f"  Probe: {probe} (n={n})")
        gate_counts = subset["revision_gate"].value_counts()
        for g in all_gates:
            count = gate_counts.get(g, 0)
            pct = count / n * 100
            print(f"    {g:<25} {count:>5}  ({pct:>5.1f}%)")
        print()

    print(f"  Overall (n={len(df)})")
    gate_counts = df["revision_gate"].value_counts()
    for g in all_gates:
        count = gate_counts.get(g, 0)
        pct = count / len(df) * 100
        print(f"    {g:<25} {count:>5}  ({pct:>5.1f}%)")

    print()

    # =================================================================
    # 4. Median overcorrection by condition
    # =================================================================
    print("=" * 70)
    print("4. Median Overcorrection by Condition")
    print("=" * 70)

    for probe in sorted(df["probe_type"].unique()):
        subset = df[df["probe_type"] == probe]
        vals = subset["overcorrection"].dropna()
        print(f"  {probe}: median={vals.median():.1f}, mean={vals.mean():.2f}, n={len(vals)}")

    overall = df["overcorrection"].dropna()
    print(f"  Overall: median={overall.median():.1f}, mean={overall.mean():.2f}, n={len(overall)}")

    print()
    print("  By probe x threshold_level:")
    for probe in sorted(df["probe_type"].unique()):
        for level in sorted(df["threshold_level"].unique()):
            subset = df[(df["probe_type"] == probe) & (df["threshold_level"] == level)]
            vals = subset["overcorrection"].dropna()
            if len(vals) > 0:
                print(f"    {probe} | threshold={level}: median={vals.median():.1f}, mean={vals.mean():.2f}, n={len(vals)}")


if __name__ == "__main__":
    main()
