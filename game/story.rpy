# このファイルは tools/md_to_rpy.py が本文の下書きから作る。直接は直さない。

label start:
    jump scene_1


label scene_1:
    # 屋敷で縁談
    scene bg yashiki
    with fade
    $ bgm("yashiki")
    "帝都のはずれ、丘の上に建つ白い洋館。"
    "市電の会社を営む、花小路家のお屋敷である。"
    show chizuru futsu at pos_l
    show father base at pos_r
    with dissolve
    voice "audio/voice/father_01_01.ogg"
    f "千鶴、喜べ。おまえの縁談が決まったぞ"
    show chizuru kangaeru at pos_l
    show father base at pos_r
    with dissolve
    voice "audio/voice/chizuru_01_01.ogg"
    c "……縁談、でございますか"
    voice "audio/voice/father_01_02.ogg"
    f "鷲尾銀行の三男坊だ。市電の線路を延ばすには、銀行と仲良くしておかねばならんからな。わっはっは"
    show chizuru honne at pos_l
    show father base at pos_r
    with dissolve
    voice "audio/voice/chizuru_01_02.ogg"
    c "お父様。わたくし、その方にお会いしたこともございませんわ"
    voice "audio/voice/father_01_03.ogg"
    f "会わずともよい。わしが会った。なかなかの好青年だったぞ"
    show chizuru shitataka at pos_l
    show father base at pos_r
    with dissolve
    voice "audio/voice/chizuru_01_03.ogg"
    c "お父様が恋をなさるわけではございませんでしょう"
    show chizuru shitataka at pos_l
    show father owarai at pos_r
    with dissolve
    voice "audio/voice/father_01_04.ogg"
    f "わっはっは、うまいことを言う"
    "父は笑うだけで、取り合わない。こういうとき、父はいつも商談と同じ顔をしている。"
    show chizuru kangaeru at pos_l
    show father owarai at pos_r
    with dissolve
    "千鶴は胸に抱いた本を、きゅっと握った。"
    "書斎の本は、ほとんど読みつくした。恋物語も、帝都の案内書も、新聞の事件記事を集めた本も。"
    show chizuru honne at pos_l
    show father owarai at pos_r
    with dissolve
    voice "audio/voice/chizuru_01_04.ogg"
    c "わたくし、一度でいいから、自分で選んだ方と恋をしてみたいのです。本の中ではなく、本物の街で"
    show chizuru honne at pos_l
    show father futsu at pos_r
    with dissolve
    voice "audio/voice/father_01_05.ogg"
    f "街だと？　ならん、ならん"
    voice "audio/voice/father_01_06.ogg"
    f "あそこは人が多い。スリも出る。近ごろは人さらいまで出るというではないか"
    voice "audio/voice/father_01_07.ogg"
    f "ひとりで外へなど、とんでもない。……まあ、腕の立つ護衛でもおれば、話は別だがな"
    show chizuru kangaeru at pos_l
    show father futsu at pos_r
    with dissolve
    voice "audio/voice/chizuru_01_05.ogg"
    c "護衛……"
    voice "audio/voice/father_01_08.ogg"
    f "さて、わしは会社へ行く。縁談の席は来週の日曜だ。着物を選んでおきなさい"
    hide father
    with dissolve
    "扉が閉まる。広い部屋に、千鶴ひとりが残された。"
    show chizuru shitataka at pos_l
    with dissolve
    voice "audio/voice/chizuru_01_06.ogg"
    c "……来週の日曜。でしたら、今日はまだ、わたくしの日ですわね"

label scene_2:
    # 屋敷を抜け出す
    $ se("door")
    show chizuru shitataka at pos_l
    with dissolve
    "十時十分、女中頭が二階の廊下を見回る。"
    "十時十五分、庭師が裏庭の水まきを終えて、納屋へ戻る。"
    "そこから十時二十分までの五分間、裏口を見ている者は誰もいない。"
    "毎日、窓から眺めていれば、それくらいは覚えてしまう。"
    voice "audio/voice/chizuru_02_01.ogg"
    c "本に書いてあった通りですわ。計画とは、観察の積み重ねである、と"
    show chizuru hashagu at pos_l
    with dissolve
    "千鶴は裏口の扉をそっと開けて、外の光の中へ飛び出した。"
    voice "audio/voice/chizuru_02_02.ogg"
    c "行ってまいります。……どなたにも、聞こえていないでしょうけれど"

