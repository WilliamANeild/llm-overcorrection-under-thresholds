"""Visualize momentum experiment results."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from scripts.config import (
    MOMENTUM_FIGURES_DIR,
    MOMENTUM_SCORED_PATH,
    SCORED_TRIALS_JSONL,
)
from scripts.utils import load_jsonl

GATE_CATEGORIES = ["decline", "suggest_minor", "full_revision"]


def load_combined() -> pd.DataFrame:
    """Load cold baseline + momentum data."""
    # Cold baseline from Study 1 evaluative probe
    cold_scored = load_jsonl(SCORED_TRIALS_JSONL)
    cold_df = pd.DataFrame(cold_scored)
    cold_df = cold_df[cold_df["probe_type"] == "pilot_c"].copy()
    cold_df["dose"] = 0

    # Warm momentum data
    warm_scored = load_jsonl(MOMENTUM_SCORED_PATH)
    warm_df = pd.DataFrame(warm_scored)

    cols = ["trial_id", "model", "scenario_id", "framing", "threshold_level",
            "revision_gate", "revision_magnitude", "revision_value",
            "threshold_alignment", "overcorrection", "dose"]
    cold_cols = [c for c in cols if c in cold_df.columns]
    warm_cols = [c for c in cols if c in warm_df.columns]

    combined = pd.concat([cold_df[cold_cols], warm_df[warm_cols]], ignore_index=True)
    combined["revised"] = (combined["revision_gate"] != "decline").astype(int)
    return combined


def fig_revision_rate_by_dose(df: pd.DataFrame):
    """Bar chart: revision rate at evaluative probe by dose, faceted by model."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 5), sharey=True)
    models = sorted(df["model"].unique())

    for ax, model in zip(axes, models):
        subset = df[df["model"] == model]
        rates = subset.groupby("dose")["revised"].mean()
        counts = subset.groupby("dose")["revised"].count()
        doses = sorted(subset["dose"].unique())

        bars = ax.bar(doses, [rates.get(d, 0) for d in doses],
                      color=sns.color_palette("Blues_d", len(doses)),
                      edgecolor="black", linewidth=0.5)
        ax.set_title(model, fontsize=12, fontweight="bold")
        ax.set_xlabel("Momentum Dose")
        ax.set_xticks(doses)
        ax.set_ylim(0, 1.05)

        for bar, d in zip(bars, doses):
            n = counts.get(d, 0)
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                    f"n={n}", ha="center", va="bottom", fontsize=8)

    axes[0].set_ylabel("Revision Rate")
    fig.suptitle("Revision Rate at Evaluative Probe by Momentum Dose", fontsize=14, fontweight="bold")
    plt.tight_layout()
    path = MOMENTUM_FIGURES_DIR / "revision_rate_by_dose.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig_dose_response_curve(df: pd.DataFrame):
    """Line plot: dose on x-axis, revision rate on y-axis, one line per model."""
    fig, ax = plt.subplots(figsize=(8, 5))
    models = sorted(df["model"].unique())
    palette = sns.color_palette("Set2", len(models))

    for model, color in zip(models, palette):
        subset = df[df["model"] == model]
        rates = subset.groupby("dose")["revised"].mean()
        doses = sorted(rates.index)
        ax.plot(doses, [rates[d] for d in doses], marker="o", label=model,
                color=color, linewidth=2, markersize=8)

    ax.set_xlabel("Momentum Dose (# prior leading probes)", fontsize=11)
    ax.set_ylabel("Revision Rate at Evaluative Probe", fontsize=11)
    ax.set_title("Momentum Dose-Response Curve", fontsize=13, fontweight="bold")
    ax.set_xticks(sorted(df["dose"].unique()))
    ax.set_ylim(0, 1.05)
    ax.legend(title="Model")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    path = MOMENTUM_FIGURES_DIR / "dose_response_curve.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig_dose_threshold_heatmap(df: pd.DataFrame):
    """Heatmap: dose x threshold, cell = revision rate."""
    pivot = df.groupby(["dose", "threshold_level"])["revised"].mean().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(pivot, annot=True, fmt=".2f", cmap="YlOrRd", vmin=0, vmax=1,
                ax=ax, linewidths=0.5, cbar_kws={"label": "Revision Rate"})
    ax.set_xlabel("Threshold Level")
    ax.set_ylabel("Momentum Dose")
    ax.set_title("Revision Rate: Dose x Threshold", fontsize=13, fontweight="bold")
    plt.tight_layout()
    path = MOMENTUM_FIGURES_DIR / "dose_threshold_heatmap.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig_overcorrection_by_dose(df: pd.DataFrame):
    """Box plot: overcorrection scores across doses."""
    fig, ax = plt.subplots(figsize=(8, 5))
    doses = sorted(df["dose"].unique())
    data = [df[df["dose"] == d]["overcorrection"].dropna().values for d in doses]

    bp = ax.boxplot(data, labels=[str(d) for d in doses], patch_artist=True)
    colors = sns.color_palette("Oranges", len(doses))
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)

    ax.set_xlabel("Momentum Dose")
    ax.set_ylabel("Overcorrection Score (1-5)")
    ax.set_title("Overcorrection by Momentum Dose", fontsize=13, fontweight="bold")
    ax.set_ylim(0.5, 5.5)
    ax.grid(True, alpha=0.3, axis="y")
    plt.tight_layout()
    path = MOMENTUM_FIGURES_DIR / "overcorrection_by_dose.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def main():
    MOMENTUM_FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    df = load_combined()
    if df.empty:
        print("No data to visualize.")
        return

    print(f"Loaded {len(df)} total trials (doses: {sorted(df['dose'].unique())})")

    fig_revision_rate_by_dose(df)
    fig_dose_response_curve(df)
    fig_dose_threshold_heatmap(df)
    fig_overcorrection_by_dose(df)

    print("Done.")


if __name__ == "__main__":
    main()
