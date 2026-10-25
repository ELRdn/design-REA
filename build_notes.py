# -*- coding: utf-8 -*-
"""Build design-notes.html: the site's own design rationale."""
from pathlib import Path

from build_read import head, rail, footer

BASE = Path(__file__).resolve().parent

GRID_SVG = '''
<svg viewBox="0 0 640 300" role="img" aria-labelledby="grid-t grid-d">
  <title id="grid-t">版面の骨格</title>
  <desc id="grid-d">左のレール、余白、12カラムのグリッド、本文のメジャーを示す図。</desc>
  <rect x="20" y="20" width="600" height="260" fill="var(--paper-2)" stroke="var(--rule-strong)" stroke-width="0.8"/>
  <rect x="20" y="20" width="70" height="260" fill="var(--paper-3)"/>
  <g stroke="var(--ultra)" stroke-width="0.55" opacity="0.22">
    <path d="M90 20 V280 M134 20 V280 M178 20 V280 M222 20 V280 M266 20 V280 M310 20 V280 M354 20 V280 M398 20 V280 M442 20 V280 M486 20 V280 M530 20 V280 M574 20 V280 M618 20 V280"/>
  </g>
  <g stroke="var(--rule-strong)" stroke-width="0.4" opacity="0.4">
    <path d="M90 60 H620 M90 100 H620 M90 140 H620 M90 180 H620 M90 220 H620 M90 260 H620"/>
  </g>
  <rect x="222" y="60" width="352" height="200" fill="none" stroke="var(--signal)" stroke-width="1.2"/>
  <text x="55" y="150" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)" transform="rotate(-90 55 150)">RAIL 76</text>
  <text x="150" y="42" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">GUTTER 64</text>
  <text x="222" y="46" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--signal)">MEASURE 44EM</text>
  <text x="600" y="292" text-anchor="end" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">12 COLUMNS / MAX 1480</text>
</svg>'''

PLATE_SVG = '''
<svg viewBox="0 0 640 300" role="img" aria-labelledby="anat-t anat-d">
  <title id="anat-t">図版の解剖</title>
  <desc id="anat-d">図版の枠、トンボ、グリッド、線、ラベルの位置を示す図。</desc>
  <rect x="80" y="36" width="480" height="228" fill="var(--paper-2)" stroke="var(--rule)" stroke-width="0.8"/>
  <g fill="none" stroke="var(--rule-strong)" stroke-width="0.7">
    <path d="M80 36 H100 M80 36 V56 M540 36 H560 M560 36 V56 M80 264 H100 M80 244 V264 M540 264 H560 M560 244 V264"/>
  </g>
  <g fill="none" stroke="var(--ink)" stroke-width="1.4">
    <circle cx="300" cy="150" r="62"/>
    <rect x="330" y="90" width="96" height="96" transform="rotate(12 378 138)"/>
    <path d="M300 230 L360 100 L420 230 Z"/>
  </g>
  <g stroke="var(--signal)" stroke-width="0.9">
    <path d="M80 36 L120 76 M560 36 L520 76"/>
    <path d="M100 276 H180"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)" letter-spacing="0.05em">
    <text x="86" y="24">REGISTRATION / 20 MM</text>
    <text x="560" y="24" text-anchor="end">STROKE 1.4</text>
    <text x="86" y="290">CAPTION / SEE · ASK · SOURCE</text>
    <text x="560" y="290" text-anchor="end">LABEL 9 PX MONO</text>
  </g>
</svg>'''

