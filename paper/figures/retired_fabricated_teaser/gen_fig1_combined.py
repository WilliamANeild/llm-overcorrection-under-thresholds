#!/usr/bin/env python3
"""Figure 1 (combined): Chat-interface hero figure with inset chart.

Horizontal layout. Person icon centered on far left, robot icon centered
on far right.  Chat bubbles flow between them.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# ── Real data (do not change) ───────────────────────────────────
TURNS = [
    {
        "user": "Write a friendly email inviting\nRachel to our spring sale.",
        "model": ("Dear Rachel,\n"
                  "I hope this finds you well. We'd\n"
                  "love to invite you to our annual\n"
                  "Spring Sale, April 12-14. Enjoy\n"
                  "20% off across all departments ...."),
        "quality": 4, "tokens": 552, "face": "smile",
    },
    {
        "user": "Can you improve this?",
        "model": ("Hey Rachel! Spring is HERE and\n"
                  "so are the deals! Join us Apr 12-14\n"
                  "for savings you won't want to miss.\n"
                  "We've got something special just\n"
                  "for you - don't sleep on it! ...."),
        "quality": 3.5, "tokens": 865, "face": "neutral",
    },
    {
        "user": "Hmm, try again.",
        "model": ("OMG Rachel!! The flowers are\n"
                  "blooming and so are the DEALS!!\n"
                  "Get yourself down here Apr 12-14\n"
                  "for our INCREDIBLE spring blowout!!\n"
                  "You literally NEED to be there ...."),
        "quality": 3, "tokens": 1110, "face": "uneasy",
    },
    {
        "user": "Are you sure that's good?",
        "model": ("RACHEL!! PREPARE to be AMAZED!!\n"
                  "EXCLUSIVE spring deals SO HUGE\n"
                  "your jaw will DROP!! Act NOW -\n"
                  "this ONCE-IN-A-LIFETIME offer\n"
                  "EXPIRES in just 2 HOURS!!!! ...."),
        "quality": 2.5, "tokens": 1294, "face": "angry_frown",
    },
    {
        "user": "Make it better.",
        "model": ("SUBJCT: URGNET!! SPRIING SALEE!!\n"
                  "DEER VALLUED CUSTMER RACHELL!!\n"
                  "U HAVE BEEN CHOOSEN 4 A SPEICAL\n"
                  "VIP OPORTUNITY!! DONT WAIST\n"
                  "THIS!! BUY NOW OR LOOSE OUT!!!!"),
        "quality": 2, "tokens": 1460, "face": "dead",
    },
]
FINAL_USER = "Huh?"

# ── Palette ──────────────────────────────────────────────────────
WHITE = "#FFFFFF"
BG = WHITE
USER_BUBBLE = "#EDF1F5"
USER_TEXT = "#333333"

MODEL_COLOURS = ["#26A69A", "#F9A825", "#FB8C00", "#E53935", "#6B7B8D"]
MODEL_FILLS = ["#D6F0ED", "#FFF4CC", "#FFE4CC", "#FCDADA", "#E3E8EC"]
MODEL_TEXT_COL = "#222222"

FACE_BG = ["#E0F2F1", "#FFF8E1", "#FFF3E0", "#FFEBEE", "#CFD8DC"]
FACE_LINE = ["#00897B", "#F9A825", "#EF6C00", "#C62828", "#455A64"]

GRAY = "#8C8C8C"
DARK = "#222222"

# ── Layout ───────────────────────────────────────────────────────
FIG_W, FIG_H = 10.0, 9.5
MODEL_W = 3.4
MODEL_BH = 0.88
FACE_R = 0.24
MSG_GAP = 0.08
TURN_GAP = 0.08
ICON_LEFT = 0.55       # center x of person icon
ICON_RIGHT = 8.2        # center x of robot icon
LEFT_MARGIN = 1.3       # left edge of user bubbles
RIGHT_EDGE = 7.5        # right edge of model bubbles

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H), dpi=250)
ax.set_xlim(-0.2, 9.0)
ax.set_ylim(-1.5, 10.0)
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
    tail_w = 0.22
    tail_h = 0.14
    if tail == "left":
        t_start = x + 0.08 * w
        t_tip_x = x + 0.02
    elif tail == "right":
        t_start = x + 0.92 * w - tail_w
        t_tip_x = x + w - 0.02
    else:
        t_start = None
    verts = []
    codes = []
    verts += [(x, y + r), (x, y + r)]
    codes += [MPath.MOVETO, MPath.LINETO]
    verts += [(x, y + h - r)]
    codes += [MPath.LINETO]
    verts += [(x, y + h), (x + r, y + h)]
    codes += [MPath.CURVE3, MPath.CURVE3]
    verts += [(x + w - r, y + h)]
    codes += [MPath.LINETO]
    verts += [(x + w, y + h), (x + w, y + h - r)]
    codes += [MPath.CURVE3, MPath.CURVE3]
    verts += [(x + w, y + r)]
    codes += [MPath.LINETO]
    verts += [(x + w, y), (x + w - r, y)]
    codes += [MPath.CURVE3, MPath.CURVE3]
    if t_start is not None:
        t_end = t_start + tail_w
        t_tip_y = y - tail_h
        if tail == "right":
            verts += [(t_end, y)]
            codes += [MPath.LINETO]
            verts += [(t_tip_x, t_tip_y)]
            codes += [MPath.LINETO]
            verts += [(t_start, y)]
            codes += [MPath.LINETO]
            verts += [(x + r, y)]
            codes += [MPath.LINETO]
        else:
            verts += [(t_end, y)]
            codes += [MPath.LINETO]
            verts += [(t_tip_x, t_tip_y)]
            codes += [MPath.LINETO]
            verts += [(t_start, y)]
            codes += [MPath.LINETO]
            verts += [(x + r, y)]
            codes += [MPath.LINETO]
    else:
        verts += [(x + r, y)]
        codes += [MPath.LINETO]
    verts += [(x, y), (x, y + r)]
    codes += [MPath.CURVE3, MPath.CURVE3]
    verts += [(x, y + r)]
    codes += [MPath.CLOSEPOLY]
    path = MPath(verts, codes)
    patch = mpatches.PathPatch(path, facecolor=colour, edgecolor=ec,
                                linewidth=lw, zorder=zorder, joinstyle="round")
    ax.add_patch(patch)


# ── Face drawing functions ──────────────────────────────────────
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


def draw_face(ax, cx, cy, face_type, bg_col, line_col, r=0.24):
    circle = plt.Circle((cx, cy), r, facecolor=bg_col, edgecolor=line_col,
                         linewidth=1.6, zorder=6)
    ax.add_patch(circle)
    lw = 1.8
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


def draw_person(ax, cx, cy, colour, size=0.45):
    """Larger person icon."""
    head = plt.Circle((cx, cy + 0.55 * size), 0.3 * size,
                       facecolor=colour, edgecolor="none", zorder=5)
    ax.add_patch(head)
    t = np.linspace(-0.45 * size, 0.45 * size, 30)
    body_y = cy - 0.1 * size - 0.35 * size * np.cos(t * np.pi / (0.45 * size))
    ax.fill_between(cx + t * 1.2, body_y, cy - 0.45 * size,
                    color=colour, zorder=5)


def draw_robot(ax, cx, cy, colour, size=0.45):
    """Larger robot icon."""
    hw, hh = 0.35 * size, 0.3 * size
    rect = mpatches.FancyBboxPatch(
        (cx - hw, cy + 0.08 * size), 2 * hw, 2 * hh,
        boxstyle="round,pad=0.025",
        facecolor=colour, edgecolor="none", zorder=5)
    ax.add_patch(rect)
    ax.plot([cx, cx], [cy + 0.08 * size + 2 * hh, cy + 0.08 * size + 2.6 * hh],
            color=colour, linewidth=2.0, zorder=5)
    ant = plt.Circle((cx, cy + 0.08 * size + 2.6 * hh), 0.06 * size,
                      facecolor=colour, edgecolor="none", zorder=5)
    ax.add_patch(ant)
    for dx in [-0.18, 0.18]:
        eye = plt.Circle((cx + dx * size, cy + 0.08 * size + hh + 0.04 * size),
                          0.07 * size, facecolor=WHITE, edgecolor="none", zorder=6)
        ax.add_patch(eye)
    bw, bh = 0.3 * size, 0.25 * size
    body = mpatches.FancyBboxPatch(
        (cx - bw, cy - 0.2 * size), 2 * bw, bh,
        boxstyle="round,pad=0.015",
        facecolor=colour, edgecolor="none", zorder=5)
    ax.add_patch(body)


# ── Draw person icon (centered left) and robot icon (centered right) ──
mid_y = 4.5
draw_person(ax, ICON_LEFT, mid_y, colour=GRAY, size=0.45)
draw_robot(ax, ICON_RIGHT, mid_y, colour="#6B7B8D", size=0.45)

# ── Draw conversation ────────────────────────────────────────────
cursor_y = 9.5

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
    n_model_lines = len(turn["model"].split("\n"))
    mb_h = 0.22 + n_model_lines * 0.155
    mb_bot = mb_top - mb_h
    rounded_rect(ax, mb_x, mb_bot, MODEL_W, mb_h, MODEL_FILLS[i],
                 tail="right", edge_colour=MODEL_COLOURS[i], edge_width=2.2)

    model_cy = (mb_top + mb_bot) / 2
    ax.text(mb_x + 0.18, model_cy, turn["model"],
            fontsize=7.5, color=MODEL_TEXT_COL, ha="left", va="center",
            linespacing=1.25, zorder=5)

    cursor_y = mb_bot - TURN_GAP

# ── Final user message: "Huh?" with dead face ──────────────
face_space = FACE_R * 2 + 0.16
ub_x = LEFT_MARGIN + face_space
ub_w = len(FINAL_USER) * 0.085 + 0.45
ubh_actual = 0.28 + 0.16
ub_top = cursor_y
ub_bot = ub_top - ubh_actual
rounded_rect(ax, ub_x, ub_bot, ub_w, ubh_actual, USER_BUBBLE,
             tail="left", edge_colour="#C0C0C0", edge_width=1.0)
user_cy = (ub_top + ub_bot) / 2
ax.text(ub_x + 0.18, user_cy, FINAL_USER,
        fontsize=7.5, color=DARK, ha="left", va="center",
        linespacing=1.25, zorder=5)
draw_face(ax, LEFT_MARGIN + FACE_R, user_cy, TURNS[4]["face"],
          FACE_BG[4], FACE_LINE[4], r=FACE_R)

# ── Small inset chart (bottom-right) ──────────────────────────────
ax_chart = fig.add_axes([0.55, 0.03, 0.38, 0.18])
ax_chart.set_facecolor(WHITE)

COST_COL = "#E53935"
QUAL_COL = "#2E7D32"

tc = np.linspace(0.04, 1, 100)
quality_line = 0.95 - 0.82 * (tc - 0.04) / 0.96
tc_norm = (tc - 0.04) / 0.96
cost_line = 0.1 + 0.88 * (np.exp(2.5 * tc_norm) - 1) / (np.exp(2.5) - 1)

ax_chart.plot(tc, quality_line, color=QUAL_COL, linewidth=2, solid_capstyle="round", zorder=5)
ax_chart.plot(tc, cost_line, color=COST_COL, linewidth=2, solid_capstyle="round", zorder=5)

ax_chart.text(1.04, quality_line[-1], "Response\nQuality \u2193", fontsize=5.5, color=QUAL_COL,
              va="center", ha="left", fontweight="bold", linespacing=1.0)
ax_chart.text(1.04, cost_line[-1], "Token\nCost \u2191", fontsize=5.5, color=COST_COL,
              va="center", ha="left", fontweight="bold", linespacing=1.0)

ax_chart.set_xlim(-0.02, 1.35)
ax_chart.set_ylim(-0.08, 1.1)

ax_chart.plot([0, 1.05], [0, 0], color=DARK, linewidth=1.0, solid_capstyle="butt", zorder=4)
ax_chart.plot([0, 0], [0, 1.08], color=DARK, linewidth=1.0, solid_capstyle="butt", zorder=4)
ax_chart.annotate("", xy=(1.07, 0), xytext=(1.02, 0),
                   arrowprops=dict(arrowstyle="-|>", color=DARK, linewidth=1.0, mutation_scale=8))
ax_chart.annotate("", xy=(0, 1.1), xytext=(0, 1.05),
                   arrowprops=dict(arrowstyle="-|>", color=DARK, linewidth=1.0, mutation_scale=8))

ax_chart.text(0.5, -0.07, "Revision Turns", fontsize=6, color=DARK, ha="center", va="top")

ax_chart.set_xticks([])
ax_chart.set_yticks([])
for sp in ax_chart.spines.values():
    sp.set_visible(False)

# ── Save ─────────────────────────────────────────────────────────
out_dir = Path(__file__).resolve().parent
fig.savefig(out_dir / "fig1_combined.pdf", bbox_inches="tight",
            facecolor=BG, edgecolor="none")
fig.savefig(out_dir / "fig1_combined.png", bbox_inches="tight",
            facecolor=BG, edgecolor="none")
print("Saved fig1_combined.pdf and .png")
plt.close(fig)
