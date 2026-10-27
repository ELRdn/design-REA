# -*- coding: utf-8 -*-
"""Build textbooks.html: a critical, researched shelf of design manuals."""
from pathlib import Path

from build_read import head, rail, footer

BASE = Path(__file__).resolve().parent

BOOKS = [
    {
        "id": "book-nondesigner",
        "no": "01",
        "shelf": "ノンデザイナーズ",
        "short": "ノンデザイナーズ・デザインブック［第4版］",
        "title": "ノンデザイナーズ・デザインブック［第4版］",
        "cover_title": "ノンデザイナーズ・<br>デザインブック",
        "author": "Robin Williams / ロビン・ウィリアムズ",
        "year": "2016",
        "publisher": "マイナビ出版",
        "format": "B5判 / 260ページ",
        "isbn": "978-4-8399-5555-7",
        "genre": "視覚文法",
        "level": "入門",
        "role": "視覚文法",
        "strength": "4原則とBefore/After",
        "caution_short": "原則は万能ではない",
        "thesis": "非デザイナーのための、4原則の定番書。近接・整列・反復・コントラストを、具体例で体に入れる。",
        "learn": [
            "近接：関連する要素を近づけ、グループを作る。",
            "整列：見えない線で要素を揃える。",
            "反復：色・形・書体を繰り返し、一貫性を作る。",
            "コントラスト：違いを強め、優先順位を見せる。",
            "日本語版の追加章で、名刺・フライヤー・Webへの適用を確認する。",
        ],
        "for": "はじめてレイアウトを学ぶ人。資料・チラシ・名刺・Webの見た目を整えたい人。",
        "caution": "4原則は出発点であり、法則ではない。文化・身体・アクセシビリティの文脈は別途学ぶ。日本語版の追加章まで読むこと。",
        "official": "https://book.mynavi.jp/ec/products/detail/id=53645",
        "officialLabel": "マイナビBOOKS",
        "cover_bg": "var(--cover-ink)",
        "cover_fg": "var(--cover-paper)",
        "spine_h": "270px",
    },
    {
        "id": "book-naruhodo",
        "no": "02",
        "shelf": "なるほどデザイン",
        "short": "なるほどデザイン",
        "title": "なるほどデザイン〈目で見て楽しむ新しいデザインの本。〉",
        "cover_title": "なるほど<br>デザイン",
        "author": "筒井美希",
        "year": "2015",
        "publisher": "エムディエヌコーポレーション / インプレス",
        "format": "A5判 / 272ページ",
        "isbn": "978-4-8443-6517-4",
        "genre": "デザイン的思考",
        "level": "入門",
        "role": "思考",
        "strength": "編集・7つの道具",
        "caution_short": "方法論の体系書ではない",
        "thesis": "デザインを「編集」として捉え、7つの道具と豊富なビジュアルで、見方を変える。",
        "learn": [
            "デザインに「正解」はないという前提から始める。",
            "ダイジ度天秤、スポットライト、擬人化力、連想力、翻訳機、虫めがね、愛。",
            "文字と組、言葉と文章、色、写真、グラフを、例えで理解する。",
            "正解を暗記するのではなく、対象の見方を組み替える。",
        ],
        "for": "発想の入口が欲しい人。デザインを「楽しい」と感じたい初学者。言葉とビジュアルの橋を探す人。",
        "caution": "比喩とビジュアルが主役で、体系的な手順書ではない。2015年の作例は古い。レイアウトの実務書と併用する。",
        "official": "https://books.mdn.co.jp/books/3215303004/",
        "officialLabel": "MdN / インプレス",
        "cover_bg": "var(--cover-yellow)",
        "cover_fg": "var(--cover-ink)",
        "spine_h": "245px",
    },
    {
        "id": "book-nyumon",
        "no": "03",
        "shelf": "デザイン入門教室",
        "short": "デザイン入門教室［特別講義］",
        "title": "デザイン入門教室［特別講義］ 確かな力を身に付けられる ～学び、考え、作る授業～",
        "cover_title": "デザイン<br>入門教室",
        "author": "坂本伸二",
        "year": "2015",
        "publisher": "SBクリエイティブ",
        "format": "B5判 / 207ページ",
        "isbn": "978-4-7973-5142-2",
        "genre": "総合入門",
        "level": "入門",
        "role": "総合",
        "strength": "8章＋実践演習",
        "caution_short": "2015年版、最新版を確認",
        "thesis": "レイアウト、写真、配色、文字、文章、図解、演習まで。教室のように、基礎を順番に積む。",
        "learn": [
            "デザインを始める前の目的設定と情報整理。",
            "レイアウトの基本：グループ化、対比、反復、重心、余白、黄金比。",
            "写真・画像、配色、文字と書体、文章のデザイン。",
            "インフォグラフィックと、最後の実践演習。",
        ],
        "for": "独学の最初の一冊が欲しい人。紙面・資料・プレゼンを作る人。デザイナー1年目。",
        "caution": "2015年の初版。ソフトの画面や作例は古い。増補改訂版（ISBN 978-4-8156-2430-9）も刊行されているので、購入前に最新版を確認する。",
        "official": "https://www.sbcr.jp/product/4797351422/",
        "officialLabel": "SBクリエイティブ",
        "cover_bg": "var(--cover-ultra)",
        "cover_fg": "var(--cover-paper)",
        "spine_h": "260px",
    },
    {
        "id": "book-tsutawaru",
        "no": "04",
        "shelf": "伝わるデザイン",
        "short": "伝わるデザインの基本 増補改訂版",
        "title": "伝わるデザインの基本 増補改訂版 よい資料を作るためのレイアウトのルール",
        "cover_title": "伝わる<br>デザイン",
        "author": "高橋佑磨 / 片山なつ",
        "year": "2016 / 2021",
        "publisher": "技術評論社",
        "format": "B5変形 / 240ページ（2016） / 256ページ（3版）",
        "isbn": "978-4-7741-8321-3 / 978-4-297-11985-0",
        "genre": "資料デザイン",
        "level": "入門〜実務",
        "role": "資料",
        "strength": "文字・図表・UD",
        "caution_short": "表現より伝達",
        "thesis": "スライド、チラシ、企画書。WordやPowerPointでも「伝わる資料」を作るための、体系的なルール。",
        "learn": [
            "書体と文字、文章と箇条書きの法則。",
            "図・グラフ・表の法則。",
            "レイアウトの5法則：余白、揃える、グループ化、強弱、繰り返し。",
            "配色と、色覚多様性・弱視・読み書き障害への配慮。",
            "Word / PowerPoint での実装手順。",
        ],
        "for": "学生、研究者、教員、社会人。スライド・ポスター・企画書・レポートをよく作る人。",
        "caution": "「伝わる」ための実務書で、表現の実験やアートの本ではない。2016年版より、2021年の増補改訂3版（ISBN 978-4-297-11985-0）を推奨。",
        "official": "https://gihyo.jp/book/2021/978-4-297-11985-0",
        "officialLabel": "技術評論社（3版）",
        "cover_bg": "var(--cover-paper-3)",
        "cover_fg": "var(--cover-ink)",
        "spine_h": "250px",
    },
    {
        "id": "book-zukai",
        "no": "05",
        "shelf": "図解の基本",
        "short": "ノンデザイナーでも役立つ図解の基本",
        "title": "ノンデザイナーでも役立つ図解の基本",
        "cover_title": "図解の<br>基本",
        "author": "鷹野雅弘 / 荒砂智之",
        "year": "2023",
        "publisher": "マイナビ出版",
        "format": "PDF電子小冊子 / 5章",
        "isbn": "—（電子版）",
        "genre": "図解",
        "level": "入門〜実務",
        "role": "図解",
        "strength": "図・グラフ・表",
        "caution_short": "PDF小冊子",
        "thesis": "「図解の4原則」を、図・グラフ・チャート・地図・アイコン・レイアウトに落とす小冊子。",
        "learn": [
            "図解とは何か、図解制作の基本。",
            "図解の「型」とスタイリング。",
            "わかりやすく美しい図のための20のテクニック。",
            "図解と4つの基本原則（近接・整列・反復・コントラスト）の接続。",
        ],
        "for": "文章や数字を図で説明する人。プレゼン・レポート・提案書で図解を使う人。",
        "caution": "PDFの電子小冊子（2023年、1,320円）。単体の紙書籍ではない。『ノンデザイナーズ・デザインブック』とのセットも販売されている。",
        "official": "https://book.mynavi.jp/ec/products/detail/id=141554",
        "officialLabel": "マイナビBOOKS",
        "cover_bg": "var(--cover-cyan)",
        "cover_fg": "var(--cover-paper)",
        "spine_h": "220px",
    },
    {
        "id": "book-taizen",
        "no": "06",
        "shelf": "デザイン大全",
        "short": "イメージをパッと形に変えるデザイン大全",
        "title": "イメージをパッと形に変えるデザイン大全",
        "cover_title": "デザイン<br>大全",
        "author": "尾沢早飛",
        "year": "2021",
        "publisher": "SBクリエイティブ",
        "format": "A5判 / 288ページ",
        "isbn": "978-4-8156-0316-8",
        "genre": "ビジュアルリファレンス",
        "level": "実務",
        "role": "参照",
        "strength": "12イメージ / 200作例",
        "caution_short": "作例集、模倣に注意",
        "thesis": "「きれい」「かわいい」「信頼感」…。言葉のイメージから、具体的なビジュアルを引くための大全。",
        "learn": [
            "12のイメージワードと39のテーマ。",
            "200点を超える作例を、配色・写真・レイアウト・装飾・文字に分解して見る。",
            "クライアントとのイメージ共有、ムードボード作り。",
            "「言葉 → ビジュアル」の引き出しを増やす。",
        ],
        "for": "デザイナー、発注者、ディレクター。イメージを言葉にしづらい人。作例から出発したい人。",
        "caution": "作例集であり、方法論の教科書ではない。そのまま模倣すると過去の流行に固定される。原則に戻って分解し、文脈に合わせて作り直す。",
        "official": "https://www.sbcr.jp/product/4815603168/",
        "officialLabel": "SBクリエイティブ",
        "cover_bg": "var(--cover-signal)",
        "cover_fg": "var(--cover-ink)",
        "spine_h": "255px",
    },
    {
        "id": "book-optin",
        "no": "07",
        "shelf": "オプトインLP",
        "short": "ノンデザイナーのためのオプトインLP制作術！",
        "title": "ノンデザイナーのためのオプトインLP（ランディングページ）制作術！ 集客できるホームページの作り方",
        "cover_title": "オプトイン<br>LP",
        "author": "城智英",
        "year": "2024",
        "publisher": "自主出版（Amazon Kindle）",
        "format": "Kindle / ペーパーバック",
        "isbn": "979-8-3246-9148-6",
        "genre": "LP制作",
        "level": "実務",
        "role": "LP",
        "strength": "企画・制作・改善",
        "caution_short": "自己出版、マーケ特化",
        "thesis": "リスト獲得のためのオプトインLPを、企画・制作・改善の3ステップで組む実践書。",
        "learn": [
            "オプトインLPの目的とファネルの考え方。",
            "企画・制作・改善の3ステップ。",
            "ヘッドコピー、CTA、モックアップ、3色以内のデザイン。",
            "ABテスト、計測、ツール（UTAGEなど）の使い方。",
        ],
        "for": "自分でLPを作る小規模事業者、マーケター、非デザイナー。リスト獲得の仕組みを作りたい人。",
        "caution": "Kindle/自己出版のマーケティング実践書。ツール、広告、法規（景表法・個人情報保護）は執筆時点の情報であり、必ず最新を確認する。一般のデザイン教科書ではない。",
        "official": "https://www.amazon.co.jp/dp/B0D3VCN4K8",
        "officialLabel": "Amazon Kindle",
        "cover_bg": "var(--cover-green)",
        "cover_fg": "var(--cover-paper)",
        "spine_h": "235px",
    },
]

