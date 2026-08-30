#!/usr/bin/env python3
"""Generate Figure 2: The Overcorrection Paradox.

A visual-argument figure showing two key statistics side by side:
- 64.3% revision-despite-sufficiency rate (RQ4)
- 93.3% T1 preference rate in blind comparison (RQ10)

Data source: data/study3/analysis/study3_results.json
"""

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# ---------------------------------------------------------------------------
# Load exact numbers from results
# ---------------------------------------------------------------------------
RESULTS_PATH = Path(__file__).resolve().parents[2] / "data" / "study3" / "analysis" / "study3_results.json"
with open(RESULTS_PATH) as f:
    results = json.load(f)

rds_rate = results["rq4"]["revision_despite_sufficiency_rate"]  # 0.6434
t1_pref  = results["rq10"]["prefers_t1_rate"]                   # 0.9331

left_pct  = f"{rds_rate * 100:.1f}%"
right_pct = f"{t1_pref * 100:.1f}%"

# ---------------------------------------------------------------------------
# Colours
# ---------------------------------------------------------------------------
RED   = "#C44E52"
AMBER = "#E8A838"
DARK  = "#2B2B2B"
GRAY  = "#888888"

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 3.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis("off")
fig.patch.set_facecolor("white")

# --- Title ---
ax.text(5, 4.65, "The Overcorrection Paradox",
        ha="center", va="center", fontsize=16, fontweight="bold", color=DARK)

# --- Rounded rectangles ---
box_kw = dict(boxstyle="round,pad=0.4,rounding_size=0.3", linewidth=2)

# Left box
left_box = mpatches.FancyBboxPatch(
    (0.5, 1.15), 3.6, 3.0,
    boxstyle="round,pad=0,rounding_size=0.25",
    facecolor=RED, alpha=0.12, edgecolor=RED, linewidth=2,
    transform=ax.transData, zorder=1,
)
ax.add_patch(left_box)

# Right box
right_box = mpatches.FancyBboxPatch(
    (5.9, 1.15), 3.6, 3.0,
    boxstyle="round,pad=0,rounding_size=0.25",
    facecolor=AMBER, alpha=0.12, edgecolor=AMBER, linewidth=2,
    transform=ax.transData, zorder=1,
)
ax.add_patch(right_box)

# --- Left card content ---
lcx = 2.3  # center x of left box
ax.text(lcx, 4.05, "WHAT THEY DO", ha="center", va="center",
        fontsize=9, fontweight="bold", color=RED, zorder=2)
ax.text(lcx, 3.1, left_pct, ha="center", va="center",
        fontsize=40, fontweight="bold", color=DARK, zorder=2)
ax.text(lcx, 2.35, "of the time, models revise", ha="center", va="center",
        fontsize=11, color=DARK, zorder=2)
ax.text(lcx, 1.95, "output already rated sufficient", ha="center", va="center",
        fontsize=11, color=DARK, zorder=2)

# --- Right card content ---
rcx = 7.7  # center x of right box
ax.text(rcx, 4.05, "WHAT THEY KNOW", ha="center", va="center",
        fontsize=9, fontweight="bold", color=AMBER, zorder=2)
ax.text(rcx, 3.1, right_pct, ha="center", va="center",
        fontsize=40, fontweight="bold", color=DARK, zorder=2)
ax.text(rcx, 2.35, "of the time, models prefer", ha="center", va="center",
        fontsize=11, color=DARK, zorder=2)
ax.text(rcx, 1.95, "Turn 1 over Turn 5 in blind test", ha="center", va="center",
        fontsize=11, color=DARK, zorder=2)

# --- Connector word ---
ax.text(5.0, 2.75, "yet", ha="center", va="center",
        fontsize=24, fontstyle="italic", color=GRAY, zorder=2)

# --- Bottom tagline ---
ax.text(5.0, 0.55,
        "Models know revision makes output worse, but revise anyway.",
        ha="center", va="center", fontsize=12, fontstyle="italic", color=GRAY)

# --- Save ---
out_dir = Path(__file__).resolve().parent
fig.savefig(out_dir / "fig2_paradox.pdf", bbox_inches="tight", facecolor="white")
fig.savefig(out_dir / "fig2_paradox.png", bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"Saved fig2_paradox.pdf and .png to {out_dir}")
print(f"  Left panel:  {left_pct} revision-despite-sufficiency (RQ4)")
print(f"  Right panel: {right_pct} T1 preference rate (RQ10)")
