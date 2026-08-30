#!/usr/bin/env python3
"""Figure 6: The Revision Tax (Economic Cost).

Horizontal bar chart showing real dollar cost of undirected revision
across models and pricing tiers.
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

rq16 = data["rq16"]

# Model data sorted by revision tax
models = [
    ("gemini-2.5-flash", "Gemini 2.5 Flash", "$0.15/MTok"),
    ("deepseek-v4", "DeepSeek V4", "$0.55/MTok"),
    ("gpt-4o", "GPT-4o", "$10.00/MTok"),
    ("llama-3.3-70b", "Llama 3.3 70B", "$0.88/MTok"),
    ("qwen-3-235b", "Qwen 3 235B", "$0.90/MTok"),
    ("claude-sonnet-4", "Claude Sonnet 4", "$15.00/MTok"),
]

# Sort by tax
models_sorted = sorted(models, key=lambda x: rq16[x[0]]["revision_tax_pct"])

BLUE = "#4878A8"
AMBER = "#F39C12"
ORANGE = "#E8833A"
GRAY = "#8C8C8C"

# -- Figure --
fig, ax = plt.subplots(figsize=(6.5, 3.5), dpi=250)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

names = []
taxes = []
waste_dollars = []
colors = []

for model_id, display_name, pricing in models_sorted:
    md = rq16[model_id]
    tax = md["revision_tax_pct"]
    waste = md["waste_dollars_per_task"]

    names.append(display_name)
    taxes.append(tax)
    waste_dollars.append(waste)

    if tax < 50:
        colors.append(BLUE)
    elif tax < 150:
        colors.append(AMBER)
    else:
        colors.append(ORANGE)

y_pos = range(len(names))

# Bars
bars = ax.barh(y_pos, taxes, color=colors, alpha=0.75, height=0.6,
               edgecolor=[c for c in colors], linewidth=0.8)

# 100% reference line (2x cost)
ax.axvline(100, color=GRAY, linestyle="--", linewidth=0.8, alpha=0.6)
ax.text(100, len(names) - 0.2, "2x cost", fontsize=6.5, color=GRAY,
        ha="center", va="bottom")

# Labels on bars (percentage only; dollar figures are in the paper table)
for i, tax in enumerate(taxes):
    ax.text(tax + 4, i, f"{tax:.0f}%", va="center", fontsize=8,
            fontweight="bold", color="#333333")

# Y-tick labels with pricing integrated
ax.set_yticks(list(y_pos))
ylabels = [f"{name}\n({models_sorted[i][2]})" for i, name in enumerate(names)]
ax.set_yticklabels(ylabels, fontsize=7.5)

# Enterprise callout
# 500 people, 30 tasks/day, 22 working days
# Claude: $0.0182/task * 500 * 30 * 22 = $6,006/month
claude_monthly = rq16["claude-sonnet-4"]["waste_dollars_per_task"] * 500 * 30 * 22
gpt_monthly = rq16["gpt-4o"]["waste_dollars_per_task"] * 500 * 30 * 22

ax.text(0.98, 0.05,
        f"Upper-bound projection (500 staff, 30 tasks/day):\n"
        f"  Claude Sonnet 4: ${claude_monthly:,.0f}/month\n"
        f"  GPT-4o: ${gpt_monthly:,.0f}/month",
        transform=ax.transAxes, fontsize=7, color="#333333", ha="right",
        va="bottom", family="monospace",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#F8F8F8",
                  edgecolor="#cccccc"))

# Axes
ax.set_xlim(0, 310)
ax.set_xlabel("Extra tokens past quality peak (%)", fontsize=9, labelpad=6)

ax.grid(False)
ax.yaxis.grid(True, alpha=0.3, color='#cccccc', linewidth=0.5)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#444444")
ax.spines["bottom"].set_color("#444444")
ax.tick_params(colors="#444444", length=4, labelsize=8)

ax.set_title("The Revision Tax: Real Cost of Undirected Iteration",
             fontsize=12, fontweight="bold", pad=12, color="#222222")
ax.text(0.5, 1.03, "Wasted tokens at June 2026 API pricing",
        transform=ax.transAxes, ha="center", fontsize=8.5, color=GRAY)

# Save
out_dir = Path(__file__).resolve().parent
fig.tight_layout()
fig.savefig(out_dir / "fig6_revision_tax.pdf", bbox_inches="tight")
fig.savefig(out_dir / "fig6_revision_tax.png", bbox_inches="tight")
print("Saved fig6_revision_tax.pdf and .png")
plt.close(fig)