SITE = {
    "id": "site-desaken",
    "short": "デザイン研究所（デザ研）",
    "title": "デザイン研究所（デザ研）",
    "author": "運営: デザイン研究所",
    "year": "2020–",
    "publisher": "desaken.com",
    "format": "Webメディア / 記事・動画・SNS",
    "isbn": "—",
    "genre": "実践リファレンス",
    "level": "初〜中級",
    "role": "リファレンス",
    "strength": "検索・カテゴリ・実例",
    "caution_short": "記事単位、商用/提携",
    "thesis": "「読んでデザインを学ぶ参考ブログ」。レイアウト、色、文字、図形、背景、Web、資料を、実例と手順で検索できる。",
    "learn": [
        "レイアウト、図形、文字、背景、色のカテゴリ。",
        "近接・整列・反復・コントラストのタグ。",
        "チラシ、名刺、バナー、ポスター、Web、プレゼン資料の実例。",
        "まとめ記事、検索ページ、YouTube、書籍『デザインのミカタ』。",
    ],
    "for": "「今、このパーツをどう作るか」を調べたい人。初心者〜中級者の副読本。",
    "caution": "記事単位の実践リファレンスで、体系的なカリキュラムではない。広告・提携・商用コンテンツを含むため、情報の鮮度と利害を確認する。",
    "official": "https://desaken.com/",
    "officialLabel": "desaken.com",
}

