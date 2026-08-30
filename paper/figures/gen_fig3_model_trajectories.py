"""
Figure 3: Five Out of Six Models Degrade
Small multiples showing quality trajectory per model across turns 1-5.
Data: user-specified T1/T5 endpoints with linear interpolation for T2-T4.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def interpolate(t1, t5, n=5):
    """Linear interpolation from t1 to t5 over n points."""
    return [t1 + (t5 - t1) * i / (n - 1) for i in range(n)]


# Per-model quality trajectories (user-specified endpoints, interpolated middle)
models = {
    "Claude Sonnet 4": {
        "trajectory": interpolate(4.45, 2.07),
        "direction": "degrades",
        "n": 11,
    },
    "DeepSeek V4": {
        "trajectory": interpolate(4.52, 1.61),
        "direction": "degrades",
        "n": 21,
    },
    "Gemini 2.5 Flash": {
        "trajectory": interpolate(4.52, 1.33),
        "direction": "degrades",
        "n": 2,
    },
    "GPT-4o": {
        "trajectory": interpolate(4.19, 1.67),
        "direction": "degrades",
        "n": 12,
    },
    "Llama 3.3 70B": {
        "trajectory": interpolate(3.85, 4.35),
        "direction": "improves",
        "n": 54,
    },
    "Qwen 3 235B": {
        "trajectory": interpolate(4.52, 1.76),
        "direction": "degrades",
        "n": 35,
    },
}

turns = [1, 2, 3, 4, 5]
THRESHOLD = 4.0
RED = "#C44E52"
TEAL = "#55A868"
GEMINI_GRAY = "#BBBBBB"

# Distinct linestyles for grayscale printing
LINESTYLES = {
    "Claude Sonnet 4": "solid",
    "DeepSeek V4": "dashed",
    "GPT-4o": "dashdot",
    "Llama 3.3 70B": "solid",
    "Qwen 3 235B": (0, (3, 1, 1, 1)),
    "Gemini 2.5 Flash": "dotted",
}
LINEWIDTHS = {
    "Llama 3.3 70B": 3.0,  # thick to distinguish from Claude's solid
}

fig, axes = plt.subplots(2, 3, figsize=(8, 5), sharex=True, sharey=True)
fig.suptitle("Five Out of Six Models Degrade", fontsize=14, fontweight="bold", y=0.97)

for ax, (name, info) in zip(axes.flat, models.items()):
    traj = info["trajectory"]
    is_gemini = name == "Gemini 2.5 Flash"
    if is_gemini:
        color = GEMINI_GRAY
    elif info["direction"] == "improves":
        color = TEAL
    else:
        color = RED
    delta = traj[-1] - traj[0]

    # Threshold line
    ax.axhline(THRESHOLD, color="#AAAAAA", linestyle="--", linewidth=0.8, zorder=1)

    # Shading below threshold for degrading models
    if info["direction"] == "degrades":
        traj_arr = np.array(traj)
        ax.fill_between(
            turns,
            np.minimum(traj_arr, THRESHOLD),
            THRESHOLD,
            alpha=0.10,
            color=RED,
            zorder=0,
        )

    # Quality line
    lw = LINEWIDTHS.get(name, 2.0)
    ls = LINESTYLES.get(name, "solid")
    alpha = 0.5 if is_gemini else 1.0
    ax.plot(turns, traj, color=color, linewidth=lw, linestyle=ls,
            marker="o", markersize=4, zorder=3, alpha=alpha)

    # Delta annotation
    sign = "+" if delta > 0 else ""
    delta_str = f"{sign}{delta:.2f}"
    if info["direction"] == "improves":
        # Place above the last point
        ax.annotate(
            delta_str,
            xy=(5, traj[-1]),
            xytext=(5, traj[-1] + 0.40),
            fontsize=9.5,
            fontweight="bold",
            color=color,
            ha="center",
            va="bottom",
            zorder=4,
        )
    else:
        # Place below the last point
        ax.annotate(
            delta_str,
            xy=(5, traj[-1]),
            xytext=(5, traj[-1] - 0.45),
            fontsize=9.5,
            fontweight="bold",
            color=color,
            ha="center",
            va="top",
            zorder=4,
        )

    # n annotation near right edge of line
    if is_gemini:
        ax.text(3.0, traj[2] + 0.45, "n=2 (insufficient)", fontsize=7,
                color=GEMINI_GRAY, va="center", ha="center", style="italic")
    else:
        ax.text(5.4, traj[-1], f"n={info['n']}", fontsize=7, color=color,
                va="center", ha="left")

    # Panel title
    ax.set_title(name, fontsize=10, pad=4)

    # Axis config
    ax.set_ylim(0.5, 6.0)
    ax.set_xlim(0.7, 5.7)
    ax.set_xticks(turns)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.tick_params(axis="both", which="both", labelsize=8, length=3)

    # Remove gridlines and spines, add y-axis grid
    ax.grid(False)
    ax.yaxis.grid(True, alpha=0.3, color='#cccccc', linewidth=0.5)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

# Shared axis labels
for ax in axes[1, :]:
    ax.set_xlabel("Turn", fontsize=9)
for ax in axes[:, 0]:
    ax.set_ylabel("Quality (1\u20136)", fontsize=9)

# "Sufficient" label on threshold in first panel
axes[0, 0].text(
    1.0, THRESHOLD + 0.18, "Sufficient", fontsize=7, color="#999999",
    ha="left", va="bottom", style="italic",
)

plt.tight_layout(rect=[0, 0, 1, 0.93])

out_base = "/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/figures/fig3_model_trajectories"
fig.savefig(f"{out_base}.pdf", dpi=300, bbox_inches="tight", facecolor="white")
fig.savefig(f"{out_base}.png", dpi=300, bbox_inches="tight", facecolor="white")
print(f"Saved {out_base}.pdf and .png")
plt.close()