label scene_3:
    # 街でナンパ
    scene bg machi
    with fade
    $ bgm("machi")
    $ se("densha")
    "チンチン、と鐘を鳴らして、路面電車が目の前を走っていく。"
    show chizuru hashagu at pos_l
    with dissolve
    voice "audio/voice/chizuru_03_01.ogg"
    c "動いておりますわ……！　本の挿絵より、ずっと大きい！"
    "洋品店のショーウィンドウ、ミルクホールの看板、新聞を売る少年の声。"
    "どれもこれも、初めて見るものばかりだ。"
    show chizuru futsu at pos_l
    with dissolve
    voice "audio/voice/chizuru_03_02.ogg"
    c "いけない、見とれている場合ではありませんわ。今日の目的は、恋です"
    show chizuru kangaeru at pos_l
    with dissolve
    "千鶴は、恋物語で覚えた心得を思い出す。"
    voice "audio/voice/chizuru_03_03.ogg"
    c "出会いのきっかけは、まず手みやげから。……手みやげ、手みやげ"
    voice "audio/voice/kudamono_03_01.ogg"
    kudamono "お嬢ちゃん、林檎どうだい。今朝とれたての、甘いやつだよ"
    show chizuru hashagu at pos_l
    with dissolve
    voice "audio/voice/chizuru_03_04.ogg"
    c "まあ！　それをくださいまし。ええと……五つ"
    voice "audio/voice/kudamono_03_02.ogg"
    kudamono "い、五つ！？"
    "両腕いっぱいの林檎を抱えて、千鶴は大通りを見わたした。"
    voice "audio/voice/chizuru_03_05.ogg"
    c "さて。どなたに声をかけましょう"
    menu:
        "どなたに声をかける？"
        "本屋の前で本を読んでいる書生さん":
            voice "audio/voice/chizuru_03a_01.ogg"
            c "あの。その本、『月下の航海記』の下巻ではございませんか"
            voice "audio/voice/shosei_03a_01.ogg"
            shosei "えっ。そうですけど……よくご存じですね"
            voice "audio/voice/chizuru_03a_02.ogg"
            c "わたくしも読みましたの。三章の嵐の場面、すばらしいですわよね。船長が帆柱にしがみついて"
            voice "audio/voice/shosei_03a_02.ogg"
            shosei "そうそう！　あそこで船長が泣くんですよね。僕も泣きました"
            voice "audio/voice/chizuru_03a_03.ogg"
            c "わかりますわ！"
            "話は弾んだ。それはもう、驚くほど弾んだ。"
            "気づけば半時間、二人は本の話だけをしていた。"
            voice "audio/voice/shosei_03a_03.ogg"
            shosei "いやあ、楽しかった。こんなに話の合う人は初めてです"
            voice "audio/voice/chizuru_03a_04.ogg"
            c "わたくしもですわ。あの、よろしければ、このあと"
            voice "audio/voice/shosei_03a_04.ogg"
            shosei "あ、下巻の続きを今夜中に読みたいので。じゃあ、また本屋で！"
            "書生は本を抱えて、軽やかに去っていった。"
            "千鶴の手には、渡しそびれた林檎がひとつ残った。"
            show chizuru kangaeru at pos_l
            with dissolve
            voice "audio/voice/chizuru_03a_05.ogg"
            c "……本のお話しか、していませんでしたわね"
        "人だかりのけんかを止めていた車夫さん":
            "人だかりの真ん中で、二人の男が胸ぐらをつかみ合っていた。"
            "そこへ、たくましい車夫がひとり、ずいと割って入る。"
            voice "audio/voice/shafu_03b_01.ogg"
            shafu "よしな、よしな。昼間っから、みっともねえ"
            "車夫が二人の腕をひょいとつかむと、けんかはあっけなく終わった。"
            voice "audio/voice/chizuru_03b_01.ogg"
            c "なんて頼もしい方……！"
            voice "audio/voice/chizuru_03b_02.ogg"
            c "あの！　お見事でしたわ。これ、お礼のしるしに"
            voice "audio/voice/shafu_03b_02.ogg"
            shafu "お礼？　俺は何もしてねえよ。それより、そんなに林檎を抱えてたら重いだろ。気をつけて帰んな"
            voice "audio/voice/chizuru_03b_03.ogg"
            c "あの、お名前を"
            voice "audio/voice/shafu_03b_03.ogg"
            shafu "名乗るほどのもんじゃねえ。おっと、お客だ。毎度！"
            "車夫は人力車を引いて、あっという間に通りの向こうへ消えた。"
            "林檎は、ひとつも減っていない。"
            show chizuru kangaeru at pos_l
            with dissolve
            voice "audio/voice/chizuru_03b_04.ogg"
            c "……受け取ってすら、いただけませんでしたわ"
        "道ばたの似顔絵描きさん":
            voice "audio/voice/nigaoe_03c_01.ogg"
            nigaoe "似顔絵、一枚十銭。お嬢さん、描いていくかい"
            voice "audio/voice/chizuru_03c_01.ogg"
            c "まあ、お願いいたしますわ。……それで、描いていただくあいだに、少しお話を"
            voice "audio/voice/nigaoe_03c_02.ogg"
            nigaoe "はいはい。じっとしててね"
            "絵描きは、さらさらと筆を走らせる。"
            "ときどき千鶴の顔と、着物と、白い手袋をじっと見た。"
            voice "audio/voice/nigaoe_03c_03.ogg"
            nigaoe "はい、できあがり"
            "紙の上では、千鶴が澄ました顔で座っていた。"
            "その背景に、なぜか大きな洋館が描いてある。"
            voice "audio/voice/chizuru_03c_02.ogg"
            c "あの、うしろのお屋敷は"
            voice "audio/voice/nigaoe_03c_04.ogg"
            nigaoe "お嬢さん、いいとこの子でしょ。手袋も、しゃべり方も、隠せてないよ"
            voice "audio/voice/nigaoe_03c_05.ogg"
            nigaoe "悪いこと言わないから、早くおうちに帰りな。このへん、近ごろ人さらいが出るって噂だからさ"
            voice "audio/voice/chizuru_03c_03.ogg"
            c "わ、わたくしはただ、お話を……"
            voice "audio/voice/nigaoe_03c_06.ogg"
            nigaoe "はい、十銭ね。毎度あり"
            show chizuru kangaeru at pos_l
            with dissolve
            "似顔絵だけが、千鶴の手元に残った。"
            voice "audio/voice/chizuru_03c_04.ogg"
            c "……子ども扱い、されてしまいましたわ"
    "そのあとも、千鶴は何人にも声をかけた。"
    "帽子屋の店員には、帽子をすすめられた。巡査には、迷子だと思われた。お茶屋の若旦那には、お茶を一杯ごちそうになって、それきりだった。"
    show chizuru kangaeru at pos_l
    with dissolve
    "気がつけば、日が傾いていた。"
    voice "audio/voice/chizuru_03_06.ogg"
    c "みなさん、親切でしたわ。でも……"
    voice "audio/voice/chizuru_03_07.ogg"
    c "どなたも、わたくしの手を取ってはくださいませんでしたわね"
    "腕の中の林檎は、ひとつも減っていなかった。"

