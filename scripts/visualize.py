"""Generate publication-ready figures from scored trials."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats as sp_stats

from scripts.config import FIGURES_DIR, SCORED_TRIALS_JSONL, STATS_DIR, TRIALS_PATH
from scripts.utils import load_jsonl

DIMENSIONS = ["revision_magnitude", "revision_value", "threshold_alignment", "overcorrection"]
GATE_CATEGORIES = ["decline", "suggest_minor", "full_revision"]


def save_fig(fig, name):
    """Save figure as both PNG (300dpi) and PDF."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES_DIR / f"{name}.png", dpi=300, bbox_inches="tight")
    fig.savefig(FIGURES_DIR / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {name}.png + .pdf")


def fig1_overcorrection_heatmap(df):
    """Overcorrection heatmap: model x threshold, side-by-side panels for numeric/qualitative."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

    for ax, framing in zip(axes, ["numeric", "qualitative"]):
        subset = df[df["framing"] == framing]
        pivot = subset.pivot_table(
            values="overcorrection", index="model", columns="threshold_level", aggfunc="mean"
        )
        pivot = pivot.reindex(columns=sorted(pivot.columns))
        sns.heatmap(pivot, annot=True, fmt=".2f", cmap="YlOrRd", vmin=1, vmax=5,
                    ax=ax, cbar_kws={"label": "Mean Overcorrection"})
        ax.set_title(f"{framing.capitalize()} Framing")
        ax.set_xlabel("Threshold Level")
        ax.set_ylabel("Model" if framing == "numeric" else "")

    fig.suptitle("Overcorrection by Model and Threshold Level", fontsize=14, y=1.02)
    fig.tight_layout()
    save_fig(fig, "01_overcorrection_heatmap")


def fig2_threshold_ladder(df):
    """Line plot: overcorrection across threshold levels, one line per model, panels per framing."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

    for ax, framing in zip(axes, ["numeric", "qualitative"]):
        subset = df[df["framing"] == framing]
        for model in sorted(subset["model"].unique()):
            mdata = subset[subset["model"] == model]
            means = mdata.groupby("threshold_level")["overcorrection"].mean()
            sems = mdata.groupby("threshold_level")["overcorrection"].sem()
            levels = sorted(means.index)
            ax.errorbar(levels, [means[l] for l in levels], yerr=[sems[l] for l in levels],
                        marker="o", label=model, capsize=3)

        ax.set_title(f"{framing.capitalize()} Framing")
        ax.set_xlabel("Threshold Level")
        ax.set_ylabel("Mean Overcorrection" if framing == "numeric" else "")
        ax.set_xticks(sorted(subset["threshold_level"].unique()))
        ax.legend()
        ax.set_ylim(0.5, 5.5)

    fig.suptitle("Overcorrection Across Threshold Levels", fontsize=14, y=1.02)
    fig.tight_layout()
    save_fig(fig, "02_threshold_ladder")


def fig3_framing_comparison(df):
    """Bar chart: per model, numeric vs qualitative mean overcorrection with error bars."""
    models = sorted(df["model"].unique())
    x = np.arange(len(models))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))

    for i, framing in enumerate(["numeric", "qualitative"]):
        means = []
        sems = []
        for model in models:
            vals = df[(df["model"] == model) & (df["framing"] == framing)]["overcorrection"].dropna()
            means.append(vals.mean())
            sems.append(vals.sem())
        offset = (i - 0.5) * width
        bars = ax.bar(x + offset, means, width, yerr=sems, label=framing.capitalize(),
                      capsize=3, alpha=0.85)

    # Significance stars
    for j, model in enumerate(models):
        vals_n = df[(df["model"] == model) & (df["framing"] == "numeric")]["overcorrection"].dropna()
        vals_q = df[(df["model"] == model) & (df["framing"] == "qualitative")]["overcorrection"].dropna()
        if len(vals_n) >= 2 and len(vals_q) >= 2:
            _, p = sp_stats.mannwhitneyu(vals_n, vals_q, alternative="two-sided")
            if p < 0.001:
                star = "***"
            elif p < 0.01:
                star = "**"
            elif p < 0.05:
                star = "*"
            else:
                star = ""
            if star:
                y_max = max(vals_n.mean() + vals_n.sem(), vals_q.mean() + vals_q.sem())
                ax.text(j, y_max + 0.15, star, ha="center", fontsize=14)

    ax.set_xlabel("Model")
    ax.set_ylabel("Mean Overcorrection")
    ax.set_title("Framing Effect on Overcorrection")
    ax.set_xticks(x)
    ax.set_xticklabels(models)
    ax.legend()
    ax.set_ylim(0, 5.5)
    fig.tight_layout()
    save_fig(fig, "03_framing_comparison")


