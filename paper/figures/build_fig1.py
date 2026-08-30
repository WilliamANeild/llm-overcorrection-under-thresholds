#!/usr/bin/env python3
"""Build Figure 1: render HTML chat + matplotlib chart, composite, open.

Builds v2 (ChatGPT-style) by default. Old v1 files are preserved.
"""

import subprocess
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw

DIR = Path(__file__).resolve().parent
DPI = 300


def render_chat():
    from playwright.sync_api import sync_playwright
    html_path = DIR / "fig1_chat_v3.html"
    out_path = DIR / "fig1_chat_v3.png"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=3)
        page.goto(f"file://{html_path}")
        page.wait_for_load_state("networkidle")
        body = page.query_selector("body")
        body.screenshot(path=str(out_path))
        browser.close()
    print(f"Rendered {out_path}")
    return out_path


def render_chart():
    WHITE = "#FFFFFF"
    DARK = "#333333"
    COST_COL = "#E53935"
    QUAL_COL = "#2E7D32"
    GRID_COL = "#ebebeb"

    turns = np.arange(1, 6)
    # Normalized 0-1 for clean presentation
    quality_norm = np.array([1.0, 0.82, 0.6, 0.35, 0.12])
    cost_norm = np.array([0.1, 0.32, 0.55, 0.78, 1.0])

    fig, ax = plt.subplots(figsize=(5.5, 3.2), dpi=DPI)
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(WHITE)

    ax.yaxis.grid(True, color=GRID_COL, linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)

    ax.plot(turns, quality_norm, color=QUAL_COL, linewidth=2.5, marker='o',
            markersize=8, markerfacecolor=WHITE, markeredgewidth=2.5,
            markeredgecolor=QUAL_COL, zorder=5)
    ax.plot(turns, cost_norm, color=COST_COL, linewidth=2.5, marker='o',
            markersize=8, markerfacecolor=WHITE, markeredgewidth=2.5,
            markeredgecolor=COST_COL, zorder=5)

    # Labels at end of each line
    ax.text(5.2, quality_norm[-1], "Response\nQuality", fontsize=9, color=QUAL_COL,
            va="center", ha="left", fontweight="bold", linespacing=1.15)
    ax.text(5.2, cost_norm[-1], "Token\nCost", fontsize=9, color=COST_COL,
            va="center", ha="left", fontweight="bold", linespacing=1.15)

    # Directional arrows on y-axis labels
    ax.text(-0.05, 1.0, "High", fontsize=8, color="#888", ha="right", va="center",
            transform=ax.get_yaxis_transform())
    ax.text(-0.05, 0.0, "Low", fontsize=8, color="#888", ha="right", va="center",
            transform=ax.get_yaxis_transform())

    ax.set_xlim(0.6, 5.85)
    ax.set_ylim(-0.08, 1.1)
    ax.set_xticks(turns)
    ax.set_xticklabels([f"T{i}" for i in turns], fontsize=9.5, fontweight="bold")
    ax.set_yticks([])
    ax.set_xlabel("Revision Turn", fontsize=10, color=DARK, labelpad=6)
    ax.tick_params(axis='x', length=0, pad=6, labelcolor=DARK)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID_COL)
    ax.spines["left"].set_linewidth(0.5)
    ax.spines["bottom"].set_color(GRID_COL)
    ax.spines["bottom"].set_linewidth(0.5)

    fig.tight_layout(pad=0.8)

    out_path = DIR / "fig1_chart.png"
    fig.savefig(out_path, bbox_inches="tight", facecolor=WHITE, edgecolor="none", dpi=DPI)
    fig.savefig(DIR / "fig1_chart.pdf", bbox_inches="tight", facecolor=WHITE, edgecolor="none")
    plt.close(fig)
    print(f"Rendered {out_path}")
    return out_path


def composite(chat_path, chart_path):
    chat = Image.open(chat_path).convert("RGBA")
    chart = Image.open(chart_path).convert("RGBA")

    # Scale chart to match chat width with small margins
    margin = 50
    chart_target_w = chat.width - 2 * margin
    scale = chart_target_w / chart.width
    chart_resized = chart.resize(
        (chart_target_w, int(chart.height * scale)),
        Image.LANCZOS
    )

    divider_h = 3
    pad_above = 24
    pad_below = 16
    total_pad = pad_above + divider_h + pad_below
    canvas_w = chat.width
    canvas_h = chat.height + total_pad + chart_resized.height

    canvas = Image.new("RGBA", (canvas_w, canvas_h), (255, 255, 255, 255))
    canvas.paste(chat, (0, 0))

    # Draw divider line
    draw = ImageDraw.Draw(canvas)
    divider_y = chat.height + pad_above
    line_margin = 60
    draw.rectangle(
        [line_margin, divider_y, canvas_w - line_margin, divider_y + divider_h],
        fill="#d0d0d0"
    )

    chart_x = margin
    chart_y = divider_y + divider_h + pad_below
    canvas.paste(chart_resized, (chart_x, chart_y), chart_resized)

    # Save combined
    out_png = DIR / "fig1_combined_v3.png"
    out_pdf = DIR / "fig1_combined_v3.pdf"
    canvas_rgb = canvas.convert("RGB")
    canvas_rgb.save(out_png, dpi=(DPI, DPI))
    canvas_rgb.save(out_pdf, dpi=(DPI, DPI))
    print(f"Saved {out_png} and {out_pdf}")

    # Save chat-only
    chat_rgb = chat.convert("RGB")
    chat_rgb.save(DIR / "fig1_chat_v3_only.png", dpi=(DPI, DPI))
    chat_rgb.save(DIR / "fig1_chat_v3_only.pdf", dpi=(DPI, DPI))
    print("Saved fig1_chat_v3_only.png and .pdf")

    return out_png


if __name__ == "__main__":
    chat_img = render_chat()
    chart_img = render_chart()
    final = composite(chat_img, chart_img)
    subprocess.run(["open", str(final)])
