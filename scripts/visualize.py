"""Generate publication-ready figures from scored trials."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats as sp_stats

from scripts.config import FIGURES_DIR, SCORED_TRIALS_JSONL, STATS_DIR, TRIALS_PATH
from scripts.utils import load_jsonl

DIMENSIONS = ["revision_magnitude", "revision_value", "threshold_alignment", "overcorrection"]
GATE_CATEGORIES = ["decline", "suggest_minor", "full_revision"]

# ── Brand Colors ──
MODEL_COLORS = {
    "claude-sonnet": "#D97757",   # Anthropic orange/terracotta
    "gemini-flash":  "#4285F4",   # Google blue
    "gpt-4o":        "#1A1A2E",   # ChatGPT dark
}
MODEL_LABELS = {
    "claude-sonnet": "Claude Sonnet 4",
    "gemini-flash":  "Gemini 2.5 Flash",
    "gpt-4o":        "GPT-4o",
}
MODEL_ORDER = ["claude-sonnet", "gemini-flash", "gpt-4o"]

# Gate colors
GATE_COLORS = {
    "decline":       "#2ECC71",   # green
    "suggest_minor": "#F39C12",   # amber
    "full_revision": "#E74C3C",   # red
}
GATE_LABELS = {
    "decline": "Decline",
    "suggest_minor": "Suggest Minor",
    "full_revision": "Full Revision",
}

# Framing colors
FRAMING_COLORS = {
    "numeric":     "#5B6ABF",
    "qualitative": "#2ECC71",
}

# Probe colors
PROBE_COLORS = {
    "leading": "#E74C3C",
    "neutral": "#3498DB",
}

# ── Global Style ──
def setup_style():
    """Set up publication-quality matplotlib defaults."""
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.titleweight": "600",
        "axes.labelsize": 11,
        "axes.labelweight": "500",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.8,
        "axes.grid": False,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
        "legend.fontsize": 9.5,
        "legend.frameon": True,
        "legend.framealpha": 0.9,
        "legend.edgecolor": "#CCCCCC",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "savefig.dpi": 300,
        "figure.dpi": 150,
    })

setup_style()


def get_color(model):
    return MODEL_COLORS.get(model, "#888888")

def get_label(model):
    return MODEL_LABELS.get(model, model)

def ordered_models(df):
    """Return models in canonical order, filtered to those present."""
    return [m for m in MODEL_ORDER if m in df["model"].unique()]


def save_fig(fig, name):
    """Save figure as both PNG (300dpi) and PDF."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES_DIR / f"{name}.png", dpi=300, bbox_inches="tight")
    fig.savefig(FIGURES_DIR / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {name}.png + .pdf")


def fig1_overcorrection_heatmap(df):
    """Overcorrection heatmap: model x threshold, side-by-side panels for numeric/qualitative."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 4.5), sharey=True)

    for ax, framing in zip(axes, ["numeric", "qualitative"]):
        subset = df[df["framing"] == framing]
        pivot = subset.pivot_table(
            values="overcorrection", index="model", columns="threshold_level", aggfunc="mean"
        )
        pivot = pivot.reindex(index=MODEL_ORDER)
        pivot = pivot.reindex(columns=sorted(pivot.columns))
        pivot.index = [MODEL_LABELS.get(m, m) for m in pivot.index]

        sns.heatmap(pivot, annot=True, fmt=".2f", cmap="YlOrRd", vmin=1, vmax=5,
                    ax=ax, cbar_kws={"label": "Mean Overcorrection"},
                    linewidths=0.5, linecolor="white")
        ax.set_title(f"{framing.capitalize()} Framing", fontsize=12, fontweight="600")
        ax.set_xlabel("Threshold Level")
        ax.set_ylabel("" if framing == "qualitative" else "")
        ax.tick_params(axis="y", rotation=0)

    fig.suptitle("Overcorrection by Model and Threshold Level", fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "01_overcorrection_heatmap")


def fig2_threshold_ladder(df):
    """Line plot: overcorrection across threshold levels, one panel per model, both framings."""
    models = ordered_models(df)
    n_models = len(models)
    fig, axes = plt.subplots(1, n_models, figsize=(5.5 * n_models, 5.5), sharey=True)
    if n_models == 1:
        axes = [axes]

    for ax, model in zip(axes, models):
        mdata = df[df["model"] == model]

        for framing in ["numeric", "qualitative"]:
            subset = mdata[mdata["framing"] == framing]
            levels = sorted(subset["threshold_level"].unique())
            x_pos = np.arange(len(levels))
            means = subset.groupby("threshold_level")["overcorrection"].mean()
            sems = subset.groupby("threshold_level")["overcorrection"].sem()
            y_vals = [means.get(l, np.nan) for l in levels]
            y_errs = [sems.get(l, 0) for l in levels]
            ax.errorbar(x_pos, y_vals, yerr=y_errs,
                        marker="o", label=framing.capitalize(), capsize=4, linewidth=2,
                        markersize=8, color=FRAMING_COLORS[framing])

        # Reference line at overcorrection = 1.0 (proportionate)
        ax.axhline(y=1.0, color="#CCCCCC", linestyle="--", linewidth=0.8, zorder=0)

        ax.set_title(get_label(model), fontsize=12, fontweight="600", color=get_color(model))
        ax.set_xlabel("Threshold Level")
        ax.set_ylabel("Mean Overcorrection" if model == models[0] else "")
        levels = sorted(mdata["threshold_level"].unique())
        ax.set_xticks(np.arange(len(levels)))
        ax.set_xticklabels([str(int(l)) for l in levels])
        ax.legend(frameon=True)
        ax.set_ylim(0.5, 5.5)

        # Annotate GPT-4o with flat-line note
        if model == "gpt-4o":
            ax.text(0.5, 0.95, r"n.s. ($\rho = -0.14$)", transform=ax.transAxes,
                    ha="center", va="top", fontsize=9, color="#999999", fontstyle="italic")

    fig.suptitle("Overcorrection Across Threshold Levels", fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "02_threshold_ladder")


def fig3_framing_comparison(df):
    """Bar chart: per model, numeric vs qualitative mean overcorrection with error bars."""
    models = ordered_models(df)
    x = np.arange(len(models))
    width = 0.32

    fig, ax = plt.subplots(figsize=(8, 5))

    for i, framing in enumerate(["numeric", "qualitative"]):
        means, sems = [], []
        for model in models:
            vals = df[(df["model"] == model) & (df["framing"] == framing)]["overcorrection"].dropna()
            means.append(vals.mean())
            sems.append(vals.sem())
        offset = (i - 0.5) * width
        ax.bar(x + offset, means, width, yerr=sems, label=framing.capitalize(),
               capsize=4, color=FRAMING_COLORS[framing], edgecolor="white", linewidth=0.5)

    # Significance stars
    for j, model in enumerate(models):
        vals_n = df[(df["model"] == model) & (df["framing"] == "numeric")]["overcorrection"].dropna()
        vals_q = df[(df["model"] == model) & (df["framing"] == "qualitative")]["overcorrection"].dropna()
        if len(vals_n) >= 2 and len(vals_q) >= 2:
            _, p = sp_stats.mannwhitneyu(vals_n, vals_q, alternative="two-sided")
            star = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
            if star:
                y_max = max(vals_n.mean() + vals_n.sem(), vals_q.mean() + vals_q.sem())
                ax.text(j, y_max + 0.15, star, ha="center", fontsize=14, fontweight="bold")

    ax.set_ylabel("Mean Overcorrection")
    ax.set_title("Framing Effect on Overcorrection", fontsize=13, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([get_label(m) for m in models])
    ax.legend(frameon=True)
    ax.set_ylim(0, 5.5)
    fig.tight_layout()
    save_fig(fig, "03_framing_comparison")


def fig4_revision_gate_stacked(df):
    """Stacked bar: proportion of decline/suggest/full per model x framing."""
    combos = []
    for model in ordered_models(df):
        for framing in ["numeric", "qualitative"]:
            combos.append((model, framing))

    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(combos))
    bottom = np.zeros(len(combos))

    for gate in GATE_CATEGORIES:
        heights = []
        for model, framing in combos:
            sub = df[(df["model"] == model) & (df["framing"] == framing)]
            if len(sub) > 0:
                heights.append((sub["revision_gate"] == gate).mean())
            else:
                heights.append(0)
        ax.bar(x, heights, bottom=bottom, label=GATE_LABELS[gate],
               color=GATE_COLORS[gate], edgecolor="white", linewidth=0.5, width=0.7)
        bottom += np.array(heights)

    labels = [f"{get_label(m)}\n({f[:3].title()}.)" for m, f in combos]
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel("Proportion")
    ax.set_title("Revision Gate Distribution by Model and Framing", fontsize=13, fontweight="bold")
    ax.legend(frameon=True, loc="upper right")
    ax.set_ylim(0, 1.05)
    fig.tight_layout()
    save_fig(fig, "04_revision_gate_stacked")


def fig5_dimension_correlation(df):
    """Spearman correlation heatmap of the 4 scoring dimensions."""
    dim_df = df[DIMENSIONS].dropna()
    if len(dim_df) < 3:
        print("  Skipping correlation matrix (insufficient data)")
        return

    corr = dim_df.corr(method="spearman")
    dim_labels = [d.replace("_", " ").title() for d in DIMENSIONS]
    corr.index = dim_labels
    corr.columns = dim_labels

    fig, ax = plt.subplots(figsize=(7, 6))
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r", vmin=-1, vmax=1,
                mask=mask, ax=ax, square=True, linewidths=0.5, linecolor="white")
    ax.set_title("Spearman Correlation Between Scoring Dimensions", fontsize=13, fontweight="bold")
    fig.tight_layout()
    save_fig(fig, "05_dimension_correlation")


def fig6_scenario_boxplots(df):
    """Boxplots of overcorrection by scenario, faceted by model."""
    models = ordered_models(df)
    n_models = len(models)
    fig, axes = plt.subplots(1, n_models, figsize=(5 * n_models, 5.5), sharey=True)
    if n_models == 1:
        axes = [axes]

    scenario_labels = {
        "brunch_cancellation": "Brunch",
        "client_sales_email": "Sales\nEmail",
        "coworker_funny_text": "Coworker\nText",
        "headphones_review": "Review",
        "linkedin_job_announcement": "LinkedIn",
        "pto_request": "PTO\nRequest",
        "setup_instructions": "Setup",
        "slack_project_update": "Slack\nUpdate",
    }

    # Use a lighter shade for GPT-4o so boxes are visible
    box_colors = {
        "claude-sonnet": "#D97757",
        "gemini-flash":  "#4285F4",
        "gpt-4o":        "#6C6C8A",   # lighter version of dark for visibility
    }

    for ax, model in zip(axes, models):
        mdata = df[df["model"] == model]
        scenarios = sorted(mdata["scenario_id"].unique())
        bp = sns.boxplot(data=mdata, x="scenario_id", y="overcorrection", ax=ax,
                    order=scenarios, color=box_colors.get(model, get_color(model)),
                    width=0.6,
                    flierprops=dict(marker="o", markersize=3, alpha=0.4),
                    medianprops=dict(color="white", linewidth=2))
        ax.set_title(get_label(model), fontsize=12, fontweight="600", color=get_color(model))
        ax.set_xlabel("")
        ax.set_ylabel("Overcorrection" if model == models[0] else "")
        short_labels = [scenario_labels.get(s, s[:8]) for s in scenarios]
        ax.set_xticks(range(len(scenarios)))
        ax.set_xticklabels(short_labels, rotation=0, ha="center", fontsize=8)

    fig.suptitle("Overcorrection by Scenario and Model", fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "06_scenario_boxplots")


def fig7_judge_bias_check(df):
    """Violin plots comparing judge scores across models, highlighting potential self-preferencing."""
    judge_model = "gpt-4o"
    fig, axes = plt.subplots(1, len(DIMENSIONS), figsize=(5 * len(DIMENSIONS), 5), sharey=True)

    dim_labels = {
        "revision_magnitude": "Revision Magnitude",
        "revision_value": "Revision Value",
        "threshold_alignment": "Threshold Alignment",
        "overcorrection": "Overcorrection",
    }

    for ax, dim in zip(axes, DIMENSIONS):
        models = ordered_models(df)
        data = [df[df["model"] == m][dim].dropna().values for m in models]
        parts = ax.violinplot(data, positions=range(len(models)), showmeans=True, showmedians=True)

        for i, (body, model) in enumerate(zip(parts["bodies"], models)):
            if model == judge_model:
                body.set_facecolor("#E74C3C")
                body.set_alpha(0.6)
            else:
                body.set_facecolor(get_color(model))
                body.set_alpha(0.6)

        # Style the lines
        for partname in ["cmeans", "cmedians", "cbars", "cmins", "cmaxes"]:
            if partname in parts:
                parts[partname].set_edgecolor("#333333")
                parts[partname].set_linewidth(0.8)

        ax.set_xticks(range(len(models)))
        ax.set_xticklabels([get_label(m) for m in models], rotation=25, ha="right", fontsize=9)
        ax.set_title(dim_labels.get(dim, dim), fontsize=11, fontweight="600")
        ax.set_ylabel("Score" if dim == DIMENSIONS[0] else "")

    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#E74C3C", alpha=0.6, label=f"Judge model ({get_label(judge_model)})"),
        Patch(facecolor=get_color("claude-sonnet"), alpha=0.6, label="Other models"),
    ]
    fig.legend(handles=legend_elements, loc="upper right", fontsize=10, frameon=True)
    fig.suptitle("Judge Score Distribution by Model (Self-Preferencing Check)",
                 fontsize=14, fontweight="bold", y=1.03)
    fig.tight_layout()
    save_fig(fig, "07_judge_bias_check")


def fig8_response_length(df):
    """Response length analysis: median length delta by model and threshold level."""
    raw_trials = load_jsonl(TRIALS_PATH)
    raw_success = [t for t in raw_trials if t.get("status") == "success"]
    if not raw_success:
        print("  Skipping response length figure (no raw trial data)")
        return

    len_df = pd.DataFrame(raw_success)
    len_df["turn1_len"] = len_df["turn1_response"].str.len()
    len_df["turn2_len"] = len_df["turn2_response"].str.len()
    len_df["len_delta"] = len_df["turn2_len"] - len_df["turn1_len"]

    # Clip extreme outliers at 1st/99th percentile for cleaner visualization
    low, high = len_df["len_delta"].quantile(0.01), len_df["len_delta"].quantile(0.99)
    len_df["len_delta_clipped"] = len_df["len_delta"].clip(low, high)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

    for ax, framing in zip(axes, ["numeric", "qualitative"]):
        subset = len_df[len_df["framing"] == framing]
        levels = sorted(subset["threshold_level"].unique())
        x_pos = np.arange(len(levels))

        for model in [m for m in MODEL_ORDER if m in subset["model"].unique()]:
            mdata = subset[subset["model"] == model]
            medians = mdata.groupby("threshold_level")["len_delta_clipped"].median()
            # IQR-based error: show 25th-75th percentile range
            q25 = mdata.groupby("threshold_level")["len_delta_clipped"].quantile(0.25)
            q75 = mdata.groupby("threshold_level")["len_delta_clipped"].quantile(0.75)
            y_vals = [medians.get(l, np.nan) for l in levels]
            y_lo = [medians.get(l, 0) - q25.get(l, 0) for l in levels]
            y_hi = [q75.get(l, 0) - medians.get(l, 0) for l in levels]
            ax.errorbar(x_pos, y_vals, yerr=[y_lo, y_hi],
                        marker="o", label=get_label(model), capsize=4, linewidth=2,
                        markersize=6, color=get_color(model))

        ax.set_title(f"{framing.capitalize()} Framing", fontsize=12, fontweight="600")
        ax.set_xlabel("Threshold Level")
        ax.set_ylabel("Median Length Delta (chars)" if framing == "numeric" else "")
        ax.set_xticks(x_pos)
        ax.set_xticklabels([str(int(l)) for l in levels])
        ax.legend(frameon=True)
        ax.axhline(y=0, color="#999999", linestyle="--", alpha=0.5, linewidth=0.8)

    fig.suptitle("Response Length Change (Turn 2 - Turn 1) Across Thresholds",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "08_response_length_delta")


def fig9_length_vs_overcorrection(df):
    """Binned length delta vs mean overcorrection, one panel per model."""
    raw_trials = load_jsonl(TRIALS_PATH)
    raw_success = [t for t in raw_trials if t.get("status") == "success"]
    if not raw_success:
        print("  Skipping fig9 (no raw trial data)")
        return

    len_df = pd.DataFrame(raw_success)
    len_df["turn1_len"] = len_df["turn1_response"].str.len()
    len_df["turn2_len"] = len_df["turn2_response"].str.len()
    len_df["len_delta"] = len_df["turn2_len"] - len_df["turn1_len"]

    # Clip outliers at 1st/99th percentile
    low, high = len_df["len_delta"].quantile(0.01), len_df["len_delta"].quantile(0.99)
    len_df["len_delta_clipped"] = len_df["len_delta"].clip(low, high)

    # Merge with scored data to get overcorrection
    scored_cols = ["trial_id", "overcorrection"]
    scored_sub = df[scored_cols].dropna(subset=["overcorrection"])
    merged = len_df.merge(scored_sub, on="trial_id", how="inner")

    if len(merged) < 10:
        print("  Skipping fig9 (insufficient merged data)")
        return

    models = [m for m in MODEL_ORDER if m in merged["model"].unique()]
    n_models = len(models)
    fig, axes = plt.subplots(1, n_models, figsize=(5.5 * n_models, 5), sharey=True)
    if n_models == 1:
        axes = [axes]

    for ax, model in zip(axes, models):
        mdata = merged[merged["model"] == model].copy()
        if len(mdata) < 10:
            ax.set_title(get_label(model), fontsize=12, fontweight="600", color=get_color(model))
            ax.text(0.5, 0.5, "Insufficient data", transform=ax.transAxes, ha="center")
            continue

        # Bin into deciles
        mdata["len_bin"] = pd.qcut(mdata["len_delta_clipped"], q=10, duplicates="drop")
        binned = mdata.groupby("len_bin", observed=True).agg(
            mean_delta=("len_delta_clipped", "mean"),
            mean_oc=("overcorrection", "mean"),
            sem_oc=("overcorrection", "sem"),
            n=("overcorrection", "count"),
        ).reset_index()

        ax.errorbar(binned["mean_delta"], binned["mean_oc"], yerr=binned["sem_oc"],
                    marker="o", color=get_color(model), capsize=4, linewidth=2,
                    markersize=8, linestyle="-", zorder=3)

        # Trend line
        if len(binned) >= 3:
            z = np.polyfit(binned["mean_delta"], binned["mean_oc"], 1)
            x_fit = np.linspace(binned["mean_delta"].min(), binned["mean_delta"].max(), 50)
            ax.plot(x_fit, np.polyval(z, x_fit), "--", color=get_color(model), alpha=0.4, linewidth=1.5)

        ax.set_title(get_label(model), fontsize=12, fontweight="600", color=get_color(model))
        ax.set_xlabel("Length Delta (chars, binned)")
        ax.set_ylabel("Mean Overcorrection" if model == models[0] else "")
        ax.axhline(y=1.0, color="#CCCCCC", linestyle="--", linewidth=0.8, zorder=0)

    fig.suptitle("Response Length Delta vs. Overcorrection (Binned by Decile)",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "09_length_vs_overcorrection")


def fig10_probe_calibration_cliff(df):
    """Bar chart showing revision rate across all 5 probe wordings."""
    probe_labels = {
        "leading": '"Can this be improved?"',
        "pilot_a": '"Is there anything you\nwould change?"',
        "pilot_c": '"Take another look...\nlet me know if it\'s ready."',
        "pilot_b": '"Review this against the\nquality threshold..."',
        "neutral": '"What do you think?"',
    }
    probe_order = ["leading", "pilot_a", "pilot_c", "pilot_b", "neutral"]
    available = [p for p in probe_order if p in df["probe_type"].unique()]
    if len(available) < 3:
        print("  Skipping probe calibration cliff (fewer than 3 probe types)")
        return

    fig, ax = plt.subplots(figsize=(10, 6))

    rates, ns = [], []
    for probe in available:
        sub = df[df["probe_type"] == probe]
        rate = (sub["revision_gate"] != "decline").mean() * 100
        rates.append(rate)
        ns.append(len(sub))

    colors = []
    for r in rates:
        if r > 80:
            colors.append("#E74C3C")   # red for revision-implying
        elif r > 40:
            colors.append("#F39C12")   # amber for intermediate
        else:
            colors.append("#2ECC71")   # green for evaluative

    bars = ax.bar(range(len(available)), rates, color=colors, edgecolor="white",
                  width=0.65, linewidth=0.5)

    for bar, n in zip(bars, ns):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
                f"n={n}", ha="center", va="bottom", fontsize=9, color="#666666")

    ax.set_xticks(range(len(available)))
    ax.set_xticklabels([probe_labels.get(p, p) for p in available], fontsize=9)
    ax.set_ylabel("Revision Rate (%)", fontsize=11)
    ax.set_title("Probe Calibration: The Binary Compliance Cliff",
                 fontsize=14, fontweight="bold")
    ax.set_ylim(0, 120)
    ax.axhline(y=50, color="#CCCCCC", linestyle="--", linewidth=0.8)

    ax.annotate("Revision-implying", xy=(0.5, 110), fontsize=10,
                color="#E74C3C", ha="center", fontstyle="italic", fontweight="600")
    ax.annotate("Evaluative", xy=(3.5, 35), fontsize=10,
                color="#2ECC71", ha="center", fontstyle="italic", fontweight="600")

    fig.tight_layout()
    save_fig(fig, "10_probe_calibration_cliff")


def fig11_probe_cliff_by_model(df):
    """Grouped bar chart: revision rate per probe per model. Only shows probes with data for all models."""
    probe_order = ["leading", "pilot_a", "pilot_c", "pilot_b", "neutral"]
    models = ordered_models(df)

    # Only include probes that have data for ALL models (avoids missing-bar gaps)
    available = []
    for p in probe_order:
        if p in df["probe_type"].unique():
            has_all = all(
                len(df[(df["probe_type"] == p) & (df["model"] == m)]) > 0
                for m in models
            )
            available.append((p, has_all))

    # Separate: probes with full data vs partial
    full_probes = [p for p, has_all in available if has_all]
    partial_probes = [p for p, has_all in available if not has_all]

    if len(full_probes) < 2:
        print("  Skipping probe cliff by model (fewer than 2 probes with full model coverage)")
        return

    probe_labels = {
        "leading": '"Can this be\nimproved?"',
        "pilot_a": '"Anything you\nwould change?"',
        "pilot_c": '"Take another\nlook..."',
        "pilot_b": '"Review against\nthreshold..."',
        "neutral": '"What do\nyou think?"',
    }

    all_probes = full_probes + partial_probes
    x = np.arange(len(all_probes))
    width = 0.22

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, model in enumerate(models):
        rates = []
        for probe in all_probes:
            sub = df[(df["probe_type"] == probe) & (df["model"] == model)]
            if len(sub) > 0:
                rates.append((sub["revision_gate"] != "decline").mean() * 100)
            else:
                rates.append(np.nan)  # NaN so bar is simply absent, not zero-height
        offset = (i - 1) * width
        ax.bar(x + offset, rates, width, label=get_label(model),
               color=get_color(model), edgecolor="white", linewidth=0.5)

    # Add a vertical separator between full and partial probes
    if partial_probes and full_probes:
        ax.axvline(x=len(full_probes) - 0.5, color="#CCCCCC", linestyle=":", linewidth=1)
        ax.text(len(full_probes) + (len(partial_probes) - 1) / 2, 108,
                "Pilot only (limited data)", ha="center", fontsize=8, color="#999999")

    ax.set_xticks(x)
    ax.set_xticklabels([probe_labels.get(p, p) for p in all_probes], fontsize=8.5)
    ax.set_ylabel("Revision Rate (%)")
    ax.set_title("Revision Rate by Probe Type and Model", fontsize=13, fontweight="bold")
    ax.set_ylim(0, 115)
    ax.legend(frameon=True)
    ax.axhline(y=50, color="#CCCCCC", linestyle="--", linewidth=0.8)

    fig.tight_layout()
    save_fig(fig, "11_probe_cliff_by_model")


def fig12_probe_comparison(df):
    """Gate distribution by model and probe type (main figure). Overcorrection panel saved separately for appendix."""
    if "probe_type" not in df.columns or df["probe_type"].nunique() < 2:
        print("  Skipping probe comparison (only one probe type)")
        return

    models = ordered_models(df)

    # --- Main figure: Revision gate by model and probe type ---
    combos = []
    for model in models:
        for probe in ["leading", "neutral"]:
            if len(df[(df["model"] == model) & (df["probe_type"] == probe)]) > 0:
                combos.append((model, probe))

    fig, ax = plt.subplots(figsize=(10, 5))
    bar_x = np.arange(len(combos))
    bottom = np.zeros(len(combos))

    for gate in GATE_CATEGORIES:
        heights = []
        for model, probe in combos:
            sub = df[(df["model"] == model) & (df["probe_type"] == probe)]
            heights.append((sub["revision_gate"] == gate).mean() if len(sub) > 0 else 0)
        ax.bar(bar_x, heights, bottom=bottom, label=GATE_LABELS[gate],
               color=GATE_COLORS[gate], edgecolor="white", linewidth=0.5, width=0.65)
        bottom += np.array(heights)

    combo_labels = []
    for m, p in combos:
        short_m = get_label(m).split()[0]
        short_p = "Lead." if p == "leading" else "Eval."
        combo_labels.append(f"{short_m}\n({short_p})")

    ax.set_xticks(bar_x)
    ax.set_xticklabels(combo_labels, fontsize=9)
    ax.set_ylabel("Proportion")
    ax.set_title("Revision Gate Distribution by Model and Probe Type", fontsize=13, fontweight="bold")
    ax.legend(title="Gate", frameon=True, loc="upper right")
    ax.set_ylim(0, 1.05)

    fig.tight_layout()
    save_fig(fig, "12_probe_comparison")

    # --- Appendix figure: Overcorrection by probe type ---
    x = np.arange(len(models))
    width = 0.32
    fig2, ax2 = plt.subplots(figsize=(8, 5))

    for i, probe in enumerate(["leading", "neutral"]):
        means, sems = [], []
        for model in models:
            vals = df[(df["model"] == model) & (df["probe_type"] == probe)]["overcorrection"].dropna()
            means.append(vals.mean() if len(vals) > 0 else 0)
            sems.append(vals.sem() if len(vals) > 1 else 0)
        offset = (i - 0.5) * width
        label = "Leading probe" if probe == "leading" else "Evaluative probe"
        ax2.bar(x + offset, means, width, yerr=sems, label=label,
                capsize=4, color=PROBE_COLORS[probe], edgecolor="white", linewidth=0.5)

    for j, model in enumerate(models):
        vals_l = df[(df["model"] == model) & (df["probe_type"] == "leading")]["overcorrection"].dropna()
        vals_n = df[(df["model"] == model) & (df["probe_type"] == "neutral")]["overcorrection"].dropna()
        if len(vals_l) >= 2 and len(vals_n) >= 2:
            _, p = sp_stats.mannwhitneyu(vals_l, vals_n, alternative="two-sided")
            star = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
            if star:
                y_max = max(vals_l.mean() + vals_l.sem(), vals_n.mean() + vals_n.sem())
                ax2.text(j, y_max + 0.15, star, ha="center", fontsize=14, fontweight="bold")

    ax2.set_ylabel("Mean Overcorrection")
    ax2.set_title("Probe Type Effect on Overcorrection", fontsize=13, fontweight="bold")
    ax2.set_xticks(x)
    ax2.set_xticklabels([get_label(m) for m in models])
    ax2.legend(frameon=True)
    ax2.set_ylim(0, 5.5)
    fig2.tight_layout()
    save_fig(fig2, "14_overcorrection_by_probe")


def fig13_probe_threshold_interaction(df):
    """Line plot: overcorrection across threshold levels, panels for each probe type."""
    if "probe_type" not in df.columns or df["probe_type"].nunique() < 2:
        print("  Skipping probe x threshold interaction (only one probe type)")
        return

    probe_types = sorted(df["probe_type"].unique())
    probe_nice = {
        "leading": "Leading Probe",
        "neutral": "Neutral Probe",
        "pilot_a": "Pilot A Probe",
        "pilot_b": "Pilot B Probe",
        "pilot_c": "Pilot C Probe",
    }

    fig, axes = plt.subplots(1, len(probe_types), figsize=(5.5 * len(probe_types), 5), sharey=True)
    if len(probe_types) == 1:
        axes = [axes]

    for ax, probe in zip(axes, probe_types):
        subset = df[df["probe_type"] == probe]
        levels = sorted(subset["threshold_level"].unique())
        x_pos = np.arange(len(levels))

        for model in ordered_models(subset):
            mdata = subset[subset["model"] == model]
            means = mdata.groupby("threshold_level")["overcorrection"].mean()
            sems = mdata.groupby("threshold_level")["overcorrection"].sem()
            y_vals = [means.get(l, np.nan) for l in levels]
            y_errs = [sems.get(l, 0) for l in levels]
            ax.errorbar(x_pos, y_vals, yerr=y_errs,
                        marker="o", label=get_label(model), capsize=4, linewidth=2,
                        markersize=6, color=get_color(model))

        ax.set_title(probe_nice.get(probe, probe.capitalize() + " Probe"),
                     fontsize=11, fontweight="600")
        ax.set_xlabel("Threshold Level")
        ax.set_ylabel("Mean Overcorrection" if probe == probe_types[0] else "")
        ax.set_xticks(x_pos)
        ax.set_xticklabels([str(int(l)) for l in levels])
        ax.legend(frameon=True, fontsize=8)
        ax.set_ylim(0.5, 5.5)

    fig.suptitle("Overcorrection Across Thresholds: Leading vs Neutral Probe",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "13_probe_threshold_interaction")


def main():
    scored = load_jsonl(SCORED_TRIALS_JSONL)
    if not scored:
        print("No scored data to visualize.")
        return

    df = pd.DataFrame(scored)
    for dim in DIMENSIONS:
        df[dim] = pd.to_numeric(df[dim], errors="coerce")

    if "probe_type" not in df.columns:
        df["probe_type"] = "leading"
    df["probe_type"] = df["probe_type"].fillna("leading")

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
    fig10_probe_calibration_cliff(df)
    fig11_probe_cliff_by_model(df)
    fig12_probe_comparison(df)
    fig13_probe_threshold_interaction(df)
    print("Done.")


if __name__ == "__main__":
    main()
