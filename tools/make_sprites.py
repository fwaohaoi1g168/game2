"""立ち絵の元の絵（白い背景）から、背景を透明にした立ち絵を作る。

使い方（game2 フォルダで）：
  python tools/make_sprites.py <元の絵のフォルダ>

元の絵のフォルダにあるファイルのうち、下の SOURCES に書いたものを変換して
game/images/chara/<名前>.png に書き出す。表情の差分を足したら、SOURCES に1行足す。
白い背景のうち、絵のふちとつながっている部分だけを透明にする（手袋などの白は残る）。
"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "game" / "images" / "chara"

# 出力の名前 → (元の絵のファイル名, 元の絵を引き伸ばしたあとの高さ px, 画面に出す上からの高さ px)
# 11/6 本人：全身だと遠いので、腰から上にした。元の絵を大きく引き伸ばしてから、上から「画面に出す高さ」だけを切り出す。
# 画面の下にそろえて出すので、頭の位置は 1080 − 画面に出す高さ（鉄次・父は上から40px、千鶴は190px。千鶴のほうが背が低い）
# 11/6 本人：腰から上の絵を追加。「基本的にそれ使って」。背景がはじめから透明な絵（RGBA）は、背景を消す処理を飛ばす。
# 4つ目に "flip" と書いたものは左右を反転する（11/6 本人：お嬢様は左右反転させて）。
# 引き伸ばす高さは、全身の絵のときと顔の大きさがそろうように合わせた（AI が目で見て決めた）。
SOURCES = {
    "chizuru_base": ("2026-11-06_お嬢様_腰から上_本を抱く_笑顔.png", 1045, 890, "flip"),
    "chizuru_hashagu": ("2026-11-06_お嬢様_腰から上_はしゃぐ.png", 1045, 890, "flip"),
    "chizuru_shitataka": ("2026-11-06_お嬢様_腰から上_したたか.png", 1045, 890, "flip"),
    "chizuru_honne": ("2026-11-06_お嬢様_腰から上_本音.png", 1045, 890, "flip"),
    "chizuru_kangaeru": ("2026-11-08_お嬢様_腰から上_考え込む.png", 1045, 890, "flip"),  # 11/8 本人が足した
    "tetsuji_base": ("2026-11-06_人さらい_腰から上_あごに手_困る.png", 1300, 1040),
    "tetsuji_komaru": ("2026-11-06_人さらい_腰から上_あごに手_困る.png", 1300, 1040),
    "tetsuji_sugomu": ("2026-11-06_人さらい_腰から上_すごむ.png", 1300, 1040),
    "tetsuji_kuzure": ("2026-11-06_人さらい_腰から上_崩れ.png", 1300, 1040),
    "father_base": ("2026-11-06_ひげの紳士_腰から上_腕組み.png", 1200, 1040),
    "father_owarai": ("2026-11-06_ひげの紳士_腰から上_大笑い.png", 1200, 1040),
}
# 11/6：表情の差分を足した。同じ人の表情は、切り出す範囲を全部同じにする（表情ごとに絵の端の細かな点がちがい、
# そのまま切り出すと幅が変わって、表情が変わるたびに体が横にずれるため）。範囲は、その人の全部の表情を合わせた範囲。


def enclosed_gaps(lo, bg, white=249, ring_dark=215, min_size=20):
    """髪のすき間のように、絵に囲まれて残った白い背景を探す（11/6 追加）。
    ほぼ真っ白なかたまりのうち、まわりの色が濃いもの（髪など）だけを背景とみなす。
    手袋やえりのように、まわりも明るいものは残す。"""
    H, W = lo.shape
    cand = (lo >= white) & ~bg
    seen = np.zeros_like(cand)
    out = np.zeros_like(cand)
    ys, xs = np.nonzero(cand)
    for y0, x0 in zip(ys, xs):
        if seen[y0, x0]:
            continue
        stack = [(y0, x0)]; seen[y0, x0] = True; comp = []
        while stack:
            y, x = stack.pop(); comp.append((y, x))
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < H and 0 <= nx < W and cand[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True; stack.append((ny, nx))
        if len(comp) < min_size:
            continue
        cy, cx = np.array(comp).T
        ring = []
        for dy, dx in ((3, 0), (-3, 0), (0, 3), (0, -3)):
            ry, rx = np.clip(cy + dy, 0, H - 1), np.clip(cx + dx, 0, W - 1)
            v = lo[ry, rx]
            ring.append(v[~cand[ry, rx]])
        ring = np.concatenate(ring)
        if ring.size and np.median(ring) < ring_dark:
            out[cy, cx] = True
    return out


def from_alpha(src):
    """背景がはじめから透明な絵：ほぼ不透明（245以上）は不透明に、ほぼ透明（10以下）は透明にそろえる。"""
    rgba = np.asarray(Image.open(src).convert("RGBA")).copy()
    al = rgba[..., 3]
    al[al >= 245] = 255
    al[al <= 10] = 0
    return Image.fromarray(rgba, "RGBA")


def cut(src, height, visible=None):
    if Image.open(src).mode == "RGBA":
        return fit(from_alpha(src), height, visible)
    im = Image.open(src).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    lo = a.min(axis=2)
    whiteish = lo > 228
    # 白っぽい部分のうち、絵のふちとつながっているところを塗りつぶしで探す
    m = Image.fromarray(np.where(whiteish, 255, 0).astype(np.uint8), "L").copy()
    H, W = whiteish.shape
    border = [(x, 0) for x in range(W)] + [(x, H - 1) for x in range(W)] + \
             [(0, y) for y in range(H)] + [(W - 1, y) for y in range(H)]
    for xy in border:
        if m.getpixel(xy) == 255:
            ImageDraw.floodfill(m, xy, 128)
    bg = np.asarray(m) == 128
    bg |= enclosed_gaps(lo, bg)
    # ふちを少しなめらかに：背景に接する画素は、白さに応じて半透明にする
    # 11/6：大きく引き伸ばすと白いふちが目立ったので、ふちを3pxに広げ、白をまぜた分の色を引き戻す
    grown = np.asarray(Image.fromarray(bg.astype(np.uint8) * 255, "L").filter(ImageFilter.MaxFilter(7))) > 0
    near = grown & ~bg
    alpha = np.where(bg, 0, 255).astype(np.float32)
    soft = np.clip((240 - lo) / (240 - 150), 0, 1) * 255
    alpha[near] = np.minimum(alpha[near], soft[near])
    rgb = a.astype(np.float32)
    k = np.clip(alpha / 255.0, 1e-3, 1)[..., None]
    fixed = np.clip((rgb - 255 * (1 - k)) / k, 0, 255)
    rgb = np.where(near[..., None], fixed, rgb)
    rgba = np.dstack([rgb.astype(np.uint8), alpha.astype(np.uint8)])
    return fit(Image.fromarray(rgba, "RGBA"), height, visible)


def fit(out, height, visible):
    box = out.getbbox()
    out = out.crop(box)
    w = round(out.width * height / out.height)
    out = out.resize((w, height), Image.LANCZOS)
    if visible:
        out = out.crop((0, 0, out.width, visible))
        l, t, r, b = out.getbbox()
        out = out.crop((l, 0, r, visible))
    return out


def same_box(imgs, height, visible):
    """同じ人の表情を、同じ範囲で切り出して同じ大きさにする（背景が透明な絵だけ）。"""
    box = imgs[0].getbbox()
    for im in imgs[1:]:
        b = im.getbbox()
        box = (min(box[0], b[0]), min(box[1], b[1]), max(box[2], b[2]), max(box[3], b[3]))
    w = round((box[2] - box[0]) * height / (box[3] - box[1]))
    outs = [im.crop(box).resize((w, height), Image.LANCZOS).crop((0, 0, w, visible)) for im in imgs]
    l = min(o.getbbox()[0] for o in outs); r = max(o.getbbox()[2] for o in outs)
    return [o.crop((l, 0, r, visible)) for o in outs]


if __name__ == "__main__":
    src_dir = Path(sys.argv[1])
    OUT.mkdir(parents=True, exist_ok=True)
    groups = {}
    for name, (fn, h, vis, *opt) in SOURCES.items():
        groups.setdefault(name.split("_")[0], []).append((name, fn, h, vis, opt))
    for ch, items in groups.items():
        if all(Image.open(src_dir / fn).mode == "RGBA" for _, fn, _, _, _ in items):
            imgs = same_box([from_alpha(src_dir / fn) for _, fn, _, _, _ in items], items[0][2], items[0][3])
        else:
            imgs = [cut(src_dir / fn, h, vis) for _, fn, h, vis, _ in items]
        for (name, fn, h, vis, opt), img in zip(items, imgs):
            if "flip" in opt:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            img.save(OUT / f"{name}.png")
            print(name, img.size)