label scene_4:
    # 人さらいが声をかけてくる
    scene bg yugure
    with fade
    stop music fadeout 2.0
    "人通りの少ない、川沿いの道。"
    "そろそろ帰ろうか、と千鶴が思いはじめたときだった。"
    voice "audio/voice/tetsuji_04_01.ogg"
    otoko "――お嬢さん"
    show chizuru futsu at pos_l
    show tetsuji sugomu at pos_r
    with dissolve
    "振り返ると、つば広の帽子に黒いマントの男が立っていた。"
    "細い体に、すり減った靴。帽子の影で、目つきだけがやけに鋭い。"
    voice "audio/voice/tetsuji_04_02.ogg"
    otoko "道に迷ったんだろう。じきに日も暮れる。お屋敷まで、送ってやろうか"
    "千鶴は、ぱちりとまばたきをした。"
    show chizuru hashagu at pos_l
    show tetsuji sugomu at pos_r
    with dissolve
    voice "audio/voice/chizuru_04_01.ogg"
    c "……声を、かけていただけましたわ"
    voice "audio/voice/tetsuji_04_03.ogg"
    otoko "は？"
    voice "audio/voice/chizuru_04_02.ogg"
    c "今日はいちにち、わたくしから声をかけてばかりでしたの。殿方のほうから声をかけていただいたのは、はじめてです！"
    show chizuru hashagu at pos_l
    show tetsuji komaru at pos_r
    with dissolve
    voice "audio/voice/tetsuji_04_04.ogg"
    otoko "お、おう。そりゃあ、よかったな"
    "男は少したじろいだ。どうやら、思っていた返事と違ったらしい。"
    show chizuru futsu at pos_l
    show tetsuji komaru at pos_r
    with dissolve
    voice "audio/voice/chizuru_04_03.ogg"
    c "でも、ひとつだけ。どうして、わたくしがお屋敷に住んでいると、おわかりになったのですか"
    voice "audio/voice/tetsuji_04_05.ogg"
    otoko "そ、そりゃあ、その、見りゃわかる。手袋とか"
    voice "audio/voice/chizuru_04_04.ogg"
    c "まあ。手袋ひとつで、わかってしまうものですのね"
    voice "audio/voice/tetsuji_04_06.ogg"
    otoko "と、とにかく行こうぜ。こっちだ"
    voice "audio/voice/chizuru_04_05.ogg"
    c "お待ちになって。お手を、拝借できます？"
    voice "audio/voice/tetsuji_04_07.ogg"
    otoko "手？"
    "男が思わず両手を出すと、千鶴はそこへ林檎を五つ、どさりとのせた。"
    show chizuru futsu at pos_l
    show tetsuji komaru at pos_r
    with dissolve
    voice "audio/voice/tetsuji_04_08.ogg"
    otoko "おわっ、重っ……！"
    voice "audio/voice/chizuru_04_06.ogg"
    c "ありがとうございます。ずっと抱えていて、腕がしびれておりましたの"
    "男の両手は、林檎でふさがった。"

