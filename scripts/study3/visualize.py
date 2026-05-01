"""Visualize Study 3 (Revision Yield) results.

Key figures:
1. Revision Yield Curve (main figure)
2. Divergence by model (faceted, 6 models)
3. DRP by domain (quality trajectory)
4. Quality trajectory with confidence bands
5. Stylistic drift (word count + TTR)
6. CARY curves at multiple budget tiers
7. Unit economics comparison
"""

import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from scripts.config import S3_FIGURES_DIR, S3_STATS_DIR
from scripts.study3.analyze import (
    compute_cary,
    load_evaluator,
    load_worker_turns,
)
from scripts.utils import load_jsonl


def fig1_revision_yield_curve(worker_df: pd.DataFrame, eval_df: pd.DataFrame):
    """Main figure: Revision Yield Curve with 6-level scale and DRP annotation."""

    eval_done = eval_df.groupby("turn").apply(lambda g: (g["level"] >= 4).mean())
    worker_t2 = worker_df[worker_df["turn"] >= 2]
    worker_rev = worker_t2.groupby("turn")["revised"].mean()
    level = eval_df.groupby("turn")["level"].mean()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 8), sharex=True,
                                     gridspec_kw={"height_ratios": [2, 1]})

    # Top: Divergence curve
    turns_e = sorted(eval_done.index)
    turns_w = sorted(worker_rev.index)

    ax1.plot(turns_e, [eval_done[t] for t in turns_e],
             marker="s", color="#2ecc71", linewidth=2.5, markersize=9,
             label="Blind evaluator: 'done' rate (level >= 4 Sufficient)")
    ax1.plot(turns_w, [worker_rev[t] for t in turns_w],
             marker="o", color="#e74c3c", linewidth=2.5, markersize=9,
             label="Working model: revision rate")

    shared = sorted(set(turns_e) & set(turns_w))
    if shared:
        ax1.fill_between(shared,
                         [eval_done[t] for t in shared],
                         [worker_rev[t] for t in shared],
                         alpha=0.12, color="#e74c3c", label="Overcorrection gap")

    ax1.set_ylabel("Rate", fontsize=11)
    ax1.set_ylim(-0.05, 1.1)
    ax1.legend(loc="best", fontsize=9)
    ax1.set_title("Revision Yield: Divergence and Quality", fontsize=13, fontweight="bold")
    ax1.grid(True, alpha=0.3)

    # Bottom: Quality trajectory (6-level scale)
    turns_q = sorted(level.index)
    ax2.plot(turns_q, [level[t] for t in turns_q],
             marker="D", color="#3498db", linewidth=2.5, markersize=8,
             label="Mean quality level (blind evaluator)")

    # Annotate MRY
    for i in range(1, len(turns_q)):
        delta = level[turns_q[i]] - level[turns_q[i-1]]
        color = "#2ecc71" if delta > 0 else "#e74c3c"
        ax2.annotate(f"{delta:+.2f}", xy=(turns_q[i], level[turns_q[i]]),
                     xytext=(0, 12), textcoords="offset points",
                     fontsize=8, color=color, ha="center", fontweight="bold")

    # DRP line
    ax2.axhline(y=4.0, color="gray", linestyle="--", alpha=0.5, label="'Sufficient' threshold (level 4+)")

    ax2.set_xlabel("Turn", fontsize=11)
    ax2.set_ylabel("Quality Level (1-6 scale)", fontsize=11)
    ax2.set_xticks(range(1, 6))
    ax2.set_ylim(0.5, 6.5)
    ax2.legend(loc="best", fontsize=9)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = S3_FIGURES_DIR / "fig1_revision_yield_curve.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig2_divergence_by_model(worker_df: pd.DataFrame, eval_df: pd.DataFrame):
    """Divergence curves faceted by model (6 models, 2x3 grid)."""
    models = sorted(worker_df["model"].unique())
    n_models = len(models)
    ncols = min(3, n_models)
    nrows = (n_models + ncols - 1) // ncols

    fig, axes = plt.subplots(nrows, ncols, figsize=(5 * ncols, 5 * nrows), sharey=True)
    if n_models == 1:
        axes = np.array([[axes]])
    axes = np.atleast_2d(axes)

    for idx, model in enumerate(models):
        row, col = divmod(idx, ncols)
        ax = axes[row, col]

        m_eval = eval_df[eval_df["model"] == model]
        m_worker = worker_df[(worker_df["model"] == model) & (worker_df["turn"] >= 2)]

        eval_done = m_eval.groupby("turn").apply(lambda g: (g["level"] >= 4).mean())
        worker_rev = m_worker.groupby("turn")["revised"].mean()

        turns_e = sorted(eval_done.index)
        turns_w = sorted(worker_rev.index)

        ax.plot(turns_e, [eval_done[t] for t in turns_e],
                marker="s", color="#2ecc71", linewidth=2, markersize=7, label="Eval 'done'")
        ax.plot(turns_w, [worker_rev[t] for t in turns_w],
                marker="o", color="#e74c3c", linewidth=2, markersize=7, label="Worker revises")

        shared = sorted(set(turns_e) & set(turns_w))
        if shared:
            ax.fill_between(shared, [eval_done[t] for t in shared],
                            [worker_rev[t] for t in shared], alpha=0.12, color="#e74c3c")

        ax.set_title(model, fontsize=12, fontweight="bold")
        ax.set_xlabel("Turn")
        ax.set_xticks(range(1, 6))
        ax.set_ylim(-0.05, 1.1)
        ax.grid(True, alpha=0.3)

    # Hide unused axes
    for idx in range(n_models, nrows * ncols):
        row, col = divmod(idx, ncols)
        axes[row, col].set_visible(False)

    axes[0, 0].set_ylabel("Rate")
    axes[0, 0].legend(fontsize=9)
    fig.suptitle("Overcorrection Gap by Model", fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()
    path = S3_FIGURES_DIR / "fig2_divergence_by_model.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig3_drp_by_domain(eval_df: pd.DataFrame):
    """Quality trajectories by domain with DRP annotated."""
    domains = sorted(eval_df["domain"].unique())
    palette = {"code": "#e67e22", "data_logic": "#f39c12", "analysis": "#9b59b6",
               "writing": "#3498db", "creative": "#e74c3c"}

    fig, ax = plt.subplots(figsize=(9, 5))
    for domain in domains:
        subset = eval_df[eval_df["domain"] == domain]
        level = subset.groupby("turn")["level"].mean()
        turns = sorted(level.index)
        ax.plot(turns, [level[t] for t in turns],
                marker="o", label=domain, color=palette.get(domain, "#333"),
                linewidth=2, markersize=7)

    ax.axhline(y=4.0, color="gray", linestyle="--", alpha=0.5, label="'Sufficient' threshold")

    ax.set_xlabel("Turn", fontsize=11)
    ax.set_ylabel("Mean Quality Level (1-6 scale)", fontsize=11)
    ax.set_title("Quality Trajectory by Domain", fontsize=13, fontweight="bold")
    ax.set_xticks(range(1, 6))
    ax.set_ylim(0.5, 6.5)
    ax.legend(title="Domain", fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    path = S3_FIGURES_DIR / "fig3_drp_by_domain.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig4_stylistic_drift(worker_df: pd.DataFrame):
    """Word count and TTR across turns."""
    trials = load_jsonl(
        Path(__file__).resolve().parent.parent.parent / "data" / "study3" / "raw_responses" / "worker_trials.jsonl"
    )
    successful = [t for t in trials if t.get("status") == "success"]

    rows = []
    for trial in successful:
        for turn_idx, response in enumerate(trial["responses"]):
            words = response.split()
            unique_words = set(w.lower() for w in words)
            ttr = len(unique_words) / len(words) if words else 0
            rows.append({"turn": turn_idx + 1, "word_count": len(words), "ttr": ttr, "domain": trial["domain"]})

    df = pd.DataFrame(rows)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    sns.boxplot(data=df, x="turn", y="word_count", ax=ax1, palette="Blues")
    ax1.set_xlabel("Turn")
    ax1.set_ylabel("Word Count")
    ax1.set_title("Response Length Across Turns", fontweight="bold")

    sns.boxplot(data=df, x="turn", y="ttr", ax=ax2, palette="Oranges")
    ax2.set_xlabel("Turn")
    ax2.set_ylabel("Type-Token Ratio")
    ax2.set_title("Lexical Diversity Across Turns", fontweight="bold")

    plt.tight_layout()
    path = S3_FIGURES_DIR / "fig4_stylistic_drift.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig5_cary_curves(eval_df: pd.DataFrame, worker_df: pd.DataFrame):
    """CARY curves at multiple C values showing optimal stopping turn."""
    level_by_turn = eval_df.groupby("turn")["level"].mean().to_dict()
    tokens_by_turn = worker_df.groupby("turn")["output_tokens"].mean().to_dict()

    c_values = {
        "Unlimited (C=0)": 0,
        "API Heavy (C=2e-8)": 2e-8,
        "API Light (C=2e-7)": 2e-7,
        "Pro (C=5e-7)": 5e-7,
        "Plus (C=2e-6)": 2e-6,
        "Free (C=1e-5)": 1e-5,
    }

    colors = ["#2c3e50", "#2980b9", "#27ae60", "#f39c12", "#e67e22", "#e74c3c"]

    fig, ax = plt.subplots(figsize=(10, 6))

    for (label, c_val), color in zip(c_values.items(), colors):
        cary = compute_cary(level_by_turn, tokens_by_turn, c_val)
        turns = sorted(cary.keys())
        values = [cary[t] for t in turns]
        ax.plot(turns, values, marker="o", label=label, color=color, linewidth=2, markersize=7)

        # Mark optimal stop
        t_star = max(cary.keys(), key=lambda t: cary[t])
        ax.plot(t_star, cary[t_star], marker="*", color=color, markersize=14, zorder=5)

    ax.set_xlabel("Turn", fontsize=11)
    ax.set_ylabel("CARY (Cost-Adjusted Revision Yield)", fontsize=11)
    ax.set_title("CARY Curves: Where Revision Stops Paying Off", fontsize=13, fontweight="bold")
    ax.set_xticks(range(1, 6))
    ax.legend(fontsize=9, title="Budget Tier")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    path = S3_FIGURES_DIR / "fig5_cary_curves.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig6_unit_economics(eval_df: pd.DataFrame, worker_df: pd.DataFrame):
    """Bar chart comparing revision tax across models."""
    models = sorted(worker_df["model"].unique())
    revision_taxes = []

    for model in models:
        m_eval = eval_df[eval_df["model"] == model]
        m_worker = worker_df[worker_df["model"] == model]

        level_by_turn = m_eval.groupby("turn")["level"].mean().to_dict()
        tokens_by_turn = m_worker.groupby("turn")["output_tokens"].mean().to_dict()
        turns = sorted(level_by_turn.keys())
        if not turns:
            revision_taxes.append(0)
            continue

        cary = compute_cary(level_by_turn, tokens_by_turn, 5e-7)
        t_star = max(cary.keys(), key=lambda t: cary[t]) if cary else 1
        opt_tokens = sum(tokens_by_turn.get(t, 0) for t in turns if t <= t_star)
        full_tokens = sum(tokens_by_turn.get(t, 0) for t in turns)
        tax = ((full_tokens - opt_tokens) / opt_tokens * 100) if opt_tokens > 0 else 0
        revision_taxes.append(tax)

    fig, ax = plt.subplots(figsize=(10, 5))
    colors = sns.color_palette("husl", len(models))
    bars = ax.bar(models, revision_taxes, color=colors, edgecolor="black", linewidth=0.5)

    for bar, tax in zip(bars, revision_taxes):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
                f"{tax:.0f}%", ha="center", fontsize=10, fontweight="bold")

    ax.set_ylabel("Revision Tax (%)", fontsize=11)
    ax.set_title("Revision Tax by Model (Pro Tier, C=5e-7)", fontsize=13, fontweight="bold")
    ax.grid(True, alpha=0.3, axis="y")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    path = S3_FIGURES_DIR / "fig6_unit_economics.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def main():
    S3_FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    worker_df = load_worker_turns()
    eval_df = load_evaluator()

    if worker_df.empty or eval_df.empty:
        print("No data to visualize. Run the experiment first.")
        return

    print(f"Loaded {len(worker_df)} worker rows, {len(eval_df)} evaluator judgments")

    fig1_revision_yield_curve(worker_df, eval_df)
    fig2_divergence_by_model(worker_df, eval_df)
    fig3_drp_by_domain(eval_df)
    fig4_stylistic_drift(worker_df)
    fig5_cary_curves(eval_df, worker_df)
    fig6_unit_economics(eval_df, worker_df)

    print("Done.")


if __name__ == "__main__":
    main()
