#!/usr/bin/env python3
"""Standalone test sheet for the 5 face icons. Renders them large so
details are easy to inspect. Run, check the PNG, tweak, repeat."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Arc
import numpy as np
from pathlib import Path

WHITE = "#FFFFFF"
FACE_BG   = ["#E0F2F1", "#FFF8E1", "#FFF3E0", "#FFEBEE", "#CFD8DC"]
FACE_LINE = ["#00897B", "#F9A825", "#EF6C00", "#C62828", "#455A64"]
LABELS    = ["T1: Smile\nQuality 4", "T2: Neutral\nQuality 3.5",
             "T3: Frown\nQuality 3", "T4: Grimace\nQuality 2.5",
             "T5: Dead\nQuality 2"]
TYPES     = ["smile", "neutral", "frown", "grimace", "dead"]

R = 1.0


def draw_face(ax, cx, cy, face_type, bg_col, line_col, r=1.0):
    """Draw one face at (cx, cy) with radius r."""
    circle = plt.Circle((cx, cy), r, facecolor=bg_col, edgecolor=line_col,
                         linewidth=3.0, zorder=2)
    ax.add_patch(circle)

    lw = 3.5
    ec = line_col
    s = r

    if face_type == "smile":
        # ── Eyes: filled circles with highlight ──
        for dx in [-0.32, 0.32]:
            ex, ey = cx + dx * s, cy + 0.2 * s
            eye = plt.Circle((ex, ey), 0.1 * s, facecolor=ec,
                              edgecolor="none", zorder=3)
            ax.add_patch(eye)
            hl = plt.Circle((ex + 0.03 * s, ey + 0.04 * s), 0.03 * s,
                             facecolor=WHITE, edgecolor="none", zorder=4)
            ax.add_patch(hl)

        # ── Mouth: wide cheerful U-smile ──
        # Parametric curve for more control than Arc
        t = np.linspace(-1, 1, 60)
        mouth_x = cx + t * 0.38 * s
        mouth_y = (cy - 0.15 * s) - 0.22 * s * (1 - t**2)
        ax.plot(mouth_x, mouth_y, color=ec, linewidth=lw,
                solid_capstyle="round", zorder=3)

    elif face_type == "neutral":
        # ── Eyes ──
        for dx in [-0.32, 0.32]:
            eye = plt.Circle((cx + dx * s, cy + 0.2 * s), 0.09 * s,
                              facecolor=ec, edgecolor="none", zorder=3)
            ax.add_patch(eye)

        # ── Mouth: flat line ──
        ax.plot([cx - 0.28 * s, cx + 0.28 * s],
                [cy - 0.25 * s, cy - 0.25 * s],
                color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    elif face_type == "frown":
        # ── Eyes ──
        for dx in [-0.32, 0.32]:
            eye = plt.Circle((cx + dx * s, cy + 0.15 * s), 0.09 * s,
                              facecolor=ec, edgecolor="none", zorder=3)
            ax.add_patch(eye)

        # ── Furrowed brows (thicker, more aggressive angle) ──
        for dx in [-0.32, 0.32]:
            sign = -1 if dx < 0 else 1
            bx0 = cx + (dx - sign * 0.16) * s
            bx1 = cx + (dx + sign * 0.16) * s
            by0 = cy + 0.37 * s
            by1 = cy + 0.27 * s
            ax.plot([bx0, bx1], [by0, by1], color=ec, linewidth=lw * 0.8,
                    solid_capstyle="round", zorder=3)

        # ── Mouth: strong downward curve ──
        t = np.linspace(-1, 1, 60)
        mouth_x = cx + t * 0.32 * s
        mouth_y = (cy - 0.35 * s) + 0.2 * s * (1 - t**2)
        ax.plot(mouth_x, mouth_y, color=ec, linewidth=lw,
                solid_capstyle="round", zorder=3)

    elif face_type == "grimace":
        # ── X eyes (moderate) ──
        for dx in [-0.32, 0.32]:
            d = 0.11 * s
            ex, ey = cx + dx * s, cy + 0.2 * s
            ax.plot([ex - d, ex + d], [ey - d, ey + d],
                    color=ec, linewidth=lw, solid_capstyle="round", zorder=3)
            ax.plot([ex - d, ex + d], [ey + d, ey - d],
                    color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

        # ── Gritted teeth (wider) ──
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
        # ── Big X eyes ──
        for dx in [-0.32, 0.32]:
            d = 0.16 * s
            ex, ey = cx + dx * s, cy + 0.2 * s
            ax.plot([ex - d, ex + d], [ey - d, ey + d],
                    color=ec, linewidth=lw * 1.3, solid_capstyle="round", zorder=3)
            ax.plot([ex - d, ex + d], [ey + d, ey - d],
                    color=ec, linewidth=lw * 1.3, solid_capstyle="round", zorder=3)

        # ── Open round mouth (larger, more impactful) ──
        mouth = plt.Circle((cx, cy - 0.28 * s), 0.18 * s,
                            facecolor=ec, edgecolor="none", zorder=3)
        ax.add_patch(mouth)
        mouth_inner = plt.Circle((cx, cy - 0.28 * s), 0.10 * s,
                                  facecolor=bg_col, edgecolor="none", zorder=4)
        ax.add_patch(mouth_inner)


# ── Render test sheet ────────────────────────────────────────────
fig, axes = plt.subplots(1, 5, figsize=(15, 3.5), dpi=200)
fig.patch.set_facecolor(WHITE)
fig.suptitle("Face Icon Test Sheet", fontsize=14, fontweight="bold", y=0.98)

for idx, ax in enumerate(axes):
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_facecolor(WHITE)
    draw_face(ax, 0, 0, TYPES[idx], FACE_BG[idx], FACE_LINE[idx], r=R)
    ax.set_title(LABELS[idx], fontsize=9, pad=8)

out = Path(__file__).resolve().parent / "_face_test.png"
fig.savefig(out, bbox_inches="tight", facecolor=WHITE, edgecolor="none")
print(f"Saved {out}")
plt.close(fig)
