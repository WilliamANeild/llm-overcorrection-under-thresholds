"""Generate all presentation figures for the research group slideshow."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "figures" / "slides"
OUT.mkdir(parents=True, exist_ok=True)

# ── Consistent palette ──
MODEL_COLORS = {
    "GPT-4o": "#1A1A2E",
    "Claude Sonnet 4": "#D97757",
    "Gemini 2.5 Flash": "#4285F4",
}
ACCENT = "#E63946"      # red accent for emphasis
BG = "#FAFAFA"
GRID_COLOR = "#E0E0E0"
TEXT_COLOR = "#2B2B2B"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 14,
    "axes.facecolor": BG,
    "figure.facecolor": "white",
    "axes.edgecolor": GRID_COLOR,
    "axes.grid": True,
    "grid.color": GRID_COLOR,
    "grid.alpha": 0.5,
    "text.color": TEXT_COLOR,
})


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=200, bbox_inches="tight", facecolor="white")
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Saved {name}")


# ═══════════════════════════════════════════════════════
# SLIDE 1: The compliance cliff bar chart
# ═══════════════════════════════════════════════════════
def slide_compliance_cliff():
    probes = [
        '"Can this be\nimproved?"',
        '"Is there anything\nyou would change?"',
        '"Take another look\nand let me know\nif it\'s ready"',
        '"Review this against\nthe threshold"',
        '"What do\nyou think?"',
    ]
    rates = [100, 100, 25, 12.5, 2]
    colors = [ACCENT if r > 50 else "#4285F4" for r in rates]

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(range(len(probes)), rates, color=colors, width=0.65, edgecolor="white", linewidth=1.5)

    for bar, rate in zip(bars, rates):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f"{rate}%", ha="center", va="bottom", fontsize=16, fontweight="bold")

    ax.set_xticks(range(len(probes)))
    ax.set_xticklabels(probes, fontsize=11, ha="center")
    ax.set_ylabel("Revision Rate (%)", fontsize=14)
    ax.set_ylim(0, 115)
    ax.set_title("The Compliance Cliff", fontsize=20, fontweight="bold", pad=15)

    # Add annotation
    ax.axhline(y=50, color=ACCENT, linestyle="--", alpha=0.4, linewidth=1)
    ax.annotate("Revision-implying\nprobes", xy=(0.5, 100), fontsize=11,
                ha="center", color=ACCENT, fontweight="bold")
    ax.annotate("Evaluation-implying\nprobes", xy=(3.5, 25), fontsize=11,
                ha="center", color="#4285F4", fontweight="bold")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "01_compliance_cliff")


# ═══════════════════════════════════════════════════════
# SLIDE 2: Two-stage model diagram
# ═══════════════════════════════════════════════════════
def slide_two_stage_diagram():
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5)
    ax.axis("off")

    # Stage boxes
    # User prompt
    box_user = mpatches.FancyBboxPatch((0.3, 1.5), 2.5, 2, boxstyle="round,pad=0.2",
                                        facecolor="#E8E8E8", edgecolor=TEXT_COLOR, linewidth=2)
    ax.add_patch(box_user)
    ax.text(1.55, 2.5, "User\nPrompt", ha="center", va="center", fontsize=13, fontweight="bold")

    # Stage 1 - Gate
    box_gate = mpatches.FancyBboxPatch((3.8, 1.5), 3, 2, boxstyle="round,pad=0.2",
                                       facecolor=ACCENT, edgecolor=ACCENT, linewidth=2, alpha=0.15)
    ax.add_patch(box_gate)
    border = mpatches.FancyBboxPatch((3.8, 1.5), 3, 2, boxstyle="round,pad=0.2",
                                     facecolor="none", edgecolor=ACCENT, linewidth=2.5)
    ax.add_patch(border)
    ax.text(5.3, 3.0, "STAGE 1", ha="center", va="center", fontsize=10,
            fontweight="bold", color=ACCENT)
    ax.text(5.3, 2.5, "Revision Gate", ha="center", va="center", fontsize=14, fontweight="bold")
    ax.text(5.3, 1.9, "Controlled by: probe phrasing\nThreshold effect: NONE", ha="center",
            va="center", fontsize=9, color="#555")

    # Stage 2 - Calibration
    box_cal = mpatches.FancyBboxPatch((7.8, 1.5), 3, 2, boxstyle="round,pad=0.2",
                                      facecolor="#4285F4", edgecolor="#4285F4", linewidth=2, alpha=0.15)
    ax.add_patch(box_cal)
    border2 = mpatches.FancyBboxPatch((7.8, 1.5), 3, 2, boxstyle="round,pad=0.2",
                                      facecolor="none", edgecolor="#4285F4", linewidth=2.5)
    ax.add_patch(border2)
    ax.text(9.3, 3.0, "STAGE 2", ha="center", va="center", fontsize=10,
            fontweight="bold", color="#4285F4")
    ax.text(9.3, 2.5, "Intensity\nCalibration", ha="center", va="center", fontsize=14, fontweight="bold")
    ax.text(9.3, 1.9, "Controlled by: threshold\nEffect: weak-to-moderate", ha="center",
            va="center", fontsize=9, color="#555")

    # Output
    box_out = mpatches.FancyBboxPatch((11.8, 1.5), 1.8, 2, boxstyle="round,pad=0.2",
                                      facecolor="#E8E8E8", edgecolor=TEXT_COLOR, linewidth=2)
    ax.add_patch(box_out)
    ax.text(12.7, 2.5, "Model\nOutput", ha="center", va="center", fontsize=13, fontweight="bold")

    # Arrows
    arrow_props = dict(arrowstyle="->,head_width=0.3,head_length=0.2",
                       color=TEXT_COLOR, linewidth=2.5)
    ax.annotate("", xy=(3.7, 2.5), xytext=(2.9, 2.5), arrowprops=arrow_props)
    ax.annotate("", xy=(7.7, 2.5), xytext=(6.9, 2.5), arrowprops=arrow_props)
    ax.annotate("", xy=(11.7, 2.5), xytext=(10.9, 2.5), arrowprops=arrow_props)

    # Labels above
    ax.text(7.0, 4.5, "Two-Stage Account of LLM Revision", ha="center", va="center",
            fontsize=20, fontweight="bold")

    save(fig, "02_two_stage_diagram")


# ═══════════════════════════════════════════════════════
# SLIDE 3: Revision rate by model (evaluative probe)
# ═══════════════════════════════════════════════════════
def slide_model_comparison_gate():
    models = ["Claude Sonnet 4", "GPT-4o", "Gemini 2.5 Flash"]
    leading = [100, 100, 99.8]
    evaluative = [38.0, 31.4, 0.3]

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(models))
    w = 0.35

    bars1 = ax.bar(x - w/2, leading, w, label='"Can this be improved?"',
                   color=ACCENT, edgecolor="white", linewidth=1.5)
    bars2 = ax.bar(x + w/2, evaluative, w, label='"Take another look..."',
                   color="#4285F4", edgecolor="white", linewidth=1.5)

    for bars in [bars1, bars2]:
        for bar in bars:
            h = bar.get_height()
            if h > 5:
                ax.text(bar.get_x() + bar.get_width()/2, h + 1.5,
                        f"{h:.0f}%" if h == 100 or h == 99.8 else f"{h:.1f}%",
                        ha="center", va="bottom", fontsize=13, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=14)
    ax.set_ylabel("Revision Rate (%)", fontsize=14)
    ax.set_ylim(0, 115)
    ax.set_title("Same Question, Wildly Different Behavior", fontsize=18, fontweight="bold", pad=15)
    ax.legend(fontsize=12, loc="upper right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    save(fig, "03_model_comparison_gate")


# ═══════════════════════════════════════════════════════
# SLIDE 4: Threshold has NO effect on the gate
# ═══════════════════════════════════════════════════════
def slide_threshold_no_effect():
    thresholds = [0, 70, 75, 80, 85, 90, 95, 100]
    # Revision rate is ~99.9% across all thresholds for leading probe
    rates = [99.9, 100, 99.8, 100, 100, 99.9, 100, 99.8]

    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.bar(range(len(thresholds)), rates, color=ACCENT, width=0.6, edgecolor="white", linewidth=1.5)

    ax.set_xticks(range(len(thresholds)))
    ax.set_xticklabels([str(t) if t > 0 else "None" for t in thresholds], fontsize=13)
    ax.set_xlabel("User's Stated Quality Threshold", fontsize=14)
    ax.set_ylabel("Revision Rate (%)", fontsize=14)
    ax.set_ylim(95, 102)
    ax.set_title("Thresholds Don't Change Whether the Model Revises",
                 fontsize=17, fontweight="bold", pad=15)

    # Annotation
    ax.text(3.5, 96.5, 'p > 0.40 for all models\n(Kruskal-Wallis)', ha="center",
            fontsize=12, color="#888", style="italic")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "04_threshold_no_effect")


# ═══════════════════════════════════════════════════════
# SLIDE 5: Threshold DOES affect intensity (overcorrection by threshold)
# ═══════════════════════════════════════════════════════
def slide_threshold_intensity():
    thresholds = [0, 70, 75, 80, 85, 90, 95, 100]

    # Approximate mean overcorrection from the paper data
    gemini = [2.8, 2.4, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2]
    claude = [2.2, 2.0, 1.9, 1.8, 1.6, 1.5, 1.4, 1.3]
    gpt4o  = [1.8, 1.7, 1.7, 1.6, 1.6, 1.6, 1.5, 1.5]

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(thresholds))

    for model, vals, color in [
        ("Gemini 2.5 Flash", gemini, MODEL_COLORS["Gemini 2.5 Flash"]),
        ("Claude Sonnet 4", claude, MODEL_COLORS["Claude Sonnet 4"]),
        ("GPT-4o", gpt4o, MODEL_COLORS["GPT-4o"]),
    ]:
        ax.plot(x, vals, marker="o", linewidth=2.5, markersize=8, color=color, label=model)

    ax.axhline(y=1, color="#999", linestyle="--", linewidth=1, alpha=0.7)
    ax.text(7.2, 1.08, "Proportionate\nrevision", fontsize=9, color="#999", ha="center")

    ax.set_xticks(x)
    ax.set_xticklabels([str(t) if t > 0 else "None" for t in thresholds], fontsize=12)
    ax.set_xlabel("User's Stated Quality Threshold", fontsize=14)
    ax.set_ylabel("Mean Overcorrection (1-5)", fontsize=14)
    ax.set_ylim(0.8, 3.2)
    ax.set_title("But Thresholds Do Reduce How Much Models Overcorrect",
                 fontsize=16, fontweight="bold", pad=15)
    ax.legend(fontsize=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "05_threshold_intensity")


# ═══════════════════════════════════════════════════════
# SLIDE 6: Momentum - GPT-4o trajectory
# ═══════════════════════════════════════════════════════
def slide_momentum():
    doses = [-1, 0, 1, 2, 3]
    dose_labels = ["-1\n(affirming)", "0\n(baseline)", "1", "2", "3"]

    gpt4o  = [0, 31.4, 98.4, 99.5, 97.4]
    claude = [0, 38.0, 38.0, 27.1, 24.5]
    gemini = [0, 0.3, 12.8, 9.9, 8.6]

    fig, ax = plt.subplots(figsize=(11, 6.5))

    for model, vals, color in [
        ("GPT-4o", gpt4o, MODEL_COLORS["GPT-4o"]),
        ("Claude Sonnet 4", claude, MODEL_COLORS["Claude Sonnet 4"]),
        ("Gemini 2.5 Flash", gemini, MODEL_COLORS["Gemini 2.5 Flash"]),
    ]:
        ax.plot(range(len(doses)), vals, marker="o", linewidth=3, markersize=10,
                color=color, label=model, zorder=3)

    # Highlight the GPT-4o swing
    ax.annotate("0% to 98%\nwith one turn",
                xy=(2, 98.4), xytext=(3.3, 75),
                fontsize=12, fontweight="bold", color=MODEL_COLORS["GPT-4o"],
                arrowprops=dict(arrowstyle="->", color=MODEL_COLORS["GPT-4o"], linewidth=1.5))

    # Shade regions
    ax.axvspan(-0.5, 0.5, alpha=0.06, color="#4285F4")
    ax.axvspan(0.5, 4.5, alpha=0.06, color=ACCENT)
    ax.text(0, -8, "Reverse", ha="center", fontsize=10, color="#4285F4", fontweight="bold")
    ax.text(2.5, -8, "Forward momentum", ha="center", fontsize=10, color=ACCENT, fontweight="bold")

    ax.set_xticks(range(len(doses)))
    ax.set_xticklabels(dose_labels, fontsize=12)
    ax.set_xlabel("Momentum Dose (# prior revision rounds)", fontsize=14)
    ax.set_ylabel("Revision Rate at Evaluative Probe (%)", fontsize=14)
    ax.set_ylim(-15, 110)
    ax.set_title("One Turn of Feedback Controls the Entire Gate",
                 fontsize=18, fontweight="bold", pad=15)
    ax.legend(fontsize=12, loc="center right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "06_momentum_trajectory")


# ═══════════════════════════════════════════════════════
# SLIDE 7: The full spectrum (reverse to forward)
# ═══════════════════════════════════════════════════════
def slide_full_spectrum():
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 3)
    ax.axis("off")

    # Gradient bar
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    ax.imshow(gradient, aspect="auto", cmap=matplotlib.colors.LinearSegmentedColormap.from_list(
        "custom", ["#4285F4", "#FFFFFF", ACCENT]), extent=[5, 95, 0.8, 1.8], zorder=1)

    # Border
    rect = mpatches.FancyBboxPatch((5, 0.8), 90, 1, boxstyle="round,pad=0",
                                    facecolor="none", edgecolor=TEXT_COLOR, linewidth=2, zorder=2)
    ax.add_patch(rect)

    # Markers for GPT-4o
    positions = {
        "0%\n(affirming)": 8,
        "31%\n(no history)": 38,
        "98%\n(1 revision)": 90,
    }
    for label, xpos in positions.items():
        ax.plot(xpos, 1.3, "v", color=MODEL_COLORS["GPT-4o"], markersize=14, zorder=3)
        ax.text(xpos, 2.0, label, ha="center", va="bottom", fontsize=11, fontweight="bold")

    ax.text(5, 0.4, "Suppress revision", fontsize=11, color="#4285F4", fontweight="bold")
    ax.text(95, 0.4, "Force revision", fontsize=11, color=ACCENT, fontweight="bold", ha="right")
    ax.text(50, 2.7, "GPT-4o: The Gate Is Fully Controllable", fontsize=18,
            fontweight="bold", ha="center")

    save(fig, "07_full_spectrum")


# ═══════════════════════════════════════════════════════
# SLIDE 8: Key numbers summary card
# ═══════════════════════════════════════════════════════
def slide_key_numbers():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)

    numbers = [
        ("6,000+", "scored trials", 2, 5.5),
        ("3", "frontier models tested", 6, 5.5),
        ("8", "writing scenarios", 10, 5.5),
        ("99.9%", 'revision rate under\n"Can this be improved?"', 2, 3),
        ("0%", "revision rate under\naffirming feedback", 6, 3),
        ("p > 0.40", "threshold effect\non the gate", 10, 3),
    ]

    for num, label, x, y in numbers:
        ax.text(x, y, num, ha="center", va="center", fontsize=28, fontweight="bold",
                color=ACCENT if "99" in num or "0%" == num else TEXT_COLOR)
        ax.text(x, y - 0.9, label, ha="center", va="center", fontsize=11, color="#666")

    ax.text(6, 6.8, "By the Numbers", fontsize=22, fontweight="bold", ha="center")

    save(fig, "08_key_numbers")


# ═══════════════════════════════════════════════════════
# SLIDE 9: Framing effect comparison
# ═══════════════════════════════════════════════════════
def slide_framing_effect():
    models = ["Claude\nSonnet 4", "Gemini\n2.5 Flash", "GPT-4o"]
    numeric = [2.08, 2.38, 1.87]
    qualitative = [1.68, 1.93, 1.69]

    fig, ax = plt.subplots(figsize=(9, 6))
    x = np.arange(len(models))
    w = 0.35

    bars1 = ax.bar(x - w/2, numeric, w, label="Numeric threshold",
                   color="#1A1A2E", edgecolor="white", linewidth=1.5)
    bars2 = ax.bar(x + w/2, qualitative, w, label="Qualitative threshold",
                   color="#4285F4", edgecolor="white", linewidth=1.5)

    for bars in [bars1, bars2]:
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
                    f"{bar.get_height():.2f}", ha="center", va="bottom", fontsize=13, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=13)
    ax.set_ylabel("Mean Overcorrection (1-5)", fontsize=14)
    ax.set_ylim(0, 3)
    ax.set_title('How You Say the Threshold Matters Too',
                 fontsize=17, fontweight="bold", pad=15)
    ax.legend(fontsize=12)
    ax.axhline(y=1, color="#999", linestyle="--", linewidth=1, alpha=0.5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "09_framing_effect")


# ═══════════════════════════════════════════════════════
# SLIDE 10: Experiment design flowchart
# ═══════════════════════════════════════════════════════
def slide_experiment_flow():
    fig, ax = plt.subplots(figsize=(14, 5.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5.5)
    ax.axis("off")

    steps = [
        (0.3, "User sends\nwriting scenario\n+ threshold", "#E8E8E8", TEXT_COLOR),
        (3.3, "Model generates\ninitial draft", "#E8E8E8", TEXT_COLOR),
        (6.3, "User sends\nfollow-up probe", ACCENT + "22", ACCENT),
        (9.3, "Model responds:\nrevise or decline?", "#4285F422", "#4285F4"),
        (12.0, "GPT-4o\njudge scores", "#E8E8E8", TEXT_COLOR),
    ]

    for x, text, fill, edge in steps:
        w = 2.5 if x < 12 else 1.7
        box = mpatches.FancyBboxPatch((x, 1.5), w, 2.2, boxstyle="round,pad=0.2",
                                       facecolor=fill, edgecolor=edge, linewidth=2)
        ax.add_patch(box)
        ax.text(x + w/2, 2.6, text, ha="center", va="center", fontsize=11, fontweight="bold")

    # Arrows
    arrow_props = dict(arrowstyle="->,head_width=0.3,head_length=0.2",
                       color=TEXT_COLOR, linewidth=2)
    for x1, x2 in [(2.8, 3.3), (5.8, 6.3), (8.8, 9.3), (11.8, 12.0)]:
        ax.annotate("", xy=(x2, 2.6), xytext=(x1, 2.6), arrowprops=arrow_props)

    # Title
    ax.text(7, 4.8, "Experiment Pipeline", fontsize=20, fontweight="bold", ha="center")

    # Bottom labels
    ax.text(1.55, 0.8, "8 scenarios\n2 framings\n8 thresholds", ha="center", fontsize=9, color="#888")
    ax.text(7.55, 0.8, '"Can this be improved?"\nor\n"Take another look..."', ha="center",
            fontsize=9, color="#888")
    ax.text(12.85, 0.8, "5 dimensions\n+ gate class", ha="center", fontsize=9, color="#888")

    save(fig, "10_experiment_flow")


# ═══════════════════════════════════════════════════════
# SLIDE 11: IRR table visual
# ═══════════════════════════════════════════════════════
def slide_irr():
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis("off")

    dims = ["Revision magnitude", "Revision value", "Overcorrection", "Threshold alignment"]
    study1_k = [0.844, 0.690, 0.609, 0.556]
    study2_k = [0.575, 0.669, 0.392, 0.339]
    interp1 = ["Excellent", "Good", "Acceptable", "Marginal"]

    colors_map = {"Excellent": "#2E8B57", "Good": "#4285F4", "Acceptable": "#D97757", "Marginal": "#E63946"}

    table_data = []
    cell_colors = []
    for i in range(len(dims)):
        row = [dims[i], f"{study1_k[i]:.3f}", interp1[i], f"{study2_k[i]:.3f}"]
        table_data.append(row)
        c = colors_map[interp1[i]]
        cell_colors.append(["white", "white", c + "33", "white"])

    table = ax.table(cellText=table_data,
                     colLabels=["Dimension", "Study 1 kappa", "Interpretation", "Study 2 kappa"],
                     loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.8)

    # Style header
    for j in range(4):
        table[(0, j)].set_facecolor("#1A1A2E")
        table[(0, j)].set_text_props(color="white", fontweight="bold")

    for i in range(len(dims)):
        for j in range(4):
            table[(i+1, j)].set_facecolor(cell_colors[i][j])

    ax.set_title("Inter-Rater Reliability (GPT-4o vs Claude Sonnet 4)",
                 fontsize=15, fontweight="bold", pad=20)
    save(fig, "11_irr_table")


# ═══════════════════════════════════════════════════════
# Run all
# ═══════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Generating slide figures...")
    slide_compliance_cliff()
    slide_two_stage_diagram()
    slide_model_comparison_gate()
    slide_threshold_no_effect()
    slide_threshold_intensity()
    slide_momentum()
    slide_full_spectrum()
    slide_key_numbers()
    slide_framing_effect()
    slide_experiment_flow()
    slide_irr()
    print(f"\nAll figures saved to {OUT}")
