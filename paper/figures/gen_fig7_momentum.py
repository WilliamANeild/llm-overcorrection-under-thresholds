"""
Figure 7: Momentum Step Function -- GPT-4o's Dramatic Shift
ACL publication-ready figure.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
doses = [-1, 0, 1, 2, 3]

gpt4o   = [1.0,  31.4, 98.4, 99.5, 97.4]
claude  = [21.9, 38.0, 38.0, 27.1, 24.5]
gemini  = [0.0,   0.3, 12.8,  9.9,  8.6]

x_labels = [
    "Reverse\n(affirm)",
    "No\nhistory",
    "+1\nround",
    "+2\nrounds",
    "+3\nrounds",
]

# ---------------------------------------------------------------------------
# Colors / styles
# ---------------------------------------------------------------------------
C_GPT    = "#C44E52"
C_CLAUDE = "#4878A8"
C_GEMINI = "#8C8C8C"

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(doses, gpt4o,  color=C_GPT,    linewidth=2.5, marker="o", markersize=7,
        zorder=3, label="GPT-4o")
ax.plot(doses, claude, color=C_CLAUDE,  linewidth=1.5, marker="s", markersize=6,
        zorder=2, label="Claude Sonnet 4")
ax.plot(doses, gemini, color=C_GEMINI,  linewidth=1.5, marker="^", markersize=6,
        zorder=2, label="Gemini 2.5 Flash")

# ---------------------------------------------------------------------------
# Direct labels at line ends (right side)
# ---------------------------------------------------------------------------
ax.text(3.12, 97.4, "GPT-4o",            fontsize=8.5, color=C_GPT,
        va="center", fontweight="bold")
ax.text(3.12, 24.5, "Claude\nSonnet 4",  fontsize=8, color=C_CLAUDE,
        va="center")
ax.text(3.12, 8.6,  "Gemini\n2.5 Flash", fontsize=8, color=C_GEMINI,
        va="center")

# ---------------------------------------------------------------------------
# Annotate GPT-4o jump (dose 0 -> dose 1)
# ---------------------------------------------------------------------------
ax.annotate(
    "31% \u2192 98%",
    xy=(1, 98.4),
    xytext=(0.15, 72),
    fontsize=9,
    fontweight="bold",
    color=C_GPT,
    arrowprops=dict(
        arrowstyle="->,head_width=0.3,head_length=0.15",
        color=C_GPT,
        lw=1.3,
        connectionstyle="arc3,rad=-0.2",
    ),
    zorder=4,
)

# ---------------------------------------------------------------------------
# Annotate reverse-momentum region
# ---------------------------------------------------------------------------
ax.annotate(
    "Affirmative\nfeedback",
    xy=(-1, 1.0),
    xytext=(-0.85, 18),
    fontsize=8,
    color="#555555",
    fontstyle="italic",
    arrowprops=dict(
        arrowstyle="->,head_width=0.25,head_length=0.12",
        color="#999999",
        lw=1.0,
    ),
    zorder=4,
)

# ---------------------------------------------------------------------------
# Axes
# ---------------------------------------------------------------------------
ax.set_xticks(doses)
ax.set_xticklabels(x_labels, fontsize=9)
ax.set_xlim(-1.4, 3.8)
ax.set_ylim(-3, 108)
ax.set_ylabel("Revision Rate (%)", fontsize=11)
ax.yaxis.set_major_locator(mticker.MultipleLocator(25))
ax.yaxis.set_minor_locator(mticker.MultipleLocator(12.5))

# Remove spines & gridlines
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#CCCCCC")
ax.spines["bottom"].set_color("#CCCCCC")
ax.tick_params(colors="#555555", labelsize=9)

# White background, no grid
ax.set_facecolor("white")
fig.patch.set_facecolor("white")

# ---------------------------------------------------------------------------
# Title / subtitle
# ---------------------------------------------------------------------------
ax.set_title(
    "One Prior Revision Locks GPT-4o Into Compliance",
    fontsize=14,
    fontweight="bold",
    pad=22,
)
ax.text(
    0.5, 1.04,
    "Revision rate at evaluative probe by conversational history",
    transform=ax.transAxes,
    ha="center",
    fontsize=11,
    color="#777777",
)

plt.tight_layout()

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
out_base = "/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/figures/fig7_momentum"
fig.savefig(out_base + ".pdf", dpi=300, bbox_inches="tight", facecolor="white")
fig.savefig(out_base + ".png", dpi=300, bbox_inches="tight", facecolor="white")
print(f"Saved {out_base}.pdf and .png")
plt.close()
