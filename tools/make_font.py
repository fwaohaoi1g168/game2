"""（1）今のフォント（SourceHanSansLite）にない字を探し、Noto Sans JP からその字だけを切り出して補う。

使い方（game2 フォルダで）：
  python tools/make_font.py

game/*.rpy の文を全部調べ、SourceHanSansLite.ttf にない字を
Windows の Noto Sans JP（C:/Windows/Fonts/NotoSansJP-VF.ttf、太さ 400 にする）から切り出して
game/fonts/hosoku.ttf に書き出し、game/fonts_hosoku.rpy（どの字を補うか）を作る。
本文を変えたら、もう一度これを動かす。
（2）題名・メニュー・名前に使う明朝体 game/fonts/serif.ttf も作る（下のほう）。
11/6：「罠」が文字化けしていた（本人が遊んで気づいた）。
Noto Sans JP は SIL Open Font License 1.1。切り出したファイルにも、著作権と使用条件の記録（name 表）を残す。
"""
import glob
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools import subset

ROOT = Path(__file__).resolve().parent.parent
GAME = ROOT / "game"
BASE = GAME / "SourceHanSansLite.ttf"
NOTO = Path("C:/Windows/Fonts/NotoSansJP-VF.ttf")
OUT = GAME / "fonts" / "hosoku.ttf"
RPY = GAME / "fonts_hosoku.rpy"
# Ren'Py が別のフォントで出す記号（スキップ中の ▸ など）と、ファイルの先頭の印は調べない
SKIP = {"\ufeff", "▸"}

base = TTFont(BASE).getBestCmap()
text = "".join(Path(f).read_text(encoding="utf-8") for f in sorted(glob.glob(str(GAME / "*.rpy")))
               if not f.endswith("fonts_hosoku.rpy"))
missing = sorted({ch for ch in text if ord(ch) > 127 and ord(ch) not in base and ch not in SKIP})
noto = TTFont(NOTO)
nocmap = noto.getBestCmap()
lack = [ch for ch in missing if ord(ch) not in nocmap]
if lack:
    print("Noto Sans JP にもない字：", "".join(lack))
chars = [ch for ch in missing if ord(ch) in nocmap]
print("補う字：", "".join(chars) or "なし")

OUT.parent.mkdir(parents=True, exist_ok=True)
if chars:
    font = instancer.instantiateVariableFont(noto, {"wght": 400})
    opt = subset.Options()
    opt.name_IDs = ["*"]          # 著作権と使用条件の記録を残す
    opt.name_languages = ["*"]
    opt.notdef_outline = True
    sub = subset.Subsetter(opt)
    sub.populate(unicodes=[ord(c) for c in chars])
    sub.subset(font)
    font.save(OUT)

RPY.write_text(
    "## tools/make_font.py が作る。手で直さない。\n"
    "## SourceHanSansLite にない字だけを fonts/hosoku.ttf（Noto Sans JP から切り出し）で出す。\n"
    "init -2 python:\n"
    f"    HOSOKU_CHARS = {''.join(chars)!r}\n"
    "    def hosoku_font(base):\n"
    "        g = FontGroup()\n"
    "        for ch in HOSOKU_CHARS:\n"
    "            g.add(\"fonts/hosoku.ttf\", ord(ch), ord(ch))\n"
    "        return g.add(base, None, None)\n",
    encoding="utf-8")
print("書き出し：", OUT if chars else "(フォントなし)", RPY)

# 11/6：題名・メニュー・名前に使う明朝体（Noto Serif JP、太さ 600）。
# game/*.rpy に出てくる字と、英数字・ひらがな・カタカナだけを切り出す（全部入れると重いため）。
# 名前やメニューの文字を変えたら、もう一度これを動かす。
SERIF_SRC = Path("C:/Windows/Fonts/NotoSerifJP-VF.ttf")
SERIF_OUT = GAME / "fonts" / "serif.ttf"
serif = TTFont(SERIF_SRC)
want = {ord(ch) for ch in text if ord(ch) > 32} | set(range(0x20, 0x7f)) | set(range(0x3000, 0x3100)) | set(range(0x30a0, 0x3100)) | set(range(0xff01, 0xff5f))
want &= set(serif.getBestCmap())
serif = instancer.instantiateVariableFont(serif, {"wght": 600})
opt = subset.Options()
opt.name_IDs = ["*"]
opt.name_languages = ["*"]
opt.notdef_outline = True
sub = subset.Subsetter(opt)
sub.populate(unicodes=sorted(want))
sub.subset(serif)
serif.save(SERIF_OUT)
print("明朝体：", len(want), "字", SERIF_OUT)
