"""
Figure 4: The Revision Tax -- horizontal bar chart showing wasted tokens by model.
Publication-ready for ACL.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Data sorted by revision tax (descending)
models = [
    "Claude Sonnet 4",
    "Qwen 3 235B",
    "Llama 3.3 70B",
    "GPT-4o",
    "DeepSeek V4",
    "Gemini 2.5 Flash",
]
tax_pct = [251.6, 198.6, 148.1, 125.8, 118.9, 30.6]
cost_per_task = [0.0182, 0.0053, 0.0010, 0.0009, 0.0005, 0.0001]

# Reverse for bottom-to-top plotting (highest at top)
models = models[::-1]
tax_pct = tax_pct[::-1]
cost_per_task = cost_per_task[::-1]

# Color gradient: pale salmon (lowest) to deep red (highest)
deep_red = np.array([0.769, 0.306, 0.322])   # #C44E52
pale_salmon = np.array([0.976, 0.808, 0.812]) # #F9CECFish
n = len(models)
colors = [tuple(pale_salmon + (deep_red - pale_salmon) * (i / (n - 1))) for i in range(n)]

# Figure setup
fig, ax = plt.subplots(figsize=(7, 4))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

bars = ax.barh(range(n), tax_pct, color=colors, edgecolor="none", height=0.62)

# Y-axis model labels
ax.set_yticks(range(n))
ax.set_yticklabels(models, fontsize=10)

# X-axis
ax.set_xlabel("Extra Tokens Past Quality Peak (%)", fontsize=10, labelpad=8)
ax.xaxis.set_major_formatter(mticker.PercentFormatter(decimals=0))

# Remove all spines except bottom
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#CCCCCC")

# Remove gridlines and ticks
ax.tick_params(axis="y", length=0)
ax.tick_params(axis="x", colors="#666666", labelsize=9)
ax.set_xlim(0, 340)

# 100% reference line
ax.axvline(x=100, color="#999999", linestyle="--", linewidth=1, zorder=0)
ax.text(100, n - 0.15, "Doubles the cost", fontsize=8, color="#999999",
        ha="center", va="bottom", style="italic")

# Bar-end labels (percentage) and cost annotations
for i, (bar, pct, cost) in enumerate(zip(bars, tax_pct, cost_per_task)):
    # Percentage label at bar end
    ax.text(pct + 3, i, f"{pct:.0f}%", va="center", ha="left",
            fontsize=9.5, fontweight="bold", color="#333333")
    # Cost annotation (right-aligned)
    ax.text(330, i, f"${cost:.4f}/task", va="center", ha="right",
            fontsize=8, color="#999999")

# Title and subtitle
ax.set_title("The Revision Tax", fontsize=16, fontweight="bold",
             loc="left", pad=20, color="#222222")
fig.text(0.125, 0.92, "Additional tokens spent for zero or negative quality return",
         fontsize=11, color="#888888", ha="left")

plt.tight_layout(rect=[0, 0, 1, 0.90])

# Save
out_base = "/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/figures/fig4_revision_tax"
fig.savefig(f"{out_base}.pdf", dpi=300, bbox_inches="tight", facecolor="white")
fig.savefig(f"{out_base}.png", dpi=300, bbox_inches="tight", facecolor="white")
print(f"Saved to {out_base}.pdf and .png")
plt.close()
