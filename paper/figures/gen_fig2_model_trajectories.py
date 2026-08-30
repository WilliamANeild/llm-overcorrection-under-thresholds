#!/usr/bin/env python3
"""Figure 2: Six Models, One Story (and One Exception).

All 6 models overlaid on one panel. 5 lines plunging, 1 (Llama) rising.
Uses per-model balanced-panel trajectories.
"""

import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# -- Load data --
ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS = ROOT / "data" / "study3" / "analysis" / "study3_results.json"
with open(RESULTS) as f:
    data = json.load(f)

per_model = data["edge_cases"]["cohort_trajectories"]["per_model"]

TURNS = [1, 2, 3, 4, 5]
THRESHOLD = 4.0

# Model colors and display names
MODEL_CONFIG = {
    "claude-sonnet-4":  {"color": "#D97757", "name": "Claude Sonnet 4"},
    "deepseek-v4":      {"color": "#7B68EE", "name": "DeepSeek V4"},
    "gemini-2.5-flash": {"color": "#4285F4", "name": "Gemini 2.5 Flash"},
    "gpt-4o":           {"color": "#1A1A2E", "name": "GPT-4o"},
    "llama-3.3-70b":    {"color": "#55A868", "name": "Llama 3.3 70B"},
    "qwen-3-235b":      {"color": "#E377C2", "name": "Qwen 3 235B"},
}

GRAY = "#8C8C8C"

# -- Figure --
fig, ax = plt.subplots(figsize=(6, 4), dpi=250)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Gray zone below threshold
ax.axhspan(0, THRESHOLD, alpha=0.04, color="#888888", zorder=0)
ax.axhline(THRESHOLD, ls="--", lw=1.0, color=GRAY, alpha=0.6, zorder=1)
ax.text(5.15, THRESHOLD + 0.05, "Sufficient", fontsize=7, color=GRAY,
        va="bottom", style="italic")

# Plot each model
for model_id, cfg in MODEL_CONFIG.items():
    md = per_model[model_id]
    traj = md["trajectory"]
    means = [traj[str(t)]["mean"] for t in TURNS]
    delta = md["mean_delta_t1_t5"]
    n = md["n_balanced"]
    survival = md["n_balanced"] / md["n_total"]

    # Llama gets thicker line
    lw = 2.8 if model_id == "llama-3.3-70b" else 1.8
    ms = 6 if model_id == "llama-3.3-70b" else 4
    alpha = 1.0 if model_id == "llama-3.3-70b" else 0.8

    ax.plot(TURNS, means, "o-", color=cfg["color"], markersize=ms,
            linewidth=lw, alpha=alpha, label=cfg["name"],
            markeredgecolor="white", markeredgewidth=0.5, zorder=3)

    # Delta annotation at right side
    color = "#55A868" if delta > 0 else "#C44E52"
    sign = "+" if delta > 0 else ""
    ax.text(5.15, means[-1], f"{sign}{delta:.1f}",
            fontsize=7, fontweight="bold", color=color, va="center")

# Annotations for the exception
llama_means = [per_model["llama-3.3-70b"]["trajectory"][str(t)]["mean"] for t in TURNS]
ax.annotate("Only model that\nimproves with revision",
            xy=(3, llama_means[2]),
            xytext=(1.5, 5.3),
            fontsize=7, color="#55A868", ha="center",
            arrowprops=dict(arrowstyle="-|>", color="#55A868", lw=0.8),
            zorder=5)

# Survival rates as right-margin annotation
survival_text = "Survival\nto T5:"
y_start = 0.95
ax.text(1.02, y_start, survival_text, transform=ax.transAxes,
        fontsize=6, color=GRAY, ha="left", va="top")
for i, (model_id, cfg) in enumerate(MODEL_CONFIG.items()):
    surv = per_model[model_id]["n_balanced"] / per_model[model_id]["n_total"]
    ax.text(1.02, y_start - 0.08 - i * 0.065, f"{surv:.0%}",
            transform=ax.transAxes, fontsize=6, color=cfg["color"],
            ha="left", va="top", fontweight="bold")

# Legend
ax.legend(fontsize=7, loc="lower left", framealpha=0.9, edgecolor="#cccccc",
          ncol=2)

# Axes
ax.set_xlim(0.7, 5.5)
ax.set_ylim(0.5, 5.8)
ax.set_xticks(TURNS)
ax.set_xlabel("Revision Turn", fontsize=10, labelpad=6)
ax.set_ylabel("Quality Level (1-6)", fontsize=10, labelpad=6)

ax.grid(False)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#444444")
ax.spines["bottom"].set_color("#444444")
ax.tick_params(colors="#444444", length=4, labelsize=9)

ax.set_title("Five Models Decline, One Improves",
             fontsize=14, fontweight="bold", pad=14, color="#222222")
ax.text(0.5, 1.03, "Per-model balanced panel trajectories (n varies by survival rate)",
        transform=ax.transAxes, ha="center", fontsize=9, color=GRAY)

# Save
out_dir = Path(__file__).resolve().parent
fig.tight_layout(rect=[0, 0, 0.92, 1])
fig.savefig(out_dir / "fig2_model_trajectories.pdf", bbox_inches="tight")
fig.savefig(out_dir / "fig2_model_trajectories.png", bbox_inches="tight")
print("Saved fig2_model_trajectories.pdf and .png")
plt.close(fig)
