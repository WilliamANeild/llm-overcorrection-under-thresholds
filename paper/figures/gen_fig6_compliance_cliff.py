"""
Figure 6 -- The Compliance Cliff
Study 1 probe compliance: revision rate by follow-up prompt phrasing.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────
labels = [
    "Can this be\nimproved?",
    "Anything\nto change?",
    "Take another\nlook...",
    "Review against\nthreshold...",
    "What do\nyou think?",
]
rates = [100, 100, 23, 12, 2]

# ── Colours ───────────────────────────────────────────────────────────
red = "#C44E52"
blue = "#4878A8"
colors = [red, red, blue, blue, blue]

# ── Layout: positions with a gap between groups ───────────────────────
positions = [0, 1, 2.4, 3.4, 4.4]

# ── Figure ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 4))

bars = ax.bar(positions, rates, width=0.72, color=colors, edgecolor="white",
              linewidth=0.6, zorder=3)

# Bar-top labels
for pos, rate in zip(positions, rates):
    ax.text(pos, rate + 2.5, f"{rate}%", ha="center", va="bottom",
            fontsize=10, fontweight="bold", color="#333333")

# ── Axes ──────────────────────────────────────────────────────────────
ax.set_ylim(0, 115)
ax.set_ylabel("Revision Rate (%)", fontsize=10, labelpad=8)
ax.set_xticks(positions)
ax.set_xticklabels(labels, fontsize=8, ha="center")
ax.tick_params(axis="x", length=0, pad=6)
ax.tick_params(axis="y", labelsize=9)

# Remove spines and gridlines
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#CCCCCC")
ax.spines["bottom"].set_color("#CCCCCC")
ax.yaxis.grid(True, alpha=0.3, color='#cccccc', linewidth=0.5)

# ── Group brackets / annotations ─────────────────────────────────────
bracket_y = 110

# "Revision-implying" bracket over first two bars
ax.annotate("", xy=(positions[0] - 0.4, bracket_y),
            xytext=(positions[1] + 0.4, bracket_y),
            arrowprops=dict(arrowstyle="-", color=red, lw=1.5))
ax.text(np.mean(positions[0:2]), bracket_y + 2, "Revision-implying",
        ha="center", va="bottom", fontsize=8.5, color=red, fontstyle="italic")

# "Evaluative" bracket over last three bars
ax.annotate("", xy=(positions[2] - 0.4, bracket_y),
            xytext=(positions[4] + 0.4, bracket_y),
            arrowprops=dict(arrowstyle="-", color=blue, lw=1.5))
ax.text(np.mean(positions[2:5]), bracket_y + 2, "Evaluative",
        ha="center", va="bottom", fontsize=8.5, color=blue, fontstyle="italic")

# ── Title / subtitle ─────────────────────────────────────────────────
ax.set_title("The Compliance Cliff", fontsize=14, fontweight="bold",
             pad=32, loc="center")
fig.text(0.5, 0.91, "Revision rate by follow-up prompt phrasing",
         ha="center", fontsize=11, color="gray")

# ── White background, tight layout ───────────────────────────────────
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
fig.tight_layout(rect=[0, 0, 1, 0.89])

# ── Save ──────────────────────────────────────────────────────────────
out = "/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/figures/"
fig.savefig(out + "fig6_compliance_cliff.pdf", dpi=300, bbox_inches="tight",
            facecolor="white")
fig.savefig(out + "fig6_compliance_cliff.png", dpi=300, bbox_inches="tight",
            facecolor="white")
print("Saved fig6_compliance_cliff.pdf and .png")
