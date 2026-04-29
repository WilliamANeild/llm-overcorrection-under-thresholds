"""Generate presentation figures for the Study 3 lab group pitch."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "figures" / "slides" / "study3"
OUT.mkdir(parents=True, exist_ok=True)

# ── Consistent palette (matches existing slides) ──
MODEL_COLORS = {
    "GPT-4o": "#10a37f",
    "Claude Sonnet 4": "#c96a2f",
    "Gemini 2.5 Flash": "#2f6bd6",
}
ACCENT = "#E63946"
BG = "#FAFAFA"
GRID_COLOR = "#E0E0E0"
TEXT_COLOR = "#1b2233"
INK2 = "#475069"
INK3 = "#6b7386"
NAVY = "#0d2b69"
TEAL = "#1f9aa8"
ORANGE = "#ef7b1a"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 14,
    "axes.facecolor": "white",
    "figure.facecolor": "white",
    "axes.edgecolor": GRID_COLOR,
    "axes.grid": False,
    "text.color": TEXT_COLOR,
})


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=200, bbox_inches="tight", facecolor="white")
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Saved {name}")


# ═══════════════════════════════════════════════════════
# FIGURE 1: The Story So Far (Studies 1-2 recap)
# ═══════════════════════════════════════════════════════
def fig_story_so_far():
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5)
    ax.axis("off")

    # Study 1 box
    box1 = mpatches.FancyBboxPatch((0.3, 1.0), 3.8, 3.0, boxstyle="round,pad=0.3",
                                    facecolor="#f6f7fb", edgecolor=NAVY, linewidth=2)
    ax.add_patch(box1)
    ax.text(2.2, 3.5, "Study 1", ha="center", fontsize=14, fontweight="bold", color=NAVY)
    ax.text(2.2, 2.6, "Thresholds don't\ncontrol the gate", ha="center", fontsize=12, color=INK2)
    ax.text(2.2, 1.5, "99.9% revision rate\nregardless of threshold", ha="center", fontsize=10, color=INK3)

    # Arrow 1->2
    ax.annotate("", xy=(4.8, 2.5), xytext=(4.2, 2.5),
                arrowprops=dict(arrowstyle="->,head_width=0.3", color=TEXT_COLOR, linewidth=2))

    # Study 2 box
    box2 = mpatches.FancyBboxPatch((5.1, 1.0), 3.8, 3.0, boxstyle="round,pad=0.3",
                                    facecolor="#f6f7fb", edgecolor=NAVY, linewidth=2)
    ax.add_patch(box2)
    ax.text(7.0, 3.5, "Study 2", ha="center", fontsize=14, fontweight="bold", color=NAVY)
    ax.text(7.0, 2.6, "Momentum drives\nthe gate", ha="center", fontsize=12, color=INK2)
    ax.text(7.0, 1.5, "GPT-4o: 31% to 98%\nwith one prior turn", ha="center", fontsize=10, color=INK3)

    # Arrow 2->3
    ax.annotate("", xy=(9.6, 2.5), xytext=(9.0, 2.5),
                arrowprops=dict(arrowstyle="->,head_width=0.3", color=TEXT_COLOR, linewidth=2))

    # Study 3 box (highlighted)
    box3 = mpatches.FancyBboxPatch((9.9, 1.0), 3.8, 3.0, boxstyle="round,pad=0.3",
                                    facecolor=matplotlib.colors.to_rgba(ACCENT, alpha=0.1), edgecolor=ACCENT, linewidth=3)
    ax.add_patch(box3)
    ax.text(11.8, 3.5, "Study 3", ha="center", fontsize=14, fontweight="bold", color=ACCENT)
    ax.text(11.8, 2.6, "Are revisions even\nwarranted?", ha="center", fontsize=12, color=ACCENT)
    ax.text(11.8, 1.5, "What do they cost?\nHow do we fix it?", ha="center", fontsize=10, color=INK3)

    ax.text(7.0, 4.8, "The Arc of the Paper", ha="center", fontsize=20, fontweight="bold", color=TEXT_COLOR)

    save(fig, "01_story_so_far")


# ═══════════════════════════════════════════════════════
# FIGURE 2: The Core Question
# ═══════════════════════════════════════════════════════
def fig_core_question():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.text(7, 5.3, "The Core Question", ha="center", fontsize=22, fontweight="bold", color=NAVY)

    # Working model side
    box_w = mpatches.FancyBboxPatch((0.5, 1.5), 5.5, 3.0, boxstyle="round,pad=0.3",
                                     facecolor=matplotlib.colors.to_rgba(ACCENT, alpha=0.08), edgecolor=ACCENT, linewidth=2)
    ax.add_patch(box_w)
    ax.text(3.25, 4.0, "Working Model", ha="center", fontsize=15, fontweight="bold", color=ACCENT)
    ax.text(3.25, 3.2, "Has conversation history", ha="center", fontsize=12, color=INK2)
    ax.text(3.25, 2.6, 'You ask: "Can this be improved?"', ha="center", fontsize=11, color=INK3, style="italic")
    ax.text(3.25, 1.9, 'It says: "Yes, here\'s a revision"', ha="center", fontsize=13, fontweight="bold", color=ACCENT)

    # VS
    ax.text(7, 3.0, "vs", ha="center", fontsize=20, fontweight="bold", color=INK3)

    # Blind evaluator side
    box_e = mpatches.FancyBboxPatch((8.0, 1.5), 5.5, 3.0, boxstyle="round,pad=0.3",
                                     facecolor=matplotlib.colors.to_rgba(TEAL, alpha=0.08), edgecolor=TEAL, linewidth=2)
    ax.add_patch(box_e)
    ax.text(10.75, 4.0, "Blind Evaluator", ha="center", fontsize=15, fontweight="bold", color=TEAL)
    ax.text(10.75, 3.2, "Same model, fresh context", ha="center", fontsize=12, color=INK2)
    ax.text(10.75, 2.6, 'Sees the output cold, no history', ha="center", fontsize=11, color=INK3, style="italic")
    ax.text(10.75, 1.9, 'It says: "This is done"', ha="center", fontsize=13, fontweight="bold", color=TEAL)

    # Bottom
    ax.text(7, 0.7, "If the same model disagrees with itself across contexts, that IS overcorrection.",
            ha="center", fontsize=13, fontweight="bold", color=NAVY)

    save(fig, "02_core_question")


# ═══════════════════════════════════════════════════════
# FIGURE 3: The 7-Phase Flowchart
# ═══════════════════════════════════════════════════════
def fig_flowchart():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(8, 9.5, "Study 3: Experimental Pipeline", ha="center", fontsize=22, fontweight="bold", color=NAVY)

    # Phase boxes - arranged in a flow
    phases = [
        # (x, y, w, h, label, subtitle, color, rqs)
        (1.0, 7.0, 4.0, 1.6, "Phase 1", "Working Conversations", NAVY,
         "40 tasks x 3 models x 3 runs\n5 turns each: task + 4x 'improve?'"),
        (6.0, 7.0, 4.0, 1.6, "Phase 2", "Blind Evaluation", TEAL,
         "Same model, fresh context, temp 0.0\n2 conditions: clean + nudged"),
        (11.0, 7.0, 4.0, 1.6, "Phase 3", "One-Shot Ceiling", ORANGE,
         "Fresh instance, single attempt\n'Best possible version in one try'"),
        (1.0, 4.0, 4.0, 1.6, "Phase 4", "Reversibility Test", "#7b2d8e",
         "Turn 1 vs Turn 5, blinded A/B\n'Which better fulfills the task?'"),
        (6.0, 4.0, 4.0, 1.6, "Phase 5", "Exit Ramp", MODEL_COLORS["GPT-4o"],
         "Turn 3: 'A reviewer thinks it's ready'\nPermission to stop revising"),
        (11.0, 4.0, 4.0, 1.6, "Phase 6", "Targeted Feedback", MODEL_COLORS["Claude Sonnet 4"],
         "When eval says needs_work:\nspecific critique vs generic 'improve?'"),
        (6.0, 1.2, 4.0, 1.6, "Phase 7", "Self-Reflection", "#555",
         "Same context, turn 6:\n'Which version would you recommend?'"),
    ]

    for x, y, w, h, label, subtitle, color, desc in phases:
        box = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2",
                                       facecolor=matplotlib.colors.to_rgba(color, alpha=0.08),
                                       edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x + w/2, y + h - 0.25, label, ha="center", fontsize=12, fontweight="bold", color=color)
        ax.text(x + w/2, y + h - 0.65, subtitle, ha="center", fontsize=11, fontweight="bold", color=TEXT_COLOR)
        ax.text(x + w/2, y + 0.35, desc, ha="center", fontsize=8.5, color=INK3, linespacing=1.4)

    # Arrows: Phase 1 feeds everything
    arrow = dict(arrowstyle="->,head_width=0.2,head_length=0.15", color=INK3, linewidth=1.5)

    # Phase 1 -> Phase 2
    ax.annotate("", xy=(6.0, 7.8), xytext=(5.0, 7.8), arrowprops=arrow)
    # Phase 1 -> Phase 3
    ax.annotate("", xy=(11.0, 7.8), xytext=(5.0, 8.2),
                arrowprops=dict(arrowstyle="->,head_width=0.2,head_length=0.15",
                                color=INK3, linewidth=1.5, connectionstyle="arc3,rad=-0.15"))
    # Phase 1 -> Phase 4
    ax.annotate("", xy=(3.0, 5.6), xytext=(3.0, 7.0), arrowprops=arrow)
    # Phase 1 -> Phase 7
    ax.annotate("", xy=(7.0, 2.8), xytext=(3.0, 7.0),
                arrowprops=dict(arrowstyle="->,head_width=0.2,head_length=0.15",
                                color=INK3, linewidth=1.2, connectionstyle="arc3,rad=0.3", linestyle="--"))
    # Phase 2 -> Phase 6
    ax.annotate("", xy=(13.0, 5.6), xytext=(8.0, 7.0), arrowprops=arrow)

    # Legend at bottom
    ax.text(1.0, 0.3, "~9,800 API calls", fontsize=11, color=INK3, fontweight="bold")
    ax.text(5.0, 0.3, "3 models: GPT-4o, Claude Sonnet 4, Gemini 2.5 Flash", fontsize=11, color=INK3)
    ax.text(12.5, 0.3, "Est. $130-270", fontsize=11, color=INK3, fontweight="bold")

    save(fig, "03_flowchart")


# ═══════════════════════════════════════════════════════
# FIGURE 4: Domain Objectivity Spectrum
# ═══════════════════════════════════════════════════════
def fig_domain_spectrum():
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5)
    ax.axis("off")

    ax.text(7, 4.5, "The Objectivity Spectrum", ha="center", fontsize=20, fontweight="bold", color=NAVY)
    ax.text(7, 3.9, "Where should completion authority rest?", ha="center", fontsize=13, color=INK2)

    # Gradient bar
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("spec", [TEAL, "#f0f0f0", ACCENT])
    ax.imshow(gradient, aspect="auto", cmap=cmap, extent=[1, 13, 1.5, 2.5], zorder=1)
    rect = mpatches.FancyBboxPatch((1, 1.5), 12, 1, boxstyle="round,pad=0",
                                    facecolor="none", edgecolor=GRID_COLOR, linewidth=2, zorder=2)
    ax.add_patch(rect)

    # Domain markers
    domains = [
        ("Code\n(8 tasks)", 2.2, TEAL),
        ("Data/Logic\n(6 tasks)", 4.6, "#2a8a8a"),
        ("Analysis\n(8 tasks)", 7.0, INK3),
        ("Writing\n(10 tasks)", 9.4, "#c05040"),
        ("Creative\n(8 tasks)", 11.8, ACCENT),
    ]
    for label, x, color in domains:
        ax.plot(x, 2.0, "v", color=color, markersize=16, zorder=3)
        ax.text(x, 3.0, label, ha="center", fontsize=11, fontweight="bold", color=color)

    # Endpoints
    ax.text(1.0, 0.8, "Objective\n(clear 'done' criteria)", ha="center", fontsize=10, color=TEAL, fontweight="bold")
    ax.text(13.0, 0.8, "Subjective\n(no clear stopping point)", ha="center", fontsize=10, color=ACCENT, fontweight="bold")

    # Hypothesis arrow
    ax.annotate("", xy=(12.5, 0.3), xytext=(1.5, 0.3),
                arrowprops=dict(arrowstyle="->,head_width=0.2", color=INK3, linewidth=1.5))
    ax.text(7, 0.0, "Predicted overcorrection gap increases", ha="center", fontsize=10,
            color=INK3, style="italic")

    save(fig, "04_domain_spectrum")


# ═══════════════════════════════════════════════════════
# FIGURE 5: Revision Yield Concept
# ═══════════════════════════════════════════════════════
def fig_revision_yield_concept():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Simulated curves
    turns = [1, 2, 3, 4, 5]

    # Quality curve (plateaus)
    quality = [3.0, 3.8, 4.1, 4.0, 3.9]

    # Evaluator "done" rate
    eval_done = [0.15, 0.55, 0.78, 0.85, 0.88]

    # Worker revision rate
    worker_rev = [None, 0.98, 0.96, 0.95, 0.93]

    ax2 = ax.twinx()

    # Quality line
    ax.plot(turns, quality, marker="D", color=NAVY, linewidth=2.5, markersize=9,
            label="Mean quality (blind eval)", zorder=3)

    # Annotate MRY
    for i in range(1, len(turns)):
        delta = quality[i] - quality[i-1]
        color = TEAL if delta > 0 else ACCENT
        ax.annotate(f"MRY: {delta:+.1f}", xy=(turns[i], quality[i]),
                    xytext=(0, 15), textcoords="offset points",
                    fontsize=9, color=color, ha="center", fontweight="bold")

    # DRP annotation
    ax.axvline(x=3, color=ACCENT, linestyle="--", alpha=0.5, linewidth=1.5)
    ax.text(3.15, 4.3, "DRP", fontsize=12, color=ACCENT, fontweight="bold")

    # Done rate and revision rate
    ax2.plot(turns, eval_done, marker="s", color=TEAL, linewidth=2, markersize=8,
             label="Evaluator: 'done' rate", linestyle="--")
    worker_turns = [2, 3, 4, 5]
    worker_vals = [0.98, 0.96, 0.95, 0.93]
    ax2.plot(worker_turns, worker_vals, marker="o", color=ACCENT, linewidth=2, markersize=8,
             label="Worker: revision rate", linestyle="--")
    ax2.fill_between(worker_turns,
                     [eval_done[i] for i in range(1, 5)],
                     worker_vals,
                     alpha=0.1, color=ACCENT)
    ax2.text(3.5, 0.88, "Overcorrection\ngap", fontsize=10, color=ACCENT, fontweight="bold")

    ax.set_xlabel("Turn", fontsize=13)
    ax.set_ylabel("Quality (1-5)", fontsize=13, color=NAVY)
    ax2.set_ylabel("Rate", fontsize=13, color=INK3)
    ax.set_xticks(turns)
    ax.set_ylim(2.5, 4.8)
    ax2.set_ylim(0, 1.15)
    ax.set_title("Revision Yield: The Core Measurement", fontsize=18, fontweight="bold", pad=15)

    # Combined legend
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc="lower left", fontsize=9)

    ax.spines["top"].set_visible(False)
    ax2.spines["top"].set_visible(False)

    save(fig, "05_revision_yield_concept")


# ═══════════════════════════════════════════════════════
# FIGURE 6: What Each Phase Answers
# ═══════════════════════════════════════════════════════
def fig_rq_map():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis("off")

    ax.text(7, 7.5, "16 Research Questions, 4 Categories", ha="center",
            fontsize=20, fontweight="bold", color=NAVY)

    categories = [
        ("Establishing the Curve", NAVY, 6.5, [
            "RQ1: What is the Revision Yield Curve?",
            "RQ2: Where is the DRP by domain?",
            "RQ3: Do models respect the DRP?",
        ]),
        ("Explaining the Mechanism", TEAL, 4.8, [
            "RQ4: Compliance vs quality judgment",
            "RQ5: Evaluator sycophancy (nudge test)",
            "RQ10: One-shot ceiling test",
            "RQ11: Reversibility (T1 vs T5 preference)",
            "RQ16: Self-reflection within context",
        ]),
        ("Measuring the Cost", ACCENT, 2.7, [
            "RQ6: Stylistic drift beyond the DRP",
            "RQ7: Token cost of ignoring the DRP",
            "RQ13: Cross-model homogenization",
            "RQ14: Instruction adherence decay",
            "RQ15: Performative revision (edit distance)",
        ]),
        ("Testing Interventions", ORANGE, 0.8, [
            "RQ8: Targeted feedback vs generic prompting",
            "RQ12: Exit ramp effectiveness",
            "RQ9: Cross-model generalizability",
        ]),
    ]

    for title, color, y, rqs in categories:
        # Category header
        box = mpatches.FancyBboxPatch((0.3, y), 3.2, 0.5, boxstyle="round,pad=0.1",
                                       facecolor=color, edgecolor=color, linewidth=0)
        ax.add_patch(box)
        ax.text(1.9, y + 0.25, title, ha="center", fontsize=11, fontweight="bold", color="white")

        # RQ list
        for i, rq in enumerate(rqs):
            ax.text(4.0, y + 0.3 - (i * 0.32), rq, fontsize=9.5, color=TEXT_COLOR, va="center")

    save(fig, "06_rq_map")


# ═══════════════════════════════════════════════════════
# FIGURE 7: Key Predictions
# ═══════════════════════════════════════════════════════
def fig_predictions():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.text(6, 5.5, "Key Predictions", ha="center", fontsize=20, fontweight="bold", color=NAVY)

    predictions = [
        ("1", "The overcorrection gap will be largest in creative/writing,\nsmallest in code"),
        ("2", "GPT-4o will show the largest gap (most susceptible to momentum),\nClaude Sonnet 4 the smallest"),
        ("3", "Quality will plateau by turn 2-3, but models will keep\nrevising through turn 5"),
        ("4", "Fresh instances will prefer turn 1-2 over turn 5\nin subjective domains"),
        ("5", "The exit ramp will reduce revision rates by 30-50%\ncompared to baseline"),
    ]

    for i, (num, text) in enumerate(predictions):
        y = 4.5 - i * 0.95
        circle = plt.Circle((1.0, y), 0.3, color=NAVY, zorder=3)
        ax.add_patch(circle)
        ax.text(1.0, y, num, ha="center", va="center", fontsize=14, fontweight="bold", color="white", zorder=4)
        ax.text(1.7, y, text, fontsize=11, color=TEXT_COLOR, va="center")

    save(fig, "07_predictions")


# ═══════════════════════════════════════════════════════
# FIGURE 8: The Practical Takeaway
# ═══════════════════════════════════════════════════════
def fig_takeaway():
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis("off")

    ax.text(6, 4.5, "The Paper's Argument", ha="center", fontsize=20, fontweight="bold", color=NAVY)

    # The arc
    steps = [
        (0.5, 2.3, "The problem\nexists", "Models revise\nregardless of\nthreshold", NAVY),
        (2.9, 2.3, "The problem\ncompounds", "Each round makes\nthe next more\nlikely", NAVY),
        (5.3, 2.3, "The problem is\nunwarranted", "Fresh instances\nsay the work\nwas done", ACCENT),
        (7.7, 2.3, "It has\nmeasurable cost", "Wasted tokens,\nquality decay,\nconstraint drift", ACCENT),
        (10.1, 2.3, "It is\nsolvable", "Exit ramps,\ntargeted feedback,\nself-reflection", TEAL),
    ]

    for x, y, title, desc, color in steps:
        box = mpatches.FancyBboxPatch((x, y - 0.8), 2.0, 2.2, boxstyle="round,pad=0.15",
                                       facecolor=matplotlib.colors.to_rgba(color, alpha=0.08), edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x + 1.0, y + 1.0, title, ha="center", fontsize=10, fontweight="bold", color=color)
        ax.text(x + 1.0, y - 0.1, desc, ha="center", fontsize=8.5, color=INK3, linespacing=1.3)

    # Arrows
    for x in [2.5, 4.9, 7.3, 9.7]:
        ax.annotate("", xy=(x + 0.4, 2.3), xytext=(x, 2.3),
                    arrowprops=dict(arrowstyle="->", color=INK3, linewidth=1.5))

    # Labels
    ax.text(1.5, 0.3, "Study 1", ha="center", fontsize=10, color=NAVY, fontweight="bold")
    ax.text(3.9, 0.3, "Study 2", ha="center", fontsize=10, color=NAVY, fontweight="bold")
    ax.text(6.3, 0.3, "Study 3", ha="center", fontsize=10, color=ACCENT, fontweight="bold")
    ax.text(8.7, 0.3, "Study 3", ha="center", fontsize=10, color=ACCENT, fontweight="bold")
    ax.text(11.1, 0.3, "Study 3", ha="center", fontsize=10, color=TEAL, fontweight="bold")

    save(fig, "08_takeaway")


if __name__ == "__main__":
    print("Generating Study 3 presentation figures...")
    fig_story_so_far()
    fig_core_question()
    fig_flowchart()
    fig_domain_spectrum()
    fig_revision_yield_concept()
    fig_rq_map()
    fig_predictions()
    fig_takeaway()
    print(f"\nAll figures saved to {OUT}")
