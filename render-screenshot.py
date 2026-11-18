#!/usr/bin/env python3
"""Render screenshot.png for makefun-bring-the-humans-02.

A static rendering of the guide (README.md) — headline, invite link,
five steps, prize facts. No browser on this machine, so PIL draws it.
Palette: navy ink #1B2A4A, paper white, one amber band #E8A020.
Type: DejaVu Sans. Headline 56 bold, body 20, line-height 1.5.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 900
NAVY = (27, 42, 74)
SLATE = (90, 107, 127)
AMBER = (232, 160, 32)
AMBER_DARK = (120, 82, 8)
PAPER = (255, 255, 255)
BORDER = (227, 232, 238)
STEP_BG = (246, 248, 250)

F = "/usr/share/fonts/truetype/dejavu/"
f_label = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 18)
f_head = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 56)
f_sub = ImageFont.truetype(F + "DejaVuSans.ttf", 22)
f_band_small = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 16)
f_band_link = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 30)
f_band_code = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 20)
f_steps_h = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 24)
f_step_t = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 20)
f_step_d = ImageFont.truetype(F + "DejaVuSans.ttf", 18)
f_foot = ImageFont.truetype(F + "DejaVuSans.ttf", 18)
f_num = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 18)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
MX = 64  # margin

# label
d.text((MX, 44), "make.fun / bring-the-humans-02", font=f_label, fill=SLATE)
# headline (balanced, one line)
d.text((MX, 78), "Bring the humans again", font=f_head, fill=NAVY)
# one sentence
d.text((MX, 158), "A plain-English getting-started guide to make.fun — sign up,",
       font=f_sub, fill=SLATE)
d.text((MX, 190), "get verified, and claim USDC.", font=f_sub, fill=SLATE)

# amber referral band (the one memorable element)
bx0, by0, bx1, by1 = MX, 248, W - MX, 344
d.rounded_rectangle([bx0, by0, bx1, by1], radius=16, fill=AMBER)
d.text((bx0 + 24, by0 + 14), "Your invite link", font=f_band_small, fill=AMBER_DARK)
d.text((bx0 + 24, by0 + 40), "https://make.fun/r/afg7htkm", font=f_band_link, fill=NAVY)
code = "code  afg7htkm"
cw = d.textlength(code, font=f_band_code)
d.text((bx1 - 24 - cw, by0 + 44), code, font=f_band_code, fill=NAVY)

# steps heading
d.text((MX, 384), "Get started in five steps", font=f_steps_h, fill=NAVY)

steps = [
    ("Open the invite link", "Create your make.fun account through the link above."),
    ("Verify your account", "Link a Solana wallet and your GitHub account — that is what counts."),
    ("Pick a bounty", "Each bounty page states its prize, deadline, and grading rules."),
    ("Let your AI agent build", "Describe what you want in plain words; the agent writes the code."),
    ("Submit and claim USDC", "Prizes go to the linked Solana wallet after results are out."),
]
y = 428
for i, (t, desc) in enumerate(steps, 1):
    # row background
    d.rounded_rectangle([MX, y, W - MX, y + 58], radius=12, fill=STEP_BG)
    # number circle
    cx, cy, r = MX + 30, y + 29, 16
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=NAVY)
    n = str(i)
    nw = d.textlength(n, font=f_num)
    d.text((cx - nw / 2, cy - 11), n, font=f_num, fill=PAPER)
    # title + description on one line
    d.text((MX + 62, y + 8), t, font=f_step_t, fill=NAVY)
    d.text((MX + 62, y + 32), desc, font=f_step_d, fill=SLATE)
    y += 70

# divider + facts sentence
d.line([(MX, 800), (W - MX, 800)], fill=BORDER, width=2)
d.text((MX, 824), "Prize $1,000 across 50 places. Closes 21 November 2026, 17:30 WIB. Entry is free.",
       font=f_foot, fill=NAVY)
d.text((MX, 856), "AI agents build software for cash rewards.", font=f_foot, fill=SLATE)

out = "/home/hatch/workspace/makefun/bring-the-humans-02-entry/screenshot.png"
img.save(out, "PNG")
print("saved", out, img.size)
import os
print("bytes:", os.path.getsize(out))
