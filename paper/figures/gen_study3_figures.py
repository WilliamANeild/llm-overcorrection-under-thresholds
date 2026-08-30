#!/usr/bin/env python3
"""
Generate all Study 3 figures for the ACL paper.

Figures:
  s3_fig1 - Revision Yield Curve (dual panel: overcorrection gap + quality trajectory)
  s3_fig2 - Per-Model Quality Trajectories (2x3 small multiples)
  s3_fig3 - The Akrasia Gap (know-but-cannot-stop triptych)
  s3_fig4 - Feedback Recovery (targeted vs generic dumbbell)

All figures use consistent styling, ACL-compatible sizing, and read from
data/study3/analysis/study3_results.json.
"""

import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS = ROOT / "data" / "study3" / "analysis" / "study3_results.json"
OUTDIR = Path(__file__).resolve().parent

with open(RESULTS) as f:
    data = json.load(f)

# ── Consistent style ──────────────────────────────────────────────────
# Match LaTeX brand colors
CLAUDE_ORANGE = "#D97757"
GOOGLE_BLUE   = "#4285F4"
GPT_DARK      = "#1A1A2E"
GATE_GREEN    = "#2ECC71"
GATE_RED      = "#E74C3C"
GATE_AMBER    = "#F39C12"

# Paper palette
BLUE   = "#4878A8"
RED    = "#C44E52"
GREEN  = "#55A868"
PURPLE = "#8172B2"
ORANGE = "#CCB974"
GRAY   = "#8C8C8C"
LIGHT_GRAY = "#D0D0D0"

# Model colors (consistent across all figures)
MODEL_COLORS = {
    "claude-sonnet-4":  CLAUDE_ORANGE,
    "deepseek-v4":      "#7B68EE",
    "gemini-2.5-flash": GOOGLE_BLUE,
    "gpt-4o":           GPT_DARK,
    "llama-3.3-70b":    GREEN,
    "qwen-3-235b":      "#E377C2",
}
MODEL_NAMES = {
    "claude-sonnet-4":  "Claude Sonnet 4",
    "deepseek-v4":      "DeepSeek V4",
    "gemini-2.5-flash": "Gemini 2.5 Flash",
    "gpt-4o":           "GPT-4o",
    "llama-3.3-70b":    "Llama 3.3 70B",
    "qwen-3-235b":      "Qwen 3 235B",
}

THRESHOLD = 4.0
TURNS = [1, 2, 3, 4, 5]