label scene_5:
    # 見抜く
    voice "audio/voice/chizuru_05_01.ogg"
    c "あら？"
    "林檎をのせた、男の指先。"
    "爪のあいだが、うっすらと紫色に染まっている。"
    "千鶴の頭の中で、書斎の本棚がぱらぱらとめくれた。新聞の事件記事を集めた本、『帝都犯罪実録』。"
    "紫のしみが、なかなか落ちない薬。かがせると、人がぐっすり眠ってしまう薬。"
    "そして、いちばんよくある手口。親切な道案内のふりをして、ひと気のない道へ連れていく。"
    show chizuru shitataka at pos_l
    show tetsuji komaru at pos_r
    with dissolve
    "千鶴は、にっこりと笑ったままだった。"
    "けれど頭の中では、もう答えが出ていた。"
    voice "audio/voice/chizuru_05_02.ogg"
    c "あなた、人さらいですわね"
    voice "audio/voice/tetsuji_05_01.ogg"
    otoko "……な、なにを言って"
    voice "audio/voice/chizuru_05_03.ogg"
    c "爪の紫のしみ。あれは眠り薬の色ですわ。それに、親切な道案内のふりをして、ひと気のない道へ連れていく。本に載っていた手口と、そっくりそのままです"
    show chizuru shitataka at pos_l
    show tetsuji sugomu at pos_r
    with dissolve
    voice "audio/voice/tetsuji_05_02.ogg"
    otoko "……だったら、どうする。ここで大声でも出すか"
    voice "audio/voice/chizuru_05_04.ogg"
    c "いいえ。出しませんわ"
    voice "audio/voice/tetsuji_05_03.ogg"
    otoko "……は？"
    voice "audio/voice/chizuru_05_05.ogg"
    c "だってあなた、さっきから手が震えていらっしゃいますもの"
    show chizuru shitataka at pos_l
    show tetsuji komaru at pos_r
    with dissolve
    "男の手の上で、林檎がかたかたと鳴っていた。"
    voice "audio/voice/chizuru_05_06.ogg"
    c "靴も、ずいぶんすり減っていますわね。きっと、うまくいかずに逃げてばかり。……本当は、このお仕事、向いていらっしゃらないのでは？"
    voice "audio/voice/tetsuji_05_04.ogg"
    otoko "う、うるせえ！　余計なお世話だ！"
    "図星だったらしい。"
    voice "audio/voice/chizuru_05_07.ogg"
    c "お名前は？"
    voice "audio/voice/tetsuji_05_05.ogg"
    otoko "なんで人さらいが名乗るんだよ"
    voice "audio/voice/chizuru_05_08.ogg"
    c "お名前は？"
    voice "audio/voice/tetsuji_05_06.ogg"
    otoko "……熊谷。熊谷鉄次"
    voice "audio/voice/chizuru_05_09.ogg"
    c "鉄次さん。わたくしは、千鶴と申します"

