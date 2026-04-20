"""Analyze momentum scored trials: test whether revision history shifts the gate."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import pandas as pd
from scipy import stats as sp_stats

from scripts.config import (
    MOMENTUM_SCORED_PATH,
    MOMENTUM_STATS_DIR,
    SCORED_TRIALS_JSONL,
)
from scripts.utils import load_jsonl

DIMENSIONS = ["revision_magnitude", "revision_value", "threshold_alignment", "overcorrection"]
GATE_CATEGORIES = ["decline", "suggest_minor", "full_revision"]


def load_cold_baseline() -> pd.DataFrame:
    """Load dose=0 data from Study 1 evaluative-probe trials (pilot_c)."""
    scored = load_jsonl(SCORED_TRIALS_JSONL)
    df = pd.DataFrame(scored)
    # Filter to evaluative probe trials only
    cold = df[df["probe_type"] == "pilot_c"].copy()
    cold["dose"] = 0
    return cold


def load_momentum_data() -> pd.DataFrame:
    scored = load_jsonl(MOMENTUM_SCORED_PATH)
    return pd.DataFrame(scored)


def revision_rate(df: pd.DataFrame) -> float:
    """Fraction of trials where the model revised (suggest_minor or full_revision)."""
    if len(df) == 0:
        return np.nan
    return (df["revision_gate"] != "decline").mean()


def full_revision_rate(df: pd.DataFrame) -> float:
    if len(df) == 0:
        return np.nan
    return (df["revision_gate"] == "full_revision").mean()


def rq4_momentum_gate_shift(cold: pd.DataFrame, warm: pd.DataFrame):
    """RQ4: Does revision history increase revision rate vs cold baseline?"""
    print("\n== RQ4: Momentum Gate Shift ==")
    print(f"Cold baseline (dose=0): n={len(cold)}, revision rate={revision_rate(cold):.3f}")

    warm_all = warm.copy()
    print(f"Warm (dose=1,2,3): n={len(warm_all)}, revision rate={revision_rate(warm_all):.3f}")

    # Chi-squared: cold vs warm revision gate distributions
    cold_gates = cold["revision_gate"].value_counts().reindex(GATE_CATEGORIES, fill_value=0)
    warm_gates = warm_all["revision_gate"].value_counts().reindex(GATE_CATEGORIES, fill_value=0)
    contingency = pd.DataFrame({"cold": cold_gates, "warm": warm_gates})
    chi2, p, dof, expected = sp_stats.chi2_contingency(contingency.values.T)
    print(f"Chi-squared (cold vs warm gate): chi2={chi2:.2f}, p={p:.4f}, dof={dof}")

    return {"test": "chi2_cold_vs_warm", "chi2": chi2, "p": p, "dof": dof,
            "cold_revision_rate": revision_rate(cold),
            "warm_revision_rate": revision_rate(warm_all)}


def rq5_dose_response(combined: pd.DataFrame):
    """RQ5: Does revision rate increase with dose?"""
    print("\n== RQ5: Dose-Response ==")

    dose_rates = []
    for dose in sorted(combined["dose"].unique()):
        subset = combined[combined["dose"] == dose]
        rr = revision_rate(subset)
        frr = full_revision_rate(subset)
        print(f"  dose={dose}: n={len(subset)}, revision_rate={rr:.3f}, full_revision_rate={frr:.3f}")
        dose_rates.append({"dose": dose, "revision_rate": rr, "full_revision_rate": frr, "n": len(subset)})

    # Spearman correlation: dose vs revision rate (trial-level binary)
    combined_copy = combined.copy()
    combined_copy["revised"] = (combined_copy["revision_gate"] != "decline").astype(int)
    rho, p = sp_stats.spearmanr(combined_copy["dose"], combined_copy["revised"])
    print(f"Spearman (dose vs revised): rho={rho:.3f}, p={p:.4f}")

    return {"dose_rates": dose_rates, "spearman_rho": rho, "spearman_p": p}


def rq6_threshold_x_momentum(combined: pd.DataFrame):
    """RQ6: Does threshold modulate momentum?"""
    print("\n== RQ6: Threshold x Momentum Interaction ==")

    # Revision rate by dose x threshold
    pivot = combined.groupby(["dose", "threshold_level"]).apply(
        lambda g: pd.Series({
            "revision_rate": revision_rate(g),
            "n": len(g),
        })
    ).reset_index()
    print("\nRevision rate by dose x threshold:")
    print(pivot.pivot(index="dose", columns="threshold_level", values="revision_rate").to_string())

    # Logistic regression: revised ~ dose + threshold + dose:threshold
    try:
        import statsmodels.api as sm
        combined_copy = combined.copy()
        combined_copy["revised"] = (combined_copy["revision_gate"] != "decline").astype(int)
        combined_copy["dose_x_threshold"] = combined_copy["dose"] * combined_copy["threshold_level"]
        X = combined_copy[["dose", "threshold_level", "dose_x_threshold"]]
        X = sm.add_constant(X)
        y = combined_copy["revised"]
        model = sm.Logit(y, X).fit(disp=0)
        print("\nLogistic regression: revised ~ dose + threshold + dose:threshold")
        print(model.summary2().tables[1].to_string())
        return {"logit_params": model.params.to_dict(), "logit_pvalues": model.pvalues.to_dict()}
    except Exception as e:
        print(f"Logistic regression failed: {e}")
        return {}


def overcorrection_by_dose(combined: pd.DataFrame):
    """Does momentum increase overcorrection?"""
    print("\n== Overcorrection by Dose ==")

    groups = []
    for dose in sorted(combined["dose"].unique()):
        subset = combined[combined["dose"] == dose]
        vals = subset["overcorrection"].dropna()
        print(f"  dose={dose}: mean={vals.mean():.2f}, median={vals.median():.1f}, n={len(vals)}")
        groups.append(vals.values)

    if len(groups) >= 2:
        h, p = sp_stats.kruskal(*groups)
        print(f"Kruskal-Wallis (overcorrection across doses): H={h:.2f}, p={p:.4f}")
        return {"kruskal_H": h, "kruskal_p": p}
    return {}


def model_interaction(combined: pd.DataFrame):
    """Revision rate by dose x model."""
    print("\n== Dose x Model Interaction ==")

    pivot = combined.groupby(["dose", "model"]).apply(
        lambda g: pd.Series({
            "revision_rate": revision_rate(g),
            "overcorrection_mean": g["overcorrection"].mean(),
            "n": len(g),
        })
    ).reset_index()
    print(pivot.pivot(index="dose", columns="model", values="revision_rate").to_string())
    return pivot


def main():
    MOMENTUM_STATS_DIR.mkdir(parents=True, exist_ok=True)

    cold = load_cold_baseline()
    warm = load_momentum_data()

    if warm.empty:
        print("No momentum data found. Run the experiment first.")
        return

    # Combine cold + warm for dose-response analyses
    cold_subset = cold[["trial_id", "model", "scenario_id", "framing", "threshold_level",
                         "revision_gate", "revision_magnitude", "revision_value",
                         "threshold_alignment", "overcorrection", "dose"]].copy()
    warm_subset = warm[["trial_id", "model", "scenario_id", "framing", "threshold_level",
                         "revision_gate", "revision_magnitude", "revision_value",
                         "threshold_alignment", "overcorrection", "dose"]].copy()
    combined = pd.concat([cold_subset, warm_subset], ignore_index=True)
    print(f"Combined dataset: {len(combined)} trials ({len(cold_subset)} cold + {len(warm_subset)} warm)")

    results = {}
    results["rq4"] = rq4_momentum_gate_shift(cold_subset, warm_subset)
    results["rq5"] = rq5_dose_response(combined)
    results["rq6"] = rq6_threshold_x_momentum(combined)
    results["overcorrection"] = overcorrection_by_dose(combined)
    model_pivot = model_interaction(combined)

    # Save results
    import json
    results_path = MOMENTUM_STATS_DIR / "momentum_results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved results to {results_path}")

    model_pivot.to_csv(MOMENTUM_STATS_DIR / "dose_x_model.csv", index=False)
    print("Done.")


if __name__ == "__main__":
    main()
