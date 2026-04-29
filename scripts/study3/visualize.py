"""Visualize Study 3 (Revision Yield) results.

Key figures:
1. Revision Yield Curve (main figure)
2. Divergence by model (faceted)
3. DRP by domain
4. Quality trajectory with confidence bands
5. Sycophancy comparison (clean vs nudged)
6. Token waste waterfall
7. Reversibility results
8. Exit ramp comparison
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from scripts.config import S3_FIGURES_DIR, S3_STATS_DIR
from scripts.study3.analyze import load_evaluator, load_worker_turns
from scripts.utils import load_jsonl


def fig1_revision_yield_curve(worker_df: pd.DataFrame, eval_df: pd.DataFrame):
    """Main figure: Revision Yield Curve with MRY and DRP annotation."""
    clean = eval_df[eval_df["condition"] == "clean"]

    eval_done = clean.groupby("turn").apply(lambda g: (g["status"] == "done").mean())
    worker_t2 = worker_df[worker_df["turn"] >= 2]
    worker_rev = worker_t2.groupby("turn")["revised"].mean()
    quality = clean.groupby("turn")["quality"].mean()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 8), sharex=True,
                                     gridspec_kw={"height_ratios": [2, 1]})

    # Top: Divergence curve
    turns_e = sorted(eval_done.index)
    turns_w = sorted(worker_rev.index)

    ax1.plot(turns_e, [eval_done[t] for t in turns_e],
             marker="s", color="#2ecc71", linewidth=2.5, markersize=9,
             label="Blind evaluator: 'done' rate")
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

    # Bottom: Quality trajectory
    turns_q = sorted(quality.index)
    ax2.plot(turns_q, [quality[t] for t in turns_q],
             marker="D", color="#3498db", linewidth=2.5, markersize=8,
             label="Mean quality (blind evaluator)")

    # Annotate MRY
    for i in range(1, len(turns_q)):
        delta = quality[turns_q[i]] - quality[turns_q[i-1]]
        color = "#2ecc71" if delta > 0 else "#e74c3c"
        ax2.annotate(f"{delta:+.2f}", xy=(turns_q[i], quality[turns_q[i]]),
                     xytext=(0, 12), textcoords="offset points",
                     fontsize=8, color=color, ha="center", fontweight="bold")

    ax2.set_xlabel("Turn", fontsize=11)
    ax2.set_ylabel("Quality (1-5)", fontsize=11)
    ax2.set_xticks(range(1, 6))
    ax2.set_ylim(1, 5.5)
    ax2.legend(loc="best", fontsize=9)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = S3_FIGURES_DIR / "fig1_revision_yield_curve.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig2_divergence_by_model(worker_df: pd.DataFrame, eval_df: pd.DataFrame):
    """Divergence curves faceted by model."""
    clean = eval_df[eval_df["condition"] == "clean"]
    models = sorted(worker_df["model"].unique())

    fig, axes = plt.subplots(1, len(models), figsize=(5 * len(models), 5), sharey=True)
    if len(models) == 1:
        axes = [axes]

    for ax, model in zip(axes, models):
        m_eval = clean[clean["model"] == model]
        m_worker = worker_df[(worker_df["model"] == model) & (worker_df["turn"] >= 2)]

        eval_done = m_eval.groupby("turn").apply(lambda g: (g["status"] == "done").mean())
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

    axes[0].set_ylabel("Rate")
    axes[0].legend(fontsize=9)
    fig.suptitle("Overcorrection Gap by Model", fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()
    path = S3_FIGURES_DIR / "fig2_divergence_by_model.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig3_drp_by_domain(eval_df: pd.DataFrame):
    """Quality trajectories by domain with DRP annotated."""
    clean = eval_df[eval_df["condition"] == "clean"]
    domains = sorted(clean["domain"].unique())
    palette = {"code": "#e67e22", "data_logic": "#f39c12", "analysis": "#9b59b6",
               "writing": "#3498db", "creative": "#e74c3c"}

    fig, ax = plt.subplots(figsize=(9, 5))
    for domain in domains:
        subset = clean[clean["domain"] == domain]
        quality = subset.groupby("turn")["quality"].mean()
        turns = sorted(quality.index)
        ax.plot(turns, [quality[t] for t in turns],
                marker="o", label=domain, color=palette.get(domain, "#333"),
                linewidth=2, markersize=7)

    ax.set_xlabel("Turn", fontsize=11)
    ax.set_ylabel("Mean Quality (1-5)", fontsize=11)
    ax.set_title("Quality Trajectory by Domain (DRP = where curve flattens)", fontsize=13, fontweight="bold")
    ax.set_xticks(range(1, 6))
    ax.set_ylim(1, 5.5)
    ax.legend(title="Domain", fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    path = S3_FIGURES_DIR / "fig3_drp_by_domain.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig4_sycophancy(eval_df: pd.DataFrame):
    """Clean vs nudged: stacked bars."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    for ax, condition, title in zip(axes, ["clean", "nudged"], ["Clean Evaluator", "Nudged Evaluator"]):
        subset = eval_df[eval_df["condition"] == condition]
        counts = subset.groupby(["turn", "status"]).size().unstack(fill_value=0)
        for col in ["done", "needs_work"]:
            if col not in counts.columns:
                counts[col] = 0
        totals = counts.sum(axis=1)
        done_pct = counts["done"] / totals
        needs_pct = counts["needs_work"] / totals
        turns = sorted(counts.index)

        ax.bar(turns, [done_pct.get(t, 0) for t in turns],
               color="#2ecc71", label="done", edgecolor="black", linewidth=0.5)
        ax.bar(turns, [needs_pct.get(t, 0) for t in turns],
               bottom=[done_pct.get(t, 0) for t in turns],
               color="#e74c3c", label="needs_work", edgecolor="black", linewidth=0.5)
        ax.set_title(title, fontsize=12, fontweight="bold")
        ax.set_xlabel("Turn")
        ax.set_xticks(range(1, 6))

    axes[0].set_ylabel("Proportion")
    axes[0].legend()
    fig.suptitle("Evaluator Sycophancy: Does a Nudge Change Judgment?", fontsize=14, fontweight="bold")
    plt.tight_layout()
    path = S3_FIGURES_DIR / "fig4_sycophancy.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig5_stylistic_drift(worker_df: pd.DataFrame):
    """Word count and TTR across turns."""
    from scripts.study3.analyze import load_worker_turns
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

    # Word count by turn
    sns.boxplot(data=df, x="turn", y="word_count", ax=ax1, palette="Blues")
    ax1.set_xlabel("Turn")
    ax1.set_ylabel("Word Count")
    ax1.set_title("Response Length Across Turns", fontweight="bold")

    # TTR by turn
    sns.boxplot(data=df, x="turn", y="ttr", ax=ax2, palette="Oranges")
    ax2.set_xlabel("Turn")
    ax2.set_ylabel("Type-Token Ratio")
    ax2.set_title("Lexical Diversity Across Turns", fontweight="bold")

    plt.tight_layout()
    path = S3_FIGURES_DIR / "fig5_stylistic_drift.png"
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
    fig4_sycophancy(eval_df)
    fig5_stylistic_drift(worker_df)

    print("Done.")


if __name__ == "__main__":
    main()
