## キャラ・立ち絵・背景・音の設定。物語は story.rpy（tools/md_to_rpy.py が作る）。

## 話す人
define c = Character("千鶴", color="#ffd2de")  # 11/6 名前の札が海老茶になったので明るい色に
define t = Character("鉄次", color="#e2d4ff")
define otoko = Character("男", color="#e2d4ff")
define f = Character("父", color="#f6dc96")
define shosei = Character("書生", color="#f2ead8")
define shafu = Character("車夫", color="#f2ead8")
define nigaoe = Character("似顔絵描き", color="#f2ead8")
define kudamono = Character("果物屋", color="#f2ead8")

## 立ち絵の位置（下をそろえる）
transform pos_l:
    xalign 0.22 yalign 1.0
transform pos_c:
    xalign 0.5 yalign 1.0
transform pos_r:
    xalign 0.78 yalign 1.0

init python:
    def _first(*files):
        for fn in files:
            if renpy.loadable(fn):
                return fn
        return None

    def _placeholder(label, color):
        return Composite((1920, 1080),
                         (0, 0), Solid(color),
                         (60, 40), Text("仮の絵：" + label, size=40, color="#00000088"))

    ## 立ち絵：images/chara/<キャラ>_<表情>.png があればそれを、なければ <キャラ>_base.png を使う
    _EXPRS = {
        "chizuru": ["futsu", "hashagu", "shitataka", "honne", "kangaeru"],
        "tetsuji": ["sugomu", "komaru", "kuzure"],
        "father": ["base", "futsu", "owarai"],
    }
    for _ch, _exs in _EXPRS.items():
        for _ex in _exs:
            _fn = _first("images/chara/%s_%s.png" % (_ch, _ex), "images/chara/%s_base.png" % _ch)
            renpy.image((_ch, _ex), _fn)

    ## 背景と一枚絵：images/bg/<名前>.png（または .jpg）があればそれを、なければ仮の色の絵
    _BGS = {
        ("bg", "yashiki"): ("屋敷の中（洋館の広い部屋）", "#d8ccb4"),
        ("bg", "yashiki_soto"): ("屋敷の外（門と玄関の前）", "#cfc0a0"),
        ("bg", "machi"): ("大正の街", "#c4d0c8"),
        ("bg", "yugure"): ("夕暮れの道", "#e0a888"),
        ("cg", "ochi"): ("一枚絵・オチの場面", "#f0d8a0"),
    }
    for _tag, (_label, _color) in _BGS.items():
        _fn = _first("images/%s/%s.png" % _tag, "images/%s/%s.jpg" % _tag)
        renpy.image(_tag, _fn if _fn else _placeholder(_label, _color))

    ## BGM と効果音：audio/bgm/<名前>.ogg、audio/se/<名前>.ogg があれば鳴らす（なければ何もしない）
    def bgm(name):
        fn = _first("audio/bgm/%s.ogg" % name, "audio/bgm/%s.mp3" % name)
        if fn:
            renpy.music.play(fn, channel="music", loop=True, fadein=1.0, fadeout=1.0, if_changed=True)
        else:
            renpy.music.stop(channel="music", fadeout=1.0)

    def se(name):
        fn = _first("audio/se/%s.ogg" % name, "audio/se/%s.mp3" % name)
        if fn:
            renpy.sound.play(fn, channel="sound")

## タイトル画面の曲：屋敷の曲があれば流す
init python:
    _title = _first("audio/bgm/yashiki.ogg", "audio/bgm/yashiki.mp3")
    if _title:
        config.main_menu_music = _title