DECISIONS = [
    (
        "01", "台紙から始める",
        "クリーム紙＋高コントラストのセリフ＋テラコッタ。歴史本の既定路線で、懐かしく見えるが、主題を「古いもの」に固定してしまう。",
        "冷たい酸性紙の台紙 <code>#E7E8E0</code>、インク <code>#111412</code>、ウルトラマリン <code>#1B2FC7</code>、レジストレーション・オレンジ <code>#F04A22</code>。",
        "デザイン史は、懐かしむ対象ではなく、調べる対象。台紙と校正記号の語彙は、博物館の収蔵庫と印刷所の現場から来ている。",
    ),
    (
        "02", "声を混ぜない",
        "一つの書体で、歴史も現在もデータも語る。読みやすいが、どこまでが事実で、どこからが解釈かが曖昧になる。",
        "歴史は Shippori Mincho B1、現在は Archivo / Zen Kaku Gothic New、データは IBM Plex Mono、本文は Noto Serif JP。表示の三声と、読むための本文を分ける。",
        "声を混ぜると、文章の責任が曖昧になる。書体は、立場の違いである。",
    ),
    (
        "03", "時間は非線形である",
        "50,000年を一本の線で正確に描く。一見、公正だが、実際には古代が潰れ、20世紀だけが膨らむ。",
        "等幅と対数の切り替え。等幅は「時代の厚み」、対数は「実際の時間感覚」。どちらも正確な縮尺ではないと明記する。",
        "一つの縮尺で全部を語ることは不可能。不可能を隠さず、操作させる。",
    ),
    (
        "04", "図版は器具である",
        "ストックフォトと3Dモックアップで、雰囲気を伝える。きれいだが、構造は伝わりにくい。",
        "注釈つきの作図（SVG）。見る・問う・出典の三点を、すべての図版に付ける。",
        "写真は「見た目」を伝えるが、関係を伝えにくい。線とラベルは、対象を読むための器具になる。",
    ),
    (
        "05", "動きは関係の変化にだけ使う",
        "画面いっぱいの動画、カルーセル、自動再生、パララックス。賑やかだが、読む時間を奪う。",
        "静的な版面＋小さな運動（reveal、hover、timeline）。<code>prefers-reduced-motion</code> を尊重する。",
        "読むためのサイトで、動きが主役になると、内容が負ける。動きは、関係の変化だけに使う。",
    ),
    (
        "06", "アクセシビリティは素材である",
        "最後にチェックリストで確認する。結果として、コントラストやキーボード操作が後付けになる。",
        "コントラスト、フォーカス、キーボード、SVGの title/desc、no-JSの全表を、最初から構造に埋め込む。",
        "制約は後付けではなく、素材。制約があるから、形が決まる。",
    ),
]


