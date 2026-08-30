#!/usr/bin/env python3
"""Final face set v3: standardized eyes + brows on T1-T4, refined brow angles."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

WHITE = "#FFFFFF"
FACE_BG   = ["#E0F2F1", "#FFF8E1", "#FFF3E0", "#FFEBEE", "#CFD8DC"]
FACE_LINE = ["#00897B", "#F9A825", "#EF6C00", "#C62828", "#455A64"]
LABELS    = ["T1: Smile\n4/5", "T2: Neutral\n3.5/5",
             "T3: Uneasy\n3/5", "T4: Angry frown\n2.5/5",
             "T5: Dead\n2/5"]
TYPES     = ["smile", "neutral", "uneasy", "angry_frown", "dead"]

R = 0.9


def _eyes(ax, cx, cy, s, ec):
    """Plain filled-dot eyes, T1-T4."""
    for dx in [-0.32, 0.32]:
        ex, ey = cx + dx * s, cy + 0.15 * s
        eye = plt.Circle((ex, ey), 0.09 * s, facecolor=ec,
                          edgecolor="none", zorder=3)
        ax.add_patch(eye)


def _brows(ax, cx, cy, s, ec, lw, angle="neutral"):
    """Eyebrows sitting just above the eyes."""
    eye_top = cy + 0.15 * s + 0.1 * s  # top of eye circle
    brow_y = eye_top + 0.06 * s         # base brow height, close to eyes
    half = 0.13 * s

    for dx in [-0.32, 0.32]:
        sign = -1 if dx < 0 else 1
        bx_c = cx + dx * s

        if angle == "happy":
            # Gentle arch upward in the middle
            bx0 = bx_c - half
            bx1 = bx_c + half
            by0 = brow_y - 0.01 * s
            by1 = brow_y - 0.01 * s
            # Draw as slight arc instead of line
            t = np.linspace(-1, 1, 30)
            bx = bx_c + t * half
            by = brow_y + 0.04 * s * (1 - t**2)
            ax.plot(bx, by, color=ec, linewidth=lw * 0.7,
                    solid_capstyle="round", zorder=3)
            continue

        elif angle == "neutral":
            bx0 = bx_c - half
            bx1 = bx_c + half
            by0 = brow_y
            by1 = brow_y

        elif angle == "concerned":
            # Inner end tilts up slightly (worried look)
            bx0 = bx_c - sign * half   # outer end
            bx1 = bx_c + sign * half   # inner end
            by0 = brow_y - 0.02 * s    # outer: slightly lower
            by1 = brow_y + 0.05 * s    # inner: slightly higher

        elif angle == "angry":
            # Inner end tilts down hard (angry V shape)
            bx0 = bx_c - sign * half   # outer end
            bx1 = bx_c + sign * half   # inner end
            by0 = brow_y + 0.06 * s    # outer: higher
            by1 = brow_y - 0.06 * s    # inner: lower

        if angle == "skeptical":
            # Left brow raised high, right brow stays flat
            if dx < 0:  # left brow - raised and tilted
                bx0 = bx_c - half
                bx1 = bx_c + half
                by0 = brow_y + 0.06 * s
                by1 = brow_y + 0.16 * s
            else:  # right brow - flat, slightly furrowed
                bx0 = bx_c - half
                bx1 = bx_c + half
                by0 = brow_y
                by1 = brow_y - 0.02 * s

        ax.plot([bx0, bx1], [by0, by1], color=ec, linewidth=lw * 0.7,
                solid_capstyle="round", zorder=3)


def draw_face(ax, cx, cy, face_type, bg_col, line_col, r=0.9):
    circle = plt.Circle((cx, cy), r, facecolor=bg_col, edgecolor=line_col,
                         linewidth=2.8, zorder=2)
    ax.add_patch(circle)
    lw = 3.2
    ec = line_col
    s = r

    if face_type == "smile":
        _eyes(ax, cx, cy, s, ec)
        _brows(ax, cx, cy, s, ec, lw, angle="happy")
        t = np.linspace(-1, 1, 60)
        mx = cx + t * 0.38 * s
        my = (cy - 0.18 * s) - 0.2 * s * (1 - t**2)
        ax.plot(mx, my, color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    elif face_type == "neutral":
        _eyes(ax, cx, cy, s, ec)
        _brows(ax, cx, cy, s, ec, lw, angle="neutral")
        ax.plot([cx - 0.28 * s, cx + 0.28 * s],
                [cy - 0.25 * s, cy - 0.25 * s],
                color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    elif face_type == "uneasy":
        _eyes(ax, cx, cy, s, ec)
        # Skeptical: one brow raised, one flat, but ROUNDED/curved
        eye_top = cy + 0.15 * s + 0.09 * s
        brow_y = eye_top + 0.06 * s
        half = 0.13 * s
        for dx in [-0.32, 0.32]:
            bx_c = cx + dx * s
            t = np.linspace(-1, 1, 30)
            bx = bx_c + t * half
            if dx < 0:
                # Left brow: raised arch
                by = brow_y + 0.1 * s + 0.06 * s * (1 - t**2)
            else:
                # Right brow: flat arch
                by = brow_y + 0.02 * s * (1 - t**2)
            ax.plot(bx, by, color=ec, linewidth=lw * 0.7,
                    solid_capstyle="round", zorder=3)
        # Slight symmetric frown (shallower than T4)
        t = np.linspace(-1, 1, 60)
        mx = cx + t * 0.28 * s
        my = (cy - 0.3 * s) + 0.1 * s * (1 - t**2)
        ax.plot(mx, my, color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    elif face_type == "angry_frown":
        _eyes(ax, cx, cy, s, ec)
        _brows(ax, cx, cy, s, ec, lw, angle="concerned")
        # Full symmetric frown
        t = np.linspace(-1, 1, 60)
        mx = cx + t * 0.32 * s
        my = (cy - 0.35 * s) + 0.2 * s * (1 - t**2)
        ax.plot(mx, my, color=ec, linewidth=lw, solid_capstyle="round", zorder=3)

    elif face_type == "dead":
        # X-eyes, no brows, O-mouth
        for dx in [-0.32, 0.32]:
            d = 0.16 * s
            ex, ey = cx + dx * s, cy + 0.18 * s
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


fig, axes = plt.subplots(1, 5, figsize=(15, 3.5), dpi=200)
fig.patch.set_facecolor(WHITE)
fig.suptitle("Final Face Set v3", fontsize=14, fontweight="bold", y=0.98)

for idx, ax in enumerate(axes):
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_facecolor(WHITE)
    draw_face(ax, 0, 0, TYPES[idx], FACE_BG[idx], FACE_LINE[idx], r=R)
    ax.set_title(LABELS[idx], fontsize=9, pad=8, color="#666666")

out = Path(__file__).resolve().parent / "_face_final.png"
fig.savefig(out, bbox_inches="tight", facecolor=WHITE, edgecolor="none")
print(f"Saved {out}")
plt.close(fig)
