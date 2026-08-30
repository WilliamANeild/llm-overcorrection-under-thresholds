#!/usr/bin/env python3
"""Test faces at actual figure scale (r=0.25) to verify legibility."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

WHITE = "#FFFFFF"
FACE_BG   = ["#E0F2F1", "#FFF8E1", "#FFF3E0", "#FFEBEE", "#CFD8DC"]
FACE_LINE = ["#00897B", "#F9A825", "#EF6C00", "#C62828", "#455A64"]
LABELS    = ["T1: Smile", "T2: Neutral", "T3: Frown", "T4: Grimace", "T5: Dead"]
TYPES     = ["smile", "neutral", "frown", "grimace", "dead"]

R = 0.25  # actual size in the figure


def draw_face(ax, cx, cy, face_type, bg_col, line_col, r=0.25):
    circle = plt.Circle((cx, cy), r, facecolor=bg_col, edgecolor=line_col,
                         linewidth=1.6, zorder=2)
    ax.add_patch(circle)

    lw = 1.8
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
        mouth_x = cx + t * 0.38 * s
        mouth_y = (cy - 0.15 * s) - 0.22 * s * (1 - t**2)
        ax.plot(mouth_x, mouth_y, color=ec, linewidth=lw,
                solid_capstyle="round", zorder=3)

    elif face_type == "neutral":
        for dx in [-0.32, 0.32]:
            eye = plt.Circle((cx + dx * s, cy + 0.2 * s), 0.09 * s,
                              facecolor=ec, edgecolor="none", zorder=3)
            ax.add_patch(eye)
        ax.plot([cx - 0.28 * s, cx + 0.28 * s],
                [cy - 0.25 * s, cy - 0.25 * s],
                color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    elif face_type == "frown":
        for dx in [-0.32, 0.32]:
            eye = plt.Circle((cx + dx * s, cy + 0.15 * s), 0.09 * s,
                              facecolor=ec, edgecolor="none", zorder=3)
            ax.add_patch(eye)
        for dx in [-0.32, 0.32]:
            sign = -1 if dx < 0 else 1
            bx0 = cx + (dx - sign * 0.16) * s
            bx1 = cx + (dx + sign * 0.16) * s
            by0 = cy + 0.37 * s
            by1 = cy + 0.27 * s
            ax.plot([bx0, bx1], [by0, by1], color=ec, linewidth=lw * 0.8,
                    solid_capstyle="round", zorder=3)
        t = np.linspace(-1, 1, 60)
        mouth_x = cx + t * 0.32 * s
        mouth_y = (cy - 0.35 * s) + 0.2 * s * (1 - t**2)
        ax.plot(mouth_x, mouth_y, color=ec, linewidth=lw,
                solid_capstyle="round", zorder=3)

    elif face_type == "grimace":
        for dx in [-0.32, 0.32]:
            d = 0.11 * s
            ex, ey = cx + dx * s, cy + 0.2 * s
            ax.plot([ex - d, ex + d], [ey - d, ey + d],
                    color=ec, linewidth=lw, solid_capstyle="round", zorder=3)
            ax.plot([ex - d, ex + d], [ey + d, ey - d],
                    color=ec, linewidth=lw, solid_capstyle="round", zorder=3)
        teeth_w = 0.6 * s
        teeth_h = 0.22 * s
        teeth_l = cx - teeth_w / 2
        teeth_y = cy - 0.28 * s
        rect = mpatches.FancyBboxPatch(
            (teeth_l, teeth_y - teeth_h / 2), teeth_w, teeth_h,
            boxstyle="round,pad=0.03",
            facecolor=bg_col, edgecolor=ec, linewidth=lw * 0.8, zorder=3)
        ax.add_patch(rect)
        for frac in [0.2, 0.4, 0.6, 0.8]:
            xd = teeth_l + frac * teeth_w
            ax.plot([xd, xd],
                    [teeth_y - teeth_h / 2 + 0.015 * s,
                     teeth_y + teeth_h / 2 - 0.015 * s],
                    color=ec, linewidth=lw * 0.45, zorder=4)

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
        mouth_inner = plt.Circle((cx, cy - 0.28 * s), 0.10 * s,
                                  facecolor=bg_col, edgecolor="none", zorder=4)
        ax.add_patch(mouth_inner)


fig, ax = plt.subplots(figsize=(8, 2), dpi=250)
ax.set_xlim(-0.5, 5.5)
ax.set_ylim(-0.6, 0.8)
ax.set_aspect("equal")
ax.axis("off")
fig.patch.set_facecolor(WHITE)
ax.set_facecolor(WHITE)

for idx in range(5):
    cx = idx * 1.1
    draw_face(ax, cx, 0, TYPES[idx], FACE_BG[idx], FACE_LINE[idx], r=R)
    ax.text(cx, -0.45, LABELS[idx], fontsize=7, ha="center", va="center",
            color="#555555")

ax.set_title("Faces at actual figure scale (r = 0.25)", fontsize=10,
             fontweight="bold", pad=10)

out = Path(__file__).resolve().parent / "_face_test_small.png"
fig.savefig(out, bbox_inches="tight", facecolor=WHITE, edgecolor="none")
print(f"Saved {out}")
plt.close(fig)