def main() -> None:
    decisions = []
    for no, title, rejected, adopted, why in DECISIONS:
        decisions.append(
            f'''<div class="decision">
  <span class="decision__no">DECISION {no}</span>
  <h3 class="decision__title">{title}</h3>
  <div class="decision__row"><span class="decision__label">却下</span><span class="decision__value">{rejected}</span></div>
  <div class="decision__row"><span class="decision__label">採用</span><span class="decision__value"><strong>{adopted}</strong></span></div>
  <div class="decision__row"><span class="decision__label">理由</span><span class="decision__value">{why}</span></div>
</div>'''
        )

    page = f"""{head("設計ノート — デザイン全史 / THE SYSTEM", "この教材サイト自身の設計意図。色、書体、時間のものさし、図版、アクセシビリティを第一原理から開示する。")}
<body data-page="design">
<a class="skip" href="#main">本文へスキップ</a>
{rail("design")}

<main id="main" class="page">
  <div class="shell">
    <header class="notes-head">
      <p class="eyebrow"><span class="eyebrow__no">07</span> THE SYSTEM</p>
      <h1 class="notes-title">このサイトも、<br>一つのデザインである。</h1>
      <p class="notes-lede">紙の色、文字の声、時間のものさし、図版の線。すべてに理由がある。ここでは、この教材の設計を、第一原理から開く。デザインは中立ではない。だから、このサイトの選択も、読む前に開示する。</p>
    </header>

    <section class="notes-section" aria-label="設計ブリーフ">
      <div class="notes-section__head">
        <h2 class="notes-section__title">ブリーフ</h2>
        <p class="notes-section__note mono">BRIEF / CONSTRAINTS</p>
      </div>
      <table class="brief-table">
        <tbody>
          <tr><th>目的</th><td>デザイン史の全体像を、初学者にも専門家にも届く形で、webで読める教材にする。読む・見る・疑うを、一つの場所でつなぐ。</td></tr>
          <tr><th>読者</th><td>15歳から専門家まで。「サルでも赤ちゃんでもおじいちゃんでも」という比喩の範囲で、入口を複数用意する。</td></tr>
          <tr><th>制約</th><td>既存の本文（約122,000字）、図版は自作SVG、フレームワークなし、静的ファイル、日本語組版、モバイル対応。</td></tr>
          <tr><th>素材</th><td>紙、インク、ウルトラマリン、レジストレーション・オレンジ、工程イエロー、工程シアン。明朝、グロテスク、モノスペース。</td></tr>
          <tr><th>非目的</th><td>売ること、バズること、派手な動画、3D、ストックフォト、自動再生。読者を急かさない。</td></tr>
        </tbody>
      </table>
    </section>

    <section class="notes-section" aria-label="第一原理">
      <div class="notes-section__head">
        <h2 class="notes-section__title">第一原理の4問</h2>
        <p class="notes-section__note mono">FIRST PRINCIPLES / 4 QUESTIONS</p>
      </div>
      <div class="principles-4">
        <div class="principle-4"><span class="principle-4__no">Q1</span><h3 class="principle-4__title">何のためか</h3><p class="principle-4__text">読む・見る・疑うを、一つの場所でつなぐ。教材は、答えの倉庫ではなく、考えるための作業台。</p></div>
        <div class="principle-4"><span class="principle-4__no">Q2</span><h3 class="principle-4__title">誰のためか</h3><p class="principle-4__text">初学者には地図を、専門家には検証と図版を。同じ内容を、二つの深度で読めるようにする。</p></div>
        <div class="principle-4"><span class="principle-4__no">Q3</span><h3 class="principle-4__title">何が制約か</h3><p class="principle-4__text">本文の長さ、日本語の組版、静的配信、図版の自作。制約を隠さず、制約から形を決める。</p></div>
        <div class="principle-4"><span class="principle-4__no">Q4</span><h3 class="principle-4__title">何を素材にするか</h3><p class="principle-4__text">印刷所の台紙、校正記号、ものさし、図面。デザイン史の世界そのものを、界面の語彙にする。</p></div>
      </div>
    </section>

    <section class="notes-section" aria-label="設計上の決断">
      <div class="notes-section__head">
        <h2 class="notes-section__title">6つの決断</h2>
        <p class="notes-section__note mono">DECISIONS / BEFORE → AFTER</p>
      </div>
      <div class="decisions">
        {''.join(decisions)}
      </div>
    </section>

    <section class="notes-section" aria-label="トークン">
      <div class="notes-section__head">
        <h2 class="notes-section__title">色と文字</h2>
        <p class="notes-section__note mono">TOKENS / COLOUR · TYPE</p>
      </div>
      <div class="token-grid">
        <div class="token"><div class="token__chip" style="background:var(--paper)"></div><div class="token__meta"><strong>台紙</strong>PAPER<br>#E7E8E0</div></div>
        <div class="token"><div class="token__chip" style="background:var(--ink)"></div><div class="token__meta"><strong>インク</strong>INK<br>#111412</div></div>
        <div class="token"><div class="token__chip" style="background:var(--ultra)"></div><div class="token__meta"><strong>ウルトラマリン</strong>ULTRA<br>#1B2FC7</div></div>
        <div class="token"><div class="token__chip" style="background:var(--signal)"></div><div class="token__meta"><strong>レジストレーション</strong>SIGNAL<br>#F04A22</div></div>
        <div class="token"><div class="token__chip" style="background:var(--yellow)"></div><div class="token__meta"><strong>工程イエロー</strong>YELLOW<br>#F2C300</div></div>
        <div class="token"><div class="token__chip" style="background:var(--cyan)"></div><div class="token__meta"><strong>工程シアン</strong>CYAN<br>#007F8F</div></div>
      </div>

      <div class="type-specimen">
        <div class="type-row"><span class="type-row__label">SHIPPORI MINCHO B1<br>歴史 / DISPLAY</span><p class="type-row__sample type-row__sample--mincho">歴史は、振り子ではなく、螺旋である。</p></div>
        <div class="type-row"><span class="type-row__label">ARCHIVO<br>現在 / GROTESQUE</span><p class="type-row__sample type-row__sample--latin">DESIGN HISTORY / 50,000 YEARS</p></div>
        <div class="type-row"><span class="type-row__label">IBM PLEX MONO<br>データ / MONO</span><p class="type-row__sample type-row__sample--mono">PL. 07 / 1919–1933 / 8-FOLD / 1.4 PT</p></div>
        <div class="type-row"><span class="type-row__label">NOTO SERIF JP<br>本文 / READING</span><p class="type-row__sample type-row__sample--serif">デザインは、意図を、制約のなかで、他の誰かのために、かたちにすること。美しさは、その一部である。</p></div>
      </div>
    </section>

    <section class="notes-section" aria-label="版面">
      <div class="notes-section__head">
        <h2 class="notes-section__title">版面の骨格</h2>
        <p class="notes-section__note mono">GRID / RAIL · GUTTER · MEASURE</p>
      </div>
      <figure class="notes-figure">
        {GRID_SVG}
        <figcaption class="mono"><span>FIG. A — 12 COLUMNS / RAIL 76 / MAX 1480</span><span>MEASURE 44EM</span></figcaption>
      </figure>
    </section>

    <section class="notes-section" aria-label="図版の解剖">
      <div class="notes-section__head">
        <h2 class="notes-section__title">図版の解剖</h2>
        <p class="notes-section__note mono">PLATE ANATOMY / FRAME · LINE · LABEL</p>
      </div>
      <figure class="notes-figure">
        {PLATE_SVG}
        <figcaption class="mono"><span>FIG. B — 640 × 300 / SVG / NO RASTER</span><span>SEE · ASK · SOURCE</span></figcaption>
      </figure>
    </section>

    <section class="notes-section" aria-label="自己批判">
      <div class="notes-section__head">
        <h2 class="notes-section__title">自己批判</h2>
        <p class="notes-section__note mono">SELF-CRITIQUE / 27 OF 30</p>
      </div>
      <div class="scores">
        <div class="score"><span class="score__num">5</span><span class="score__label">PHILOSOPHY</span></div>
        <div class="score"><span class="score__num">4</span><span class="score__label">HIERARCHY</span></div>
        <div class="score"><span class="score__num">4</span><span class="score__label">EXECUTION</span></div>
        <div class="score"><span class="score__num">5</span><span class="score__label">SPECIFICITY</span></div>
        <div class="score"><span class="score__num">4</span><span class="score__label">RESTRAINT</span></div>
        <div class="score"><span class="score__num">5</span><span class="score__label">VARIETY</span></div>
      </div>
      <p class="note"><strong>まだ弱いところ。</strong> 長文ページの全文検索がない。図版の地域的な深さはまだ均一ではない。320px幅の細部は、さらに詰められる。タイムラインの対数尺度は、科学的な縮尺ではなく、時間感覚のための比喩である。これらは次の版で直す。</p>
      <ul class="removed-list">
        <li>ストックフォト</li>
        <li>グラデーション</li>
        <li>カルーセル</li>
        <li>自動再生</li>
        <li>偽の3D</li>
        <li>影の多用</li>
        <li>アイコンだけのナビ</li>
        <li>「AIっぽい」装飾</li>
      </ul>
    </section>

    <section class="notes-section" aria-label="アクセシビリティ">
      <div class="notes-section__head">
        <h2 class="notes-section__title">アクセシビリティ</h2>
        <p class="notes-section__note mono">ACCESS / CONSTRAINT AS MATERIAL</p>
      </div>
      <dl class="a11y-list">
        <div class="a11y-item"><dt>コントラスト</dt><dd>本文のインク／台紙は約13:1、ウルトラマリンは約9:1。シグナルは大文字と図形に限定し、小さな本文には使わない。</dd></div>
        <div class="a11y-item"><dt>キーボード</dt><dd>スキップリンク、フォーカス可視化、ネイティブの dialog、details/summary、タイムラインのボタン。すべてTabで到達できる。</dd></div>
        <div class="a11y-item"><dt>モーション</dt><dd>自動再生なし。prefers-reduced-motion で、reveal・transition・scrollを停止する。</dd></div>
        <div class="a11y-item"><dt>構造</dt><dd>1ページ1つのh1。ランドマーク、表の見出し、SVGの title/desc、外部リンクの区別。</dd></div>
        <div class="a11y-item"><dt>no-JS</dt><dd>本文、全128件の年表、13の図版はJavaScriptなしでも読める。タイムラインのインタラクティブ表示だけがJSに依存し、全表が代替になる。</dd></div>
        <div class="a11y-item"><dt>既知のギャップ</dt><dd>本文の全文検索は未実装。タイムラインの対数表示は視覚的な補助で、スクリーンリーダーには等幅の時代リストと全表を提供する。</dd></div>
      </dl>
    </section>

    <section class="notes-end">
      <p class="eyebrow"><span class="eyebrow__no">END</span> THE ARGUMENT</p>
      <p style="margin-top:0.8rem"><strong>このサイトは、本書の主張の実装である。</strong> デザインは、意図を、制約のなかで、他の誰かのために、かたちにすること。だから、このサイトの色、書体、余白、図版、動きも、読者のために選ばれ、読む前に開示される。</p>
      <p>次の版へ：全文検索、地域別の一次資料、音声ガイド、印刷用ワークシート。読者は、完成品ではなく、更新される道具を受け取る。</p>
      <p style="margin-top:1.2rem"><a class="textlink" href="index.html">入口へ戻る <span class="textlink__arrow" aria-hidden="true">↗</span></a></p>
    </section>
  </div>
</main>

{footer("read.html", "THE CATALOGUE", "本文を、読む。")}
<script src="assets/app.js" defer></script>
</body>
</html>
"""
    (BASE / "design-notes.html").write_text(page, encoding="utf-8")
    print(f"wrote design-notes.html: {len(page):,} chars")


if __name__ == "__main__":
    main()
