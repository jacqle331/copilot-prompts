from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
img = Image.new("RGB", (W, H), "#1e1b4b")
draw = ImageDraw.Draw(img)

# Vertical gradient: deep indigo -> violet
top = (49, 27, 105)      # #311b69
bot = (124, 58, 173)     # #7c3aad
for y in range(H):
    t = y / H
    r = int(top[0] + (bot[0] - top[0]) * t)
    g = int(top[1] + (bot[1] - top[1]) * t)
    b = int(top[2] + (bot[2] - top[2]) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Subtle decorative dots
import random
random.seed(7)
for _ in range(60):
    x = random.randint(0, W); y = random.randint(0, H)
    rad = random.choice([1, 1, 2, 2, 3])
    draw.ellipse([x, y, x + rad, y + rad], fill=(255, 255, 255, 40))

def font(path, size):
    return ImageFont.truetype(path, size)

F = "C:/Windows/Fonts/"
title_f = font(F + "segoeuib.ttf", 92)
tag_f = font(F + "segoeui.ttf", 38)
sub_f = font(F + "segoeui.ttf", 27)
chip_f = font(F + "segoeuib.ttf", 26)

def center_text(y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return w

# Title
center_text(120, "Copilot Prompts", title_f, "#ffffff")

# Tagline
center_text(238, "A community library of helpful, reusable AI prompts", tag_f, "#e9d5ff")

# Subtitle
center_text(300, "Browse  \u00b7  Copy  \u00b7  Adapt  \u00b7  Share", sub_f, "#c4b5fd")

# Category chips
chips = [
    ("Productivity", "#22c55e"),
    ("Writing", "#3b82f6"),
    ("Research", "#f59e0b"),
    ("Leadership", "#ec4899"),
]
pad_x, chip_h, gap = 28, 58, 22
widths = [draw.textlength(c[0], font=chip_f) + pad_x * 2 for c in chips]
total = sum(widths) + gap * (len(chips) - 1)
x = (W - total) / 2
cy = 400
for (label, color), w in zip(chips, widths):
    draw.rounded_rectangle([x, cy, x + w, cy + chip_h], radius=chip_h // 2, fill=color)
    tw = draw.textlength(label, font=chip_f)
    draw.text((x + (w - tw) / 2, cy + (chip_h - 34) / 2 - 2), label, font=chip_f, fill="#ffffff")
    x += w + gap

# Footer
center_text(530, "No coding required  \u2022  github.com/jacqle331/copilot-prompts", sub_f, "#ddd6fe")

out = "C:/Users/jacqle/repos/copilot-prompts/.github/social-preview.png"
img.save(out, "PNG")
print("Saved", out, img.size)
