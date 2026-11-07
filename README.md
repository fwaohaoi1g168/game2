# game2

Ren'Py で作ったノベルゲーム。


## 外付けの目との関係

このゲームは、全盲の守井清吾が作った、ゲームを自分の手で遊ぶための道具「外付けの目」（https://github.com/shingo-morii/sotozuke-no-me ）を確かめるために、チームのもう1人（守井の妻、みお）が作った。Built with Claude: Japan 2026 の作品の一部。

- 2026年11月2日 12:30 のキックオフのあとに作った（下の「作った時期」）
- 外付けの目に合わせた作りはしていない。普通のノベルゲームとして作った。
- 外付けの目の側（何も知らない Claude Code のセッション）は、遊べる形だけを受け取って、画面と音だけで調べた。ゲームのファイルの中は開いていない

## 遊ぶには（Windows）

Release（https://github.com/fwaohaoi1g168/game2/releases/latest ）の `game2-1.0-pc.zip` を落として展開し、`game2-1.0-pc\game2.exe` を起動する。外付けの目の取り込みに使ったのと同じ、2026-11-06 に書き出した版。作りは Ren'Py 8.5.2。

## ライセンス

- コード（`game/` の `.rpy` のうち、スクリプトと仕組みの部分、`tools/` の Python）：MIT ライセンス（`LICENSE`）
- 絵、音楽、声、台本の文、画面の部品の画像（`game/images/`、`game/gui/`、`game/audio/` と、台本の文（台詞と地の文））：再利用できない。このゲームを遊ぶこと、紹介のために画面や音を見せることはよい
- フォント（`game/fonts/hosoku.ttf`、`game/fonts/serif.ttf` の Noto Sans JP・Noto Serif JP と、`game/SourceHanSansLite.ttf`）は SIL Open Font License 1.1（`OFL.txt`）

## 開き方

- Ren'Py 8.5.2 の SDK で開く。ランチャーの「プロジェクトディレクトリ」を、このフォルダの1つ上にすると、一覧に `game2` が出る
- 「プロジェクトを起動する」で遊べる

## フォルダ

- `game/`：ゲームの本体（Ren'Py のスクリプト、画像、音）
- `tools/`：作るときに使った道具（配布物には入らない）
- `OFL.txt`：ゲームに入れたフォント3つの著作権の表示と、SIL Open Font License 1.1 の全文（書き出すと配布物に入る）

## 作った時期

Built with Claude: Japan 2026 の期間中（2026-11-02 12:30 のキックオフのあと）に、新しく作った。キックオフより前に作った台本・絵・音・コードは入っていない。

- 11/4：人物の絵を作りはじめた
- 11/6：物語の流れと台本を書き、Ren'Py に組み込んだ。背景、表情の違い、声、BGM、画面の部品を作って入れた
- 11/7：このリポジトリを作った。それまではこのPCの中だけで作っていたので、GitHub の記録は 11/7 から始まる。それぞれの素材を作った日は、下の「作ったもの、借りたもの」に書いた

物語は、作者（みお）が昔考えた小説のアイデアを土台にした。小説の文章は使っていない。

## 作ったもの、借りたもの

| もの | 作り方 | 作った日 |
| --- | --- | --- |
| 台本（`game/story.rpy`）と、ゲームのスクリプト（`game/*.rpy`） | Claude Code（Anthropic）が、作者の決めた筋と指示をもとに書いた。台本の下書きから `story.rpy` への変換は `tools/md_to_rpy.py` | 11/6 |
| 作るときの道具（`tools/`） | Claude Code が書いた | 11/6 |
| 画面の部品（`game/gui/`） | Claude Code が、プログラム（`tools/make_gui.py`、Python の Pillow）で描いた | 11/6 |
| 人物の絵、背景、一枚絵（`game/images/`） | ChatGPT（OpenAI の画像生成）で作った。表情の違いの一部は、OpenAI の画像生成（Codex に入っているもの）で作った。人物の絵の白い背景を透明にするのは `tools/make_sprites.py` | 11/4〜11/6 |
| 声（`game/audio/voice/`、149本） | Gemini TTS（Google）で作った。作る手順は Claude Code が書いた。音声には SynthID の透かしが入る | 11/6 |
| BGM（`game/audio/bgm/`、5曲） | 作者が Gemini（Google）で作った。全部インスト（歌なし） | 11/6 |
| フォント | Noto Sans JP、Noto Serif JP（Google・Adobe）と、Ren'Py に付いている Source Han Sans の軽量版。どれも SIL Open Font License 1.1（`OFL.txt`） | — |
| ゲームの仕組み | Ren'Py 8.5.2 | — |