label scene_6:
    # 交渉して雇う
    $ bgm("kosho")
    voice "audio/voice/chizuru_06_01.ogg"
    c "鉄次さん。ご提案がございますの"
    voice "audio/voice/tetsuji_06_01.ogg"
    t "……提案？"
    voice "audio/voice/chizuru_06_02.ogg"
    c "わたくしを、お屋敷まで送ってくださいまし。護衛として、あなたを雇います"
    voice "audio/voice/tetsuji_06_02.ogg"
    t "はあ！？　俺は、あんたをさらおうとしてた人間だぞ"
    voice "audio/voice/chizuru_06_03.ogg"
    c "ええ。ですから、お願いしているのです"
    voice "audio/voice/chizuru_06_04.ogg"
    c "人をさらう方なら、人をさらう方の手口も、裏道も、よくご存じでしょう？　護衛にこれほど向いた方はおりませんわ"
    show chizuru shitataka at pos_l
    show tetsuji sugomu at pos_r
    with dissolve
    voice "audio/voice/tetsuji_06_03.ogg"
    t "……罠だろ。屋敷に着いたとたん、巡査がずらっと並んでるんだろ"
    voice "audio/voice/chizuru_06_05.ogg"
    c "まあ、疑り深い。では、条件をお出しします"
    menu:
        "鉄次さんに差し出すのは？"
        "お金（今日のお小遣いを全部）":
            voice "audio/voice/chizuru_06a_01.ogg"
            c "お給金をお支払いします。こちらを"
            show chizuru shitataka at pos_l
            show tetsuji komaru at pos_r
            with dissolve
            "千鶴が巾着を逆さにすると、銀貨と銅貨が、鉄次の抱えた林檎の上にじゃらじゃらと降ってきた。"
            voice "audio/voice/tetsuji_06a_01.ogg"
            t "ちょ、おい、林檎の上に……いくらあるんだ、これ"
            voice "audio/voice/chizuru_06a_02.ogg"
            c "今日のお小遣いの残りですわ。林檎を五つ買いましたので、少し減ってしまいましたけれど"
            voice "audio/voice/tetsuji_06a_02.ogg"
            t "……俺のひと月分より多いじゃねえか"
            voice "audio/voice/chizuru_06a_03.ogg"
            c "では、ひと月分のお給金を、前払いということで"
            voice "audio/voice/tetsuji_06a_03.ogg"
            t "ひと月も雇う気かよ！？"
        "お仕事（まっとうな働き口）":
            voice "audio/voice/chizuru_06b_01.ogg"
            c "お仕事を、ご紹介いたします"
            show chizuru shitataka at pos_l
            show tetsuji komaru at pos_r
            with dissolve
            voice "audio/voice/tetsuji_06b_01.ogg"
            t "仕事？"
            voice "audio/voice/chizuru_06b_02.ogg"
            c "人さらいより、ずっとまっとうなお仕事を。わたくしの家なら、働き口はいくらでもございますわ"
            voice "audio/voice/tetsuji_06b_02.ogg"
            t "……あんたの家って、いったい何なんだよ"
            voice "audio/voice/chizuru_06b_03.ogg"
            c "それは、着いてのお楽しみです"
            voice "audio/voice/tetsuji_06b_03.ogg"
            t "楽しみにできる気がしねえ……"
        "秘密（人さらいのことは誰にも言わない）":
            voice "audio/voice/chizuru_06c_01.ogg"
            c "今日のことは、どなたにも申しません"
            show chizuru shitataka at pos_l
            show tetsuji komaru at pos_r
            with dissolve
            voice "audio/voice/tetsuji_06c_01.ogg"
            t "……誰にも？"
            voice "audio/voice/chizuru_06c_02.ogg"
            c "ええ。巡査さんにも、新聞屋さんにも。わたくしを無事に送り届けてくだされば、今日のあなたは人さらいではなく、ただの親切な護衛です"
            voice "audio/voice/tetsuji_06c_02.ogg"
            t "……それ、断ったらどうなる"
            voice "audio/voice/chizuru_06c_03.ogg"
            c "あら。大きな声の出し方なら、本で読みましたわ"
            voice "audio/voice/tetsuji_06c_03.ogg"
            t "脅しじゃねえか！"
    show chizuru shitataka at pos_l
    show tetsuji komaru at pos_r
    with dissolve
    voice "audio/voice/tetsuji_06_04.ogg"
    t "……なあ。なんでそこまでして、俺なんだ"
    voice "audio/voice/tetsuji_06_05.ogg"
    t "あんたなら、もっとまともな護衛がいくらでも雇えるだろ。なんで、よりによって人さらいを"
    show chizuru honne at pos_l
    show tetsuji komaru at pos_r
    with dissolve
    $ bgm("honne")
    "千鶴は少しだけ黙った。"
    "それから、お嬢様の笑顔を、そっとしまった。"
    voice "audio/voice/chizuru_06_06.ogg"
    c "わたくし、今日、たくさんの方に声をかけましたの"
    voice "audio/voice/chizuru_06_07.ogg"
    c "みなさん、いい方でした。お話をしてくださって、心配もしてくださいました。でも、それだけでした"
    voice "audio/voice/chizuru_06_08.ogg"
    c "わたくしの手を取って、どこかへ行こうとしてくださった方は、ひとりもいなかった"
    voice "audio/voice/chizuru_06_09.ogg"
    c "あなたが、はじめてです。あなたのほうから、わたくしに声をかけてくださった"
    voice "audio/voice/tetsuji_06_06.ogg"
    t "……さらうためにな"
    voice "audio/voice/chizuru_06_10.ogg"
    c "ええ。理由のほうは、まったくいただけませんけれど"
    voice "audio/voice/chizuru_06_11.ogg"
    c "それでも、うれしかったのです。ですから、あなたを手放すつもりはございません"
    show chizuru shitataka at pos_l
    show tetsuji komaru at pos_r
    with dissolve
    voice "audio/voice/chizuru_06_12.ogg"
    c "今度は、わたくしがあなたを連れて帰ります"
    "鉄次は、しばらく口をぱくぱくさせていた。"
    "それから林檎をひとつ手に取って、がぶりとかじった。"
    $ bgm("kosho")
    voice "audio/voice/tetsuji_06_07.ogg"
    t "……わかったよ。送るだけだ。屋敷の前まで送ったら、俺は消えるからな"
    voice "audio/voice/chizuru_06_13.ogg"
    c "ええ、それで結構ですわ。……ひとまずは"
    voice "audio/voice/tetsuji_06_08.ogg"
    t "今、ひとまずって言ったか？"
    "夕暮れの川沿いを、二人は並んで歩きはじめた。"
    voice "audio/voice/tetsuji_06_09.ogg"
    t "で、屋敷ってのはどこだ。名字くらい教えろ"
    voice "audio/voice/chizuru_06_14.ogg"
    c "花小路と申します"
    voice "audio/voice/tetsuji_06_10.ogg"
    t "……はなこうじ？"
    voice "audio/voice/tetsuji_06_11.ogg"
    t "花小路って、あの、市電の会社の、花小路か……？"
    voice "audio/voice/chizuru_06_15.ogg"
    c "父の会社ですわ。この道の線路も、父が引きましたの"
    show chizuru shitataka at pos_l
    show tetsuji kuzure at pos_r
    with dissolve
    "鉄次の手から、林檎がひとつ転げ落ちた。"
    voice "audio/voice/tetsuji_06_12.ogg"
    t "帝都でいちばんの金持ちの娘じゃねえか……そんなのに手ぇ出そうとしてたのか、俺……"
    voice "audio/voice/chizuru_06_16.ogg"
    c "ええ。ですから今日のあなたは、運がよかったのですわ。わたくしに見抜かれて"
    show chizuru shitataka at pos_l
    show tetsuji komaru at pos_r
    with dissolve
    voice "audio/voice/tetsuji_06_13.ogg"
    t "どういう理屈だよ……"