PATHS = [
    {
        "no": "01",
        "title": "視覚文法の背骨",
        "books": ["book-nondesigner", "book-naruhodo", "book-nyumon"],
        "why": "4原則で「見る目」を作り、7つの道具で「考える目」を開き、8章の演習で「作る手」につなぐ。",
    },
    {
        "no": "02",
        "title": "資料と図解を強くする",
        "books": ["book-tsutawaru", "book-zukai", "book-taizen"],
        "why": "文字・図表・レイアウトのルールを押さえ、図解の型を学び、最後にイメージの引き出しを増やす。",
    },
    {
        "no": "03",
        "title": "Web / LPで届ける",
        "books": ["book-nyumon", "book-optin", "site-desaken"],
        "why": "基礎 → ファネルとCTA → 継続的な実例。LPは「作って終わり」ではなく、計測と改善まで含めてデザインする。",
    },
]

SOURCES = [
    ("マイナビBOOKS / ノンデザイナーズ", "https://book.mynavi.jp/ec/products/detail/id=53645"),
    ("マイナビBOOKS / 図解の基本", "https://book.mynavi.jp/ec/products/detail/id=141554"),
    ("MdN / なるほどデザイン", "https://books.mdn.co.jp/books/3215303004/"),
    ("技術評論社 / 伝わるデザイン 2016", "https://gihyo.jp/book/2016/978-4-7741-8321-3"),
    ("技術評論社 / 伝わるデザイン 2021", "https://gihyo.jp/book/2021/978-4-297-11985-0"),
    ("紀伊國屋 / デザイン入門教室", "https://www.kinokuniya.co.jp/f/dsg-01-9784797351422"),
    ("紀伊國屋 / デザイン大全", "https://www.kinokuniya.co.jp/f/dsg-01-9784815603168"),
    ("Amazon / オプトインLP", "https://www.amazon.co.jp/dp/B0D3VCN4K8"),
    ("デザイン研究所 / desaken.com", "https://desaken.com/"),
    ("版元ドットコム / ノンデザイナーズ", "https://www.hanmoto.com/bd/isbn/9784839955557"),
]


