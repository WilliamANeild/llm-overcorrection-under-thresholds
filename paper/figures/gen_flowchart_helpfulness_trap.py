#!/usr/bin/env python3
"""
Generate 'The Helpfulness Trap' conceptual flowchart for ACL paper.
Shows the self-reinforcing loop where RLHF-trained models revise
even when revision degrades quality.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# ── Colour palette ──────────────────────────────────────────────
RED = "#C44E52"
TEAL = "#55A868"
STEEL = "#4878A8"
AMBER = "#E8A838"
GRAY = "#8C8C8C"
LIGHT_RED = "#F5E0E1"
LIGHT_TEAL = "#DFF0E4"
LIGHT_STEEL = "#DCE6F0"
LIGHT_AMBER = "#FDF3DC"
WHITE = "#FFFFFF"

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.set_aspect("equal")
ax.axis("off")
fig.patch.set_facecolor(WHITE)

# ── Helper: draw a rounded box with text ────────────────────────
def draw_box(ax, xy, width, height, text, facecolor, edgecolor,
             fontsize=9, fontweight="normal", textcolor="white",
             alpha=1.0, linestyle="-", linewidth=1.8):
    x, y = xy
    box = FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.15",
        facecolor=facecolor, edgecolor=edgecolor,
        linewidth=linewidth, alpha=alpha, linestyle=linestyle,
        zorder=2,
    )
    ax.add_patch(box)
    ax.text(
        x + width / 2, y + height / 2, text,
        ha="center", va="center", fontsize=fontsize,
        fontweight=fontweight, color=textcolor,
        zorder=3, linespacing=1.35,
    )
    return box


def draw_arrow(ax, posA, posB, color, linestyle="-", linewidth=1.8,
               connectionstyle="arc3,rad=0", shrinkA=0, shrinkB=0,
               alpha=1.0):
    arrow = FancyArrowPatch(
        posA, posB,
        arrowstyle="-|>",
        color=color,
        linewidth=linewidth,
        linestyle=linestyle,
        connectionstyle=connectionstyle,
        shrinkA=shrinkA, shrinkB=shrinkB,
        mutation_scale=14,
        alpha=alpha,
        zorder=1,
    )
    ax.add_patch(arrow)
    return arrow


# ── Layout coordinates ──────────────────────────────────────────
bw, bh = 2.4, 0.7  # standard box width/height

# 1. RLHF Training (top-left)
x1, y1 = 0.4, 6.3
# 2. User asks (top-right)
x2, y2 = 5.8, 6.3
# 3. Model revises (right)
x3, y3 = 6.2, 4.1
bw3 = 2.8  # wider box for step 3
# 4. Quality drops (bottom-right)
x4, y4 = 5.0, 2.0
bw4 = 2.6
# 5. User asks again (bottom-left)
x5, y5 = 1.6, 2.0
# Escape: Targeted feedback (left)
xe, ye = 0.3, 4.1
bwe = 2.2

# ── Draw boxes ──────────────────────────────────────────────────

# 1 - RLHF Training
draw_box(ax, (x1, y1), bw, bh,
         "RLHF Training\n\"helpful = action\"",
         facecolor=STEEL, edgecolor=STEEL,
         fontsize=9, fontweight="bold", textcolor=WHITE)

# 2 - User asks
draw_box(ax, (x2, y2), bw, bh,
         "User: \"Can this\nbe improved?\"",
         facecolor=LIGHT_RED, edgecolor=RED,
         fontsize=8.5, fontweight="normal", textcolor="#333333")

# 3 - Model revises
draw_box(ax, (x3, y3), bw3, bh,
         "Model revises (99.9%)",
         facecolor=RED, edgecolor=RED,
         fontsize=9.5, fontweight="bold", textcolor=WHITE)

# 4 - Quality drops
draw_box(ax, (x4, y4), bw4, bh,
         "Quality drops",
         facecolor=RED, edgecolor=RED,
         fontsize=9.5, fontweight="bold", textcolor=WHITE)

# 5 - User asks again
draw_box(ax, (x5, y5), bw, bh,
         "User asks again",
         facecolor=LIGHT_RED, edgecolor=RED,
         fontsize=9, fontweight="normal", textcolor="#333333")

# Escape box - Targeted feedback
draw_box(ax, (xe, ye), bwe, bh,
         "Targeted feedback\n+2.0 levels",
         facecolor=TEAL, edgecolor=TEAL,
         fontsize=8.5, fontweight="bold", textcolor=WHITE)

# ── Annotations ─────────────────────────────────────────────────

# Gate annotation (near step 3)
ax.text(x3 + bw3 / 2, y3 - 0.25,
        "Gate fires regardless of quality",
        ha="center", va="top", fontsize=7,
        fontstyle="italic", color=GRAY, zorder=3)

# Quality drop annotation
ax.text(x4 + bw4 / 2, y4 - 0.25,
        "-1.11 levels at first revision",
        ha="center", va="top", fontsize=7,
        fontstyle="italic", color=RED, fontweight="bold", zorder=3)

# Paradox annotation (amber box, below quality drops)
paradox_x, paradox_y = 3.1, 1.0
paradox_box = FancyBboxPatch(
    (paradox_x, paradox_y), 3.8, 0.55,
    boxstyle="round,pad=0.12",
    facecolor=LIGHT_AMBER, edgecolor=AMBER,
    linewidth=1.5, linestyle="--", zorder=2,
)
ax.add_patch(paradox_box)
ax.text(
    paradox_x + 1.9, paradox_y + 0.28,
    "Paradox: Model knows Turn 1 was\nbetter (93.3%) but still revises",
    ha="center", va="center", fontsize=7,
    fontweight="bold", color="#7A5C00", zorder=3, linespacing=1.3,
)

# ── Arrows (main loop) ─────────────────────────────────────────

# 1 -> 2: RLHF -> User asks
draw_arrow(ax,
           (x1 + bw, y1 + bh / 2),
           (x2, y2 + bh / 2),
           color=STEEL, linewidth=2.0)

# 2 -> 3: User asks -> Model revises
draw_arrow(ax,
           (x2 + bw / 2 + 0.4, y2),
           (x3 + bw3 / 2, y3 + bh),
           color=RED, linewidth=2.0,
           connectionstyle="arc3,rad=0.15")

# 3 -> 4: Model revises -> Quality drops
draw_arrow(ax,
           (x3 + bw3 / 2, y3),
           (x4 + bw4 / 2 + 0.2, y4 + bh),
           color=RED, linewidth=2.0,
           connectionstyle="arc3,rad=0.15")

# 4 -> 5: Quality drops -> User asks again
draw_arrow(ax,
           (x4, y4 + bh / 2),
           (x5 + bw, y5 + bh / 2),
           color=RED, linewidth=2.0)

# 5 -> 3: THE LOOP (User asks again -> Model revises)
# Big curved arrow going up the left side and across the top
draw_arrow(ax,
           (x5 + bw / 2, y5 + bh),
           (x3 + 0.2, y3),
           color=RED, linewidth=2.5,
           connectionstyle="arc3,rad=-0.5")

# "THE TRAP" label on the loop arrow
ax.text(3.2, 3.35, "THE TRAP",
        ha="center", va="center", fontsize=10,
        fontweight="black", color=RED,
        bbox=dict(boxstyle="round,pad=0.2", facecolor=LIGHT_RED,
                  edgecolor=RED, linewidth=1.5),
        zorder=4, rotation=25)

# ── Escape path (dashed, teal) ──────────────────────────────────

# Dashed arrow from "User asks" area down to "Targeted feedback"
draw_arrow(ax,
           (x2, y2 + 0.15),
           (xe + bwe, ye + bh / 2 + 0.1),
           color=TEAL, linewidth=1.8, linestyle="--",
           connectionstyle="arc3,rad=0.35", alpha=0.85)

# Escape label
ax.text(xe + bwe / 2, ye + bh + 0.25,
        "ESCAPE",
        ha="center", va="center", fontsize=8,
        fontweight="bold", color=TEAL, zorder=3)

# Small upward arrow from escape box (quality improves, exits the loop)
ax.annotate("",
            xy=(xe + bwe / 2, ye + bh + 0.6),
            xytext=(xe + bwe / 2, ye + bh + 0.1),
            arrowprops=dict(arrowstyle="-|>", color=TEAL,
                            linewidth=1.5, linestyle="--"),
            zorder=1)

# Paradox arrow from quality drops box down to paradox annotation
draw_arrow(ax,
           (x4 + bw4 / 2, y4),
           (paradox_x + 1.9, paradox_y + 0.55),
           color=AMBER, linewidth=1.3, linestyle="--",
           connectionstyle="arc3,rad=0.1")

# ── Title ───────────────────────────────────────────────────────
ax.text(5.0, 7.65, "The Helpfulness Trap",
        ha="center", va="center", fontsize=16,
        fontweight="bold", color="#222222", zorder=5)

ax.text(5.0, 7.25,
        "RLHF creates a self-reinforcing revision loop",
        ha="center", va="center", fontsize=9,
        color=GRAY, fontstyle="italic", zorder=5)

# ── Save ────────────────────────────────────────────────────────
out_base = "/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/figures/flowchart_helpfulness_trap"
fig.savefig(out_base + ".pdf", dpi=300, bbox_inches="tight",
            facecolor=WHITE, edgecolor="none")
fig.savefig(out_base + ".png", dpi=300, bbox_inches="tight",
            facecolor=WHITE, edgecolor="none")
print(f"Saved {out_base}.pdf")
print(f"Saved {out_base}.png")
plt.close(fig)
