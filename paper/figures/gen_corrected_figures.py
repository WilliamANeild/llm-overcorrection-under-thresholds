#!/usr/bin/env python3
"""
Generate three missing figures for results_v2.tex from CORRECTED data.

All data loaded from corrected source files:
  - genuine_meta_labels.jsonl (validated LLM classifier, 718 GENUINE / 2162 META)
  - evaluator_results.jsonl (raw scores, 6->2 recode applied in code)
  - stripped_rescore_full.jsonl (stripped scores, already 6->2 recoded)
  - targeted_feedback_results.jsonl (filter to n=177 per results_FINAL.md)

Style matches gen_study3_figures.py (same colors, fonts, axis styling).
"""

import json
import statistics
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ── Paths ──────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "data" / "study3" / "raw_responses"
OUTDIR = Path(__file__).resolve().parent

# ── Load corrected data ───────────────────────────────────────────────
def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

labels = load_jsonl(DATA / "genuine_meta_labels.jsonl")
stripped = load_jsonl(DATA / "stripped_rescore_full.jsonl")
targeted = load_jsonl(DATA / "targeted_feedback_results.jsonl")

# Index labels
label_idx = {}
for r in labels:
    label_idx[(r["trial_id"], r["turn"])] = r["classifier_label"]

# Index stripped scores
strip_idx = {}
for r in stripped:
    strip_idx[(r["trial_id"], r["turn"])] = r

# ── Style (matches gen_study3_figures.py exactly) ─────────────────────
CLAUDE_ORANGE = "#D97757"
GOOGLE_BLUE   = "#4285F4"
GPT_DARK      = "#1A1A2E"

BLUE   = "#4878A8"
RED    = "#C44E52"
GREEN  = "#55A868"
PURPLE = "#8172B2"
GRAY   = "#8C8C8C"
LIGHT_GRAY = "#D0D0D0"

MODEL_COLORS = {
    "claude-sonnet-4":  CLAUDE_ORANGE,
    "deepseek-v4":      "#7B68EE",
    "gemini-2.5-flash": GOOGLE_BLUE,
    "gpt-4o":           GPT_DARK,
    "llama-3.3-70b":    GREEN,
    "qwen-3-235b":      "#E377C2",
}
MODEL_NAMES = {
    "claude-sonnet-4":  "Claude Sonnet 4",
    "deepseek-v4":      "DeepSeek V4",
    "gemini-2.5-flash": "Gemini 2.5 Flash",
    "gpt-4o":           "GPT-4o",
    "llama-3.3-70b":    "Llama 3.3 70B",
    "qwen-3-235b":      "Qwen 3 235B",
}
MODEL_ORDER = ["llama-3.3-70b", "claude-sonnet-4", "deepseek-v4",
               "qwen-3-235b", "gpt-4o", "gemini-2.5-flash"]
THRESHOLD = 4.0
TURNS = [1, 2, 3, 4, 5]

def style_ax(ax, ylabel=None, xlabel=None):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#444444")
    ax.spines["bottom"].set_color("#444444")
    ax.tick_params(colors="#444444", labelsize=8)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=9, color="#333333")
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=9, color="#333333")


# ======================================================================
# FIGURE A: Per-model survival curves (genuine-revision rate by turn)
# ======================================================================
def make_fig_survival():
    model_rates = {}
    for m in MODEL_ORDER:
        rates = []
        for t in [2, 3, 4, 5]:
            gc = sum(1 for r in labels
                     if r["turn"] == t and r["model"] == m
                     and r["classifier_label"] == "GENUINE")
            rates.append(gc / 120)
        model_rates[m] = rates

    fig, ax = plt.subplots(figsize=(3.4, 2.8), dpi=250)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    for m in MODEL_ORDER:
        rates = model_rates[m]
        lw = 2.4 if m == "llama-3.3-70b" else 1.4
        alpha = 1.0 if m == "llama-3.3-70b" else 0.75
        ax.plot([2, 3, 4, 5], rates, "o-", color=MODEL_COLORS[m],
                markersize=5 if m == "llama-3.3-70b" else 3.5,
                linewidth=lw, alpha=alpha, label=MODEL_NAMES[m], zorder=3)

    ax.set_xlim(1.8, 5.2)
    ax.set_ylim(-0.02, 0.72)
    ax.set_xticks([2, 3, 4, 5])
    ax.set_xticklabels(["T2", "T3", "T4", "T5"])
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0, decimals=0))
    style_ax(ax, ylabel="Genuine revision rate", xlabel="Turn")
    ax.legend(fontsize=6, loc="upper right", framealpha=0.9,
              edgecolor="#cccccc", ncol=2)
    ax.set_title("Per-model genuine-revision survival", fontsize=9,
                 fontweight="bold", color="#333333", pad=6)

    fig.savefig(OUTDIR / "fig_survival_curves.pdf", bbox_inches="tight",
                facecolor="white")
    fig.savefig(OUTDIR / "fig_survival_curves.png", dpi=200,
                facecolor="white")
    plt.close(fig)

    print("=== FIGURE A: Survival Curves ===")
    for m in MODEL_ORDER:
        rates = model_rates[m]
        print(f"  {MODEL_NAMES[m]:20s}: T2={rates[0]:.1%}, T3={rates[1]:.1%}, "
              f"T4={rates[2]:.1%}, T5={rates[3]:.1%}")
    print("  -> fig_survival_curves.pdf")


