#!/usr/bin/env python3
"""Render the front page of THE WORLD for 25 November 2026.

Fresh artwork drawn from the bounty brief with Pillow only. No network
access, no external assets beyond the system Noto fonts. Output is a
1024x1024 PNG, white paper, black ink, dark-red accent.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 40
CONTENT_W = W - 2 * MARGIN
INK = (17, 17, 17)
PAPER = (255, 255, 255)
RED = (140, 29, 24)
GREY_RULE = (120, 120, 120)

FONT_DIR = "/usr/share/fonts/truetype/noto"
SERIF_BOLD = os.path.join(FONT_DIR, "NotoSerif-Bold.ttf")
SERIF_ITALIC = os.path.join(FONT_DIR, "NotoSerif-Italic.ttf")
SANS_BOLD = os.path.join(FONT_DIR, "NotoSans-Bold.ttf")
SANS_REG = os.path.join(FONT_DIR, "NotoSans-Regular.ttf")

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, text, fnt):
    return draw.textlength(text, font=fnt)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if text_w(draw, trial, fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, y, text, fnt, fill=INK):
    draw.text((W / 2, y), text, font=fnt, fill=fill, anchor="ma")


def draw_lines(draw, x, y, lines, fnt, fill=INK, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.18)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill, anchor="la")
        y += leading
    return y


def rule(draw, y, x0=None, x1=None, width=1, fill=INK):
    x0 = MARGIN if x0 is None else x0
    x1 = W - MARGIN if x1 is None else x1
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    masthead = font(SERIF_BOLD, 112)
    date_font = font(SANS_BOLD, 26)
    tagline_font = font(SERIF_ITALIC, 21)
    lead_kicker = font(SANS_BOLD, 20)
    lead_head = font(SANS_BOLD, 56)
    lead_sum = font(SANS_REG, 21)
    kick_font = font(SANS_BOLD, 17)
    head_font = font(SANS_BOLD, 30)
    sum_font = font(SANS_REG, 19)
    foot_font = font(SANS_BOLD, 18)

    # --- Masthead ---
    draw_centered(draw, 14, "THE WORLD", masthead, INK)
    rule(draw, 134, width=2)
    rule(draw, 138, width=1)

    # --- Date line + tagline ---
    draw_centered(draw, 148, "WEDNESDAY, 25 NOVEMBER 2026", date_font, INK)
    draw_centered(draw, 178, "The day in seven stories", tagline_font, INK)

    # --- Thick divider under the date block ---
    draw.line([(MARGIN, 210), (W - MARGIN, 210)], fill=INK, width=4)
    rule(draw, 216, width=1)

    # --- Lead story, full width ---
    y = 228
    draw.text((MARGIN, y), "UKRAINE WAR", font=lead_kicker, fill=RED, anchor="la")
    y += 30
    lead_lines = wrap(draw, "700,000 RUSSIAN TROOPS KILLED", lead_head, CONTENT_W)
    y = draw_lines(draw, MARGIN, y, lead_lines, lead_head, INK, leading=62)
    y += 8
    lead_sum_lines = wrap(
        draw,
        "A new analysis puts Russia's war dead past 700,000 in nearly "
        "five years of war in Ukraine.",
        lead_sum,
        CONTENT_W,
    )
    y = draw_lines(draw, MARGIN, y, lead_sum_lines, lead_sum, INK, leading=27)
    y += 12
    rule(draw, y, width=2)
    grid_top = y + 14

    # --- Six stories, 2 columns x 3 rows ---
    stories = [
        (
            "UKRAINE WAR",
            "UKRAINE SINKS RUSSIAN WARSHIP OFF LIBYA",
            "Kyiv says its forces struck a Russian warship and a cargo "
            "vessel near Benghazi; one ship sunk.",
        ),
        (
            "ENERGY",
            "IRAN BRACES FOR WINTER GAS CRISIS",
            "War damage deepens fuel shortages as Iran begins rationing "
            "electricity ahead of winter.",
        ),
        (
            "MIDDLE EAST",
            "IRAQ MOVES ON KURDISH OILFIELDS",
            "Baghdad orders federal forces to seize oilfields and border "
            "crossings in Kurdish-run regions.",
        ),
        (
            "ASIA",
            "INDONESIA'S VICE-PRESIDENT RESIGNS",
            "The vice-president steps down amid mounting political strain "
            "in Jakarta.",
        ),
        (
            "SPORT",
            "REAL MADRID ROUT PSV 5\u20131",
            "Bellingham's stunner and a Mbapp\u00e9 brace power a Champions "
            "League comeback in Madrid.",
        ),
        (
            "LATIN AMERICA",
            "CAR BOMB WOUNDS 23 IN COLOMBIA",
            "A blast injures at least 23 people as violence rattles the "
            "country.",
        ),
    ]

    gutter = 28
    col_w = (CONTENT_W - gutter) // 2
    # 168 keeps the footer clear of the bottom edge (grid ends ~974,
    # footer text ends ~1010, leaving a clean bottom margin).
    row_h = 168
    for idx, (kicker, headline, summary) in enumerate(stories):
        col = idx % 2
        row = idx // 2
        x = MARGIN + col * (col_w + gutter)
        cy = grid_top + row * row_h
        draw.text((x, cy), kicker, font=kick_font, fill=RED, anchor="la")
        hy = cy + 24
        head_lines = wrap(draw, headline, head_font, col_w)
        hy = draw_lines(draw, x, hy, head_lines, head_font, INK, leading=35)
        hy += 6
        sum_lines = wrap(draw, summary, sum_font, col_w)
        draw_lines(draw, x, hy, sum_lines, sum_font, INK, leading=24)

    grid_bottom = grid_top + 3 * row_h
    # Vertical divider between the two columns.
    mid_x = MARGIN + col_w + gutter // 2
    draw.line(
        [(mid_x, grid_top + 4), (mid_x, grid_bottom - 6)],
        fill=GREY_RULE,
        width=1,
    )
    # Horizontal dividers between rows.
    for r in (1, 2):
        ry = grid_top + r * row_h - 8
        rule(draw, ry, fill=GREY_RULE)

    # --- Footer ---
    rule(draw, grid_bottom + 6, width=2)
    draw_centered(draw, grid_bottom + 16, "THE WORLD \u2014 25 NOVEMBER 2026",
                  foot_font, INK)

    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} {W}x{H} {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
