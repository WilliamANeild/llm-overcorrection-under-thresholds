#!/usr/bin/env python3
"""
Two results figures, both read from the data files at build time so they cannot drift
from the analysis.

  fig_revision_tax.pdf   share of each model's output produced after the optimal turn
                         (ledger Section 6; replaces the per-model tax table)
  fig_input_level.pdf    expected change in quality by level of the input being revised
                         (ledger Section 4c; POST-HOC, not pre-registered)

House style, matching Figure 1: Helvetica, no in-figure title (the caption carries it),
rendered at the 3.17in column width so type is not resampled, PDF output.

    python3 paper/figures/gen_results_figures.py
"""
import json, statistics as st
from collections import defaultdict
from pathlib import Path
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
RAW = HERE.parents[1] / "data" / "study3" / "raw_responses"
W, INK, MID, ACCENT = 3.17, "#111", "#555", "#4878A8"
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.config import recode_level as recode


def load():
    lab, sc, mod, tok = {}, {}, {}, {}
    for line in open(RAW / "genuine_meta_labels.jsonl"):
        r = json.loads(line); lab[(r["trial_id"], r["turn"])] = r["classifier_label"]
    for line in open(RAW / "stripped_rescore_full.jsonl"):
        r = json.loads(line); sc[(r["trial_id"], r["turn"])] = recode(r["stripped_score"])
    for line in open(RAW / "worker_trials.jsonl"):
        r = json.loads(line)
        mod[r["trial_id"]] = r["model"]
        tok[r["trial_id"]] = [c["output"] for c in r["token_counts"]]
    return lab, sc, mod, tok, {t for t, _ in lab}


def style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(MID); ax.spines[s].set_linewidth(.9)
    ax.tick_params(labelsize=9, colors="#222", length=3)


def fig_tax(mod, tok, trials):
    NICE = {"llama-3.3-70b": "Llama 3.3 70B", "claude-sonnet-4": "Claude Sonnet 4",
            "qwen-3-235b": "Qwen 3 235B", "gpt-4o": "GPT-4o",
            "deepseek-v4": "DeepSeek V4", "gemini-2.5-flash": "Gemini 2.5 Flash"}
    waste = {m: sum(sum(tok[t][1:]) for t in trials if mod[t] == m)
                / sum(sum(tok[t]) for t in trials if mod[t] == m) * 100 for m in NICE}
    agg = sum(sum(tok[t][1:]) for t in trials) / sum(sum(tok[t]) for t in trials) * 100
    order = sorted(NICE, key=lambda m: waste[m]); vals = [waste[m] for m in order]
    y = np.arange(len(order))
    fig, ax = plt.subplots(figsize=(W, 2.15), dpi=400)
    ax.grid(axis="x", color="#ededed", lw=.7, zorder=0); ax.set_axisbelow(True)
    ax.axvline(agg, color="#C44E52", lw=1.1, ls=(0, (4, 3)), zorder=2)
    ax.barh(y, vals, color=ACCENT, height=.72, zorder=3)
    ax.set_yticks(y); ax.set_yticklabels([NICE[m] for m in order], fontsize=8.5)
    ax.tick_params(axis="y", length=0)
    for yi, v in zip(y, vals):
        ins = v > 30
        ax.text(v - 1.6 if ins else v + 1.6, yi, f"{v:.0f}%", va="center",
                ha="right" if ins else "left", fontsize=8.5, fontweight="bold",
                color="white" if ins else INK, zorder=5)
    ax.text(agg - 1.8, len(order) - .30, f"all trials {agg:.0f}%", fontsize=8,
            color="#C44E52", ha="right", va="center")
    style(ax)
    for s in ("left",): ax.spines[s].set_visible(False)
    ax.set_xlim(0, 88); ax.set_ylim(-.6, len(order) + .05); ax.set_xticks([0, 20, 40, 60, 80])
    ax.set_xlabel("Output tokens after the optimal turn (%)", fontsize=9.5, labelpad=4)
    fig.savefig(HERE / "fig_revision_tax.pdf", facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return agg


def fig_input_level(lab, sc, trials):
    by = defaultdict(list)
    for t in trials:
        last = sc.get((t, 1))
        for k in range(2, 6):
            if lab.get((t, k)) == "GENUINE" and (t, k) in sc and last is not None:
                by[last].append(sc[(t, k)] - last); last = sc[(t, k)]
    lv = [2, 3, 4, 5]
    mean = [st.mean(by[l]) for l in lv]
    ci = [1.96 * st.stdev(by[l]) / len(by[l]) ** .5 for l in lv]
    ns = [len(by[l]) for l in lv]
    fig, ax = plt.subplots(figsize=(W, 2.25), dpi=400)
    ax.grid(axis="y", color="#ededed", lw=.7, zorder=0); ax.set_axisbelow(True)
    ax.axhline(0, color=INK, lw=1.0, zorder=2)
    ax.errorbar(lv, mean, yerr=ci, fmt="o-", color=INK, lw=1.9, ms=6,
                capsize=3.5, capthick=1, zorder=4)
    # Place each label on the far side of its point from zero, so values near the
    # axis do not print on top of the zero line or on each other.
    for x, y, c in zip(lv, mean, ci):
        above = y >= 0
        ax.annotate(f"{y:+.2f}", (x, y + c if above else y - c),
                    textcoords="offset points", xytext=(0, 7 if above else -7),
                    ha="center", va="bottom" if above else "top",
                    fontsize=8.5, fontweight="bold", color=INK)
    style(ax)
    lo = min(m - c for m, c in zip(mean, ci)); hi = max(m + c for m, c in zip(mean, ci))
    pad = max(0.30, (hi - lo) * 0.22)
    ax.set_ylim(lo - pad, hi + pad); ax.set_xlim(1.6, 5.45)
    ax.set_yticks([-1, -.5, 0, .5, 1])
    ax.set_xticks(lv); ax.set_xticklabels([f"{l}\n$n$={n}" for l, n in zip(lv, ns)], fontsize=9)
    # "improves" sits top-right and "damages" bottom-left: the series runs from high-left
    # to low-right, so those two corners are the ones it never enters.
    ax.text(5.38, hi + pad * 0.42, "improves", fontsize=8, color=MID, ha="right", va="top")
    ax.text(1.70, lo - pad * 0.42, "damages", fontsize=8, color=MID, ha="left", va="bottom")
    ax.set_xlabel("Quality level of the input being revised", fontsize=9.5, labelpad=4)
    ax.set_ylabel("Change in quality level", fontsize=9.5, labelpad=4)
    fig.savefig(HERE / "fig_input_level.pdf", facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return dict(zip(lv, zip(mean, ns)))


if __name__ == "__main__":
    lab, sc, mod, tok, trials = load()
    agg = fig_tax(mod, tok, trials)
    pts = fig_input_level(lab, sc, trials)
    print(f"fig_revision_tax.pdf   aggregate waste {agg:.1f}%  (ledger 62.1%)")
    print("fig_input_level.pdf    " + "  ".join(f"L{k} {v[0]:+.2f} (n={v[1]})" for k, v in pts.items()))