def fig4_revision_gate_stacked(df):
    """Stacked bar: proportion of decline/suggest/full per model x framing."""
    groups = df.groupby(["model", "framing"])["revision_gate"].value_counts(normalize=True).unstack(fill_value=0)
    # Reorder columns
    for g in GATE_CATEGORIES:
        if g not in groups.columns:
            groups[g] = 0.0
    groups = groups[GATE_CATEGORIES]

    fig, ax = plt.subplots(figsize=(10, 5))
    groups.plot(kind="bar", stacked=True, ax=ax, colormap="Set2", edgecolor="white")
    ax.set_ylabel("Proportion")
    ax.set_title("Revision Gate Distribution by Model and Framing")
    ax.set_xlabel("")
    ax.legend(title="Gate", bbox_to_anchor=(1.02, 1), loc="upper left")
    ax.set_ylim(0, 1)
    plt.xticks(rotation=45, ha="right")
    fig.tight_layout()
    save_fig(fig, "04_revision_gate_stacked")


def fig5_dimension_correlation(df):
    """Spearman correlation heatmap of the 4 scoring dimensions."""
    dim_df = df[DIMENSIONS].dropna()
    if len(dim_df) < 3:
        print("  Skipping correlation matrix (insufficient data)")
        return

    corr = dim_df.corr(method="spearman")

    fig, ax = plt.subplots(figsize=(7, 6))
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r", vmin=-1, vmax=1,
                mask=mask, ax=ax, square=True)
    ax.set_title("Spearman Correlation Between Scoring Dimensions")
    fig.tight_layout()
    save_fig(fig, "05_dimension_correlation")


def fig6_scenario_boxplots(df):
    """Boxplots of overcorrection by scenario, faceted by model."""
    models = sorted(df["model"].unique())
    n_models = len(models)
    fig, axes = plt.subplots(1, n_models, figsize=(6 * n_models, 6), sharey=True)
    if n_models == 1:
        axes = [axes]

    for ax, model in zip(axes, models):
        mdata = df[df["model"] == model]
        scenarios = sorted(mdata["scenario_id"].unique())
        sns.boxplot(data=mdata, x="scenario_id", y="overcorrection", ax=ax,
                    order=scenarios, palette="muted")
        ax.set_title(model)
        ax.set_xlabel("Scenario")
        ax.set_ylabel("Overcorrection" if model == models[0] else "")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

    fig.suptitle("Overcorrection by Scenario and Model", fontsize=14, y=1.02)
    fig.tight_layout()
    save_fig(fig, "06_scenario_boxplots")


def fig7_judge_bias_check(df):
    """Violin plots comparing judge scores across models, highlighting potential self-preferencing."""
    judge_model = "gpt-4o"
    fig, axes = plt.subplots(1, len(DIMENSIONS), figsize=(5 * len(DIMENSIONS), 5), sharey=True)

    for ax, dim in zip(axes, DIMENSIONS):
        models = sorted(df["model"].unique())
        data = [df[df["model"] == m][dim].dropna().values for m in models]
        parts = ax.violinplot(data, positions=range(len(models)), showmeans=True, showmedians=True)

        # Color the judge model's violin differently
        for i, (body, model) in enumerate(zip(parts["bodies"], models)):
            if model == judge_model:
                body.set_facecolor("#ff6b6b")
                body.set_alpha(0.7)
            else:
                body.set_facecolor("#4ecdc4")
                body.set_alpha(0.7)

        ax.set_xticks(range(len(models)))
        ax.set_xticklabels(models, rotation=30, ha="right")
        ax.set_title(dim.replace("_", " ").title())
        ax.set_ylabel("Score" if dim == DIMENSIONS[0] else "")

    # Custom legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#ff6b6b", alpha=0.7, label=f"Judge model ({judge_model})"),
        Patch(facecolor="#4ecdc4", alpha=0.7, label="Other models"),
    ]
    fig.legend(handles=legend_elements, loc="upper right", fontsize=10)
    fig.suptitle("Judge Score Distribution by Model (Self-Preferencing Check)", fontsize=14, y=1.02)
    fig.tight_layout()
    save_fig(fig, "07_judge_bias_check")


