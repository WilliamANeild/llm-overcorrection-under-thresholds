#!/usr/bin/env python3
"""Figure 1: The Revision Cliff (HERO FIGURE).

Shows quality trajectory over 5 turns using the balanced panel (n=135).
Key visual: dramatic cliff from T1 to T2, red shaded area below threshold.
"""

import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.collections import LineCollection
from pathlib import Path

# -- Load data --
ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS = ROOT / "data" / "study3" / "analysis" / "study3_results.json"
with open(RESULTS) as f:
    data = json.load(f)

# Balanced panel (n=135, all trials that survive to T5)
balanced = data["edge_cases"]["cohort_trajectories"]["balanced"]["trajectory"]
n_balanced = data["edge_cases"]["cohort_trajectories"]["balanced"]["n_trials"]

# Also get pooled revision-only for comparison
rq1 = data["rq1"]

TURNS = [1, 2, 3, 4, 5]
means_balanced = [balanced[str(t)]["mean"] for t in TURNS]
means_pooled = [rq1["revision_only_level_by_turn"][str(t)] for t in TURNS]

# -- Colours --
BLUE = "#4878A8"
RED = "#C44E52"
GRAY = "#8C8C8C"
PURPLE = "#8172B2"
THRESHOLD = 4.0

# -- Figure --
fig, ax = plt.subplots(figsize=(6, 4), dpi=250)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Gradient line for balanced panel (primary)
cmap = mcolors.LinearSegmentedColormap.from_list("cliff", [BLUE, RED])
n_interp = 300
t_fine = np.linspace(1, 5, n_interp)
m_fine = np.interp(t_fine, TURNS, means_balanced)

points = np.array([t_fine, m_fine]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
norm = plt.Normalize(1, 5)
lc = LineCollection(segments, cmap=cmap, norm=norm, linewidths=3.2, zorder=3)
lc.set_array(t_fine[:-1])
ax.add_collection(lc)

# Red shaded region below threshold
cross_t = np.interp(THRESHOLD, m_fine[::-1], t_fine[::-1])
fill_mask = t_fine >= cross_t
t_fill = np.concatenate([[cross_t], t_fine[fill_mask]])
m_fill = np.concatenate([[THRESHOLD], m_fine[fill_mask]])
ax.fill_between(t_fill, m_fill, THRESHOLD, alpha=0.12, color=RED, zorder=1)

# Pooled revision-only (lighter, dashed comparison)
ax.plot(TURNS, means_pooled, "D--", color=PURPLE, markersize=4, linewidth=1.4,
        alpha=0.6, label="Pooled revision-only", zorder=2)

# Threshold line
ax.axhline(THRESHOLD, ls="--", lw=1.2, color=GRAY, zorder=2)
ax.text(5.08, THRESHOLD, "Sufficient", va="center", ha="left",
        fontsize=8.5, color=GRAY, style="italic")

# Dot markers at each turn (balanced panel)
colours = [cmap(norm(t)) for t in TURNS]
for t, m, c in zip(TURNS, means_balanced, colours):
    ax.plot(t, m, "o", color=c, markersize=7, zorder=4,
            markeredgecolor="white", markeredgewidth=1.0)

# Bold annotations at T1 and T5
ax.annotate(f"{means_balanced[0]:.2f}", (1, means_balanced[0]),
            textcoords="offset points", xytext=(0, 14), ha="center",
            fontsize=12, fontweight="bold", color=BLUE, zorder=5)
ax.annotate(f"{means_balanced[4]:.2f}", (5, means_balanced[4]),
            textcoords="offset points", xytext=(0, -16), ha="center",
            fontsize=12, fontweight="bold", color=RED, zorder=5)

# Per-turn delta annotations
for i in range(4):
    delta = means_balanced[i + 1] - means_balanced[i]
    t_mid = TURNS[i] + 0.5
    y_mid = (means_balanced[i] + means_balanced[i + 1]) / 2
    ax.text(t_mid, y_mid + 0.18, f"{delta:+.2f}", ha="center", va="bottom",
            fontsize=7.5, color=RED, fontweight="bold", zorder=5)

# Crossing-point annotation
ax.annotate("Falls below threshold\nafter 1 revision",
            xy=(cross_t, THRESHOLD),
            xytext=(cross_t + 1.05, THRESHOLD + 0.55),
            fontsize=7.5, color=GRAY, ha="left",
            arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.9),
            zorder=5)

# Key number callout box
total_drop = means_balanced[0] - means_balanced[4]
ax.text(0.97, 0.92, f"-{total_drop:.2f} levels over 5 turns",
        transform=ax.transAxes, fontsize=9, fontweight="bold",
        color=RED, ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#FDECEA",
                  edgecolor=RED, alpha=0.8))

# Legend - add balanced panel as a manual entry for the gradient line
from matplotlib.lines import Line2D
legend_handles = [
    Line2D([0], [0], color=BLUE, linewidth=2.5, label=f"Balanced panel (n={n_balanced})"),
    Line2D([0], [0], color=PURPLE, linewidth=1.4, linestyle="--", marker="D",
           markersize=4, alpha=0.6, label="Pooled revision-only"),
]
ax.legend(handles=legend_handles, fontsize=7, loc="lower left", framealpha=0.9, edgecolor="#cccccc")

# Axes styling
ax.set_xlim(0.6, 5.55)
ax.set_ylim(1.5, 5.2)
ax.set_xticks(TURNS)
ax.set_xticklabels([str(t) for t in TURNS], fontsize=10)
ax.set_yticks([2, 3, 4, 5])
ax.set_yticklabels(["2\nIncomplete", "3\nBasic", "4\nSufficient", "5\nPolished"],
                   fontsize=8)
ax.set_xlabel("Revision Turn", fontsize=11, labelpad=6)
ax.set_ylabel("Quality Level", fontsize=11, labelpad=6)

ax.grid(False)
ax.yaxis.grid(True, alpha=0.3, color='#cccccc', linewidth=0.5)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#444444")
ax.spines["bottom"].set_color("#444444")
ax.tick_params(colors="#444444", length=4)

# Title
ax.set_title("Each Revision Makes It Worse", fontsize=16, fontweight="bold",
             pad=18, color="#222222")
ax.text(0.5, 1.04, f"Balanced panel: {n_balanced} trials surviving all 5 turns",
        transform=ax.transAxes, ha="center", fontsize=10, color=GRAY)

# Save
out_dir = Path(__file__).resolve().parent
fig.tight_layout(rect=[0, 0, 0.95, 1])
fig.savefig(out_dir / "fig1_revision_cliff.pdf", bbox_inches="tight")
fig.savefig(out_dir / "fig1_revision_cliff.png", bbox_inches="tight")
print("Saved fig1_revision_cliff.pdf and .png")
plt.close(fig)
