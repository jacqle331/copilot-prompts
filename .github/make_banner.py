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

# Evergreen badge line (no category list — never goes stale)
badge_f = font(F + "segoeuib.ttf", 28)
badge_text = "Ready-to-use prompts for work & life"
bw = draw.textlength(badge_text, font=badge_f)
bx, by, bh = (W - (bw + 60)) / 2, 405, 56
draw.rounded_rectangle([bx, by, bx + bw + 60, by + bh], radius=bh // 2, fill="#a855f7")
draw.text((bx + 30, by + (bh - 36) / 2 - 1), badge_text, font=badge_f, fill="#ffffff")

# Footer
center_text(530, "No coding required  \u2022  github.com/jacqle331/copilot-prompts", sub_f, "#ddd6fe")

out = "C:/Users/jacqle/repos/copilot-prompts/.github/social-preview.png"
img.save(out, "PNG")
print("Saved", out, img.size)
