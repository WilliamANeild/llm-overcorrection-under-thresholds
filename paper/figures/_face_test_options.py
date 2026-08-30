#!/usr/bin/env python3
"""Side-by-side comparison of two T3/T4 options.
Row 1: Option A (gentle gradient)
Row 2: Option B (feature escalation)
Row 3: A proposed mix of A and B
All share the same T1, T2, T5."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

WHITE = "#FFFFFF"
FACE_BG   = ["#E0F2F1", "#FFF8E1", "#FFF3E0", "#FFEBEE", "#CFD8DC"]
FACE_LINE = ["#00897B", "#F9A825", "#EF6C00", "#C62828", "#455A64"]

R = 0.9


def draw_face(ax, cx, cy, face_type, bg_col, line_col, r=0.9):
    circle = plt.Circle((cx, cy), r, facecolor=bg_col, edgecolor=line_col,
                         linewidth=2.8, zorder=2)
    ax.add_patch(circle)
    lw = 3.2
    ec = line_col
    s = r

    if face_type == "smile":
        for dx in [-0.32, 0.32]:
            ex, ey = cx + dx * s, cy + 0.2 * s
            eye = plt.Circle((ex, ey), 0.1 * s, facecolor=ec,
                              edgecolor="none", zorder=3)
            ax.add_patch(eye)
            hl = plt.Circle((ex + 0.03 * s, ey + 0.04 * s), 0.03 * s,
                             facecolor=WHITE, edgecolor="none", zorder=4)
            ax.add_patch(hl)
        t = np.linspace(-1, 1, 60)
        mx = cx + t * 0.38 * s
        my = (cy - 0.15 * s) - 0.22 * s * (1 - t**2)
        ax.plot(mx, my, color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    elif face_type == "neutral":
        for dx in [-0.32, 0.32]:
            eye = plt.Circle((cx + dx * s, cy + 0.2 * s), 0.09 * s,
                              facecolor=ec, edgecolor="none", zorder=3)
            ax.add_patch(eye)
        ax.plot([cx - 0.28 * s, cx + 0.28 * s],
                [cy - 0.25 * s, cy - 0.25 * s],
                color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    # ── Option A: T3 = worried (gentle downturn, no brows) ──
    elif face_type == "a_worried":
        for dx in [-0.32, 0.32]:
            eye = plt.Circle((cx + dx * s, cy + 0.2 * s), 0.09 * s,
                              facecolor=ec, edgecolor="none", zorder=3)
            ax.add_patch(eye)
        # Gentle downturn mouth (shallower than full frown)
        t = np.linspace(-1, 1, 60)
        mx = cx + t * 0.3 * s
        my = (cy - 0.3 * s) + 0.12 * s * (1 - t**2)
        ax.plot(mx, my, color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    # ── Option A: T4 = angry frown (current T3 promoted: brows + frown) ──
    elif face_type == "a_angry_frown":
        for dx in [-0.32, 0.32]:
            eye = plt.Circle((cx + dx * s, cy + 0.15 * s), 0.09 * s,
                              facecolor=ec, edgecolor="none", zorder=3)
            ax.add_patch(eye)
        # Strong furrowed brows
        for dx in [-0.32, 0.32]:
            sign = -1 if dx < 0 else 1
            bx0 = cx + (dx - sign * 0.16) * s
            bx1 = cx + (dx + sign * 0.16) * s
            by0 = cy + 0.37 * s
            by1 = cy + 0.27 * s
            ax.plot([bx0, bx1], [by0, by1], color=ec, linewidth=lw * 0.8,
                    solid_capstyle="round", zorder=3)
        # Strong frown
        t = np.linspace(-1, 1, 60)
        mx = cx + t * 0.32 * s
        my = (cy - 0.35 * s) + 0.2 * s * (1 - t**2)
        ax.plot(mx, my, color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    # ── Option B: T3 = uneasy (squiggle mouth) ──
    elif face_type == "b_uneasy":
        for dx in [-0.32, 0.32]:
            eye = plt.Circle((cx + dx * s, cy + 0.2 * s), 0.09 * s,
                              facecolor=ec, edgecolor="none", zorder=3)
            ax.add_patch(eye)
        # Wavy/squiggle mouth
        t = np.linspace(-0.32, 0.32, 80)
        mx = cx + t * s
        my = cy - 0.25 * s + 0.06 * s * np.sin(t * 3 * np.pi / 0.32)
        ax.plot(mx, my, color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    # ── Option B: T4 = distressed (brows + gritted teeth, dot eyes) ──
    elif face_type == "b_distressed":
        # Dot eyes (NOT X-eyes)
        for dx in [-0.32, 0.32]:
            eye = plt.Circle((cx + dx * s, cy + 0.15 * s), 0.09 * s,
                              facecolor=ec, edgecolor="none", zorder=3)
            ax.add_patch(eye)
        # Angry brows
        for dx in [-0.32, 0.32]:
            sign = -1 if dx < 0 else 1
            bx0 = cx + (dx - sign * 0.16) * s
            bx1 = cx + (dx + sign * 0.16) * s
            by0 = cy + 0.37 * s
            by1 = cy + 0.27 * s
            ax.plot([bx0, bx1], [by0, by1], color=ec, linewidth=lw * 0.8,
                    solid_capstyle="round", zorder=3)
        # Gritted teeth
        teeth_w = 0.6 * s
        teeth_h = 0.2 * s
        teeth_l = cx - teeth_w / 2
        teeth_y = cy - 0.28 * s
        rect = mpatches.FancyBboxPatch(
            (teeth_l, teeth_y - teeth_h / 2), teeth_w, teeth_h,
            boxstyle="round,pad=0.03",
            facecolor=bg_col, edgecolor=ec, linewidth=lw * 0.75, zorder=3)
        ax.add_patch(rect)
        for frac in [0.2, 0.4, 0.6, 0.8]:
            xd = teeth_l + frac * teeth_w
            ax.plot([xd, xd],
                    [teeth_y - teeth_h / 2 + 0.015 * s,
                     teeth_y + teeth_h / 2 - 0.015 * s],
                    color=ec, linewidth=lw * 0.4, zorder=4)

    # ── Mix: T3 = worried (gentle downturn, no brows) ──
    elif face_type == "mix_t3":
        for dx in [-0.32, 0.32]:
            eye = plt.Circle((cx + dx * s, cy + 0.2 * s), 0.09 * s,
                              facecolor=ec, edgecolor="none", zorder=3)
            ax.add_patch(eye)
        # Gentle downturn
        t = np.linspace(-1, 1, 60)
        mx = cx + t * 0.3 * s
        my = (cy - 0.3 * s) + 0.12 * s * (1 - t**2)
        ax.plot(mx, my, color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    # ── Mix: T4 = distressed (brows + teeth, dot eyes) ──
    elif face_type == "mix_t4":
        # Dot eyes
        for dx in [-0.32, 0.32]:
            eye = plt.Circle((cx + dx * s, cy + 0.15 * s), 0.09 * s,
                              facecolor=ec, edgecolor="none", zorder=3)
            ax.add_patch(eye)
        # Angry brows
        for dx in [-0.32, 0.32]:
            sign = -1 if dx < 0 else 1
            bx0 = cx + (dx - sign * 0.16) * s
            bx1 = cx + (dx + sign * 0.16) * s
            by0 = cy + 0.37 * s
            by1 = cy + 0.27 * s
            ax.plot([bx0, bx1], [by0, by1], color=ec, linewidth=lw * 0.8,
                    solid_capstyle="round", zorder=3)
        # Gritted teeth
        teeth_w = 0.6 * s
        teeth_h = 0.2 * s
        teeth_l = cx - teeth_w / 2
        teeth_y = cy - 0.28 * s
        rect = mpatches.FancyBboxPatch(
            (teeth_l, teeth_y - teeth_h / 2), teeth_w, teeth_h,
            boxstyle="round,pad=0.03",
            facecolor=bg_col, edgecolor=ec, linewidth=lw * 0.75, zorder=3)
        ax.add_patch(rect)
        for frac in [0.2, 0.4, 0.6, 0.8]:
            xd = teeth_l + frac * teeth_w
            ax.plot([xd, xd],
                    [teeth_y - teeth_h / 2 + 0.015 * s,
                     teeth_y + teeth_h / 2 - 0.015 * s],
                    color=ec, linewidth=lw * 0.4, zorder=4)

    # ── T5: dead (shared across all options) ──
    elif face_type == "dead":
        for dx in [-0.32, 0.32]:
            d = 0.16 * s
            ex, ey = cx + dx * s, cy + 0.2 * s
            ax.plot([ex - d, ex + d], [ey - d, ey + d],
                    color=ec, linewidth=lw * 1.3, solid_capstyle="round", zorder=3)
            ax.plot([ex - d, ex + d], [ey + d, ey - d],
                    color=ec, linewidth=lw * 1.3, solid_capstyle="round", zorder=3)
        mouth = plt.Circle((cx, cy - 0.28 * s), 0.18 * s,
                            facecolor=ec, edgecolor="none", zorder=3)
        ax.add_patch(mouth)
        inner = plt.Circle((cx, cy - 0.28 * s), 0.10 * s,
                            facecolor=bg_col, edgecolor="none", zorder=4)
        ax.add_patch(inner)


# ── Build comparison figure ──────────────────────────────────────
rows = [
    ("Option A: Gentle gradient",
     ["smile", "neutral", "a_worried", "a_angry_frown", "dead"]),
    ("Option B: Feature escalation",
     ["smile", "neutral", "b_uneasy", "b_distressed", "dead"]),
    ("Mix: A's T3 + B's T4",
     ["smile", "neutral", "mix_t3", "mix_t4", "dead"]),
]

col_labels = ["T1: Smile\n4/5", "T2: Neutral\n3.5/5",
              "T3: ???\n3/5", "T4: ???\n2.5/5", "T5: Dead\n2/5"]

fig, axes = plt.subplots(3, 5, figsize=(15, 10), dpi=200)
fig.patch.set_facecolor(WHITE)
fig.subplots_adjust(hspace=0.55, wspace=0.25)

for row_idx, (row_label, face_types) in enumerate(rows):
    for col_idx in range(5):
        ax = axes[row_idx, col_idx]
        ax.set_xlim(-1.4, 1.4)
        ax.set_ylim(-1.4, 1.4)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_facecolor(WHITE)

        draw_face(ax, 0, 0, face_types[col_idx],
                  FACE_BG[col_idx], FACE_LINE[col_idx], r=R)

        if row_idx == 0:
            ax.set_title(col_labels[col_idx], fontsize=9, pad=10,
                         fontweight="bold")

    # Row label on the left
    axes[row_idx, 0].text(-2.8, 0, row_label, fontsize=11,
                           fontweight="bold", va="center", ha="left",
                           color="#333333", rotation=0)

# Highlight the T3/T4 columns that differ
for row_idx in range(3):
    for col_idx in [2, 3]:
        ax = axes[row_idx, col_idx]
        rect = mpatches.FancyBboxPatch(
            (-1.35, -1.35), 2.7, 2.7,
            boxstyle="round,pad=0.05",
            facecolor="none", edgecolor="#E53935",
            linewidth=2.0, linestyle="--", zorder=1)
        ax.add_patch(rect)

fig.suptitle("T3 and T4 Options (red dashed = the faces that change)",
             fontsize=14, fontweight="bold", y=0.97)

out = Path(__file__).resolve().parent / "_face_options.png"
fig.savefig(out, bbox_inches="tight", facecolor=WHITE, edgecolor="none")
print(f"Saved {out}")
plt.close(fig)