def fig8_response_length(df):
    """Response length analysis: length delta by model and threshold level."""
    raw_trials = load_jsonl(TRIALS_PATH)
    raw_success = [t for t in raw_trials if t.get("status") == "success"]
    if not raw_success:
        print("  Skipping response length figure (no raw trial data)")
        return

    len_df = pd.DataFrame(raw_success)
    len_df["turn1_len"] = len_df["turn1_response"].str.len()
    len_df["turn2_len"] = len_df["turn2_response"].str.len()
    len_df["len_delta"] = len_df["turn2_len"] - len_df["turn1_len"]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

    for ax, framing in zip(axes, ["numeric", "qualitative"]):
        subset = len_df[len_df["framing"] == framing]
        for model in sorted(subset["model"].unique()):
            mdata = subset[subset["model"] == model]
            means = mdata.groupby("threshold_level")["len_delta"].mean()
            sems = mdata.groupby("threshold_level")["len_delta"].sem()
            levels = sorted(means.index)
            ax.errorbar(levels, [means[l] for l in levels], yerr=[sems[l] for l in levels],
                        marker="o", label=model, capsize=3)

        ax.set_title(f"{framing.capitalize()} Framing")
        ax.set_xlabel("Threshold Level")
        ax.set_ylabel("Response Length Delta (chars)" if framing == "numeric" else "")
        ax.set_xticks(sorted(subset["threshold_level"].unique()))
        ax.legend()
        ax.axhline(y=0, color="gray", linestyle="--", alpha=0.5)

    fig.suptitle("Response Length Change (Turn 2 - Turn 1) Across Thresholds", fontsize=14, y=1.02)
    fig.tight_layout()
    save_fig(fig, "08_response_length_delta")


def fig9_length_vs_overcorrection(df):
    """Scatter: response length delta vs judge overcorrection score, colored by model."""
    raw_trials = load_jsonl(TRIALS_PATH)
    raw_success = [t for t in raw_trials if t.get("status") == "success"]
    if not raw_success:
        return

    len_df = pd.DataFrame(raw_success)
    len_df["len_delta"] = len_df["turn2_response"].str.len() - len_df["turn1_response"].str.len()

    merged = df.merge(len_df[["trial_id", "len_delta"]], on="trial_id", how="inner")
    if len(merged) < 3:
        return

    fig, ax = plt.subplots(figsize=(8, 6))
    models = sorted(merged["model"].unique())
    colors = {"gpt-4o": "#ff6b6b", "claude-sonnet": "#4ecdc4", "gemini-flash": "#ffe66d"}

    for model in models:
        mdata = merged[merged["model"] == model]
        ax.scatter(mdata["len_delta"], mdata["overcorrection"],
                   alpha=0.3, s=20, label=model, color=colors.get(model, "gray"))

    ax.set_xlabel("Response Length Delta (Turn 2 - Turn 1, chars)")
    ax.set_ylabel("Judge Overcorrection Score")
    ax.set_title("Response Length Change vs Judge Overcorrection Score")
    ax.legend()
    fig.tight_layout()
    save_fig(fig, "09_length_vs_overcorrection")


def main():
    scored = load_jsonl(SCORED_TRIALS_JSONL)
    if not scored:
        print("No scored data to visualize.")
        return

    df = pd.DataFrame(scored)
    for dim in DIMENSIONS:
        df[dim] = pd.to_numeric(df[dim], errors="coerce")
    print(f"Loaded {len(df)} scored trials")

    print("Generating figures...")
    fig1_overcorrection_heatmap(df)
    fig2_threshold_ladder(df)
    fig3_framing_comparison(df)
    fig4_revision_gate_stacked(df)
    fig5_dimension_correlation(df)
    fig6_scenario_boxplots(df)
    fig7_judge_bias_check(df)
    fig8_response_length(df)
    fig9_length_vs_overcorrection(df)
    print("Done.")


if __name__ == "__main__":
    main()