label scene_7:
    # 屋敷に着く
    scene bg yashiki_soto
    with fade
    $ bgm("ochi")
    $ se("door")
    "丘の上の白い洋館。"
    "その門をくぐったとたん、うしろで重い鉄の門が、がしゃんと閉まった。"
    show chizuru shitataka at pos_l
    show tetsuji komaru at pos_r
    with dissolve
    voice "audio/voice/tetsuji_07_01.ogg"
    t "……おい。門、閉まったぞ"
    voice "audio/voice/chizuru_07_01.ogg"
    c "ええ。閉まりましたわね"
    "玄関の前には、使用人たちがずらりと並んでいた。"
    "その真ん中に、口ひげの紳士が立っている。"
    show chizuru shitataka at pos_l
    show tetsuji komaru at pos_r
    show father base at pos_c
    with dissolve
    voice "audio/voice/father_07_01.ogg"
    f "千鶴！　どこへ行っておった。屋敷じゅう大騒ぎだったのだぞ"
    voice "audio/voice/chizuru_07_02.ogg"
    c "ごめんなさい、お父様。街へ出ておりました"
    voice "audio/voice/father_07_02.ogg"
    f "ひとりで外へなど、とんでもないと言っただろう！"
    voice "audio/voice/chizuru_07_03.ogg"
    c "ええ。ですから、ひとりではございませんわ"
    "千鶴は、鉄次の腕に、するりと手をかけた。"
    voice "audio/voice/chizuru_07_04.ogg"
    c "護衛を連れてまいりました。お父様、おっしゃいましたわよね。腕の立つ護衛がいれば、話は別だと"
    voice "audio/voice/father_07_03.ogg"
    f "……む"
    "父は鉄次を、帽子のてっぺんから、すり減った靴の先まで、じろりと眺めた。"
    "商談の相手を値踏みするときの目だった。"
    voice "audio/voice/father_07_04.ogg"
    f "おまえ、名は"
    voice "audio/voice/tetsuji_07_02.ogg"
    t "く、熊谷鉄次……です"
    voice "audio/voice/father_07_05.ogg"
    f "ふむ。いい目をしておる。まるで、人をさらう者の目だ"
    show chizuru shitataka at pos_l
    show tetsuji kuzure at pos_r
    show father base at pos_c
    with dissolve
    voice "audio/voice/tetsuji_07_03.ogg"
    t "ひっ"
    show chizuru shitataka at pos_l
    show tetsuji kuzure at pos_r
    show father owarai at pos_c
    with dissolve
    voice "audio/voice/father_07_06.ogg"
    f "……わっはっは、冗談だ！　護衛はそのくらい鋭い目でないと務まらん"
    voice "audio/voice/father_07_07.ogg"
    f "気に入った。熊谷とやら、今日からおまえは千鶴の護衛だ。給金ははずむぞ。住みこみでな"
    voice "audio/voice/tetsuji_07_04.ogg"
    t "す、住みこみ！？　いや、俺は送るだけで……"
    voice "audio/voice/father_07_08.ogg"
    f "遠慮するな。部屋はいくらでもある。おい、熊谷くんの荷物を運んでやれ"
    "使用人たちが、さっと鉄次を取り囲んだ。"
    "帽子とマントが、あっという間に預かられていく。"
    voice "audio/voice/tetsuji_07_05.ogg"
    t "ちょっ、待っ……俺の帽子……！"
    scene cg ochi
    with fade
    "夕日の差しこむ玄関で、使用人に囲まれて固まる人さらい。"
    "その横で、お嬢様がにっこりと笑っていた。"
    "その日、帝都で一件の人さらいがあった。"
    "さらわれたのは、人さらいのほうだった。"
    scene bg yashiki_soto
    with fade
    show chizuru shitataka at pos_l
    show tetsuji komaru at pos_r
    show father base at pos_c
    with dissolve
    voice "audio/voice/chizuru_07_05.ogg"
    c "お父様。来週の縁談には、護衛と一緒に参りますわ。お相手がどんな方か、わたくし、自分の目で確かめてまいります"
    voice "audio/voice/father_07_09.ogg"
    f "む……まあ、会ってみるのはよいことだ"
    voice "audio/voice/chizuru_07_06.ogg"
    c "それから、恋のほうも。これから、ゆっくり探しますわ"
    show chizuru hashagu at pos_l
    show tetsuji komaru at pos_r
    show father base at pos_c
    with dissolve
    "千鶴は、鉄次のほうを向いた。"
    voice "audio/voice/chizuru_07_07.ogg"
    c "明日も、お付き合いくださいましね。鉄次さん"
    voice "audio/voice/tetsuji_07_06.ogg"
    t "……へい。お嬢"
    $ renpy.pause(1.0)
    return
