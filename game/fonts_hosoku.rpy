## tools/make_font.py が作る。手で直さない。
## SourceHanSansLite にない字だけを fonts/hosoku.ttf（Noto Sans JP から切り出し）で出す。
init -2 python:
    HOSOKU_CHARS = '罠'
    def hosoku_font(base):
        g = FontGroup()
        for ch in HOSOKU_CHARS:
            g.add("fonts/hosoku.ttf", ord(ch), ord(ch))
        return g.add(base, None, None)
