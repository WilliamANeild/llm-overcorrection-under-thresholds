#!/usr/bin/env python3
"""Figure 4: What Revision Actually Does (Content Drift Multi-Panel).

2x2 grid showing 4 ways revision destroys content:
  Top-left: Instruction adherence decay (task-word overlap)
  Top-right: Semantic similarity to T1 (drift from original)
  Bottom-left: Word count collapse
  Bottom-right: Edit ratio flatline at ~0.97
"""

import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# -- Load data --
ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS = ROOT / "data" / "study3" / "analysis" / "study3_results.json"
with open(RESULTS) as f:
    data = json.load(f)

TURNS = [1, 2, 3, 4, 5]
BLUE = "#4878A8"
RED = "#C44E52"
PURPLE = "#8172B2"
GREEN = "#55A868"
GRAY = "#8C8C8C"

# Data sources
rq12 = data["rq12"]  # instruction adherence
sem = data["semantic_similarity"]  # semantic drift
rq6 = data["rq6"]  # word count
eff = data["revision_efficiency"]  # edit ratio

# -- Figure --
fig, axes = plt.subplots(2, 2, figsize=(6, 4), dpi=250)
fig.patch.set_facecolor("white")

def style_panel(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#444444")
    ax.spines["bottom"].set_color("#444444")
    ax.tick_params(colors="#444444", labelsize=7)
    ax.set_xticks(TURNS)
    ax.grid(False)

# == Top-left: Instruction adherence ==
ax = axes[0, 0]
ax.set_facecolor("white")
overlap = [rq12["overlap_by_turn"][str(t)] for t in TURNS]
ax.plot(TURNS, overlap, "o-", color=BLUE, markersize=5, linewidth=1.8, zorder=3)
ax.fill_between(TURNS, overlap, overlap[0], alpha=0.08, color=BLUE)

# Start/end labels
ax.text(1, overlap[0] + 0.012, f"{overlap[0]:.2f}", ha="center", fontsize=7,
        color=BLUE, fontweight="bold")
ax.text(5, overlap[-1] - 0.018, f"{overlap[-1]:.2f}", ha="center", fontsize=7,
        color=BLUE, fontweight="bold")

slope = rq12["trend"]["mean_slope"]
ax.text(0.97, 0.08, f"slope = {slope:.3f}/turn\np < 0.0001",
        transform=ax.transAxes, fontsize=6, color=GRAY, ha="right", va="bottom")

style_panel(ax)
ax.set_ylabel("Task-word overlap", fontsize=8, color="#333333")
ax.set_title("Instruction adherence decays", fontsize=9, fontweight="bold",
             color="#333333", pad=6)
ax.set_ylim(0.25, 0.48)

# == Top-right: Semantic similarity to T1 ==
ax = axes[0, 1]
ax.set_facecolor("white")
# T1 similarity to itself is 1.0, then drift
sim_from_t1 = [1.0] + [sem["drift_from_t1"][str(t)] for t in [2, 3, 4, 5]]
ax.plot(TURNS, sim_from_t1, "o-", color=PURPLE, markersize=5, linewidth=1.8, zorder=3)
ax.fill_between(TURNS, sim_from_t1, sim_from_t1[-1], alpha=0.08, color=PURPLE)

ax.text(1, sim_from_t1[0] + 0.02, "1.00", ha="center", fontsize=7,
        color=PURPLE, fontweight="bold")
ax.text(5, sim_from_t1[-1] - 0.04, f"{sim_from_t1[-1]:.2f}", ha="center",
        fontsize=7, color=PURPLE, fontweight="bold")

drift_slope = sem["drift_trend"]["mean_slope"]
ax.text(0.97, 0.08, f"slope = {drift_slope:.3f}/turn\np < 0.0001",
        transform=ax.transAxes, fontsize=6, color=GRAY, ha="right", va="bottom")

# Annotation: 63% content change by T5
ax.text(0.5, 0.5, f"{1 - sim_from_t1[-1]:.0%} content\ndrift by T5",
        transform=ax.transAxes, fontsize=8, color=PURPLE, ha="center",
        fontweight="bold", alpha=0.7)

style_panel(ax)
ax.set_ylabel("Cosine similarity to T1", fontsize=8, color="#333333")
ax.set_title("Semantic drift from original", fontsize=9, fontweight="bold",
             color="#333333", pad=6)
ax.set_ylim(0.25, 1.1)

# == Bottom-left: Word count collapse ==
ax = axes[1, 0]
ax.set_facecolor("white")
wc = [rq6["drift_by_turn"]["word_count"][str(t)] for t in TURNS]
ax.plot(TURNS, wc, "o-", color=RED, markersize=5, linewidth=1.8, zorder=3)
ax.fill_between(TURNS, wc, wc[-1], alpha=0.08, color=RED)

ax.text(1, wc[0] + 8, f"{wc[0]:.0f}", ha="center", fontsize=7,
        color=RED, fontweight="bold")
ax.text(5, wc[-1] - 12, f"{wc[-1]:.0f}", ha="center", fontsize=7,
        color=RED, fontweight="bold")

len_slope = rq6["length_trend"]["mean_slope"]
ax.text(0.97, 0.92, f"slope = {len_slope:.0f} words/turn\np < 0.0001",
        transform=ax.transAxes, fontsize=6, color=GRAY, ha="right", va="top")

style_panel(ax)
ax.set_ylabel("Word count", fontsize=8, color="#333333")
ax.set_xlabel("Turn", fontsize=8, color="#333333")
ax.set_title("Responses shrink each turn", fontsize=9, fontweight="bold",
             color="#333333", pad=6)
ax.set_ylim(140, 330)

# == Bottom-right: Edit ratio ==
ax = axes[1, 1]
ax.set_facecolor("white")
edit_ratios = [1.0] + [eff["by_turn"][str(t)]["edit_ratio"] for t in [2, 3, 4, 5]]
ax.plot(TURNS, edit_ratios, "o-", color=GREEN, markersize=5, linewidth=1.8, zorder=3)

# Reference line at 1.0 (complete rewrite)
ax.axhline(1.0, ls=":", lw=1.0, color=GRAY, alpha=0.5, zorder=1)
ax.text(5.1, 1.0, "Complete\nrewrite", fontsize=6, color=GRAY, va="center")

# Mean annotation
mean_er = eff["mean_edit_ratio"]
ax.axhline(mean_er, ls="--", lw=1.0, color=GREEN, alpha=0.5, zorder=1)
ax.text(0.5, 0.3, f"Mean: {mean_er:.2f}\n(97% rewrite every turn)",
        transform=ax.transAxes, fontsize=8, color=GREEN, ha="center",
        fontweight="bold")

style_panel(ax)
ax.set_ylabel("Edit ratio (0=no change, 1=rewrite)", fontsize=7, color="#333333")
ax.set_xlabel("Turn", fontsize=8, color="#333333")
ax.set_title("Models rewrite, not edit", fontsize=9, fontweight="bold",
             color="#333333", pad=6)
ax.set_ylim(0.92, 1.02)

# Caveat annotation
ax.text(0.97, 0.02, "Note: partly reflects\ntemperature-1.0 sampling",
        transform=ax.transAxes, fontsize=6, color=GRAY, ha="right", va="bottom",
        style="italic")

# Suptitle
fig.suptitle("What Revision Actually Does to Your Output",
             fontsize=12, fontweight="bold", color="#222222", y=1.02)

# Save
out_dir = Path(__file__).resolve().parent
fig.tight_layout()
fig.savefig(out_dir / "fig4_content_drift.pdf", bbox_inches="tight")
fig.savefig(out_dir / "fig4_content_drift.png", bbox_inches="tight")
print("Saved fig4_content_drift.pdf and .png")
plt.close(fig)
