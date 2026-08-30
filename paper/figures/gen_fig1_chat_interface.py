#!/usr/bin/env python3
"""Figure 1: Chat-interface hero figure.

Shows a 5-turn conversation where undirected "make it better" revision
degrades quality while spending more tokens.  Two independent encodings:
  - Face (quality): smile -> neutral -> uneasy -> angry_frown -> dead
  - Bubble colour (cost): teal -> gold -> amber -> coral -> slate

Layout: staggered chat conversation (user left, model right, alternating).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# ── Real data (do not change) ───────────────────────────────────
TURNS = [
    {
        "user": "Write a friendly email inviting\nRachel to our spring sale.",
        "model": "Dear Rachel, I hope this\nfinds you well! We'd love\nto invite you to our ....",
        "quality": 4,
        "tokens": 552,
        "face": "smile",
    },
    {
        "user": "Can you improve this?",
        "model": "Subject: You're Invited!\nDear Rachel, Spring is here\nand so are the savings ....",
        "quality": 3.5,
        "tokens": 865,
        "face": "neutral",
    },
    {
        "user": "Hmm, try again.",
        "model": "Subject: Spring Into Savings!\nHi Rachel!! As the flowers\nbloom and birds sing ....",
        "quality": 3,
        "tokens": 1110,
        "face": "uneasy",
    },
    {
        "user": "Are you sure that's good?",
        "model": "Subject: A Once-in-a-Lifetime\nSpring Extravaganza!! Rachel,\nprepare to be amazed ....",
        "quality": 2.5,
        "tokens": 1294,
        "face": "angry_frown",
    },
    {
        "user": "Make it better.",
        "model": "Subject: EXCLUSIVE VIP SPRING\nBLOWOUT!!! Dear Valued\nCustomer Rachel ....",
        "quality": 2,
        "tokens": 1460,
        "face": "dead",
    },
]

# ── Palette ──────────────────────────────────────────────────────
WHITE = "#FFFFFF"
BG = WHITE
USER_BUBBLE = "#EDF1F5"
USER_TEXT = "#333333"

MODEL_COLOURS = ["#26A69A", "#F9A825", "#FB8C00", "#E53935", "#6B7B8D"]
# Pastel fills: whitish tinted versions of MODEL_COLOURS
MODEL_FILLS = ["#D6F0ED", "#FFF4CC", "#FFE4CC", "#FCDADA", "#E3E8EC"]
MODEL_TEXT_COL = "#222222"  # all model text is dark

FACE_BG = ["#E0F2F1", "#FFF8E1", "#FFF3E0", "#FFEBEE", "#CFD8DC"]
FACE_LINE = ["#00897B", "#F9A825", "#EF6C00", "#C62828", "#455A64"]

GRAY = "#8C8C8C"
DARK = "#222222"

# ── Layout ───────────────────────────────────────────────────────
FIG_W, FIG_H = 7.0, 7.2
MODEL_W = 2.8
MODEL_BH = 0.68       # model bubble height
FACE_R = 0.22
MSG_GAP = 0.22        # vertical gap between user msg and model reply (includes tail)
TURN_GAP = 0.22       # vertical gap between turns (includes tail)
LEFT_MARGIN = 0.3     # left edge of user bubbles
RIGHT_EDGE = 6.5      # right edge of model bubbles

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H), dpi=250)
ax.set_xlim(-0.2, 7.5)
ax.set_ylim(1.0, 10.0)
ax.set_aspect("equal")
ax.axis("off")
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)


def rounded_rect(ax, x, y, w, h, colour, radius=0.12, zorder=2,
                  tail=None, edge_colour=None, edge_width=0):
    """Draw a speech bubble: rounded rect with a tail notch in the bottom edge."""
    from matplotlib.path import Path as MPath
    ec = edge_colour if edge_colour else "none"
    lw = edge_width if edge_colour else 0
    r = min(radius, h / 2, w / 2)
    # Tail geometry
    tail_w = 0.22   # width of the opening on the bottom edge
    tail_h = 0.14   # how far the tail drops below the bubble
    if tail == "left":
        t_start = x + 0.08 * w        # left side of tail opening
        t_tip_x = x + 0.02            # tip points just below left edge
    elif tail == "right":
        t_start = x + 0.92 * w - tail_w
        t_tip_x = x + w - 0.02        # tip points just below right edge
    else:
        t_start = None
    # Build path: go clockwise from bottom-left corner
    verts = []
    codes = []
    # Bottom-left corner
    verts += [(x, y + r), (x, y + r)]
    codes += [MPath.MOVETO, MPath.LINETO]
    # Left edge up to top-left
    verts += [(x, y + h - r)]
    codes += [MPath.LINETO]
    # Top-left corner (curve)
    verts += [(x, y + h), (x + r, y + h)]
    codes += [MPath.CURVE3, MPath.CURVE3]
    # Top edge
    verts += [(x + w - r, y + h)]
    codes += [MPath.LINETO]
    # Top-right corner
    verts += [(x + w, y + h), (x + w, y + h - r)]
    codes += [MPath.CURVE3, MPath.CURVE3]
    # Right edge down
    verts += [(x + w, y + r)]
    codes += [MPath.LINETO]
    # Bottom-right corner
    verts += [(x + w, y), (x + w - r, y)]
    codes += [MPath.CURVE3, MPath.CURVE3]
    # Bottom edge with optional tail
    if t_start is not None:
        t_end = t_start + tail_w
        t_tip_y = y - tail_h
        if tail == "right":
            # Bottom edge from right to tail
            verts += [(t_end, y)]
            codes += [MPath.LINETO]
            # Tail: down to tip, back up
            verts += [(t_tip_x, t_tip_y)]
            codes += [MPath.LINETO]
            verts += [(t_start, y)]
            codes += [MPath.LINETO]
            # Continue bottom edge to bottom-left corner
            verts += [(x + r, y)]
            codes += [MPath.LINETO]
        else:
            # Bottom edge from right toward left, hit tail
            verts += [(t_end, y)]
            codes += [MPath.LINETO]
            # Tail
            verts += [(t_tip_x, t_tip_y)]
            codes += [MPath.LINETO]
            verts += [(t_start, y)]
            codes += [MPath.LINETO]
            verts += [(x + r, y)]
            codes += [MPath.LINETO]
    else:
        verts += [(x + r, y)]
        codes += [MPath.LINETO]
    # Bottom-left corner
    verts += [(x, y), (x, y + r)]
    codes += [MPath.CURVE3, MPath.CURVE3]
    verts += [(x, y + r)]
    codes += [MPath.CLOSEPOLY]
    path = MPath(verts, codes)
    patch = mpatches.PathPatch(path, facecolor=colour, edgecolor=ec,
                                linewidth=lw, zorder=zorder, joinstyle="round")
    ax.add_patch(patch)


# ── Face drawing functions (LOCKED) ──────────────────────────────
def _eyes(ax, cx, cy, s, ec):
    for dx in [-0.32, 0.32]:
        ex, ey = cx + dx * s, cy + 0.15 * s
        eye = plt.Circle((ex, ey), 0.09 * s, facecolor=ec,
                          edgecolor="none", zorder=7)
        ax.add_patch(eye)


def _brows(ax, cx, cy, s, ec, lw, angle="neutral"):
    eye_top = cy + 0.15 * s + 0.1 * s
    brow_y = eye_top + 0.06 * s
    half = 0.13 * s
    for dx in [-0.32, 0.32]:
        sign = -1 if dx < 0 else 1
        bx_c = cx + dx * s
        if angle == "happy":
            t = np.linspace(-1, 1, 30)
            bx = bx_c + t * half
            by = brow_y + 0.04 * s * (1 - t**2)
            ax.plot(bx, by, color=ec, linewidth=lw * 0.7,
                    solid_capstyle="round", zorder=7)
            continue
        elif angle == "neutral":
            bx0, bx1 = bx_c - half, bx_c + half
            by0 = by1 = brow_y
        elif angle == "concerned":
            bx0 = bx_c - sign * half
            bx1 = bx_c + sign * half
            by0 = brow_y - 0.02 * s
            by1 = brow_y + 0.05 * s
        ax.plot([bx0, bx1], [by0, by1], color=ec, linewidth=lw * 0.7,
                solid_capstyle="round", zorder=7)


def draw_face(ax, cx, cy, face_type, bg_col, line_col, r=0.22):
    circle = plt.Circle((cx, cy), r, facecolor=bg_col, edgecolor=line_col,
                         linewidth=1.4, zorder=6)
    ax.add_patch(circle)
    lw = 1.6
    ec = line_col
    s = r

    if face_type == "smile":
        _eyes(ax, cx, cy, s, ec)
        _brows(ax, cx, cy, s, ec, lw, angle="happy")
        t = np.linspace(-1, 1, 60)
        mx = cx + t * 0.38 * s
        my = (cy - 0.18 * s) - 0.2 * s * (1 - t**2)
        ax.plot(mx, my, color=ec, linewidth=lw, solid_capstyle="round", zorder=7)

    elif face_type == "neutral":
        _eyes(ax, cx, cy, s, ec)
        _brows(ax, cx, cy, s, ec, lw, angle="neutral")
        ax.plot([cx - 0.28 * s, cx + 0.28 * s],
                [cy - 0.25 * s, cy - 0.25 * s],
                color=ec, linewidth=lw, solid_capstyle="round", zorder=7)

    elif face_type == "uneasy":
        _eyes(ax, cx, cy, s, ec)
        eye_top = cy + 0.15 * s + 0.09 * s
        brow_y = eye_top + 0.06 * s
        half = 0.13 * s
        for dx in [-0.32, 0.32]:
            bx_c = cx + dx * s
            t = np.linspace(-1, 1, 30)
            bx = bx_c + t * half
            if dx < 0:
                by = brow_y + 0.1 * s + 0.06 * s * (1 - t**2)
            else:
                by = brow_y + 0.02 * s * (1 - t**2)
            ax.plot(bx, by, color=ec, linewidth=lw * 0.7,
                    solid_capstyle="round", zorder=7)
        t = np.linspace(-1, 1, 60)
        mx = cx + t * 0.28 * s
        my = (cy - 0.3 * s) + 0.1 * s * (1 - t**2)
        ax.plot(mx, my, color=ec, linewidth=lw, solid_capstyle="round", zorder=7)

    elif face_type == "angry_frown":
        _eyes(ax, cx, cy, s, ec)
        _brows(ax, cx, cy, s, ec, lw, angle="concerned")
        t = np.linspace(-1, 1, 60)
        mx = cx + t * 0.32 * s
        my = (cy - 0.35 * s) + 0.2 * s * (1 - t**2)
        ax.plot(mx, my, color=ec, linewidth=lw, solid_capstyle="round", zorder=7)

    elif face_type == "dead":
        for dx in [-0.32, 0.32]:
            d = 0.16 * s
            ex, ey = cx + dx * s, cy + 0.18 * s
            ax.plot([ex - d, ex + d], [ey - d, ey + d],
                    color=ec, linewidth=lw * 1.3, solid_capstyle="round", zorder=7)
            ax.plot([ex - d, ex + d], [ey + d, ey - d],
                    color=ec, linewidth=lw * 1.3, solid_capstyle="round", zorder=7)
        mouth = plt.Circle((cx, cy - 0.28 * s), 0.18 * s,
                            facecolor=ec, edgecolor="none", zorder=7)
        ax.add_patch(mouth)
        mouth_inner = plt.Circle((cx, cy - 0.28 * s), 0.10 * s,
                                  facecolor=bg_col, edgecolor="none", zorder=8)
        ax.add_patch(mouth_inner)


def draw_person(ax, cx, cy, colour, size=0.2):
    head = plt.Circle((cx, cy + 0.55 * size), 0.3 * size,
                       facecolor=colour, edgecolor="none", zorder=5)
    ax.add_patch(head)
    t = np.linspace(-0.45 * size, 0.45 * size, 30)
    body_y = cy - 0.1 * size - 0.35 * size * np.cos(t * np.pi / (0.45 * size))
    ax.fill_between(cx + t * 1.2, body_y, cy - 0.45 * size,
                    color=colour, zorder=5)


def draw_robot(ax, cx, cy, colour, size=0.2):
    hw, hh = 0.35 * size, 0.3 * size
    rect = mpatches.FancyBboxPatch(
        (cx - hw, cy + 0.08 * size), 2 * hw, 2 * hh,
        boxstyle="round,pad=0.025",
        facecolor=colour, edgecolor="none", zorder=5)
    ax.add_patch(rect)
    ax.plot([cx, cx], [cy + 0.08 * size + 2 * hh, cy + 0.08 * size + 2.6 * hh],
            color=colour, linewidth=1.3, zorder=5)
    ant = plt.Circle((cx, cy + 0.08 * size + 2.6 * hh), 0.05 * size,
                      facecolor=colour, edgecolor="none", zorder=5)
    ax.add_patch(ant)
    for dx in [-0.18, 0.18]:
        eye = plt.Circle((cx + dx * size, cy + 0.08 * size + hh + 0.04 * size),
                          0.06 * size, facecolor=WHITE, edgecolor="none", zorder=6)
        ax.add_patch(eye)
    bw, bh = 0.3 * size, 0.25 * size
    body = mpatches.FancyBboxPatch(
        (cx - bw, cy - 0.2 * size), 2 * bw, bh,
        boxstyle="round,pad=0.015",
        facecolor=colour, edgecolor="none", zorder=5)
    ax.add_patch(body)


# ── (no title) ───────────────────────────────────────────────────

# ── Draw conversation ────────────────────────────────────────────
cursor_y = 9.6  # tracks current vertical position, moves downward

for i, turn in enumerate(TURNS):
    # ── Face icon to the left of user bubble (skip first) ───────
    face_space = FACE_R * 2 + 0.16 if i > 0 else 0
    ub_x = LEFT_MARGIN + face_space

    # Size user bubble to fit text
    longest_line = max(turn["user"].split("\n"), key=len)
    ub_w = len(longest_line) * 0.085 + 0.45
    n_lines = len(turn["user"].split("\n"))
    ubh_actual = 0.28 + n_lines * 0.16

    ub_top = cursor_y
    ub_bot = ub_top - ubh_actual
    rounded_rect(ax, ub_x, ub_bot, ub_w, ubh_actual, USER_BUBBLE,
                 tail="left", edge_colour="#C0C0C0", edge_width=1.0)

    # User text
    user_cy = (ub_top + ub_bot) / 2
    ax.text(ub_x + 0.18, user_cy, turn["user"],
            fontsize=7.5, color=DARK, ha="left", va="center",
            linespacing=1.25, zorder=5)

    if i > 0:
        face_cx = LEFT_MARGIN + FACE_R
        face_cy = user_cy
        draw_face(ax, face_cx, face_cy, TURNS[i - 1]["face"],
                  FACE_BG[i - 1], FACE_LINE[i - 1], r=FACE_R)

    cursor_y = ub_bot - MSG_GAP

    # ── Model reply (right-aligned, outlined) ──────────────────
    mb_right = RIGHT_EDGE
    mb_x = mb_right - MODEL_W
    mb_top = cursor_y
    mb_bot = mb_top - MODEL_BH
    rounded_rect(ax, mb_x, mb_bot, MODEL_W, MODEL_BH, MODEL_FILLS[i],
                 tail="right", edge_colour=MODEL_COLOURS[i], edge_width=2.2)

    model_cy = (mb_top + mb_bot) / 2
    ax.text(mb_x + 0.18, model_cy, turn["model"],
            fontsize=7.5, color=MODEL_TEXT_COL, ha="left", va="center",
            linespacing=1.25, zorder=5)

    # Small robot icon to the right of first model bubble
    if i == 0:
        draw_robot(ax, mb_right + 0.25, model_cy + 0.08, colour="#6B7B8D", size=0.18)

    cursor_y = mb_bot - TURN_GAP

# ── Final face (dead) after last model response ──────────────
final_face_cx = LEFT_MARGIN + FACE_R
final_face_cy = cursor_y - FACE_R - 0.1
draw_face(ax, final_face_cx, final_face_cy, TURNS[4]["face"],
          FACE_BG[4], FACE_LINE[4], r=FACE_R)


# ── Save ─────────────────────────────────────────────────────────
out_dir = Path(__file__).resolve().parent
fig.savefig(out_dir / "fig1_chat_interface.pdf", bbox_inches="tight",
            facecolor=BG, edgecolor="none")
fig.savefig(out_dir / "fig1_chat_interface.png", bbox_inches="tight",
            facecolor=BG, edgecolor="none")
print("Saved fig1_chat_interface.pdf and .png")
plt.close(fig)
