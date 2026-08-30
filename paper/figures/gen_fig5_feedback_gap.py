#!/usr/bin/env python3
"""Generate Figure 5: Targeted Feedback Recovers What Generic Revision Destroys.

Dumbbell/lollipop chart showing quality after targeted vs generic feedback,
broken down by domain with an overall average row.

Data source: data/study3/raw_responses/targeted_feedback_results.jsonl
             data/study3/analysis/study3_results.json (for official aggregates)
"""

import json
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]
RAW_PATH = ROOT / "data" / "study3" / "raw_responses" / "targeted_feedback_results.jsonl"
RESULTS_PATH = ROOT / "data" / "study3" / "analysis" / "study3_results.json"
OUT_DIR = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
with open(RESULTS_PATH) as f:
    results = json.load(f)

# Official aggregate from rq7
overall_targeted = results["rq7"]["mean_targeted"]  # ~4.74
overall_generic = results["rq7"]["mean_generic"]     # ~2.74
overall_p = results["rq7"]["wilcoxon_p"]

# Per-domain from raw JSONL
records = []
with open(RAW_PATH) as f:
    for line in f:
        records.append(json.loads(line))

domain_targeted = defaultdict(list)
domain_generic = defaultdict(list)
for r in records:
    domain_targeted[r["domain"]].append(r["targeted_level"])
    domain_generic[r["domain"]].append(r["generic_next_level"])

# Domain display names and order (bottom to top on the chart)
domain_order = ["writing", "data_logic", "creative", "code", "analysis"]
domain_labels = {
    "writing": "Writing",
    "code": "Code",
    "creative": "Creative",
    "analysis": "Analysis",
    "data_logic": "Data & Logic",
}

rows = []
for d in domain_order:
    t_vals = domain_targeted[d]
    g_vals = domain_generic[d]
    rows.append({
        "label": domain_labels[d],
        "targeted": np.mean(t_vals),
        "generic": np.mean(g_vals),
        "n": len(t_vals),
    })

# Add overall row at the top
rows.append({
    "label": "Overall",
    "targeted": overall_targeted,
    "generic": overall_generic,
    "n": results["rq7"]["n"],
})

# ---------------------------------------------------------------------------
# Colours
# ---------------------------------------------------------------------------
ORANGE = "#E8833A"
BLUE = "#4878A8"
GRAY_LINE = "#AAAAAA"
DARK = "#2B2B2B"
LIGHT_GRAY = "#888888"
THRESH_GRAY = "#CCCCCC"

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
n_rows = len(rows)
fig_height = max(4.0, 0.7 * n_rows + 1.8)
fig, ax = plt.subplots(figsize=(7, fig_height), dpi=300)
fig.patch.set_facecolor("white")

y_positions = list(range(n_rows))

for i, row in enumerate(rows):
    is_overall = row["label"] == "Overall"
    dot_size = 110 if is_overall else 70
    lw = 2.5 if is_overall else 1.8
    fontweight = "bold" if is_overall else "normal"
    fontsize = 10.5 if is_overall else 9.5

    # Connecting line
    ax.plot(
        [row["generic"], row["targeted"]], [i, i],
        color=GRAY_LINE, linewidth=lw, zorder=1,
    )

    # Generic dot (red, left)
    ax.scatter(
        row["generic"], i, color=ORANGE, s=dot_size,
        zorder=3, edgecolors="white", linewidths=0.5,
    )

    # Targeted dot (teal, right)
    ax.scatter(
        row["targeted"], i, color=BLUE, s=dot_size,
        zorder=3, edgecolors="white", linewidths=0.5,
    )

    # Gap annotation in the middle
    mid_x = (row["generic"] + row["targeted"]) / 2
    delta = row["targeted"] - row["generic"]
    y_offset = 0.22
    ax.text(
        mid_x, i + y_offset, f"+{delta:.1f}",
        ha="center", va="bottom", fontsize=fontsize,
        fontweight=fontweight, color=DARK,
    )

# Separator line between domain rows and overall
ax.axhline(
    y=n_rows - 1.5, color=THRESH_GRAY, linewidth=0.8,
    linestyle="-", zorder=0,
)

# Vertical threshold line at 4.0
ax.axvline(x=4.0, color=THRESH_GRAY, linewidth=1.2, linestyle="--", zorder=0)
ax.text(
    4.0, -0.7, "Sufficient",
    ha="center", va="top", fontsize=8, color=LIGHT_GRAY,
    fontstyle="italic",
)

# ---------------------------------------------------------------------------
# Axes
# ---------------------------------------------------------------------------
ax.set_yticks(y_positions)
ax.set_yticklabels(
    [r["label"] for r in rows],
    fontsize=10, color=DARK,
)
# Bold the "Overall" label
labels = ax.get_yticklabels()
labels[-1].set_fontweight("bold")

ax.set_xlim(0.5, 5.8)
ax.set_ylim(-0.8, n_rows - 0.4)
ax.set_xticks([1, 2, 3, 4, 5, 6])
ax.set_xlabel("Quality Level (1\u20136 scale)", fontsize=10, color=DARK, labelpad=8)

# Remove all spines and gridlines
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(axis="both", which="both", length=0)
ax.xaxis.grid(True, alpha=0.3, color='#cccccc', linewidth=0.5)

# ---------------------------------------------------------------------------
# Title and subtitle
# ---------------------------------------------------------------------------
ax.set_title(
    "Targeted Feedback Recovers What Generic Revision Destroys",
    fontsize=14, fontweight="bold", color=DARK, pad=22, loc="center",
)
ax.text(
    0.5, 1.04,
    "Quality level after revision, by feedback type (p < 0.0001)",
    transform=ax.transAxes,
    ha="center", va="bottom", fontsize=11, color=LIGHT_GRAY,
)

# ---------------------------------------------------------------------------
# Legend
# ---------------------------------------------------------------------------
from matplotlib.lines import Line2D

legend_elements = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor=ORANGE,
           markersize=9, label="Generic feedback"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor=BLUE,
           markersize=9, label="Targeted feedback"),
]
ax.legend(
    handles=legend_elements, loc="lower left",
    frameon=False, fontsize=9, labelcolor=DARK,
    bbox_to_anchor=(0.0, -0.02),
)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
plt.tight_layout()
fig.savefig(OUT_DIR / "fig5_feedback_gap.pdf", bbox_inches="tight", facecolor="white")
fig.savefig(OUT_DIR / "fig5_feedback_gap.png", bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Saved: {OUT_DIR / 'fig5_feedback_gap.pdf'}")
print(f"Saved: {OUT_DIR / 'fig5_feedback_gap.png'}")
print(f"Rows: {n_rows} ({n_rows - 1} domains + overall)")
for r in rows:
    print(f"  {r['label']:12s}  generic={r['generic']:.2f}  targeted={r['targeted']:.2f}  delta={r['targeted']-r['generic']:+.2f}  n={r['n']}")
