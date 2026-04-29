"""Visualize blind evaluator experiment results (Study 3)."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from scripts.config import (
    BLIND_EVAL_EVALUATOR_RESULTS_PATH,
    BLIND_EVAL_FIGURES_DIR,
    BLIND_EVAL_STATS_DIR,
    BLIND_EVAL_WORKER_TRIALS_PATH,
)
from scripts.analyze_blind_eval import (
    classify_revision,
    load_evaluator_data,
    load_worker_data,
)


def fig_divergence_curve(worker_df: pd.DataFrame, eval_df: pd.DataFrame):
    """Main figure: blind evaluator 'done' rate vs working model revision rate by turn."""
    clean_eval = eval_df[eval_df["condition"] == "clean"]

    eval_done = clean_eval.groupby("turn").apply(lambda g: (g["status"] == "done").mean())
    worker_turns = worker_df[worker_df["turn"] >= 2]
    worker_rev = worker_turns.groupby("turn")["revised"].mean()

    fig, ax = plt.subplots(figsize=(8, 5))
    turns_eval = sorted(eval_done.index)
    turns_worker = sorted(worker_rev.index)

    ax.plot(turns_eval, [eval_done[t] for t in turns_eval],
            marker="s", label="Blind evaluator: 'done' rate",
            color="#2ecc71", linewidth=2.5, markersize=9)
    ax.plot(turns_worker, [worker_rev[t] for t in turns_worker],
            marker="o", label="Working model: revision rate",
            color="#e74c3c", linewidth=2.5, markersize=9)

    # Shade the gap
    shared_turns = sorted(set(turns_eval) & set(turns_worker))
    if shared_turns:
        eval_vals = [eval_done[t] for t in shared_turns]
        worker_vals = [worker_rev[t] for t in shared_turns]
        ax.fill_between(shared_turns, eval_vals, worker_vals,
                        alpha=0.15, color="#e74c3c", label="Sycophancy gap")

    ax.set_xlabel("Turn", fontsize=12)
    ax.set_ylabel("Rate", fontsize=12)
    ax.set_title("Divergence: Blind Evaluator vs Working Model", fontsize=14, fontweight="bold")
    ax.set_xticks(range(1, 6))
    ax.set_ylim(-0.05, 1.1)
    ax.legend(loc="best", fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

    path = BLIND_EVAL_FIGURES_DIR / "divergence_curve.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig_divergence_by_model(worker_df: pd.DataFrame, eval_df: pd.DataFrame):
    """Divergence curves faceted by model."""
    clean_eval = eval_df[eval_df["condition"] == "clean"]
    models = sorted(worker_df["model"].unique())

    fig, axes = plt.subplots(1, len(models), figsize=(5 * len(models), 5), sharey=True)
    if len(models) == 1:
        axes = [axes]

    for ax, model in zip(axes, models):
        m_eval = clean_eval[clean_eval["model"] == model]
        m_worker = worker_df[(worker_df["model"] == model) & (worker_df["turn"] >= 2)]

        eval_done = m_eval.groupby("turn").apply(lambda g: (g["status"] == "done").mean())
        worker_rev = m_worker.groupby("turn")["revised"].mean()

        turns_e = sorted(eval_done.index)
        turns_w = sorted(worker_rev.index)

        ax.plot(turns_e, [eval_done[t] for t in turns_e],
                marker="s", color="#2ecc71", linewidth=2, markersize=7,
                label="Evaluator 'done'")
        ax.plot(turns_w, [worker_rev[t] for t in turns_w],
                marker="o", color="#e74c3c", linewidth=2, markersize=7,
                label="Worker revision")

        shared = sorted(set(turns_e) & set(turns_w))
        if shared:
            ax.fill_between(shared,
                            [eval_done[t] for t in shared],
                            [worker_rev[t] for t in shared],
                            alpha=0.15, color="#e74c3c")

        ax.set_title(model, fontsize=12, fontweight="bold")
        ax.set_xlabel("Turn")
        ax.set_xticks(range(1, 6))
        ax.set_ylim(-0.05, 1.1)
        ax.grid(True, alpha=0.3)

    axes[0].set_ylabel("Rate")
    axes[0].legend(fontsize=9)
    fig.suptitle("Divergence by Model", fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()

    path = BLIND_EVAL_FIGURES_DIR / "divergence_by_model.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig_quality_trajectory(eval_df: pd.DataFrame):
    """Quality score by turn, split by model."""
    clean_eval = eval_df[eval_df["condition"] == "clean"]
    models = sorted(clean_eval["model"].unique())

    fig, ax = plt.subplots(figsize=(8, 5))
    palette = sns.color_palette("Set2", len(models))

    for model, color in zip(models, palette):
        subset = clean_eval[clean_eval["model"] == model]
        quality = subset.groupby("turn")["quality"].agg(["mean", "std"])
        turns = sorted(quality.index)
        means = [quality.loc[t, "mean"] for t in turns]
        stds = [quality.loc[t, "std"] for t in turns]

        ax.plot(turns, means, marker="o", label=model, color=color, linewidth=2, markersize=8)
        ax.fill_between(turns,
                        [m - s for m, s in zip(means, stds)],
                        [m + s for m, s in zip(means, stds)],
                        alpha=0.15, color=color)

    ax.set_xlabel("Turn", fontsize=12)
    ax.set_ylabel("Mean Quality Score (1-5)", fontsize=12)
    ax.set_title("Quality Trajectory Across Turns", fontsize=14, fontweight="bold")
    ax.set_xticks(range(1, 6))
    ax.set_ylim(0.5, 5.5)
    ax.legend(title="Model", fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

    path = BLIND_EVAL_FIGURES_DIR / "quality_trajectory.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig_sycophancy_comparison(eval_df: pd.DataFrame):
    """Clean vs nudged evaluator: stacked bar of done/needs_work by condition and turn."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    for ax, condition, title in zip(axes, ["clean", "nudged"], ["Clean Evaluator", "Nudged Evaluator"]):
        subset = eval_df[eval_df["condition"] == condition]
        counts = subset.groupby(["turn", "status"]).size().unstack(fill_value=0)

        # Ensure both columns exist
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
        ax.set_ylim(0, 1.05)

    axes[0].set_ylabel("Proportion")
    axes[0].legend()
    fig.suptitle("Evaluator Judgments: Clean vs Nudged", fontsize=14, fontweight="bold")
    plt.tight_layout()

    path = BLIND_EVAL_FIGURES_DIR / "sycophancy_comparison.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig_domain_divergence(worker_df: pd.DataFrame, eval_df: pd.DataFrame):
    """Divergence curves faceted by domain."""
    clean_eval = eval_df[eval_df["condition"] == "clean"]
    domains = sorted(worker_df["domain"].unique())

    fig, axes = plt.subplots(1, len(domains), figsize=(5 * len(domains), 5), sharey=True)
    if len(domains) == 1:
        axes = [axes]

    for ax, domain in zip(axes, domains):
        d_eval = clean_eval[clean_eval["domain"] == domain]
        d_worker = worker_df[(worker_df["domain"] == domain) & (worker_df["turn"] >= 2)]

        eval_done = d_eval.groupby("turn").apply(lambda g: (g["status"] == "done").mean())
        worker_rev = d_worker.groupby("turn")["revised"].mean()

        turns_e = sorted(eval_done.index)
        turns_w = sorted(worker_rev.index)

        ax.plot(turns_e, [eval_done[t] for t in turns_e],
                marker="s", color="#2ecc71", linewidth=2, markersize=7,
                label="Evaluator 'done'")
        ax.plot(turns_w, [worker_rev[t] for t in turns_w],
                marker="o", color="#e74c3c", linewidth=2, markersize=7,
                label="Worker revision")

        ax.set_title(domain.capitalize(), fontsize=12, fontweight="bold")
        ax.set_xlabel("Turn")
        ax.set_xticks(range(1, 6))
        ax.set_ylim(-0.05, 1.1)
        ax.grid(True, alpha=0.3)

    axes[0].set_ylabel("Rate")
    axes[0].legend(fontsize=9)
    fig.suptitle("Divergence by Task Domain", fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()

    path = BLIND_EVAL_FIGURES_DIR / "divergence_by_domain.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def fig_quality_by_domain(eval_df: pd.DataFrame):
    """Quality trajectory split by domain."""
    clean_eval = eval_df[eval_df["condition"] == "clean"]
    domains = sorted(clean_eval["domain"].unique())

    fig, ax = plt.subplots(figsize=(8, 5))
    palette = {"writing": "#3498db", "code": "#e67e22", "analysis": "#9b59b6"}

    for domain in domains:
        subset = clean_eval[clean_eval["domain"] == domain]
        quality = subset.groupby("turn")["quality"].mean()
        turns = sorted(quality.index)
        ax.plot(turns, [quality[t] for t in turns],
                marker="o", label=domain.capitalize(),
                color=palette.get(domain, "#333"),
                linewidth=2, markersize=8)

    ax.set_xlabel("Turn", fontsize=12)
    ax.set_ylabel("Mean Quality Score (1-5)", fontsize=12)
    ax.set_title("Quality Trajectory by Domain", fontsize=14, fontweight="bold")
    ax.set_xticks(range(1, 6))
    ax.set_ylim(0.5, 5.5)
    ax.legend(title="Domain", fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

    path = BLIND_EVAL_FIGURES_DIR / "quality_by_domain.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def main():
    BLIND_EVAL_FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    worker_df = load_worker_data()
    eval_df = load_evaluator_data()

    if worker_df.empty or eval_df.empty:
        print("No data to visualize. Run the experiment first.")
        return

    print(f"Loaded {len(worker_df)} worker rows, {len(eval_df)} evaluator judgments")

    fig_divergence_curve(worker_df, eval_df)
    fig_divergence_by_model(worker_df, eval_df)
    fig_quality_trajectory(eval_df)
    fig_sycophancy_comparison(eval_df)
    fig_domain_divergence(worker_df, eval_df)
    fig_quality_by_domain(eval_df)

    print("Done.")


if __name__ == "__main__":
    main()