def book_card(b: dict) -> str:
    learn = "".join(f"<li>{x}</li>" for x in b["learn"])
    return f'''<article class="book-card" id="{b["id"]}">
  <div class="book-card__cover" style="--cover-bg:{b["cover_bg"]};--cover-fg:{b["cover_fg"]}">
    <div class="book-card__label"><span>SHELF {b["no"]} / {b["role"]}</span><span>{b["year"]}</span></div>
    <div>
      <h3>{b["cover_title"]}</h3>
      <p class="book-card__author">{b["author"]}</p>
      <p class="book-card__imprint">{b["publisher"]} / {b["format"]}</p>
    </div>
  </div>
  <div class="book-card__body">
    <div class="book-card__kicker"><span class="tag">{b["genre"]}</span><span class="tag">{b["level"]}</span></div>
    <p class="book-card__meta">{b["publisher"]} / {b["format"]} / ISBN {b["isbn"]}</p>
    <p class="book-card__thesis">{b["thesis"]}</p>
    <div class="book-card__cols">
      <div><h4>学ぶこと</h4><ul>{learn}</ul></div>
      <div>
        <h4>向き</h4><p>{b["for"]}</p>
        <h4 style="margin-top:0.7rem">注意</h4><p>{b["caution"]}</p>
      </div>
    </div>
    <p class="book-card__link"><a class="textlink" href="{b["official"]}" target="_blank" rel="noopener">{b["officialLabel"]} <span class="textlink__arrow" aria-hidden="true">↗</span></a></p>
  </div>
</article>'''


