"""Render assets/temporal-desk.gif: a pixel desk whose monitor shows hyperedges expiring over time."""

import os

from PIL import Image, ImageDraw

W, H, SCALE, FRAMES = 64, 48, 6, 32
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "temporal-desk.gif")

OUTLINE = (15, 23, 42)
FRAME = (51, 65, 85)
SCREEN = (11, 18, 32)
DESK = (100, 116, 139)
DESK_DARK = (71, 85, 105)
KEY = (148, 163, 184)
KEY_LIT = (241, 245, 249)
NODE = (226, 232, 240)
MUG = (203, 213, 225)
STEAM = (148, 163, 184)
LED = (34, 197, 94)
POT = (180, 83, 9)
LEAF = (74, 222, 128)
LEAF_DARK = (22, 163, 74)
EDGE_COLORS = [(249, 115, 22), (14, 165, 233), (168, 85, 247), (234, 179, 8)]

NODES = [(24, 15), (31, 13), (39, 15), (41, 22), (34, 25), (26, 24), (32, 19)]
HYPEREDGES = [
    ((0, 1, 6), 0, 14),
    ((6, 2, 3), 6, 20),
    ((5, 4, 6), 12, 26),
    ((1, 2, 6), 18, 32),
    ((0, 5, 4), 24, 38),
]


def blend(color, alpha):
    return tuple(int(SCREEN[i] + (color[i] - SCREEN[i]) * alpha) for i in range(3))


def edge_alpha(frame, start, end):
    t = frame % FRAMES
    for shift in (0, FRAMES):
        s, e = start - shift, end - shift
        if s <= t < e:
            fade = 3
            return min(1.0, (t - s + 1) / fade, (e - t) / fade)
    return 0.0


def draw_frame(frame):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    d.rectangle([17, 9, 47, 33], fill=FRAME, outline=OUTLINE)
    d.rectangle([19, 11, 45, 31], fill=SCREEN)
    d.rectangle([30, 34, 34, 36], fill=FRAME, outline=OUTLINE)
    d.rectangle([26, 36, 38, 37], fill=FRAME, outline=OUTLINE)
    if frame % 8 < 6:
        d.point((45, 32), fill=LED)

    for i, (members, start, end) in enumerate(HYPEREDGES):
        alpha = edge_alpha(frame, start, end)
        if alpha <= 0:
            continue
        color = blend(EDGE_COLORS[i % len(EDGE_COLORS)], alpha)
        pts = [NODES[m] for m in members]
        for a in range(len(pts)):
            d.line([pts[a], pts[(a + 1) % len(pts)]], fill=color)

    for x, y in NODES:
        d.rectangle([x - 1, y - 1, x, y], fill=NODE)

    d.line([(21, 29), (43, 29)], fill=FRAME)
    cursor = 21 + (frame % FRAMES) * 22 // (FRAMES - 1)
    d.line([(cursor, 28), (cursor, 30)], fill=EDGE_COLORS[0])

    d.rectangle([3, 38, 60, 40], fill=DESK, outline=OUTLINE)
    d.rectangle([6, 41, 8, 47], fill=DESK_DARK, outline=OUTLINE)
    d.rectangle([55, 41, 57, 47], fill=DESK_DARK, outline=OUTLINE)

    d.rectangle([22, 35, 42, 37], fill=FRAME, outline=OUTLINE)
    lit = {(frame * 7) % 9, (frame * 4 + 3) % 9}
    for k in range(9):
        d.point((24 + k * 2, 36), fill=KEY_LIT if k in lit else KEY)

    sway = 1 if frame % 16 < 8 else 0
    d.rectangle([51, 33, 56, 37], fill=POT, outline=OUTLINE)
    d.line([(53, 32), (53, 27)], fill=LEAF_DARK)
    for dx, dy in [(-3, -1), (2, -1), (-3, -4), (2, -4), (-1, -7)]:
        x, y = 53 + dx + (sway if dy < -3 else 0), 31 + dy
        d.rectangle([x, y, x + 1, y + 1], fill=LEAF, outline=LEAF_DARK)

    d.rectangle([8, 32, 12, 37], fill=MUG, outline=OUTLINE)
    d.rectangle([13, 33, 14, 35], outline=OUTLINE)
    for i in range(3):
        y = 30 - ((frame + i * 3) % 9)
        x = 9 + (i + (frame // 3)) % 3
        if y > 22:
            d.point((x, y), fill=STEAM)

    return img.resize((W * SCALE, H * SCALE), Image.NEAREST)


def main():
    frames = [draw_frame(f) for f in range(FRAMES)]
    paletted = []
    for f in frames:
        alpha = f.getchannel("A")
        p = f.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=255)
        mask = Image.eval(alpha, lambda a: 255 if a == 0 else 0)
        p.paste(255, mask=mask)
        paletted.append(p)
    paletted[0].save(
        OUT,
        save_all=True,
        append_images=paletted[1:],
        duration=140,
        loop=0,
        transparency=255,
        disposal=2,
        optimize=False,
    )


if __name__ == "__main__":
    main()
