#!/usr/bin/env python3
"""Companion chart for fig1: token cost (exponential up) vs quality (linear down).
Minimal, cartoonish style - no axis numbers, just labels and lines."""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

WHITE = "#FFFFFF"
DARK = "#222222"
GRAY = "#AAAAAA"

COST_COL = "#E53935"
QUAL_COL = "#2E7D32"

# Smooth curves - start slightly off the axes
t = np.linspace(0.04, 1, 100)

# Quality: linear decline
quality = 0.95 - 0.82 * (t - 0.04) / 0.96

# Token cost: exponential rise
t_norm = (t - 0.04) / 0.96
cost = 0.1 + 0.88 * (np.exp(2.5 * t_norm) - 1) / (np.exp(2.5) - 1)

fig, ax = plt.subplots(figsize=(4.0, 2.5), dpi=250)
fig.patch.set_facecolor(WHITE)
ax.set_facecolor(WHITE)

# Draw full clean lines
ax.plot(t, quality, color=QUAL_COL, linewidth=3, solid_capstyle="round", zorder=5)
ax.plot(t, cost, color=COST_COL, linewidth=3, solid_capstyle="round", zorder=5)

# Labels with arrows built into the text
ax.text(1.04, quality[-1], "Response Quality  \u2193", fontsize=8, color=QUAL_COL,
        va="center", ha="left", fontweight="bold")
ax.text(1.04, cost[-1], "Token Cost  \u2191", fontsize=8, color=COST_COL,
        va="center", ha="left", fontweight="bold")

# Minimal axis labels
ax.set_xlim(-0.02, 1.38)
ax.set_ylim(-0.05, 1.1)

# Axes as plain lines meeting at corner, with arrowheads at tips only
ax.plot([0, 1.05], [0, 0], color=DARK, linewidth=1.5, solid_capstyle="butt", zorder=4)
ax.plot([0, 0], [0, 1.08], color=DARK, linewidth=1.5, solid_capstyle="butt", zorder=4)
# Arrowheads at tips
ax.annotate("", xy=(1.07, 0), xytext=(1.02, 0),
            arrowprops=dict(arrowstyle="-|>", color=DARK, linewidth=1.5, mutation_scale=10))
ax.annotate("", xy=(0, 1.1), xytext=(0, 1.05),
            arrowprops=dict(arrowstyle="-|>", color=DARK, linewidth=1.5, mutation_scale=10))


ax.text(0.5, -0.06, "Revision Turns", fontsize=8, color=DARK,
        ha="center", va="top")

# Remove all spines and ticks
ax.set_xticks([])
ax.set_yticks([])
for sp in ax.spines.values():
    sp.set_visible(False)

plt.tight_layout()

out_dir = Path(__file__).resolve().parent
fig.savefig(out_dir / "fig1_chart.pdf", bbox_inches="tight",
            facecolor=WHITE, edgecolor="none")
fig.savefig(out_dir / "fig1_chart.png", bbox_inches="tight",
            facecolor=WHITE, edgecolor="none")
print("Saved fig1_chart.pdf and .png")
plt.close(fig)
