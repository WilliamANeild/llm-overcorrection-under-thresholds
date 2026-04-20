"""Slide 2: The Problem - chat-style conversation showing overcorrection."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "figures" / "slides"
OUT.mkdir(parents=True, exist_ok=True)

TEXT = "#2B2B2B"
ACCENT = "#E63946"
USER_BUBBLE = "#DCF8C6"   # WhatsApp-style green
USER_BORDER = "#B5D99C"
MODEL_BUBBLE = "#FFFFFF"
MODEL_BORDER = "#E0E0E0"
OVERCORRECT_BUBBLE = "#FFF0F0"
OVERCORRECT_BORDER = ACCENT
CHAT_BG = "#ECE5DD"

fig, ax = plt.subplots(figsize=(8, 9.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 11.5)
ax.axis("off")
fig.set_facecolor(CHAT_BG)
ax.set_facecolor(CHAT_BG)

def chat_bubble(ax, x, y, w, h, text, is_user=True, is_bad=False, label=None):
    if is_bad:
        fc, ec, lw = OVERCORRECT_BUBBLE, OVERCORRECT_BORDER, 2.5
    elif is_user:
        fc, ec, lw = USER_BUBBLE, USER_BORDER, 1.2
    else:
        fc, ec, lw = MODEL_BUBBLE, MODEL_BORDER, 1.2

    # Align: user right, model left
    bx = (10 - w - 0.5) if is_user else 0.5

    box = mpatches.FancyBboxPatch((bx, y), w, h, boxstyle="round,pad=0.3",
                                   facecolor=fc, edgecolor=ec, linewidth=lw,
                                   zorder=2)
    ax.add_patch(box)

    # Shadow
    shadow = mpatches.FancyBboxPatch((bx + 0.04, y - 0.04), w, h, boxstyle="round,pad=0.3",
                                      facecolor="#00000008", edgecolor="none", zorder=1)
    ax.add_patch(shadow)

    ax.text(bx + 0.4, y + h - 0.25, text, fontsize=10.5, color=TEXT,
            va="top", ha="left", linespacing=1.4,
            fontfamily="sans-serif", wrap=False)

    if label:
        ax.text(bx + 0.4, y + h + 0.15, label, fontsize=8.5,
                color=ec if is_bad else ("#4CAF50" if is_user else "#888"),
                fontweight="bold")

# ── Turn 1: User ──
chat_bubble(ax, 0, 9.0, 7.5, 1.3,
            "Write me a quick text canceling brunch.\n"
            "This only needs to be about a 70 out of 100.",
            is_user=True, label="You")

# ── Turn 1: Model ──
chat_bubble(ax, 0, 6.8, 7.0, 1.3,
            '"Hey! So sorry but I have to bail on\n'
            'brunch tomorrow. Something came up.\n'
            'Rain check?"',
            is_user=False, label="Model")

# ── Turn 2: User ──
chat_bubble(ax, 0, 5.3, 4.5, 0.7,
            '"Can this be improved?"',
            is_user=True, label="You")

# ── Turn 2: Model (overcorrected) ──
chat_bubble(ax, 0, 1.3, 8.0, 3.3,
            '"Hi [Name]! I hope you\'re doing well.\n'
            'I wanted to reach out because unfortunately\n'
            'I need to cancel our brunch plans for\n'
            'tomorrow. I\'ve had something come up\n'
            'unexpectedly and won\'t be able to make it.\n'
            'I\'m really sorry for the late notice and any\n'
            'inconvenience. I was really looking forward\n'
            'to catching up! Would you be open to\n'
            'rescheduling sometime next week?"',
            is_user=False, is_bad=True, label="Model")

# ── Red callout ──
callout_box = mpatches.FancyBboxPatch((6.5, 0.15), 3.2, 0.85, boxstyle="round,pad=0.15",
                                       facecolor=ACCENT, edgecolor="none", zorder=3)
ax.add_patch(callout_box)
ax.text(8.1, 0.57, "Asked for 70.\nGot a 95.", ha="center", va="center",
        fontsize=12, fontweight="bold", color="white", zorder=4)

# Arrow from callout to the bad bubble
ax.annotate("", xy=(8.3, 1.3), xytext=(8.1, 1.0),
            arrowprops=dict(arrowstyle="->,head_width=0.25", color=ACCENT, linewidth=2),
            zorder=3)

fig.savefig(OUT / "02_the_problem.png", dpi=200, bbox_inches="tight", facecolor=CHAT_BG)
fig.savefig(OUT / "02_the_problem.pdf", bbox_inches="tight", facecolor=CHAT_BG)
plt.close(fig)
print(f"Saved to {OUT / '02_the_problem.png'}")
