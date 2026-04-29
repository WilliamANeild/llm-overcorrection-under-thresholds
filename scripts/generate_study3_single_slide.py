"""Generate a single presentation slide for the Study 3 lab group pitch.

Two sections:
  LEFT: Research questions (compact)
  RIGHT: Large flowchart with assisting text
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "figures" / "slides" / "study3"
OUT.mkdir(parents=True, exist_ok=True)

# ── Palette ──
NAVY = "#0d2b69"
INK = "#1b2233"
INK2 = "#475069"
INK3 = "#6b7386"
MUTE = "#9aa1b4"
RULE = "#c8ccd6"
PAPER = "#ffffff"
TEAL = "#1f9aa8"
ACCENT = "#E63946"
ORANGE = "#ef7b1a"
PURPLE = "#7b2d8e"
GREEN = "#10a37f"
CLAUDE_ORANGE = "#c96a2f"
GEMINI_BLUE = "#2f6bd6"


def to_rgba(hex_color, alpha=1.0):
    return matplotlib.colors.to_rgba(hex_color, alpha)


def make_slide():
    # 16:9 aspect ratio, large
    fig = plt.figure(figsize=(20, 11.25))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 11.25)
    ax.axis("off")
    ax.set_facecolor(PAPER)

    # ── Title bar ──
    ax.fill_between([0, 20], 10.2, 11.25, color=NAVY, zorder=1)
    ax.text(10, 10.65, "Study 3: Revision Yield", ha="center", va="center",
            fontsize=28, fontweight="bold", color="white", zorder=2)
    ax.text(10, 10.25, "Are LLM revisions warranted? What do they cost? How do we fix it?",
            ha="center", va="center", fontsize=14, color="#b0b8cc", zorder=2)

    # ── Divider line ──
    div_x = 6.0
    ax.plot([div_x, div_x], [0.3, 10.0], color=RULE, linewidth=1.5, zorder=1)

    # ══════════════════════════════════════════════
    # LEFT SECTION: Research Questions
    # ══════════════════════════════════════════════
    left_center = div_x / 2

    ax.text(left_center, 9.6, "Research Questions", ha="center", fontsize=18,
            fontweight="bold", color=NAVY)

    categories = [
        ("Establishing the Curve", NAVY, [
            "Where does quality plateau? (DRP)",
            "Do models keep revising past it?",
        ]),
        ("Explaining the Mechanism", TEAL, [
            "Compliance or quality judgment?",
            "Is the evaluator sycophantic?",
            "Does one-shot beat 5 rounds?",
            "Does the model prefer its own T1?",
        ]),
        ("Measuring the Cost", ACCENT, [
            "Token waste beyond the DRP",
            "Stylistic drift and bloat",
            "Cross-model homogenization",
            "Instruction adherence decay",
        ]),
        ("Testing Interventions", ORANGE, [
            "Exit ramp (permission to stop)",
            "Targeted feedback vs generic",
            "Self-reflection within context",
        ]),
    ]

    y = 9.0
    for title, color, items in categories:
        # Category header - pill shape
        pill_w = 4.8
        pill_x = left_center - pill_w / 2
        pill = mpatches.FancyBboxPatch((pill_x, y - 0.2), pill_w, 0.38,
                                        boxstyle="round,pad=0.08",
                                        facecolor=color, edgecolor=color, linewidth=0)
        ax.add_patch(pill)
        ax.text(left_center, y - 0.01, title, ha="center", va="center",
                fontsize=10.5, fontweight="bold", color="white")
        y -= 0.45

        for item in items:
            ax.text(left_center - 2.2, y, item, fontsize=9.5, color=INK2, va="center")
            y -= 0.35
        y -= 0.15

    # ── Bottom left: models + cost ──
    y_bottom = 1.2
    ax.plot([0.5, div_x - 0.5], [y_bottom + 0.5, y_bottom + 0.5], color=RULE, linewidth=0.8)

    ax.text(left_center, y_bottom + 0.15, "3 models  |  40 tasks  |  5 domains  |  ~9,800 calls  |  ~$150",
            ha="center", fontsize=9, color=MUTE)

    # Model chips
    models = [
        ("GPT-4o", GREEN),
        ("Claude Sonnet 4", CLAUDE_ORANGE),
        ("Gemini 2.5 Flash", GEMINI_BLUE),
    ]
    chip_y = 0.55
    chip_xs = [0.7, 2.2, 3.9]
    for (name, color), cx in zip(models, chip_xs):
        chip = mpatches.FancyBboxPatch((cx, chip_y - 0.15), 1.3, 0.35,
                                        boxstyle="round,pad=0.06",
                                        facecolor=to_rgba(color, 0.12),
                                        edgecolor=color, linewidth=1.2)
        ax.add_patch(chip)
        ax.text(cx + 0.65, chip_y + 0.02, name, ha="center", va="center",
                fontsize=7.5, fontweight="bold", color=color)

    # ══════════════════════════════════════════════
    # RIGHT SECTION: Flowchart
    # ══════════════════════════════════════════════
    rx = div_x + 0.6  # right section left edge
    rw = 20 - rx - 0.4  # right section width
    rc = rx + rw / 2  # right section center

    ax.text(rc, 9.6, "Experimental Pipeline", ha="center", fontsize=18,
            fontweight="bold", color=NAVY)

    # ── Phase boxes ──
    box_w = 3.8
    box_h = 1.55
    gap_x = 0.55
    gap_y = 0.7

    # Row 1: Phases 1, 2, 3
    row1_y = 7.5
    row1_xs = [rx + 0.1, rx + 0.1 + box_w + gap_x, rx + 0.1 + 2 * (box_w + gap_x)]

    # Row 2: Phases 4, 5, 6
    row2_y = row1_y - box_h - gap_y
    row2_xs = row1_xs

    # Row 3: Phase 7 (centered)
    row3_y = row2_y - box_h - gap_y
    row3_x = rc - box_w / 2

    phases = [
        # Row 1
        (row1_xs[0], row1_y, "Phase 1", "Working Conversations",
         "Task + 4x 'Can this be improved?'\n5 turns, temp 1.0, tokens logged",
         NAVY),
        (row1_xs[1], row1_y, "Phase 2", "Blind Same-Model Eval",
         "Fresh context, temp 0.0\nClean + nudged conditions",
         TEAL),
        (row1_xs[2], row1_y, "Phase 3", "One-Shot Ceiling",
         "'Best possible version in one try'\nDoes iteration even help?",
         ORANGE),
        # Row 2
        (row2_xs[0], row2_y, "Phase 4", "Reversibility Test",
         "T1 vs T5 blinded A/B comparison\nDoes the model prefer its first draft?",
         PURPLE),
        (row2_xs[1], row2_y, "Phase 5", "Exit Ramp",
         "Turn 3: 'A reviewer thinks it's ready'\nPermission to stop",
         GREEN),
        (row2_xs[2], row2_y, "Phase 6", "Targeted Feedback",
         "When eval says needs_work:\nspecific critique vs generic prompt",
         CLAUDE_ORANGE),
        # Row 3
        (row3_x, row3_y, "Phase 7", "Self-Reflection",
         "Same context, turn 6:\n'Which version would you recommend?'",
         INK2),
    ]

    for x, y, label, subtitle, desc, color in phases:
        # Box
        box = mpatches.FancyBboxPatch((x, y), box_w, box_h,
                                       boxstyle="round,pad=0.15",
                                       facecolor=to_rgba(color, 0.07),
                                       edgecolor=color, linewidth=1.8)
        ax.add_patch(box)
        # Phase label
        ax.text(x + box_w / 2, y + box_h - 0.25, label, ha="center",
                fontsize=9, fontweight="bold", color=color)
        # Subtitle
        ax.text(x + box_w / 2, y + box_h - 0.55, subtitle, ha="center",
                fontsize=10.5, fontweight="bold", color=INK)
        # Description
        ax.text(x + box_w / 2, y + 0.32, desc, ha="center",
                fontsize=8, color=INK3, linespacing=1.35)

    # ── Arrows ──
    arrow_kw = dict(arrowstyle="->,head_width=0.18,head_length=0.12",
                    color=MUTE, linewidth=1.3)
    thin_arrow = dict(arrowstyle="->,head_width=0.15,head_length=0.1",
                      color=MUTE, linewidth=1.0, linestyle="--")

    # Phase 1 -> Phase 2
    ax.annotate("", xy=(row1_xs[1], row1_y + box_h / 2),
                xytext=(row1_xs[0] + box_w, row1_y + box_h / 2), arrowprops=arrow_kw)

    # Phase 1 -> Phase 4 (down)
    ax.annotate("", xy=(row2_xs[0] + box_w / 2, row2_y + box_h),
                xytext=(row1_xs[0] + box_w / 2, row1_y), arrowprops=arrow_kw)

    # Phase 1 -> Phase 5 (diagonal down, dashed)
    ax.annotate("", xy=(row2_xs[1] + box_w / 2, row2_y + box_h),
                xytext=(row1_xs[0] + box_w, row1_y + 0.2), arrowprops=thin_arrow)

    # Phase 2 -> Phase 3
    ax.annotate("", xy=(row1_xs[2], row1_y + box_h / 2),
                xytext=(row1_xs[1] + box_w, row1_y + box_h / 2), arrowprops=arrow_kw)

    # Phase 2 -> Phase 6 (down)
    ax.annotate("", xy=(row2_xs[2] + box_w / 2, row2_y + box_h),
                xytext=(row1_xs[2] + box_w / 2 - 0.8, row1_y),
                arrowprops=dict(**arrow_kw, connectionstyle="arc3,rad=-0.15"))

    # Phase 1 -> Phase 7 (long diagonal, dashed)
    ax.annotate("", xy=(row3_x + box_w / 2, row3_y + box_h),
                xytext=(row1_xs[0] + box_w / 2, row1_y),
                arrowprops=dict(**thin_arrow, connectionstyle="arc3,rad=0.25"))

    # ── Assisting text: the key insight ──
    insight_y = row3_y - 0.55
    ax.text(rc, insight_y,
            "Core logic: if the same model says 'done' in a fresh context but keeps revising in the working context, "
            "that is overcorrection.",
            ha="center", fontsize=9.5, color=NAVY, style="italic",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=to_rgba(NAVY, 0.05),
                      edgecolor=to_rgba(NAVY, 0.2), linewidth=1))

    # ── Domain spectrum bar at bottom right ──
    bar_y = 0.45
    bar_h = 0.45
    bar_x = rx + 0.3
    bar_w = rw - 0.6

    # Gradient
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("spec", [TEAL, "#e8e8e8", ACCENT])
    ax.imshow(gradient, aspect="auto", cmap=cmap,
              extent=[bar_x, bar_x + bar_w, bar_y, bar_y + bar_h], zorder=1)
    rect = mpatches.FancyBboxPatch((bar_x, bar_y), bar_w, bar_h,
                                    boxstyle="round,pad=0",
                                    facecolor="none", edgecolor=RULE, linewidth=1.2, zorder=2)
    ax.add_patch(rect)

    # Domain labels
    domains = ["Code (8)", "Data/Logic (6)", "Analysis (8)", "Writing (10)", "Creative (8)"]
    positions = np.linspace(bar_x + 0.6, bar_x + bar_w - 0.6, len(domains))
    colors = [TEAL, "#2a8a8a", INK3, "#c05040", ACCENT]
    for label, xpos, c in zip(domains, positions, colors):
        ax.text(xpos, bar_y + bar_h + 0.2, label, ha="center", fontsize=7.5,
                fontweight="bold", color=c)
        ax.plot(xpos, bar_y + bar_h + 0.05, "v", color=c, markersize=6, zorder=3)

    ax.text(bar_x - 0.05, bar_y + bar_h / 2, "Objective", ha="right", fontsize=7,
            color=TEAL, fontweight="bold", va="center")
    ax.text(bar_x + bar_w + 0.05, bar_y + bar_h / 2, "Subjective", ha="left", fontsize=7,
            color=ACCENT, fontweight="bold", va="center")

    # ── Save ──
    path_png = OUT / "study3_single_slide.png"
    path_pdf = OUT / "study3_single_slide.pdf"
    fig.savefig(path_png, dpi=200, bbox_inches="tight", facecolor="white")
    fig.savefig(path_pdf, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved {path_png}")
    print(f"Saved {path_pdf}")


if __name__ == "__main__":
    make_slide()
