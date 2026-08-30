#!/usr/bin/env python3
"""Figure 5: The Fix (Targeted Feedback vs Generic Revision).

Dumbbell/lollipop chart showing the dramatic difference between
generic "improve this" (-1.11) and targeted feedback (+2.0).
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

rq7 = data["rq7"]
rq1 = data["rq1"]

# Key numbers
mean_generic = rq7["mean_generic"]   # 2.74
mean_targeted = rq7["mean_targeted"]  # 4.74
delta = rq7["mean_delta"]             # +2.0
n = rq7["n"]                          # 424
p = rq7["wilcoxon_p"]

# Generic revision delta (from T1)
t1_quality = rq1["revision_only_level_by_turn"]["1"]  # 4.34
t2_quality = rq1["revision_only_level_by_turn"]["2"]  # 3.23
generic_delta = t2_quality - t1_quality  # -1.11

BLUE = "#4878A8"
ORANGE = "#E8833A"
GRAY = "#8C8C8C"
THRESHOLD = 4.0

# -- Figure --
fig, ax = plt.subplots(figsize=(6, 3.5), dpi=250)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Y positions
y_main = 1.5
y_detail = 0.5

# == Main dumbbell: Generic vs Targeted ==
# Connection line
ax.plot([mean_generic, mean_targeted], [y_main, y_main],
        color=GRAY, linewidth=3, zorder=1, solid_capstyle="round")

# Generic dot (red)
ax.scatter([mean_generic], [y_main], color=ORANGE, s=150, zorder=3,
           edgecolors="white", linewidth=1.5)
ax.text(mean_generic, y_main - 0.3, f"{mean_generic:.2f}",
        ha="center", fontsize=10, fontweight="bold", color=ORANGE)
ax.text(mean_generic, y_main + 0.3, "Generic\nrevision",
        ha="center", fontsize=8, color=ORANGE, va="bottom")

# Targeted dot (green)
ax.scatter([mean_targeted], [y_main], color=BLUE, s=150, zorder=3,
           edgecolors="white", linewidth=1.5)
ax.text(mean_targeted, y_main - 0.3, f"{mean_targeted:.2f}",
        ha="center", fontsize=10, fontweight="bold", color=BLUE)
ax.text(mean_targeted, y_main + 0.3, "Targeted\nfeedback",
        ha="center", fontsize=8, color=BLUE, va="bottom")

# Delta label in middle
mid = (mean_generic + mean_targeted) / 2
ax.text(mid, y_main + 0.15, f"+{delta:.1f} levels",
        ha="center", fontsize=11, fontweight="bold", color="#333333",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                  edgecolor="#cccccc", alpha=0.9))

# == Threshold line ==
ax.axvline(THRESHOLD, color=GRAY, linestyle="--", linewidth=1.0, alpha=0.6)
ax.text(THRESHOLD + 0.05, 2.2, "Sufficient\nthreshold",
        fontsize=7, color=GRAY, va="bottom", rotation=0)

# == Lower detail: what "generic revision" means ==
ax.annotate("", xy=(mean_generic, y_detail), xytext=(t1_quality, y_detail),
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.5))
ax.scatter([t1_quality], [y_detail], color="#4878A8", s=80, zorder=3,
           edgecolors="white", linewidth=1.0)
ax.text(t1_quality, y_detail + 0.2, f"T1: {t1_quality:.2f}",
        ha="center", fontsize=7, color="#4878A8")
ax.text((t1_quality + mean_generic) / 2, y_detail - 0.2,
        f"{generic_delta:+.2f} (one generic revision)",
        ha="center", fontsize=7, color=ORANGE, style="italic")

# == Stats annotation ==
ax.text(0.98, 0.03, f"n = {n}, p < 0.0001 (Wilcoxon signed-rank)",
        transform=ax.transAxes, fontsize=6.5, color=GRAY,
        ha="right", va="bottom")

# == Key insight ==
ax.text(0.5, 1.08,
        "The problem is not revision capacity. It is the absence of direction.",
        transform=ax.transAxes, fontsize=9, ha="center", va="top",
        color="#333333", style="italic")

# Axes
ax.set_xlim(1.5, 5.8)
ax.set_ylim(-0.2, 2.6)
ax.set_xlabel("Quality Level (1-6 scale)", fontsize=10, labelpad=8)
ax.set_yticks([])

ax.grid(False)
ax.yaxis.grid(True, alpha=0.3, color='#cccccc', linewidth=0.5)
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#444444")
ax.tick_params(colors="#444444", length=4, labelsize=9)

ax.set_title("Targeted Feedback Recovers Quality",
             fontsize=14, fontweight="bold", pad=12, color="#222222")

# Save
out_dir = Path(__file__).resolve().parent
fig.tight_layout()
fig.savefig(out_dir / "fig5_feedback_fix.pdf", bbox_inches="tight")
fig.savefig(out_dir / "fig5_feedback_fix.png", bbox_inches="tight")
print("Saved fig5_feedback_fix.pdf and .png")
plt.close(fig)
