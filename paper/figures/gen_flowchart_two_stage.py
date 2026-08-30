"""
Generate a publication-ready flowchart for the Two-Stage Account of LLM
revision behavior.  Outputs PDF and PNG to the figures/ directory.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# ── colours ──────────────────────────────────────────────────────────
RED_MAIN   = "#C44E52"
BLUE_MAIN  = "#4878A8"
AMBER      = "#E8A838"
DARK_GREY  = "#333333"
MID_GREY   = "#777777"
LIGHT_GREY = "#AAAAAA"
WHITE      = "#FFFFFF"

# ── figure setup ─────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 9)
ax.set_ylim(0, 5)
ax.axis("off")
fig.patch.set_facecolor(WHITE)

# ── title / subtitle ────────────────────────────────────────────────
ax.text(4.5, 4.72, "The Two-Stage Account", fontsize=16, fontweight="bold",
        ha="center", va="center", color=DARK_GREY)
ax.text(4.5, 4.38, "Phrasing controls the gate;  thresholds control the intensity",
        fontsize=11, ha="center", va="center", color=MID_GREY, style="italic")

# ── stage background regions ────────────────────────────────────────
# Stage 1 region
s1_bg = FancyBboxPatch((1.45, 0.35), 3.0, 3.65, boxstyle="round,pad=0.12",
                        facecolor=RED_MAIN, alpha=0.07, edgecolor=RED_MAIN,
                        linewidth=1.0, linestyle="--")
ax.add_patch(s1_bg)
ax.text(2.95, 3.82, "STAGE 1 -- THE REVISION GATE", fontsize=9,
        fontweight="bold", ha="center", va="center", color=RED_MAIN)

# Stage 2 region
s2_bg = FancyBboxPatch((5.05, 0.35), 2.95, 3.65, boxstyle="round,pad=0.12",
                        facecolor=BLUE_MAIN, alpha=0.07, edgecolor=BLUE_MAIN,
                        linewidth=1.0, linestyle="--")
ax.add_patch(s2_bg)
ax.text(6.52, 3.82, "STAGE 2 -- INTENSITY CALIBRATION", fontsize=9,
        fontweight="bold", ha="center", va="center", color=BLUE_MAIN)

# ════════════════════════════════════════════════════════════════════
# INPUT box (left)
# ════════════════════════════════════════════════════════════════════
inp_box = FancyBboxPatch((0.05, 2.05), 1.15, 0.9, boxstyle="round,pad=0.08",
                          facecolor="#F0F0F0", edgecolor=DARK_GREY, linewidth=1.2)
ax.add_patch(inp_box)
ax.text(0.625, 2.62, "User prompt", fontsize=8, ha="center", va="center",
        fontweight="bold", color=DARK_GREY)
ax.text(0.625, 2.38, "+ threshold", fontsize=7.5, ha="center", va="center",
        color=MID_GREY)
ax.text(0.625, 2.18, "+ follow-up", fontsize=7.5, ha="center", va="center",
        color=MID_GREY)

# ════════════════════════════════════════════════════════════════════
# STAGE 1: Decision diamond
# ════════════════════════════════════════════════════════════════════
diamond_cx, diamond_cy = 2.95, 2.55
diamond_r = 0.72
diamond = plt.Polygon(
    [(diamond_cx, diamond_cy + diamond_r),
     (diamond_cx + diamond_r * 1.15, diamond_cy),
     (diamond_cx, diamond_cy - diamond_r),
     (diamond_cx - diamond_r * 1.15, diamond_cy)],
    closed=True, facecolor=AMBER, edgecolor="#C08020",
    linewidth=1.5, alpha=0.85, zorder=3)
ax.add_patch(diamond)
ax.text(diamond_cx, diamond_cy + 0.13, "Does phrasing", fontsize=7.5,
        ha="center", va="center", fontweight="bold", color=DARK_GREY, zorder=4)
ax.text(diamond_cx, diamond_cy - 0.13, "imply revision?", fontsize=7.5,
        ha="center", va="center", fontweight="bold", color=DARK_GREY, zorder=4)

# ── arrow: input -> diamond ──────────────────────────────────────────
ax.annotate("", xy=(diamond_cx - diamond_r * 1.15, diamond_cy),
            xytext=(1.22, 2.5),
            arrowprops=dict(arrowstyle="-|>", color=DARK_GREY, lw=1.5))

# ════════════════════════════════════════════════════════════════════
# YES path  (down from diamond -> REVISE box -> right to Stage 2)
# ════════════════════════════════════════════════════════════════════
# YES label
ax.text(diamond_cx + 0.22, diamond_cy - diamond_r - 0.12, "YES",
        fontsize=8, fontweight="bold", color=RED_MAIN, ha="left", va="top")

# REVISE box
rev_box = FancyBboxPatch((2.35, 0.85), 1.2, 0.55, boxstyle="round,pad=0.06",
                          facecolor=RED_MAIN, edgecolor="#9E3A3E",
                          linewidth=1.3, alpha=0.9)
ax.add_patch(rev_box)
ax.text(2.95, 1.125, "REVISE", fontsize=9, ha="center", va="center",
        fontweight="bold", color=WHITE)

# Arrow diamond -> REVISE
ax.annotate("", xy=(2.95, 1.42), xytext=(diamond_cx, diamond_cy - diamond_r),
            arrowprops=dict(arrowstyle="-|>", color=RED_MAIN, lw=1.5))

# Annotation for YES rate
ax.text(2.0, 1.6, "99.9% for\n'Can this be\nimproved?'",
        fontsize=6.5, ha="center", va="center", color=RED_MAIN,
        style="italic", linespacing=1.15,
        bbox=dict(boxstyle="round,pad=0.15", facecolor=WHITE,
                  edgecolor=RED_MAIN, alpha=0.7, linewidth=0.6))

# Arrow REVISE -> Stage 2
ax.annotate("", xy=(5.25, 2.3), xytext=(3.57, 1.125),
            arrowprops=dict(arrowstyle="-|>", color=RED_MAIN, lw=1.5,
                            connectionstyle="arc3,rad=-0.25"))

# ════════════════════════════════════════════════════════════════════
# NO path  (right from diamond -> DECLINE box)
# ════════════════════════════════════════════════════════════════════
# NO label
ax.text(diamond_cx + diamond_r * 1.15 + 0.08, diamond_cy + 0.15, "NO",
        fontsize=8, fontweight="bold", color=BLUE_MAIN, ha="left")

# DECLINE box
dec_box = FancyBboxPatch((3.95, 3.15), 0.95, 0.45, boxstyle="round,pad=0.06",
                          facecolor=BLUE_MAIN, edgecolor="#365F8A",
                          linewidth=1.3, alpha=0.85)
ax.add_patch(dec_box)
ax.text(4.425, 3.375, "DECLINE", fontsize=8, ha="center", va="center",
        fontweight="bold", color=WHITE)

# Arrow diamond -> DECLINE (up-right)
ax.annotate("", xy=(3.95, 3.375),
            xytext=(diamond_cx + diamond_r * 1.15, diamond_cy),
            arrowprops=dict(arrowstyle="-|>", color=BLUE_MAIN, lw=1.5,
                            connectionstyle="arc3,rad=-0.3"))

# Annotation for NO rate
ax.text(4.425, 2.85, "0.3--38% for\nevaluative probes",
        fontsize=6.5, ha="center", va="center", color=BLUE_MAIN,
        style="italic", linespacing=1.15,
        bbox=dict(boxstyle="round,pad=0.12", facecolor=WHITE,
                  edgecolor=BLUE_MAIN, alpha=0.7, linewidth=0.6))

# ── Key insight box (bottom of Stage 1) ─────────────────────────────
insight_box = FancyBboxPatch((1.7, 0.45), 2.5, 0.32, boxstyle="round,pad=0.06",
                              facecolor="#FFF3E0", edgecolor=AMBER,
                              linewidth=1.0, alpha=0.9)
ax.add_patch(insight_box)
ax.text(2.95, 0.61, "Threshold has NO effect on this gate (p > 0.40)",
        fontsize=6.5, ha="center", va="center", fontweight="bold",
        color="#8B6914")

# ════════════════════════════════════════════════════════════════════
# STAGE 2: Intensity calibration
# ════════════════════════════════════════════════════════════════════
# "How much to revise?" box
hmr_box = FancyBboxPatch((5.25, 2.05), 1.6, 0.7, boxstyle="round,pad=0.08",
                          facecolor=WHITE, edgecolor=BLUE_MAIN, linewidth=1.5)
ax.add_patch(hmr_box)
ax.text(6.05, 2.5, "How much", fontsize=8.5, ha="center", va="center",
        fontweight="bold", color=DARK_GREY)
ax.text(6.05, 2.22, "to revise?", fontsize=8.5, ha="center", va="center",
        fontweight="bold", color=DARK_GREY)

# "Stated threshold" input arrow from above
ax.text(6.05, 3.35, "Stated\nthreshold", fontsize=7, ha="center",
        va="center", color=BLUE_MAIN, fontweight="bold", linespacing=1.1,
        bbox=dict(boxstyle="round,pad=0.12", facecolor=WHITE,
                  edgecolor=BLUE_MAIN, linewidth=0.8))
ax.annotate("", xy=(6.05, 2.77), xytext=(6.05, 3.12),
            arrowprops=dict(arrowstyle="-|>", color=BLUE_MAIN, lw=1.3))

# ── Gradient bar: Minor edit -> Full rewrite ─────────────────────────
grad_left = 5.35
grad_right = 6.75
grad_y = 1.55
grad_h = 0.28
n_seg = 80
for i in range(n_seg):
    frac = i / n_seg
    r = 0.28 + 0.69 * frac
    g = 0.47 + 0.18 * (1 - frac)
    b = 0.66 * (1 - frac) + 0.32 * frac
    x0 = grad_left + (grad_right - grad_left) * i / n_seg
    w = (grad_right - grad_left) / n_seg
    ax.add_patch(plt.Rectangle((x0, grad_y), w, grad_h,
                                facecolor=(r, g, b), edgecolor="none"))

ax.add_patch(plt.Rectangle((grad_left, grad_y),
                             grad_right - grad_left, grad_h,
                             facecolor="none", edgecolor=MID_GREY, linewidth=0.8))
ax.text(grad_left + 0.02, grad_y - 0.1, "Minor edit", fontsize=6,
        ha="left", va="top", color=BLUE_MAIN)
ax.text(grad_right - 0.02, grad_y - 0.1, "Full rewrite", fontsize=6,
        ha="right", va="top", color=RED_MAIN)

# Arrow from box to gradient
ax.annotate("", xy=(6.05, grad_y + grad_h), xytext=(6.05, 2.03),
            arrowprops=dict(arrowstyle="-|>", color=DARK_GREY, lw=1.2))

# ── Annotation boxes for Stage 2 ─────────────────────────────────────
ax.text(7.35, 1.95, r"Threshold modulates"
        "\n" r"intensity ($\rho$ = -0.14 to -0.50)",
        fontsize=6.2, ha="left", va="center", color=BLUE_MAIN,
        linespacing=1.2,
        bbox=dict(boxstyle="round,pad=0.12", facecolor=WHITE,
                  edgecolor=BLUE_MAIN, alpha=0.7, linewidth=0.6))

ax.text(7.35, 1.2, r"Qualitative framing reduces"
        "\n" r"overcorrection ($\beta$ = -1.05)",
        fontsize=6.2, ha="left", va="center", color="#2E7D32",
        linespacing=1.2,
        bbox=dict(boxstyle="round,pad=0.12", facecolor=WHITE,
                  edgecolor="#2E7D32", alpha=0.7, linewidth=0.6))

# small arrows pointing from annotations to gradient region
ax.annotate("", xy=(6.78, 1.69), xytext=(7.32, 1.88),
            arrowprops=dict(arrowstyle="-|>", color=BLUE_MAIN, lw=0.8))
ax.annotate("", xy=(6.78, 1.55), xytext=(7.32, 1.25),
            arrowprops=dict(arrowstyle="-|>", color="#2E7D32", lw=0.8))

# ════════════════════════════════════════════════════════════════════
# OUTPUT box (right)
# ════════════════════════════════════════════════════════════════════
out_box = FancyBboxPatch((7.75, 2.85), 1.1, 0.65, boxstyle="round,pad=0.08",
                          facecolor="#E8F5E9", edgecolor="#4CAF50",
                          linewidth=1.3)
ax.add_patch(out_box)
ax.text(8.3, 3.27, "Revised", fontsize=8, ha="center", va="center",
        fontweight="bold", color="#2E7D32")
ax.text(8.3, 3.03, "output", fontsize=8, ha="center", va="center",
        fontweight="bold", color="#2E7D32")

# Arrow Stage 2 -> output
ax.annotate("", xy=(7.75, 3.17), xytext=(6.87, 2.55),
            arrowprops=dict(arrowstyle="-|>", color=DARK_GREY, lw=1.5,
                            connectionstyle="arc3,rad=-0.15"))

# ── save ────────────────────────────────────────────────────────────
out_dir = os.path.dirname(os.path.abspath(__file__))
fig.tight_layout(pad=0.3)

fig.savefig(os.path.join(out_dir, "flowchart_two_stage.pdf"),
            dpi=300, bbox_inches="tight", facecolor=WHITE)
fig.savefig(os.path.join(out_dir, "flowchart_two_stage.png"),
            dpi=300, bbox_inches="tight", facecolor=WHITE)
plt.close(fig)
print("Saved flowchart_two_stage.pdf and .png")