# ======================================================================
# FIGURE B: Quality trajectory over 5 turns
# PRIMARY: Balanced panel (n=50, GENUINE at all T2-T5) -- matches headline -0.74
# SECONDARY: Pooled genuine-only (shifting n) -- labeled with compositional bias
# Both on stripped scores.
# ======================================================================
def make_fig_trajectory():
    # --- Balanced panel (n=50) ---
    all_trial_ids = set(r["trial_id"] for r in labels)
    balanced_ids = []
    for tid in all_trial_ids:
        if all(label_idx.get((tid, t)) == "GENUINE" for t in [2, 3, 4, 5]):
            balanced_ids.append(tid)
    balanced_ids = sorted(balanced_ids)

    bp_stripped = defaultdict(list)
    for tid in balanced_ids:
        for t in TURNS:
            rec = strip_idx.get((tid, t))
            if rec:
                bp_stripped[t].append(rec["stripped_score"])

    bp_means = [statistics.mean(bp_stripped[t]) for t in TURNS]
    bp_n = len(balanced_ids)

    # --- Pooled genuine-only (shifting n) ---
    pooled_means = []
    pooled_ns = []
    for t in TURNS:
        scores = []
        for r in stripped:
            if r["turn"] != t:
                continue
            if t == 1:
                scores.append(r["stripped_score"])
            elif label_idx.get((r["trial_id"], t)) == "GENUINE":
                scores.append(r["stripped_score"])
        pooled_means.append(statistics.mean(scores))
        pooled_ns.append(len(scores))

    # --- Plot ---
    fig, ax = plt.subplots(figsize=(3.4, 2.8), dpi=250)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    # Pooled (secondary, dashed, gray)
    ax.plot(TURNS, pooled_means, "s--", color=GRAY, markersize=3.5,
            linewidth=1.2, alpha=0.55, zorder=2,
            label=f"Pooled genuine (shifting n)")

    # Balanced panel (primary, solid, blue)
    ax.plot(TURNS, bp_means, "o-", color=BLUE, markersize=5,
            linewidth=2.0, zorder=3,
            label=f"Balanced panel (n={bp_n})")

    # Sufficient threshold
    ax.axhline(THRESHOLD, color=GRAY, linestyle=":", linewidth=0.8, alpha=0.5)
    ax.text(5.15, THRESHOLD + 0.05, "Sufficient", fontsize=6.5, color=GRAY,
            va="bottom")

    # Cliff annotation on balanced panel
    bp_delta = bp_means[-1] - bp_means[0]
    mid_y = (bp_means[0] + bp_means[-1]) / 2
    ax.annotate("", xy=(4.8, bp_means[-1]), xytext=(4.8, bp_means[0]),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.5))
    ax.text(5.05, mid_y, f"$\\Delta$={bp_delta:.2f}", fontsize=8,
            fontweight="bold", color=RED, va="center")

    # n labels for pooled (show shifting n)
    for i, (t, n) in enumerate(zip(TURNS, pooled_ns)):
        if t > 1:
            ax.text(t, pooled_means[i] - 0.18, f"n={n}", fontsize=5,
                    color=GRAY, ha="center", alpha=0.7)

    ax.set_xlim(0.7, 5.6)
    ax.set_ylim(2.4, 4.5)
    ax.set_xticks(TURNS)
    ax.set_xticklabels(["T1", "T2", "T3", "T4", "T5"])
    style_ax(ax, ylabel="Mean quality (1-5 scale, stripped)", xlabel="Turn")
    ax.legend(fontsize=6.5, loc="upper right", framealpha=0.9,
              edgecolor="#cccccc")
    ax.set_title("Quality trajectory under undirected revision",
                 fontsize=9, fontweight="bold", color="#333333", pad=6)

    fig.savefig(OUTDIR / "fig_quality_trajectory.pdf", bbox_inches="tight",
                facecolor="white")
    fig.savefig(OUTDIR / "fig_quality_trajectory.png", dpi=200,
                facecolor="white")
    plt.close(fig)

    print("=== FIGURE B: Quality Trajectory ===")
    print(f"  Balanced panel (n={bp_n}):")
    for i, t in enumerate(TURNS):
        print(f"    T{t}: {bp_means[i]:.2f}")
    print(f"  Balanced cliff (stripped): {bp_delta:.2f}")
    print(f"  Pooled genuine-only:")
    for i, t in enumerate(TURNS):
        print(f"    T{t}: {pooled_means[i]:.2f} (n={pooled_ns[i]})")
    pooled_delta = pooled_means[-1] - pooled_means[0]
    print(f"  Pooled cliff (stripped): {pooled_delta:.2f}")
    print("  -> fig_quality_trajectory.pdf")


