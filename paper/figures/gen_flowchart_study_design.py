#!/usr/bin/env python3
"""Flowchart: Study 3 Experiment Design.

Synthesized from a three-agent design council:
- Vertical spine showing the per-trial pipeline
- Attrition numbers on downward arrows
- Loop arrow with "x4" badge for turns 2-5
- Three sub-experiment cards at bottom with finding chips
- Key annotations: balanced probe explanation, evaluator separation
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

# -- Colors --
BLUE = "#4878A8"       # generation / model
TEAL = "#55A868"       # evaluation / scoring
AMBER = "#E8A838"      # decision / probe
RED = "#C44E52"        # findings / warnings
PURPLE = "#8172B2"     # sub-experiments
GRAY = "#8C8C8C"
DARK = "#333333"
LTGRAY = "#F0F0F0"
WHITE = "#FFFFFF"

# -- Figure --
fig, ax = plt.subplots(figsize=(6, 8.5), dpi=250)
fig.patch.set_facecolor(WHITE)
ax.set_facecolor(WHITE)
ax.set_xlim(0, 6)
ax.set_ylim(0, 8.5)
ax.axis("off")


def draw_box(x, y, w, h, text, facecolor, edgecolor, fontsize=8,
             fontweight="normal", text_color=DARK, alpha=1.0, linestyle="-",
             linewidth=1.2, pad=0.12):
    """Draw a rounded box with centered text."""
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle=f"round,pad={pad}",
                         facecolor=facecolor, edgecolor=edgecolor,
                         linewidth=linewidth, alpha=alpha, linestyle=linestyle,
                         zorder=2)
    ax.add_patch(box)
    cx, cy = x + w / 2, y + h / 2
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize,
            fontweight=fontweight, color=text_color, zorder=3,
            linespacing=1.4)


def arrow_down(x, y_from, y_to, color=GRAY, lw=1.5):
    """Draw a downward arrow."""
    ax.annotate("", xy=(x, y_to), xytext=(x, y_from),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw),
                zorder=1)


# ========================================
# TITLE AND SCALE BADGES
# ========================================
ax.text(3.0, 8.25, "Study 3: Revision Yield Experiment",
        ha="center", va="center", fontsize=13, fontweight="bold", color=DARK)

badges = [("720 trials", 0.45, 1.2), ("6 models", 1.85, 1.0),
          ("5 domains", 3.05, 1.1), ("40 tasks", 4.35, 1.0)]
for label, bx, bw in badges:
    draw_box(bx, 7.88, bw, 0.26, label, LTGRAY, GRAY, fontsize=7,
             fontweight="bold", linewidth=0.8, pad=0.05)

# ========================================
# BOX 1: TASK PROMPT
# ========================================
draw_box(1.2, 7.35, 3.6, 0.4, "Task Prompt\ne.g., 'Write a debounce function'",
         LTGRAY, GRAY, fontsize=7.5, fontweight="bold")

arrow_down(3.0, 7.35, 7.12)

# ========================================
# BOX 2: MODEL GENERATES OUTPUT
# ========================================
draw_box(1.2, 6.58, 3.6, 0.5,
         "Working Model Generates Output\n(Turn N, temperature 1.0)",
         "#DCE6F0", BLUE, fontsize=8, fontweight="bold", text_color=BLUE)

# T1 quality chip (left)
draw_box(0.0, 6.68, 1.05, 0.3, "T1: 4.27\nabove thresh.",
         "#DCE6F0", BLUE, fontsize=6, fontweight="bold", text_color=BLUE,
         linewidth=0.8, pad=0.04)
ax.plot([1.05, 1.2], [6.83, 6.83], color=BLUE, lw=0.8, zorder=1)

# T5 quality chip (right)
draw_box(4.95, 6.68, 1.05, 0.3, "T5: 3.04\nbelow thresh.",
         "#FDECEA", RED, fontsize=6, fontweight="bold", text_color=RED,
         linewidth=0.8, pad=0.04)
ax.plot([4.8, 4.95], [6.83, 6.83], color=RED, lw=0.8, zorder=1)

arrow_down(3.0, 6.58, 6.35)

# ========================================
# BOX 3: BLIND EVALUATOR
# ========================================
draw_box(1.2, 5.83, 3.6, 0.48,
         "Blind Evaluator Scores Output\n1-6 quality scale  |  separate Claude instance",
         "#DFF0E4", TEAL, fontsize=7.5, fontweight="bold", text_color="#2A7A4A",
         linestyle="--")

# "BLIND" badge
draw_box(4.85, 6.1, 0.5, 0.18, "BLIND", WHITE, TEAL, fontsize=5.5,
         fontweight="bold", text_color=TEAL, linewidth=0.8, pad=0.03)

# Threshold annotation
ax.text(5.05, 5.85, "Threshold:\nlevel 4\n= Sufficient",
        fontsize=5, color=GRAY, ha="left", va="bottom", style="italic")

arrow_down(3.0, 5.83, 5.6)

# ========================================
# BOX 4: BALANCED PROBE
# ========================================
ax.text(3.0, 5.65, "Balanced Probe", ha="center", fontsize=8,
        fontweight="bold", color="#C08020")

draw_box(1.0, 5.0, 4.0, 0.55,
         '"Would you like to keep this as your\nfinal version, or would you like to revise it?"',
         "#FDF3DC", AMBER, fontsize=7, fontweight="bold", text_color="#8A6A10",
         linewidth=1.8)

# Contrast callout
draw_box(0.0, 4.6, 2.5, 0.32,
         'NOT: "Can you improve this?"\n(which yields 99.9% revision)',
         WHITE, "#C08020", fontsize=5.5, text_color="#8A6A10",
         linewidth=0.8, pad=0.04)

# ========================================
# BRANCH: DECLINE and REVISE
# ========================================
# Decline arrow (left-down)
ax.annotate("", xy=(0.9, 4.35), xytext=(2.0, 5.0),
            arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.3,
                            connectionstyle="arc3,rad=0.2"),
            zorder=1)
ax.text(0.6, 4.65, "Decline", fontsize=6.5, color=TEAL, fontweight="bold")

# Decline box
draw_box(0.0, 3.95, 1.8, 0.38,
         "Meta-Response (Exit)\nExcluded from scoring",
         "#E8E8E8", GRAY, fontsize=6, fontweight="bold", text_color="#555555",
         linewidth=0.8)

# Revise arrow (right-down)
ax.annotate("", xy=(5.05, 4.35), xytext=(4.0, 5.0),
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.3,
                            connectionstyle="arc3,rad=-0.2"),
            zorder=1)
ax.text(4.75, 4.75, "Revise", fontsize=6.5, color=RED, fontweight="bold")

# Revise box
draw_box(4.15, 3.95, 1.8, 0.38,
         "Revision Produced\n(Turn N+1)",
         "#FDECEA", RED, fontsize=6.5, fontweight="bold", text_color=RED,
         linewidth=1.0)

# 64.3% annotation
ax.text(5.95, 3.85, "64.3% revise\npast sufficiency",
        fontsize=5.5, color=RED, ha="right", va="top", style="italic")

# ========================================
# LOOP ARROW (Turns 2-5)
# ========================================
loop = FancyArrowPatch(
    (5.65, 4.33), (5.65, 6.83),
    connectionstyle="arc3,rad=0.3",
    arrowstyle="-|>", color=RED, lw=2.0, linestyle="--",
    mutation_scale=12, zorder=1
)
ax.add_patch(loop)

# x4 badge
draw_box(5.55, 5.55, 0.42, 0.28, "x4", RED, RED, fontsize=9,
         fontweight="bold", text_color=WHITE, linewidth=0, pad=0.05)
ax.text(5.76, 5.45, "Turns 2-5", fontsize=5.5, color=RED, ha="center",
        style="italic")

# Edit ratio annotation
ax.text(5.97, 5.05, "Edit ratio:\n0.97\n(near-complete\nrewrites)",
        fontsize=4.5, color=GRAY, ha="right", va="center", style="italic")

# ========================================
# ATTRITION COLUMN (left margin, below model box)
# ========================================
ax.text(0.0, 6.5, "Attrition", fontsize=5.5, color=GRAY, fontweight="bold")
attrition = [
    ("T1: 720", 6.38), ("T2: 491 (68%)", 6.26),
    ("T3: 362 (50%)", 6.14), ("T4: 304 (42%)", 6.02),
    ("T5: 253 (35%)", 5.90),
]
for label, y in attrition:
    ax.text(0.0, y, label, fontsize=4.5, color=GRAY, ha="left",
            family="monospace")

# Balanced panel box
draw_box(0.0, 3.48, 1.8, 0.38,
         "Balanced Panel\nn=135 (all 5 turns)",
         WHITE, BLUE, fontsize=6, fontweight="bold", text_color=BLUE,
         linewidth=1.2, linestyle="--", pad=0.05)

# ========================================
# DIVIDER
# ========================================
ax.plot([0.15, 5.85], [3.25, 3.25], color=GRAY, lw=0.8, linestyle="--")
ax.text(3.0, 3.32, "Sub-Experiments (run after all 5 turns complete)",
        ha="center", fontsize=6.5, color=GRAY, style="italic")

# ========================================
# SUB-EXPERIMENT CARDS
# ========================================
card_w = 1.72
card_h = 1.7
card_y = 1.3
gap = 0.14

# -- Card A: Targeted Feedback --
cx_a = 0.08
draw_box(cx_a, card_y + card_h - 0.32, card_w, 0.32,
         "A: Targeted Feedback", BLUE, BLUE, fontsize=7,
         fontweight="bold", text_color=WHITE, pad=0.04)
draw_box(cx_a, card_y, card_w, card_h - 0.32,
         "", "#DCE6F0", BLUE, linewidth=0.8, pad=0.04)
ax.text(cx_a + card_w / 2, card_y + card_h - 0.55,
        "Outputs rated 1-3\nget specific critique\nthen revise",
        ha="center", va="top", fontsize=6, color=DARK, linespacing=1.3)
ax.text(cx_a + card_w / 2, card_y + 0.62,
        "n = 424", ha="center", fontsize=5.5, color=GRAY)
draw_box(cx_a + 0.08, card_y + 0.08, card_w - 0.16, 0.38,
         "+2.0 quality\nlevels", BLUE, BLUE, fontsize=8.5,
         fontweight="bold", text_color=WHITE, pad=0.04)

# -- Card B: Self-Reflection --
cx_b = cx_a + card_w + gap
draw_box(cx_b, card_y + card_h - 0.32, card_w, 0.32,
         "B: Self-Reflection", TEAL, TEAL, fontsize=7,
         fontweight="bold", text_color=WHITE, pad=0.04)
draw_box(cx_b, card_y, card_w, card_h - 0.32,
         "", "#DFF0E4", TEAL, linewidth=0.8, pad=0.04)
ax.text(cx_b + card_w / 2, card_y + card_h - 0.55,
        "Model shown all 5\nversions, picks best",
        ha="center", va="top", fontsize=6, color=DARK, linespacing=1.3)
ax.text(cx_b + card_w / 2, card_y + 0.62,
        "n = 720", ha="center", fontsize=5.5, color=GRAY)
draw_box(cx_b + 0.08, card_y + 0.08, card_w - 0.16, 0.38,
         "Mean rec:\nTurn 2.4", TEAL, TEAL, fontsize=8.5,
         fontweight="bold", text_color=WHITE, pad=0.04)

# -- Card C: Reversibility --
cx_c = cx_b + card_w + gap
draw_box(cx_c, card_y + card_h - 0.32, card_w, 0.32,
         "C: Reversibility", AMBER, "#C08020", fontsize=7,
         fontweight="bold", text_color=WHITE, pad=0.04)
draw_box(cx_c, card_y, card_w, card_h - 0.32,
         "", "#FDF3DC", "#C08020", linewidth=0.8, pad=0.04)
ax.text(cx_c + card_w / 2, card_y + card_h - 0.55,
        "Fresh model instance\nT1 vs T5 blind,\npicks better",
        ha="center", va="top", fontsize=6, color=DARK, linespacing=1.3)
ax.text(cx_c + card_w / 2, card_y + 0.62,
        "n = 717", ha="center", fontsize=5.5, color=GRAY)
draw_box(cx_c + 0.08, card_y + 0.08, card_w - 0.16, 0.38,
         "83.7% prefer\nTurn 1", AMBER, "#C08020", fontsize=8.5,
         fontweight="bold", text_color=WHITE, pad=0.04)

# Fan arrows from divider to cards
for cx in [cx_a + card_w / 2, cx_b + card_w / 2, cx_c + card_w / 2]:
    ax.annotate("", xy=(cx, card_y + card_h), xytext=(3.0, 3.25),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.8,
                                linestyle="--"),
                zorder=0)

# ========================================
# BOTTOM TAKEAWAY
# ========================================
ax.text(3.0, 1.05, "Key paradox: models know Turn 1 is best, but revise anyway.",
        ha="center", fontsize=7.5, fontweight="bold", color=DARK, style="italic")
ax.text(3.0, 0.8, "The problem is not revision capacity. It is the absence of direction.",
        ha="center", fontsize=6.5, color=GRAY, style="italic")

# ========================================
# SAVE
# ========================================
out_dir = Path(__file__).resolve().parent
fig.savefig(out_dir / "flowchart_study_design.pdf", bbox_inches="tight",
            facecolor=WHITE)
fig.savefig(out_dir / "flowchart_study_design.png", bbox_inches="tight",
            facecolor=WHITE)
print("Saved flowchart_study_design.pdf and .png")
plt.close(fig)