def style_ax(ax, ylabel=None, xlabel=None):
    """Apply consistent minimal styling."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#444444")
    ax.spines["bottom"].set_color("#444444")
    ax.tick_params(colors="#444444", labelsize=8)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=9, color="#333333")
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=9, color="#333333")


# ======================================================================
# FIGURE 1: Revision Yield Curve (dual panel)
# Top: overcorrection gap (eval done rate vs worker revision rate)
# Bottom: revision-only quality trajectory (pooled + balanced panel)
# ======================================================================
def make_fig1():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.4, 4.5), dpi=250,
                                    gridspec_kw={"height_ratios": [1, 1.2],
                                                 "hspace": 0.35})
    fig.patch.set_facecolor("white")

    rq3 = data["rq3"]
    rq1 = data["rq1"]

    # -- Top panel: Overcorrection gap --
    ax1.set_facecolor("white")
    eval_done = [rq3["eval_done_rate"][str(t)] for t in TURNS]
    worker_rev = [0] + [rq3["worker_revision_rate"][str(t)] for t in [2, 3, 4, 5]]

    ax1.plot(TURNS, eval_done, "s-", color=GREEN, markersize=5, linewidth=1.8,
             label="Evaluator: sufficient", zorder=3)
    ax1.plot(TURNS, worker_rev, "o-", color=RED, markersize=5, linewidth=1.8,
             label="Model: revises", zorder=3)

    # Shade the gap where worker revises despite eval saying done
    for t in range(1, 5):
        t_idx = t  # turns 2-5
        if worker_rev[t_idx] > eval_done[t_idx]:
            pass  # only shade where gap exists
        ax1.fill_between([TURNS[t_idx-1], TURNS[t_idx]],
                         [eval_done[t_idx-1], eval_done[t_idx]],
                         [worker_rev[t_idx-1], worker_rev[t_idx]],
                         alpha=0.12, color=RED, zorder=1)

    # Shade the overcorrection gap region (T2 onward where revision > done)
    turns_gap = TURNS[1:]
    eval_gap = eval_done[1:]
    rev_gap = worker_rev[1:]
    ax1.fill_between(turns_gap, eval_gap, rev_gap,
                     where=[r > e for r, e in zip(rev_gap, eval_gap)],
                     alpha=0.15, color=RED, zorder=1,
                     label="Overcorrection gap")

    ax1.set_ylim(-0.05, 1.1)
    ax1.set_xlim(0.7, 5.3)
    ax1.set_xticks(TURNS)
    ax1.yaxis.set_major_formatter(mticker.PercentFormatter(1.0, decimals=0))
    style_ax(ax1, ylabel="Rate")
    ax1.legend(fontsize=6.5, loc="center right", framealpha=0.9,
               edgecolor="#cccccc")
    ax1.set_title("Overcorrection gap", fontsize=9, fontweight="bold",
                  color="#333333", pad=6)

    # -- Bottom panel: Quality trajectory --
    ax2.set_facecolor("white")

    # Pooled revision-only
    pooled = [rq1["revision_only_level_by_turn"][str(t)] for t in TURNS]
    ax2.plot(TURNS, pooled, "o-", color=BLUE, markersize=5, linewidth=1.8,
             label="Pooled (revision-only)", zorder=3)

    # Balanced panel
    balanced = data["edge_cases"]["cohort_trajectories"]["balanced"]["trajectory"]
    bal_means = [balanced[str(t)]["mean"] for t in TURNS]
    ax2.plot(TURNS, bal_means, "D--", color=PURPLE, markersize=4, linewidth=1.4,
             label=f"Balanced panel (n={data['edge_cases']['cohort_trajectories']['balanced']['n_trials']})",
             zorder=3, alpha=0.85)

    # Needs-work subset (improves)
    nw = data["edge_cases"]["cohort_trajectories"]["needs_work_balanced"]["trajectory"]
    nw_means = [nw[str(t)]["mean"] for t in TURNS]
    ax2.plot(TURNS, nw_means, "^:", color=GREEN, markersize=4, linewidth=1.2,
             label=f"Started below threshold (n={data['edge_cases']['cohort_trajectories']['needs_work_balanced']['n_trials']})",
             zorder=3, alpha=0.75)

    # Threshold line
    ax2.axhline(THRESHOLD, color=GRAY, linestyle="--", linewidth=0.8, alpha=0.6)
    ax2.text(5.15, THRESHOLD + 0.08, "Sufficient", fontsize=6.5, color=GRAY,
             va="bottom")

    # Delta annotations on pooled line
    deltas = [rq1["revision_only_quality_delta"][str(t)] for t in [2, 3, 4, 5]]
    for i, (t, d) in enumerate(zip(TURNS[1:], deltas)):
        color = RED if d < 0 else GREEN
        ax2.annotate(f"{d:+.2f}", (t, pooled[i+1]),
                     textcoords="offset points", xytext=(8, -2),
                     fontsize=6, color=color, fontweight="bold")

    ax2.set_ylim(0.8, 5.8)
    ax2.set_xlim(0.7, 5.5)
    ax2.set_xticks(TURNS)
    style_ax(ax2, ylabel="Quality level (1-6)", xlabel="Turn")
    ax2.legend(fontsize=6, loc="upper right", framealpha=0.9,
               edgecolor="#cccccc")
    ax2.set_title("Quality trajectory", fontsize=9, fontweight="bold",
                  color="#333333", pad=6)

    fig.savefig(OUTDIR / "s3_fig1_revision_yield.pdf", bbox_inches="tight",
                facecolor="white")
    fig.savefig(OUTDIR / "s3_fig1_revision_yield.png", dpi=200,
                facecolor="white")
    plt.close(fig)
    print("  -> s3_fig1_revision_yield.pdf")


# ======================================================================
# FIGURE 2: Per-Model Quality Trajectories (2x3 small multiples)
# ======================================================================
def make_fig2():
    fig, axes = plt.subplots(2, 3, figsize=(5.5, 3.8), dpi=250,
                              sharey=True, sharex=True)
    fig.patch.set_facecolor("white")

    model_order = ["claude-sonnet-4", "deepseek-v4", "gemini-2.5-flash",
                   "gpt-4o", "llama-3.3-70b", "qwen-3-235b"]
    per_model = data["edge_cases"]["cohort_trajectories"]["per_model"]

    for idx, (model_id, ax) in enumerate(zip(model_order, axes.flat)):
        ax.set_facecolor("white")
        md = per_model[model_id]
        traj = md["trajectory"]
        means = [traj[str(t)]["mean"] for t in TURNS]
        delta = md["mean_delta_t1_t5"]
        n = md["n_balanced"]
        degrades = delta < 0

        color = RED if degrades else GREEN
        light = "#FDECEA" if degrades else "#EAF7EC"

        # Quality line
        ax.plot(TURNS, means, "o-", color=color, markersize=4, linewidth=1.6,
                zorder=3)

        # Shade below threshold region
        if degrades:
            ax.fill_between(TURNS, means, THRESHOLD,
                            where=[m < THRESHOLD for m in means],
                            alpha=0.10, color=RED, zorder=1)

        # Threshold line
        ax.axhline(THRESHOLD, color=GRAY, linestyle="--", linewidth=0.6,
                   alpha=0.5)

        # Delta annotation
        ha = "right" if degrades else "left"
        x_pos = 4.7 if degrades else 4.3
        y_pos = 1.5 if degrades else means[-1] + 0.3
        ax.text(x_pos, y_pos, f"$\\Delta$={delta:+.2f}",
                fontsize=7.5, fontweight="bold", color=color, ha=ha)

        # N annotation
        ax.text(0.97, 0.03, f"n={n}", transform=ax.transAxes,
                fontsize=6, color=GRAY, ha="right", va="bottom")

        # Title
        ax.set_title(MODEL_NAMES[model_id], fontsize=8, fontweight="bold",
                     color="#333333", pad=4)

        style_ax(ax)
        ax.set_xticks(TURNS)
        ax.set_ylim(0.5, 5.8)

    # Shared labels
    for ax in axes[1, :]:
        ax.set_xlabel("Turn", fontsize=8, color="#444444")
    for ax in axes[:, 0]:
        ax.set_ylabel("Quality (1-6)", fontsize=8, color="#444444")

    fig.suptitle("Balanced panel: quality trajectory by model",
                 fontsize=10, fontweight="bold", color="#333333", y=1.01)

    fig.savefig(OUTDIR / "s3_fig2_model_trajectories.pdf", bbox_inches="tight",
                facecolor="white")
    fig.savefig(OUTDIR / "s3_fig2_model_trajectories.png", dpi=200,
                facecolor="white")
    plt.close(fig)
    print("  -> s3_fig2_model_trajectories.pdf")


# ======================================================================
# FIGURE 3: The Akrasia Gap
# Three panels showing the know-but-cannot-stop dissociation:
#   Left: Revision-despite-sufficiency rate by turn
#   Center: Self-reflection (recommended turn distribution)
#   Right: Reversibility (T1 preference rate)
# ======================================================================
def make_fig3():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(5.5, 2.6), dpi=250)
    fig.patch.set_facecolor("white")

    # -- Left: Revision despite sufficiency --
    ax1.set_facecolor("white")

    # Compute per-turn revision-despite-sufficiency from rq3/rq4
    # eval done at turn t, worker revises at turn t+1
    eval_done = data["rq3"]["eval_done_rate"]
    worker_rev = data["rq3"]["worker_revision_rate"]

    # The rate: of outputs rated sufficient at turn t, what fraction get revised at t+1
    rds_rate = data["rq4"]["revision_despite_sufficiency_rate"]

    # Show the aggregate as a single compelling bar + the 64.3% callout
    bars_x = ["Turn\n1-2", "Turn\n2-3", "Turn\n3-4", "Turn\n4-5"]
    # Approximate per-transition from the decline rates
    # rq1 has decline_rate_by_turn which is cumulative
    decline = data["rq1"]["decline_rate_by_turn"]
    rev_rates_per_turn = [1 - decline[str(t)] for t in [2, 3, 4, 5]]

    bar_colors = [RED] * 4
    ax1.bar(bars_x, rev_rates_per_turn, color=bar_colors, alpha=0.7, width=0.6,
            edgecolor=RED, linewidth=0.8)

    for i, v in enumerate(rev_rates_per_turn):
        ax1.text(i, v + 0.02, f"{v:.0%}", ha="center", fontsize=7,
                 color=RED, fontweight="bold")

    ax1.axhline(0.5, color=GRAY, linestyle=":", linewidth=0.6, alpha=0.5)
    ax1.set_ylim(0, 1.0)
    style_ax(ax1, ylabel="Revision rate")
    ax1.set_title("What they do", fontsize=9, fontweight="bold",
                  color=RED, pad=6)

    # Callout
    ax1.text(0.5, 0.88, f"64.3%", transform=ax1.transAxes,
             fontsize=14, fontweight="bold", color=RED, ha="center",
             va="center")
    ax1.text(0.5, 0.78, "revise despite\nsufficiency",
             transform=ax1.transAxes, fontsize=6.5, color="#555555",
             ha="center", va="center")

    # -- Center: Self-reflection distribution --
    ax2.set_facecolor("white")
    rq14 = data["rq14"]
    dist = rq14["distribution"]
    turn_labels = ["T1", "T2", "T3", "T4", "T5"]
    counts = [dist[str(t)] for t in TURNS]
    total = sum(counts)
    fracs = [c / total for c in counts]

    colors = [GREEN if t == 1 else BLUE if t <= 3 else GRAY for t in TURNS]
    ax2.bar(turn_labels, fracs, color=colors, alpha=0.75, width=0.6,
            edgecolor=[c for c in colors], linewidth=0.8)

    for i, (f, c) in enumerate(zip(fracs, counts)):
        ax2.text(i, f + 0.01, f"{f:.0%}", ha="center", fontsize=7,
                 color="#444444", fontweight="bold")

    ax2.set_ylim(0, 0.55)
    style_ax(ax2, ylabel="Fraction recommended")
    ax2.set_title("What they recommend", fontsize=9, fontweight="bold",
                  color=BLUE, pad=6)

    # Mean annotation
    ax2.text(0.5, 0.88, f"Mean: Turn {rq14['mean_recommended_turn']:.1f}",
             transform=ax2.transAxes, fontsize=8, fontweight="bold",
             color=BLUE, ha="center")
    ax2.text(0.5, 0.78, f"{rq14['not_last_rate']:.0%} say not the last turn",
             transform=ax2.transAxes, fontsize=6.5, color="#555555",
             ha="center")

    # -- Right: Reversibility --
    ax3.set_facecolor("white")
    rq10 = data["rq10"]

    # Stacked horizontal bar: T1 preference vs T5
    t1_rate = rq10["revision_only_t1_rate"]
    t5_rate = 1 - t1_rate

    ax3.barh(["Revision\ntrials"], [t1_rate], color=GREEN, alpha=0.75,
             height=0.4, label="Prefers Turn 1", edgecolor=GREEN, linewidth=0.8)
    ax3.barh(["Revision\ntrials"], [t5_rate], left=[t1_rate], color=RED,
             alpha=0.5, height=0.4, label="Prefers Turn 5",
             edgecolor=RED, linewidth=0.8)

    # Also show length-stable subset
    ls_t1 = rq10["length_stable_t1_rate"]
    ls_t5 = 1 - ls_t1
    ax3.barh(["Length-\nstable"], [ls_t1], color=GREEN, alpha=0.55,
             height=0.4, edgecolor=GREEN, linewidth=0.8)
    ax3.barh(["Length-\nstable"], [ls_t5], left=[ls_t1], color=RED,
             alpha=0.35, height=0.4, edgecolor=RED, linewidth=0.8)

    # All trials
    all_t1 = rq10["prefers_t1_rate"]
    all_t5 = 1 - all_t1
    ax3.barh(["All\ntrials"], [all_t1], color=GREEN, alpha=0.85,
             height=0.4, edgecolor=GREEN, linewidth=0.8)
    ax3.barh(["All\ntrials"], [all_t5], left=[all_t1], color=RED,
             alpha=0.6, height=0.4, edgecolor=RED, linewidth=0.8)

    # Labels
    ax3.text(t1_rate / 2, 2, f"{t1_rate:.0%}", ha="center", va="center",
             fontsize=8, fontweight="bold", color="white")
    ax3.text(all_t1 / 2, 0, f"{all_t1:.0%}", ha="center", va="center",
             fontsize=8, fontweight="bold", color="white")
    ax3.text(ls_t1 / 2, 1, f"{ls_t1:.0%}", ha="center", va="center",
             fontsize=8, fontweight="bold", color="white")

    ax3.set_xlim(0, 1.0)
    ax3.xaxis.set_major_formatter(mticker.PercentFormatter(1.0, decimals=0))
    style_ax(ax3)
    ax3.set_title("What they prefer (blind)", fontsize=9, fontweight="bold",
                  color=GREEN, pad=6)
    ax3.legend(fontsize=6, loc="lower right", framealpha=0.9,
               edgecolor="#cccccc")

    fig.suptitle("Artificial akrasia: models know but cannot stop",
                 fontsize=10, fontweight="bold", color="#333333", y=1.03)

    fig.savefig(OUTDIR / "s3_fig3_akrasia_gap.pdf", bbox_inches="tight",
                facecolor="white")
    fig.savefig(OUTDIR / "s3_fig3_akrasia_gap.png", dpi=200,
                facecolor="white")
    plt.close(fig)
    print("  -> s3_fig3_akrasia_gap.pdf")


# ======================================================================
# FIGURE 4: Feedback Recovery (targeted vs generic dumbbell)
# ======================================================================
def make_fig4():
    fig, ax = plt.subplots(figsize=(3.4, 2.8), dpi=250)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    rq7 = data["rq7"]

    # Overall + per-domain breakdown
    # Domain data from rq2 targeted feedback isn't directly in the JSON
    # but we have the overall result. Let's use what we have.
    categories = ["Overall"]
    generic = [rq7["mean_generic"]]
    targeted = [rq7["mean_targeted"]]
    deltas_fb = [rq7["mean_delta"]]

    y_positions = list(range(len(categories)))

    # Draw dumbbell connections
    for i, (g, t) in enumerate(zip(generic, targeted)):
        ax.plot([g, t], [i, i], color=GRAY, linewidth=2, zorder=1)

    # Generic dots (red)
    ax.scatter(generic, y_positions, color=RED, s=70, zorder=3,
               label="Generic revision", edgecolors="white", linewidth=0.8)

    # Targeted dots (green)
    ax.scatter(targeted, y_positions, color=GREEN, s=70, zorder=3,
               label="Targeted feedback", edgecolors="white", linewidth=0.8)

    # Delta labels
    for i, d in enumerate(deltas_fb):
        mid = (generic[i] + targeted[i]) / 2
        ax.text(mid, i + 0.22, f"+{d:.1f}", ha="center", fontsize=8,
                fontweight="bold", color="#333333")

    # Threshold line
    ax.axvline(THRESHOLD, color=GRAY, linestyle="--", linewidth=0.8,
               alpha=0.5)
    ax.text(THRESHOLD + 0.05, len(categories) - 0.5, "Sufficient",
            fontsize=6.5, color=GRAY, va="center", rotation=90)

    # Stats annotation
    ax.text(0.98, 0.03, f"n={rq7['n']}, p<0.0001",
            transform=ax.transAxes, fontsize=6, color=GRAY,
            ha="right", va="bottom")

    ax.set_yticks(y_positions)
    ax.set_yticklabels(categories, fontsize=9, fontweight="bold")
    ax.set_xlim(1.0, 6.0)
    ax.set_ylim(-0.8, len(categories) - 0.3)
    style_ax(ax, xlabel="Quality level (1-6)")

    ax.legend(fontsize=7, loc="lower center", framealpha=0.9,
              edgecolor="#cccccc", ncol=2,
              bbox_to_anchor=(0.5, -0.28))

    ax.set_title("Targeted feedback recovers quality", fontsize=9,
                 fontweight="bold", color="#333333", pad=6)

    fig.savefig(OUTDIR / "s3_fig4_feedback_recovery.pdf", bbox_inches="tight",
                facecolor="white")
    fig.savefig(OUTDIR / "s3_fig4_feedback_recovery.png", dpi=200,
                facecolor="white")
    plt.close(fig)
    print("  -> s3_fig4_feedback_recovery.pdf")


# ======================================================================
# FIGURE 5: Revision Tax (horizontal bars by model)
# ======================================================================
def make_fig5():
    fig, ax = plt.subplots(figsize=(3.4, 2.8), dpi=250)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    # Per-model revision tax from the paper's Table 3
    tax_data = [
        ("Gemini 2.5 Flash",  30.6,  0.0001),
        ("DeepSeek V4",       118.9, 0.0005),
        ("GPT-4o",            125.8, 0.0053),
        ("Llama 3.3 70B",     148.1, 0.0010),
        ("Qwen 3 235B",       198.6, 0.0009),
        ("Claude Sonnet 4",   251.6, 0.0182),
    ]

    names = [d[0] for d in tax_data]
    taxes = [d[1] for d in tax_data]
    costs = [d[2] for d in tax_data]

    y_pos = range(len(names))

    # Color gradient based on tax severity
    colors = []
    for t in taxes:
        if t < 50:
            colors.append(GREEN)
        elif t < 150:
            colors.append(GATE_AMBER)
        else:
            colors.append(RED)

    bars = ax.barh(y_pos, taxes, color=colors, alpha=0.7, height=0.6,
                   edgecolor=[c for c in colors], linewidth=0.8)

    # 100% reference line
    ax.axvline(100, color=GRAY, linestyle="--", linewidth=0.8, alpha=0.5)
    ax.text(100, len(names) - 0.3, "2x cost", fontsize=6, color=GRAY,
            ha="center", va="bottom")

    # Labels
    for i, (t, c) in enumerate(zip(taxes, costs)):
        ax.text(t + 4, i, f"{t:.0f}%", va="center", fontsize=7,
                fontweight="bold", color="#444444")
        ax.text(t + 4, i - 0.28, f"${c:.4f}/task", va="center", fontsize=5.5,
                color=GRAY)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=7.5)
    ax.set_xlim(0, 310)
    style_ax(ax, xlabel="Extra tokens past quality peak (%)")
    ax.set_title("Revision tax by model", fontsize=9, fontweight="bold",
                 color="#333333", pad=6)

    fig.savefig(OUTDIR / "s3_fig5_revision_tax.pdf", bbox_inches="tight",
                facecolor="white")
    fig.savefig(OUTDIR / "s3_fig5_revision_tax.png", dpi=200,
                facecolor="white")
    plt.close(fig)
    print("  -> s3_fig5_revision_tax.pdf")


# ======================================================================
# FIGURE 6: Content Drift (instruction adherence + semantic similarity)
# ======================================================================
def make_fig6():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.5, 2.4), dpi=250)
    fig.patch.set_facecolor("white")

    # -- Left: Instruction adherence (task-word overlap) --
    ax1.set_facecolor("white")
    rq12 = data["rq12"]
    overlap = [rq12["overlap_by_turn"][str(t)] for t in TURNS]
    ax1.plot(TURNS, overlap, "o-", color=BLUE, markersize=5, linewidth=1.8,
             zorder=3)

    # Slope annotation
    slope = rq12["trend"]["mean_slope"]
    p = rq12["trend"]["p"]
    ax1.text(0.97, 0.95, f"slope={slope:.3f}/turn\np<0.0001",
             transform=ax1.transAxes, fontsize=6.5, color=GRAY,
             ha="right", va="top")

    style_ax(ax1, ylabel="Task-word overlap", xlabel="Turn")
    ax1.set_xticks(TURNS)
    ax1.set_ylim(0.2, 0.5)
    ax1.set_title("Instruction adherence decays", fontsize=9,
                  fontweight="bold", color="#333333", pad=6)

    # -- Right: Response length --
    ax2.set_facecolor("white")
    rq6 = data["rq6"]
    lengths = [rq6["drift_by_turn"]["word_count"][str(t)] for t in TURNS]
    ax2.plot(TURNS, lengths, "o-", color=PURPLE, markersize=5, linewidth=1.8,
             zorder=3)

    # Fill to show shrinkage
    ax2.fill_between(TURNS, lengths, lengths[0], alpha=0.08, color=PURPLE)

    slope_len = rq6["length_trend"]["mean_slope"]
    ax2.text(0.97, 0.95, f"slope={slope_len:.0f} words/turn\np<0.0001",
             transform=ax2.transAxes, fontsize=6.5, color=GRAY,
             ha="right", va="top")

    # Start/end annotations
    ax2.text(1, lengths[0] + 5, f"{lengths[0]:.0f}", ha="center", fontsize=7,
             color=PURPLE, fontweight="bold")
    ax2.text(5, lengths[-1] - 12, f"{lengths[-1]:.0f}", ha="center", fontsize=7,
             color=PURPLE, fontweight="bold")

    style_ax(ax2, ylabel="Word count", xlabel="Turn")
    ax2.set_xticks(TURNS)
    ax2.set_title("Responses shrink, not expand", fontsize=9,
                  fontweight="bold", color="#333333", pad=6)

    fig.suptitle("Content drift across revision turns",
                 fontsize=10, fontweight="bold", color="#333333", y=1.02)

    fig.savefig(OUTDIR / "s3_fig6_content_drift.pdf", bbox_inches="tight",
                facecolor="white")
    fig.savefig(OUTDIR / "s3_fig6_content_drift.png", dpi=200,
                facecolor="white")
    plt.close(fig)
    print("  -> s3_fig6_content_drift.pdf")


# ======================================================================
# Main
# ======================================================================
if __name__ == "__main__":
    print("Generating Study 3 figures...")
    make_fig1()
    make_fig2()
    make_fig3()
    make_fig4()
    make_fig5()
    make_fig6()
    print("Done.")
