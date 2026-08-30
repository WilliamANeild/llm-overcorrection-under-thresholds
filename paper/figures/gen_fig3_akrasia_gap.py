#!/usr/bin/env python3
"""Figure 3: The Akrasia Gap (Know-But-Can't-Stop).

Two-panel figure showing the dissociation between what models know
(prefer T1 83.7% of the time) and what they do (revise past sufficiency 64.3%).
"""

import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# -- Load data --
ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS = ROOT / "data" / "study3" / "analysis" / "study3_results.json"
with open(RESULTS) as f:
    data = json.load(f)

rq4 = data["rq4"]
rq10 = data["rq10"]
rq14 = data["rq14"]

# Key numbers
revise_past_suff = rq4["revision_despite_sufficiency_rate"]  # 0.643
prefer_t1_revision = rq10["revision_only_t1_rate"]  # 0.837
mean_rec_turn = rq14["mean_recommended_turn"]  # 2.44

BLUE = "#4878A8"
ORANGE = "#E8833A"
GRAY = "#8C8C8C"

# -- Figure --
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3.5), dpi=250,
                                gridspec_kw={"width_ratios": [1, 1], "wspace": 0.4})
fig.patch.set_facecolor("white")

# == Left panel: What models DO ==
ax1.set_facecolor("white")

# Stacked bar showing revise vs stop
categories = ["In-Context\nBehavior"]
revise_pct = revise_past_suff
stop_pct = 1 - revise_past_suff

ax1.barh(categories, [revise_pct], color=ORANGE, alpha=0.75, height=0.5,
         edgecolor=ORANGE, linewidth=0.8, label="Revise past sufficiency")
ax1.barh(categories, [stop_pct], left=[revise_pct], color=BLUE, alpha=0.5,
         height=0.5, edgecolor=BLUE, linewidth=0.8, label="Stop appropriately")

# Labels inside bars
ax1.text(revise_pct / 2, 0, f"{revise_pct:.1%}", ha="center", va="center",
         fontsize=11, fontweight="bold", color="white")
ax1.text(revise_pct + stop_pct / 2, 0, f"{stop_pct:.1%}", ha="center",
         va="center", fontsize=9, fontweight="bold", color="white")

# Self-reflection distribution below
ax1.text(0.5, -0.35, f"Self-reflection recommends Turn {mean_rec_turn:.1f} (not 5)",
         transform=ax1.transAxes, fontsize=7.5, color=BLUE, ha="center",
         style="italic")

ax1.set_xlim(0, 1.0)
ax1.set_title("What Models DO", fontsize=11, fontweight="bold", color=ORANGE, pad=10)
ax1.legend(fontsize=7, loc="upper right", framealpha=0.9, edgecolor="#cccccc")

for spine in ax1.spines.values():
    spine.set_visible(False)
ax1.tick_params(left=False, labelleft=True, bottom=False, labelbottom=False)

# == Right panel: What models KNOW ==
ax2.set_facecolor("white")

# Multiple bars showing preference rates
bars = [
    ("Revision-only\ntrials", rq10["revision_only_t1_rate"]),
    ("Length-stable\nsubset", rq10["length_stable_t1_rate"]),
    ("All trials", rq10["prefers_t1_rate"]),
]

y_pos = range(len(bars))
labels = [b[0] for b in bars]
t1_rates = [b[1] for b in bars]

for i, (label, rate) in enumerate(bars):
    # T1 preference (green)
    ax2.barh(i, rate, color=BLUE, alpha=0.75, height=0.5,
             edgecolor=BLUE, linewidth=0.8)
    # T5 preference (red)
    ax2.barh(i, 1 - rate, left=rate, color=ORANGE, alpha=0.4, height=0.5,
             edgecolor=ORANGE, linewidth=0.8)
    # Label
    ax2.text(rate / 2, i, f"{rate:.1%}", ha="center", va="center",
             fontsize=9, fontweight="bold", color="white")

ax2.set_xlim(0, 1.0)
ax2.set_yticks(y_pos)
ax2.set_yticklabels(labels, fontsize=8)
ax2.set_title("What Models KNOW", fontsize=11, fontweight="bold", color=BLUE, pad=10)

for spine in ax2.spines.values():
    spine.set_visible(False)
ax2.tick_params(left=False, labelleft=True, bottom=False, labelbottom=False)

# Legend for right panel
green_patch = mpatches.Patch(color=BLUE, alpha=0.75, label="Prefers Turn 1")
red_patch = mpatches.Patch(color=ORANGE, alpha=0.4, label="Prefers Turn 5")
ax2.legend(handles=[green_patch, red_patch], fontsize=7, loc="lower right",
           framealpha=0.9, edgecolor="#cccccc")

# Central gap annotation
fig.text(0.5, 0.02,
         "Models know Turn 1 is better. They revise anyway.",
         ha="center", fontsize=9, fontweight="bold", color="#333333")

# Gap callout
gap = prefer_t1_revision - (1 - revise_past_suff)
fig.text(0.5, 0.95,
         f"The Akrasia Gap: {gap:.0%} disconnect between knowledge and action",
         ha="center", fontsize=9, color="#555555",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFF3CD",
                   edgecolor="#F39C12", alpha=0.8))

# Save
out_dir = Path(__file__).resolve().parent
fig.savefig(out_dir / "fig3_akrasia_gap.pdf", bbox_inches="tight")
fig.savefig(out_dir / "fig3_akrasia_gap.png", bbox_inches="tight")
print("Saved fig3_akrasia_gap.pdf and .png")
plt.close(fig)
