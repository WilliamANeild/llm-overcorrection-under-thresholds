#!/usr/bin/env python3
"""Render all 4 figure variants for comparison."""

import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont

DIR = Path(__file__).resolve().parent

VARIANTS = {
    "A": ("fig1_variant_a.html", "Minimal/academic - text blocks, serif font"),
    "B": ("fig1_variant_b.html", "Clean chat bubbles, no avatars, T1-T5 labels + chart"),
    "C": ("fig1_variant_c.html", "Same as B but caption stats instead of chart"),
    "D": ("fig1_variant_d.html", "Table layout - compact, structured"),
}


def render_all():
    images = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for key, (html_file, desc) in VARIANTS.items():
            page = browser.new_page(device_scale_factor=3)
            page.goto(f"file://{DIR / html_file}")
            page.wait_for_load_state("networkidle")
            body = page.query_selector("body")
            out = DIR / f"fig1_variant_{key.lower()}.png"
            body.screenshot(path=str(out))
            images[key] = out
            page.close()
            print(f"Rendered variant {key}: {desc}")
        browser.close()
    return images


def make_comparison(images):
    imgs = {k: Image.open(v).convert("RGB") for k, v in images.items()}

    # Arrange 2x2
    pad = 40
    label_h = 60
    max_w = max(im.width for im in imgs.values())
    max_h = max(im.height for im in imgs.values())

    cell_w = max_w + pad
    cell_h = max_h + label_h + pad

    canvas_w = cell_w * 2 + pad
    canvas_h = cell_h * 2 + pad

    canvas = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
        font_sm = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
    except Exception:
        font = ImageFont.load_default()
        font_sm = font

    descs = {
        "A": "A: Minimal/academic",
        "B": "B: Clean chat + chart",
        "C": "C: Chat + caption stats",
        "D": "D: Table layout",
    }

    positions = {"A": (0, 0), "B": (1, 0), "C": (0, 1), "D": (1, 1)}

    for key, (col, row) in positions.items():
        x = pad + col * cell_w
        y = pad + row * cell_h

        draw.text((x, y), descs[key], fill="#333333", font=font)
        img = imgs[key]
        canvas.paste(img, (x, y + label_h))

        # Border
        draw.rectangle(
            [x - 2, y + label_h - 2, x + img.width + 2, y + label_h + img.height + 2],
            outline="#dddddd", width=2
        )

    out = DIR / "fig1_variants_comparison.png"
    canvas.save(out, dpi=(200, 200))
    print(f"Saved comparison: {out}")
    return out


if __name__ == "__main__":
    images = render_all()
    comp = make_comparison(images)
    subprocess.run(["open", str(comp)])