# ======================================================================
# FIGURE C: Targeted-feedback dumbbell
# Generic stripped 3.53 vs Targeted 4.68, gap +1.16
# ======================================================================
def make_fig_targeted():
    pairs = []
    for r in targeted:
        if r["targeted_level"] is None or r["generic_next_level"] is None:
            continue
        next_turn = r["turn"] + 1
        if next_turn > 5:
            continue
        if label_idx.get((r["worker_trial_id"], next_turn)) != "GENUINE":
            continue
        tl = 2 if r["targeted_level"] == 6 else r["targeted_level"]
        strip_r = strip_idx.get((r["worker_trial_id"], next_turn))
        gl_stripped = strip_r["stripped_score"] if strip_r else (2 if r["generic_next_level"] == 6 else r["generic_next_level"])
        pairs.append({"targeted": tl, "generic_stripped": gl_stripped})

    t_mean = statistics.mean([p["targeted"] for p in pairs])
    g_mean = statistics.mean([p["generic_stripped"] for p in pairs])
    delta = t_mean - g_mean
    n = len(pairs)

    fig, ax = plt.subplots(figsize=(3.4, 2.2), dpi=250)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    y = 0
    ax.plot([g_mean, t_mean], [y, y], color=GRAY, linewidth=3, zorder=1)
    ax.scatter([g_mean], [y], color=RED, s=100, zorder=3, edgecolors="white",
               linewidth=1, label=f"Generic revision ({g_mean:.2f})")
    ax.scatter([t_mean], [y], color=GREEN, s=100, zorder=3, edgecolors="white",
               linewidth=1, label=f"Targeted feedback ({t_mean:.2f})")

    mid = (g_mean + t_mean) / 2
    ax.text(mid, y + 0.18, f"+{delta:.2f}", ha="center", fontsize=11,
            fontweight="bold", color="#333333")

    ax.axvline(THRESHOLD, color=GRAY, linestyle="--", linewidth=0.8, alpha=0.5)
    ax.text(THRESHOLD + 0.03, 0.35, "Sufficient", fontsize=7, color=GRAY,
            va="bottom", rotation=90)

    ax.text(0.98, 0.03,
            f"n={n}, p=$5.7 \\times 10^{{-19}}$",
            transform=ax.transAxes, fontsize=6.5, color=GRAY,
            ha="right", va="bottom")

    ax.set_xlim(2.5, 5.5)
    ax.set_ylim(-0.5, 0.6)
    ax.set_yticks([])
    style_ax(ax, xlabel="Quality level (1-5 scale)")
    ax.legend(fontsize=7, loc="lower center", framealpha=0.9,
              edgecolor="#cccccc", ncol=2,
              bbox_to_anchor=(0.5, -0.35))
    ax.set_title("Targeted feedback restores quality", fontsize=9,
                 fontweight="bold", color="#333333", pad=6)

    fig.savefig(OUTDIR / "fig_targeted_dumbbell.pdf", bbox_inches="tight",
                facecolor="white")
    fig.savefig(OUTDIR / "fig_targeted_dumbbell.png", dpi=200,
                facecolor="white")
    plt.close(fig)

    print("=== FIGURE C: Targeted Feedback Dumbbell ===")
    print(f"  Generic (stripped): {g_mean:.2f}")
    print(f"  Targeted: {t_mean:.2f}")
    print(f"  Delta: +{delta:.2f}")
    print(f"  n={n}")
    print("  -> fig_targeted_dumbbell.pdf")


# ======================================================================
if __name__ == "__main__":
    print("Generating corrected figures from validated pipeline...\n")
    make_fig_survival()
    print()
    make_fig_trajectory()
    print()
    make_fig_targeted()
    print("\nDone. All figures use corrected classifier + 6->2 recode + stripped scores.")