def main() -> None:
    spines = []
    for b in BOOKS:
        spines.append(
            f'<a class="spine" href="#{b["id"]}" style="--spine-bg:{b["cover_bg"]};--spine-fg:{b["cover_fg"]};--spine-h:{b["spine_h"]}" aria-label="{b["short"]} の書誌とレビューへ">'
            f'<span class="spine__no">{b["no"]}</span>'
            f'<span class="spine__title">{b["shelf"]}</span>'
            f'<span class="spine__author">{b["author"].split(" / ")[0]}</span>'
            f'<span class="spine__year">{b["year"]}</span></a>'
        )

    rows = []
    for b in BOOKS + [SITE]:
        rows.append(
            f'<tr><td><a class="link" href="#{b["id"]}">{b["short"]}</a></td>'
            f'<td>{b["role"]}</td><td>{b["level"]}</td><td>{b["strength"]}</td><td>{b["caution_short"]}</td></tr>'
        )

    cards = "".join(book_card(b) for b in BOOKS)

    paths = []
    by_id = {b["id"]: b for b in BOOKS + [SITE]}
    for p in PATHS:
        links = "".join(
            f'<a href="#{bid}">{by_id[bid]["short"]}</a>' for bid in p["books"]
        )
        paths.append(
            f'''<div class="path">
  <span class="path__num">{p["no"]}</span>
  <h3 class="path__title">{p["title"]}</h3>
  <div class="path__books">{links}</div>
  <p class="path__why">{p["why"]}</p>
</div>'''
        )

    sources = "".join(
        f'''<div class="source">
  <span class="source__label"><a href="{url}" target="_blank" rel="noopener">{label} ↗</a></span>
  <span class="source__url">{url}</span>
</div>'''
        for label, url in SOURCES
    )

    page = f"""{head("教本室 — デザイン全史 / THE MANUALS", "デザインの教科書・参考書7冊と実践ブログを、REAで書誌と役割を確認して整理。歴史と教本のあいだを考える読書案内。")}
<body data-page="manuals">
<a class="skip" href="#main">本文へスキップ</a>
{rail("manuals")}

<main id="main" class="page">
  <div class="shell">
    <header class="manuals-head">
      <p class="eyebrow"><span class="eyebrow__no">SHELF</span> THE MANUALS</p>
      <h1 class="manuals-title">教本は、<br>歴史の隣に。</h1>
      <p class="manuals-lede">歴史は「なぜ」を、教本は「どう」を。7冊の実践書と1つのブログを、役割・レベル・注意点で整理した。読む順番は一つではない。必要な場所から、手を動かせばいい。</p>
      <p class="manuals-meta mono"><span>7 BOOKS + 1 SITE</span><span>2015–2024</span><span>JAPANESE EDITIONS</span><span>CHECK EDITIONS</span></p>
      <p class="manuals-meta mono"><span>REA / PUBLISHER PAGES / DOM + ACCESSIBILITY</span><span>2026.10.27</span></p>
    </header>

    <section class="shelf" aria-label="教本の棚">
      <div class="shelf__row">
        {''.join(spines)}
      </div>
      <div class="shelf__caption mono"><span>TYPOGRAPHIC SPINES / NO COVER ART</span><span>CLICK A SPINE TO READ THE NOTE</span></div>
      <p class="note">表紙画像は使っていません。書名・著者・出版社・年の活字組みで「棚」を作りました。本の内容は、出版社・書店の公式ページと、REAで取得したDOM/アクセシビリティツリーをもとに要約しています。</p>
    </section>

    <section class="manuals-section" id="matrix">
      <div class="manuals-section__head">
        <h2 class="manuals-section__title">7冊を、ひとつの表に。</h2>
        <p class="manuals-section__note mono">MATRIX / ROLE · LEVEL · STRENGTH · CAUTION</p>
      </div>
      <div class="manuals-table-wrap">
        <table class="manuals-table">
          <thead><tr><th scope="col">本</th><th scope="col">役割</th><th scope="col">レベル</th><th scope="col">強み</th><th scope="col">注意</th></tr></thead>
          <tbody>{''.join(rows)}</tbody>
        </table>
      </div>
    </section>

    <section class="manuals-section" id="paths">
      <div class="manuals-section__head">
        <h2 class="manuals-section__title">読む順番は、一つではない。</h2>
        <p class="manuals-section__note mono">3 ROUTES / START WHERE YOU ARE</p>
      </div>
      <div class="paths">{''.join(paths)}</div>
    </section>

    <section class="manuals-section" id="books">
      <div class="manuals-section__head">
        <h2 class="manuals-section__title">7冊のノート</h2>
        <p class="manuals-section__note mono">BOOK NOTES / WHAT TO LEARN · WHO IT IS FOR · WHAT TO WATCH</p>
      </div>
      <div class="book-grid">
        {cards}
        <article class="book-card book-card--site" id="{SITE["id"]}">
          <div class="book-card__cover" style="--cover-bg:var(--cover-paper-3);--cover-fg:var(--cover-ink)">
            <div class="book-card__label"><span>WEB / {SITE["role"]}</span><span>{SITE["year"]}</span></div>
            <div>
              <h3 style="font-family:var(--font-latin);font-size:clamp(1.8rem,3.4vw,3rem);letter-spacing:-0.04em">desaken.com</h3>
              <p class="book-card__author">{SITE["title"]}</p>
              <p class="book-card__imprint">{SITE["format"]}</p>
            </div>
          </div>
          <div class="book-card__body">
            <div class="book-card__kicker"><span class="tag">{SITE["genre"]}</span><span class="tag">{SITE["level"]}</span></div>
            <p class="book-card__meta">{SITE["author"]} / {SITE["format"]}</p>
            <p class="book-card__thesis">{SITE["thesis"]}</p>
            <div class="book-card__cols">
              <div><h4>学ぶこと</h4><ul>{''.join(f"<li>{x}</li>" for x in SITE["learn"])}</ul></div>
              <div>
                <h4>向き</h4><p>{SITE["for"]}</p>
                <h4 style="margin-top:0.7rem">注意</h4><p>{SITE["caution"]}</p>
              </div>
            </div>
            <p class="book-card__link"><a class="textlink" href="{SITE["official"]}" target="_blank" rel="noopener">{SITE["officialLabel"]} <span class="textlink__arrow" aria-hidden="true">↗</span></a></p>
          </div>
        </article>
      </div>
    </section>

    <section class="manuals-section" id="bridge">
      <div class="manuals-section__head">
        <h2 class="manuals-section__title">歴史と教本のあいだ</h2>
        <p class="manuals-section__note mono">HISTORY ASKS WHY / MANUALS ASK HOW</p>
      </div>
      <div class="bridge">
        <div class="bridge__col">
          <span class="bridge__label">HISTORY / デザイン全史</span>
          <h3 class="bridge__title">「なぜ」を問う</h3>
          <ul>
            <li>なぜ、その形が生まれたのか。</li>
            <li>誰の労働と権力の上に成り立っているのか。</li>
            <li>どんな世界観を提案しているのか。</li>
            <li>誰が排除され、何が失われたのか。</li>
            <li>その話は、証拠でどこまで支えられるのか。</li>
          </ul>
        </div>
        <div class="bridge__col">
          <span class="bridge__label">MANUALS / 教本室</span>
          <h3 class="bridge__title">「どう」を問う</h3>
          <ul>
            <li>どう配置すれば、読みやすいか。</li>
            <li>どう見せれば、伝わるか。</li>
            <li>どう作れば、再現できるか。</li>
            <li>どう直せば、もっと良くなるか。</li>
            <li>どう測れば、改善できるか。</li>
          </ul>
        </div>
        <p class="bridge__note">歴史だけでは手が動かず、教本だけでは判断を誤る。両方を使って、はじめて「作る理由」と「作る技術」がつながる。</p>
      </div>
    </section>

    <section class="manuals-section" id="choose">
      <div class="manuals-section__head">
        <h2 class="manuals-section__title">目的別・最小の棚</h2>
        <p class="manuals-section__note mono">CHOOSE BY JOB / NOT BY COMPLETENESS</p>
      </div>
      <div class="choose-grid">
        <div class="choose"><span class="choose__when">IF YOU BUY ONLY ONE</span><p class="choose__books"><a class="link" href="#book-tsutawaru">伝わるデザイン3版</a>（資料） / <a class="link" href="#book-nondesigner">ノンデザイナーズ</a>（視覚文法）</p><p class="choose__note">資料・スライドが主なら「伝わる」。チラシ・名刺・Webの見た目が主なら「ノンデザイナーズ」。</p></div>
        <div class="choose"><span class="choose__when">FOR A CLASS</span><p class="choose__books"><a class="link" href="#book-nondesigner">ノンデザイナーズ</a> → <a class="link" href="#book-naruhodo">なるほど</a> → <a class="link" href="#book-tsutawaru">伝わる</a></p><p class="choose__note">4原則 → 見方 → 資料の実装。3冊で、視覚文法から実務まで一本の線になる。</p></div>
        <div class="choose"><span class="choose__when">FOR PRACTICE</span><p class="choose__books"><a class="link" href="#book-nyumon">デザイン入門教室</a> + <a class="link" href="#book-taizen">デザイン大全</a> + <a class="link" href="#site-desaken">desaken</a></p><p class="choose__note">総合基礎、作例の引き出し、日々の検索。現場の「困った」に強い組み合わせ。</p></div>
        <div class="choose"><span class="choose__when">FOR LP / WEB</span><p class="choose__books"><a class="link" href="#book-optin">オプトインLP</a> + <a class="link" href="#book-tsutawaru">伝わる</a> + <a class="link" href="#site-desaken">desaken</a></p><p class="choose__note">ファネルとCTA、伝わる資料の原則、実例検索。マーケティングとデザインの橋。</p></div>
      </div>
    </section>

    <section class="manuals-section" id="caution">
      <div class="manuals-section__head">
        <h2 class="manuals-section__title">教本を読むときの注意</h2>
        <p class="manuals-section__note mono">LIMITS / RULES ARE NOT LAWS</p>
      </div>
      <div class="limits">
        <p><strong>ルールは法則ではない。</strong> 近接・整列・反復・コントラスト、グリッド、配色の原則は、強いヒューリスティクスだが、文化・身体・アクセシビリティ・用途によって変わります。「原則通りだから良い」ではなく、「誰にとって読みやすいか」をテストしてください。</p>
        <p><strong>版を確認する。</strong> 『伝わるデザインの基本』は2016年の増補改訂版と2021年の増補改訂3版があります。『デザイン入門教室』も増補改訂版（ISBN 978-4-8156-2430-9）が刊行されています。古い版のソフト手順や作例を、最新の環境にそのまま適用しないでください。</p>
        <p><strong>自己出版・メディアの情報は、鮮度と利害を確認する。</strong> オプトインLPはKindleの自己出版で、ツール・広告・法規は変わります。desaken.comは実践ブログで、広告・提携・商用コンテンツを含みます。記事は出発点であり、最終的な判断は一次情報で。</p>
        <p><strong>教本の外側がある。</strong> 歴史、労働、権力、環境、非西洋、倫理は、これらの教本の守備範囲外です。『デザイン全史』の第14章「読書案内」と合わせて、技術と文脈を往復してください。</p>
      </div>
    </section>

    <section class="manuals-section" id="research">
      <div class="manuals-section__head">
        <h2 class="manuals-section__title">REA調査ノート</h2>
        <p class="manuals-section__note mono">METHOD / SOURCES / 2026.10.27</p>
      </div>
      <p style="margin-top:1rem;color:var(--ink-2);line-height:1.95">REAのブラウザ検査をローカルChromeのCDP接続で実行し、出版社ページのDOMとアクセシビリティツリーから、書名・著者・発売日・ISBN・頁数・目次・主張を抽出しました。SBクリエイティブとAmazonはヘッドレスブラウザを遮断したため、紀伊國屋・版元ドットコム・出版社の別ページで補完しています。書誌は2026年10月27日時点。価格・版・在庫は購入前に公式ページで確認してください。</p>
      <div class="source-grid">{sources}</div>
      <p class="note">調査の全記録（書誌表、版の注意、REAの方法、未確認事項）は <a class="link" href="textbooks-research.md">textbooks-research.md</a> にまとめています。</p>
    </section>
  </div>
</main>

{footer("read.html", "THE CATALOGUE", "本文へ戻る。")}
<script src="assets/app.js" defer></script>
</body>
</html>
"""
    (BASE / "textbooks.html").write_text(page, encoding="utf-8")
    print(f"wrote textbooks.html: {len(page):,} chars, books={len(BOOKS)}, site=1")


if __name__ == "__main__":
    main()
