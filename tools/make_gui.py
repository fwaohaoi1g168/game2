"""メッセージ窓・選択肢・メニューなどの GUI の絵を作る（11/6 本人：メニューやタイトル画面のデザイン全体を見直して）。

使い方（game2 フォルダで）：
  python tools/make_gui.py

game/gui/ の絵を上書きする（Ren'Py が最初に作った絵を、大正ロマンふうの色と形に置きかえる）。
色は下の PALETTE。色を変えたら gui.rpy の色もそろえる。
【AI発案 2026-11-06】色は、生成り（和紙）・海老茶（女学生の袴の色）・くすんだ金。
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
GUI = ROOT / "game" / "gui"

KINARI = (248, 242, 229)      # 生成り
KINARI_D = (236, 225, 203)    # 少し濃い生成り
EBICHA = (110, 38, 48)        # 海老茶
EBICHA_L = (150, 56, 68)
GOLD = (184, 146, 82)         # くすんだ金
SUMI = (58, 40, 34)           # 墨（文字）

S = 3  # なめらかにするため、3倍で描いてから縮める


def canvas(w, h):
    return Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0))


def done(im, path):
    w, h = im.size
    im = im.resize((w // S, h // S), Image.LANCZOS)
    path = GUI / path
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path)
    print(path.relative_to(ROOT), im.size)


def rr(d, box, r, fill=None, outline=None, width=1):
    x0, y0, x1, y1 = [v * S for v in box]
    d.rounded_rectangle((x0, y0, x1, y1), r * S, fill=fill, outline=outline, width=width * S)


def diamond(d, cx, cy, r, fill):
    cx, cy, r = cx * S, cy * S, r * S
    d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=fill)


def a(c, alpha):
    return c + (alpha,)


# メッセージ窓：横 1920、高さ 277。上の 30px は名前の札がはみ出す分としてあける
# 下の 40px は、クイックメニュー（ロールバック・セーブなど）の細い帯（11/6：窓のふちと文字が重なったので分けた）
def textbox():
    W, H = 1920, 277
    im = canvas(W, H); d = ImageDraw.Draw(im)
    rr(d, (150, 30, 1770, 236), 16, fill=a(KINARI, 235))
    rr(d, (160, 40, 1760, 226), 10, outline=a(GOLD, 255), width=2)
    rr(d, (166, 46, 1754, 220), 7, outline=a(GOLD, 120), width=1)
    for x in (160, 1760):
        diamond(d, x, 133, 7, a(GOLD, 255))
    rr(d, (400, 242, 1520, 274), 12, fill=a(KINARI, 215), outline=a(GOLD, 200), width=1)
    done(im, "textbox.png")


# 名前の札
def namebox():
    W, H = 300, 60
    im = canvas(W, H); d = ImageDraw.Draw(im)
    rr(d, (2, 2, W - 2, H - 2), 10, fill=a(EBICHA, 250), outline=a(GOLD, 255), width=2)
    rr(d, (7, 7, W - 7, H - 7), 6, outline=a(GOLD, 110), width=1)
    done(im, "namebox.png")


# 選択肢
def choice():
    W, H = 1185, 78
    for name, fill, line in (("idle", a(KINARI, 238), GOLD), ("hover", a(EBICHA, 245), GOLD)):
        im = canvas(W, H); d = ImageDraw.Draw(im)
        rr(d, (4, 4, W - 4, H - 4), 12, fill=fill, outline=a(line, 255), width=2)
        rr(d, (10, 10, W - 10, H - 10), 8, outline=a(line, 110), width=1)
        for x in (40, W - 40):
            diamond(d, x, H / 2, 7, a(GOLD, 255))
        done(im, f"button/choice_{name}_background.png")


# セーブ・ロードの枠
def slot():
    W, H = 414, 309
    for name, line, wd in (("idle", GOLD, 2), ("hover", EBICHA, 4)):
        im = canvas(W, H); d = ImageDraw.Draw(im)
        rr(d, (3, 3, W - 3, H - 3), 10, fill=a(KINARI_D, 255), outline=a(line, 255), width=wd)
        rr(d, (15, 15, W - 15, 229), 4, fill=a((225, 212, 188), 255))
        done(im, f"button/slot_{name}_background.png")


# 確認のダイアログの枠
def frame():
    W, H = 900, 375
    im = canvas(W, H); d = ImageDraw.Draw(im)
    rr(d, (3, 3, W - 3, H - 3), 14, fill=a(KINARI, 250), outline=a(EBICHA, 255), width=3)
    rr(d, (12, 12, W - 12, H - 12), 9, outline=a(GOLD, 255), width=2)
    for x, y in ((12, 12), (W - 12, 12), (12, H - 12), (W - 12, H - 12)):
        diamond(d, x, y, 8, a(GOLD, 255))
    done(im, "frame.png")


# 通知・スキップ中の札
def small_panels():
    for path, (W, H) in (("notify.png", (1383, 64)), ("skip.png", (360, 64))):
        im = canvas(W, H); d = ImageDraw.Draw(im)
        rr(d, (2, 2, W - 2, H - 2), 10, fill=a(KINARI, 235), outline=a(GOLD, 255), width=2)
        done(im, path)


# 棒（音量など）とスライダーとスクロールバー
def bars():
    def bar(path, w, h, fill, line):
        im = canvas(w, h); d = ImageDraw.Draw(im)
        r = min(w, h) / 2 - 2
        rr(d, (2, 2, w - 2, h - 2), r, fill=fill, outline=line, width=2)
        done(im, path)
    def thumb(path, w, h, fill):
        im = canvas(w, h); d = ImageDraw.Draw(im)
        rr(d, (1, 1, w - 1, h - 1), min(w, h) / 2 - 1, fill=fill, outline=a(EBICHA, 255), width=2)
        done(im, path)
    bar("bar/left.png", 525, 38, a(EBICHA, 255), a(GOLD, 255))
    bar("bar/right.png", 525, 38, a(KINARI_D, 255), a(GOLD, 255))
    bar("bar/top.png", 38, 525, a(KINARI_D, 255), a(GOLD, 255))
    bar("bar/bottom.png", 38, 525, a(EBICHA, 255), a(GOLD, 255))
    for st, line in (("idle", GOLD), ("hover", EBICHA)):
        bar(f"slider/horizontal_{st}_bar.png", 525, 38, a(KINARI_D, 255), a(line, 255))
        bar(f"slider/vertical_{st}_bar.png", 38, 525, a(KINARI_D, 255), a(line, 255))
        thumb(f"slider/horizontal_{st}_thumb.png", 15 if st == "idle" else 15, 38, a(GOLD if st == "idle" else EBICHA_L, 255))
        thumb(f"slider/vertical_{st}_thumb.png", 38, 15, a(GOLD if st == "idle" else EBICHA_L, 255))
        bar(f"scrollbar/horizontal_{st}_bar.png", 1050, 18, a(KINARI_D, 255), a(GOLD, 160))
        bar(f"scrollbar/vertical_{st}_bar.png", 18, 1050, a(KINARI_D, 255), a(GOLD, 160))
        bar(f"scrollbar/horizontal_{st}_thumb.png", 1050, 18, a(GOLD if st == "idle" else EBICHA_L, 255), a(GOLD, 255))
        bar(f"scrollbar/vertical_{st}_thumb.png", 18, 1050, a(GOLD if st == "idle" else EBICHA_L, 255), a(GOLD, 255))


# 設定画面の「選んでいる」印（左の小さな棒）
def marks():
    for path in ("button/check_selected_foreground.png", "button/radio_selected_foreground.png"):
        im = canvas(27, 49); d = ImageDraw.Draw(im)
        diamond(d, 11, 24.5, 8, a(EBICHA, 255))
        done(im, path)
    for path in ("button/check_foreground.png", "button/radio_foreground.png"):
        im = canvas(27, 49); d = ImageDraw.Draw(im)
        x, y, r = 11 * S, 24.5 * S, 8 * S
        d.polygon([(x, y - r), (x + r, y), (x, y + r), (x - r, y)], outline=a(GOLD, 255), width=2 * S)
        done(im, path)


# 矢絣（やがすり）の地紋。うすく敷く
def yagasuri(W, H, c1, c2, cw=64, ch=96):
    im = Image.new("RGBA", (W, H), a(c1, 255)); d = ImageDraw.Draw(im)
    for i, x in enumerate(range(0, W + cw, cw)):
        off = 0 if i % 2 == 0 else ch // 2
        for y in range(-ch, H + ch, ch):
            y0 = y + off
            d.polygon([(x, y0), (x + cw / 2, y0 + ch / 3), (x + cw, y0), (x + cw, y0 + ch / 2), (x + cw / 2, y0 + ch / 2 + ch / 3), (x, y0 + ch / 2)], fill=a(c2, 255))
    return im


# ゲームメニュー（セーブ・ロード・設定など）の背景と、左の帯
def menus():
    bg = yagasuri(1920, 1080, KINARI, (243, 235, 219))
    bg.save(GUI / "game_menu.png"); print("game/gui/game_menu.png", bg.size)
    band = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0)); d = ImageDraw.Draw(band)
    d.rectangle((0, 0, 419, 1080), fill=a(KINARI_D, 235))
    d.rectangle((414, 0, 416, 1080), fill=a(GOLD, 255))
    d.rectangle((421, 0, 421, 1080), fill=a(GOLD, 150))
    band.save(GUI / "overlay" / "game_menu.png"); print("game/gui/overlay/game_menu.png")
    # タイトル画面の左の帯：絵が透けるように少し薄く
    band = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0)); d = ImageDraw.Draw(band)
    d.rectangle((0, 0, 419, 1080), fill=a(KINARI, 205))
    d.rectangle((414, 0, 416, 1080), fill=a(GOLD, 255))
    d.rectangle((421, 0, 421, 1080), fill=a(GOLD, 150))
    band.save(GUI / "overlay" / "main_menu.png"); print("game/gui/overlay/main_menu.png")
    # 確認のときに後ろを暗くする
    Image.new("RGBA", (1920, 1080), (30, 14, 16, 140)).save(GUI / "overlay" / "confirm.png")


if __name__ == "__main__":
    textbox(); namebox(); choice(); slot(); frame(); small_panels(); bars(); marks(); menus()
