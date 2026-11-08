"""本文の下書き（Markdown）を Ren'Py のスクリプト game/story.rpy に変える。

使い方（game2 フォルダで）：
  python tools/md_to_rpy.py <本文の .md のパス>

あわせて、声を作るための台詞の一覧を tools/lines.json に書き出す。
声のファイル game/audio/voice/<台詞のID>.ogg があれば、その台詞に voice 文を付ける。
"""
import sys, re, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAME = ROOT / "game"

# 話す人 → (Ren'Py のキャラ変数, 声の持ち主)
SPEAKERS = {
    "千鶴": ("c", "千鶴"), "鉄次": ("t", "鉄次"), "男": ("otoko", "鉄次"), "父": ("f", "父"),
    "書生": ("shosei", "書生"), "車夫": ("shafu", "車夫"), "似顔絵描き": ("nigaoe", "似顔絵描き"),
    "果物屋": ("kudamono", "果物屋"),
}
VOICE_ID = {"千鶴": "chizuru", "鉄次": "tetsuji", "父": "father", "書生": "shosei", "車夫": "shafu",
            "似顔絵描き": "nigaoe", "果物屋": "kudamono"}
SPRITES = {"千鶴": "chizuru", "鉄次": "tetsuji", "父": "father"}
EXPR = {"ふつう": "futsu", "はしゃぐ": "hashagu", "したたか": "shitataka", "本音": "honne", "考え込む": "kangaeru",
        "すごむ": "sugomu", "困る": "komaru", "崩れ": "kuzure", "大笑い": "owarai"}
BG = {"屋敷": "yashiki", "屋敷の中": "yashiki", "屋敷の外": "yashiki_soto", "街": "machi", "夕暮れの道": "yugure"}
CG = {"オチ": "ochi"}
BGM = {"屋敷": "yashiki", "街": "machi", "交渉と帰り道": "kosho", "本音": "honne", "オチ": "ochi"}
SE = {"屋敷の扉": "door", "路面電車": "densha", "街のざわめき": "zawameki"}


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("[", "[[").replace("{", "{{")


class Conv:
    def __init__(self):
        self.out = []
        self.lines = []
        self.shown = {}        # 名前 → 表情
        self.scene = ""
        self.count = {}
        self.indent = 1
        self.menu = None       # 選択肢の途中なら {"n":..., "base": shown}

    def emit(self, s):
        self.out.append("    " * self.indent + s)

    def positions(self):
        names = list(self.shown)
        pos = {}
        for n in names:
            if n == "千鶴":
                pos[n] = "pos_l"
            elif n == "父" and "鉄次" in names:
                pos[n] = "pos_c"
            else:
                pos[n] = "pos_r"
        return pos

    def show_all(self):
        for n, p in self.positions().items():
            e = self.shown[n]
            self.emit(f"show {SPRITES[n]} {e} at {p}")
        self.emit("with dissolve")

    def directive(self, body):
        if body.startswith("書き方"):
            return
        if body == "合流":
            self.indent = 1
            self.menu = None
            return
        if body == "終わり":
            self.emit("$ renpy.pause(1.0)")
            self.emit("return")
            return
        m = re.match(r"選択肢(\d+)：(.+)", body)
        if m:
            self.menu = {"n": m.group(1), "base": dict(self.shown)}
            self.indent = 1
            self.emit("menu:")
            self.emit(f'    "{esc(m.group(2))}"')
            return
        for part in re.split(r"[　 ]+", body):
            if "：" not in part:
                self.emit(f"# {part}")
                continue
            k, v = part.split("：", 1)
            if k == "背景":
                self.shown = {}
                self.emit(f"scene bg {BG[v]}")
                self.emit("with fade")
            elif k == "一枚絵":
                self.shown = {}
                self.emit(f"scene cg {CG[v]}")
                self.emit("with fade")
            elif k == "立ち絵":
                for item in v.split("、"):
                    mm = re.match(r"(.+?)（(.+)）", item)
                    name, ex = (mm.group(1), EXPR[mm.group(2)]) if mm else (item, self.shown.get(item, "base" if item == "父" else "futsu"))
                    self.shown[name] = ex
                self.show_all()
            elif k == "退場":
                for item in v.split("、"):
                    self.shown.pop(item, None)
                    self.emit(f"hide {SPRITES[item]}")
                self.emit("with dissolve")
            elif k == "BGM":
                if v == "止める":
                    self.emit("stop music fadeout 2.0")
                else:
                    self.emit(f'$ bgm("{BGM[v]}")')
            elif k == "効果音":
                self.emit(f'$ se("{SE[v]}")')
            else:
                self.emit(f"# {part}")

    def say(self, who, text):
        var, owner = SPEAKERS[who]
        key = f"{owner}_{self.scene}"
        self.count[key] = self.count.get(key, 0) + 1
        vid = f"{VOICE_ID[owner]}_{self.scene}_{self.count[key]:02d}"
        self.lines.append({"id": vid, "spk": owner, "scene": self.scene, "text": text})
        if (GAME / "audio" / "voice" / f"{vid}.ogg").exists():
            self.emit(f'voice "audio/voice/{vid}.ogg"')
        self.emit(f'{var} "{esc(text)}"')

    def run(self, md):
        self.out = ["# このファイルは tools/md_to_rpy.py が本文の下書きから作る。直接は直さない。", "",
                    "label start:", "    jump scene_1", ""]
        for raw in md.splitlines():
            line = raw.strip()
            if not line or line.startswith("# ") or line.startswith("種別") or line.startswith("状態") \
                    or line.startswith("上位") or line.startswith("※") or line == "---":
                continue
            if line.startswith("## 下書きで"):
                break
            m = re.match(r"## (\d+) (.+)", line)
            if m:
                self.scene = f"{int(m.group(1)):02d}"
                self.indent = 1
                self.out += ["", f"label scene_{int(m.group(1))}:", f"    # {m.group(2)}"]
                continue
            m = re.match(r"### (\d+)-([A-Z]) (.+)", line)
            if m:
                self.shown = dict(self.menu["base"])
                self.scene = self.scene[:2] + m.group(2).lower()
                self.indent = 2
                self.emit(f'"{esc(m.group(3))}":')
                self.indent = 3
                continue
            if self.menu is None and len(self.scene) > 2:
                self.scene = self.scene[:2]
            m = re.fullmatch(r"〔(.+)〕", line)
            if m:
                self.directive(m.group(1))
                continue
            m = re.fullmatch(r"【(.+?)】「(.+)」", line)
            if m:
                self.say(m.group(1), m.group(2))
                continue
            self.emit(f'"{esc(line)}"')
        return "\n".join(self.out) + "\n"


if __name__ == "__main__":
    md = Path(sys.argv[1]).read_text(encoding="utf-8")
    c = Conv()
    rpy = c.run(md)
    (GAME / "story.rpy").write_text(rpy, encoding="utf-8")
    (ROOT / "tools" / "lines.json").write_text(json.dumps(c.lines, ensure_ascii=False, indent=1), encoding="utf-8")
    n_voice = rpy.count('voice "')
    chars = sum(len(l["text"]) for l in c.lines)
    print(f"story.rpy を書いた。声のある台詞 {len(c.lines)} 本（声のファイルあり {n_voice} 本）、台詞の字数 {chars}")
