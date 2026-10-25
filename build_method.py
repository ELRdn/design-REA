# -*- coding: utf-8 -*-
"""Build method.html: method, 20 myths, 14 corrections, 100 fact-checks."""
import html
import json
import re
from pathlib import Path

import markdown

from build_read import head, rail, footer

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent


def md(text: str) -> str:
    return markdown.markdown(text, extensions=["tables", "sane_lists"], output_format="html5")


def verdict_kind(v: str) -> str:
    return {"×": "cross", "△": "triangle", "○": "circle"}.get(v, "cross")


def main() -> None:
    # Myths
    text = (ROOT / "06_part6.md").read_text(encoding="utf-8")
    start = text.index("### 神話1")
    block = text[start:]
    pat = re.compile(
        r"### 神話(\d+)：(.+?)\n\n\*\*判定：([×△○])\*\*\n\n(.*?)(?=\n---|\n### 神話|\Z)",
        re.DOTALL,
    )
    myths = pat.findall(block)

    myth_html = []
    for num, title, verdict, body in myths:
        body_clean = body.strip()
        myth_html.append(
            f'''<details class="myth myth--full">
  <summary class="myth__summary">
    <span class="myth__no">{int(num):02d}</span>
    <span class="myth__title">{title}</span>
    <span class="myth__verdict" data-v="{verdict_kind(verdict)}" aria-label="判定 {verdict}">{verdict}</span>
  </summary>
  <div class="myth__body"><div></div><div class="myth__content">{md(body_clean)}</div></div>
</details>'''
        )

    # Corrections
    app = (ROOT / "07_appendix.md").read_text(encoding="utf-8")
    i = app.index("## 修正した主な誤り")
    j = app.index("## 限界と未解決の論点", i)
    corr_block = app[i:j]
    corr_pat = re.compile(
        r"(\d+)\.\s+\*\*(.+?)\*\*\s*\n\s*→\s*(.+?)(?=\n\n\d+\.|\Z)",
        re.DOTALL,
    )
    corrections = corr_pat.findall(corr_block)
    corr_html = []
    for num, wrong, right in corrections:
        wrong = re.sub(r"」\s+と\s+「", "」と「", wrong.strip())
        right = re.sub(r"」\s+と\s+「", "」と「", right.strip())
        right = re.sub(r"\s+\n\s*", " ", right)
        corr_html.append(
            f'''<div class="correction">
  <span class="correction__no">FIX {int(num):02d}</span>
  <p class="correction__wrong">{html.escape(wrong)}</p>
  <p class="correction__right">{html.escape(right)}</p>
</div>'''
        )

    # Fact-check rows
    rows = json.loads((ROOT / "factcheck.json").read_text(encoding="utf-8"))
    trs = []
    for r in rows:
        kind = "mostly" if "概ね" in r["verdict"] else "ok"
        trs.append(
            f'<tr data-fc-row data-verdict="{html.escape(r["verdict"])}">'
            f'<td>{r["no"]}</td><td>{html.escape(r["claim"])}</td>'
            f'<td>{html.escape(r["sources"])}</td>'
            f'<td><span class="verdict" data-v="{kind}">{html.escape(r["verdict"])}</span></td></tr>'
        )

    page = f"""{head("検証 — デザイン全史 / THE EVIDENCE", "20の通説、14の修正、100件のファクトチェック。本書の検証過程をすべて公開。")}
<body data-page="method">
<a class="skip" href="#main">本文へスキップ</a>
{rail("method")}

<main id="main" class="page">
  <div class="shell">
    <header class="method-head">
      <p class="eyebrow"><span class="eyebrow__no">06</span> THE EVIDENCE</p>
      <h1 class="method-title">この本は、<br>どう作られたか。</h1>
      <p class="method-lede">206の百科事典項目を索引に、一次資料・博物館・規格で照合した。100の主張を検証し、14の誤りを直した。その記録を、隠さず公開する。歴史は、断定の集積ではなく、検証の連続である。</p>
      <div class="method-stats stats">
        <div class="stat"><span class="stat__num">206</span><span class="stat__label">百科事典項目<br>（索引として使用）</span></div>
        <div class="stat"><span class="stat__num">100</span><span class="stat__label">検証した主張<br>（CSV / JSON で公開）</span></div>
        <div class="stat"><span class="stat__num">14</span><span class="stat__label">修正した主な誤り<br>（修正前後を記録）</span></div>
        <div class="stat"><span class="stat__num">20</span><span class="stat__label">壊した神話<br>（× / △ / ○ 判定）</span></div>
      </div>
      <p style="margin-top:1.2rem;display:flex;flex-wrap:wrap;gap:0.7rem">
        <a class="btn" href="factcheck.csv" download>検証表 CSV <span class="btn__arrow" aria-hidden="true">↓</span></a>
        <a class="btn" href="デザイン全史.pdf" download>印刷版 PDF <span class="btn__arrow" aria-hidden="true">↓</span></a>
      </p>
    </header>

    <section class="method-section" aria-label="検証の方法">
      <div class="method-section__head">
        <h2 class="method-section__title">3つのパス</h2>
        <p class="method-section__note mono">METHOD / 3 PASSES</p>
      </div>
      <div class="method-steps">
        <div class="method-step">
          <span class="method-step__no">PASS 01</span>
          <h3 class="method-step__title">広く読む</h3>
          <p class="method-step__text">約200の百科事典項目を索引として、時代・地域・人物・運動の全体像をつかむ。百科事典は二次資料であり、それだけでは確定しない。</p>
        </div>
        <div class="method-step">
          <span class="method-step__no">PASS 02</span>
          <h3 class="method-step__title">深く確かめる</h3>
          <p class="method-step__text">主要な年号・引用・定義は、博物館、大学、一次文献、規格、企業史、公的資料に当たる。原典が読めない場合は、その限界を明記する。</p>
        </div>
        <div class="method-step">
          <span class="method-step__no">PASS 03</span>
          <h3 class="method-step__title">批判的に書く</h3>
          <p class="method-step__text">通説と証拠を分け、異説を併記し、西洋中心の物語を相対化する。採用しなかった通説も、×/△の判定つきで残す。</p>
        </div>
      </div>
    </section>

    <section class="method-section" aria-label="20の神話">
      <div class="method-section__head">
        <h2 class="method-section__title">20の神話を壊す</h2>
        <p class="method-section__note mono">20 MYTHS / × WRONG · △ CONDITIONAL · ○ MOSTLY RIGHT / CLICK TO OPEN</p>
      </div>
      <div class="myths">
        {''.join(myth_html)}
      </div>
    </section>

    <section class="method-section" aria-label="修正した誤り">
      <div class="method-section__head">
        <h2 class="method-section__title">14の誤りを直した</h2>
        <p class="method-section__note mono">14 CORRECTIONS / BEFORE → AFTER</p>
      </div>
      <div class="corrections">
        {''.join(corr_html)}
      </div>
    </section>

    <section class="method-section" aria-label="限界">
      <div class="method-section__head">
        <h2 class="method-section__title">この本の限界</h2>
        <p class="method-section__note mono">LIMITS / WHAT IS NOT COVERED</p>
      </div>
      <div class="limits">
        <p><strong>非西洋の記述は、英語圏の資料に依存している部分があります。</strong> 日本、中国、イスラーム、アフリカ、先住アメリカ、オセアニアの現地語一次資料は、まだ十分に読めていません。次の版では、地域ごとの研究者と資料を増やします。</p>
        <p><strong>年号には幅があります。</strong> 古代・中世の年号は、考古学の進展で変わります。本書は「〜ごろ」を多用し、異説がある場合は本文と付録Aに注記しました。年表は網羅的な学術年表ではなく、読むための索引です。</p>
        <p><strong>引用は、逐語訳ではなく要約を含みます。</strong> 英語・フランス語・ドイツ語の引用は、日本語訳・要約です。逐語訳が必要な場合は、原典を参照してください。</p>
        <p><strong>「世界最高」は、到達点ではなく、方向です。</strong> 本書は完成品ではなく、検証可能な出発点として作りました。誤りや異説があれば、次の版で直します。</p>
      </div>
    </section>

    <details class="fc-details">
      <summary>100件の検証表を開く <span class="mono">100 ROWS</span></summary>
      <p class="method-section__note" style="margin:0 0 0.8rem">この表は、本書が採用した主張を検証したものです。採用しなかった通説・誤りは、上の「20の神話」と「14の誤り」に記録しています。</p>
      <div class="fc-controls">
        <label class="sr-only" for="fc-search">検証表を検索</label>
        <input id="fc-search" type="search" placeholder="主張・資料・判定で検索（例: バウハウス）" data-fc-search>
        <label class="sr-only" for="fc-verdict">判定で絞り込む</label>
        <select id="fc-verdict" data-fc-verdict>
          <option value="all">すべての判定</option>
          <option value="確認済み">確認済み</option>
          <option value="概ね確認済み">概ね確認済み</option>
        </select>
        <span class="mono" data-fc-count>100 / 100</span>
      </div>
      <div class="fc-table-wrap">
        <table class="fc-table">
          <thead><tr><th scope="col">#</th><th scope="col">主張</th><th scope="col">確認した資料</th><th scope="col">判定・注記</th></tr></thead>
          <tbody>{''.join(trs)}</tbody>
        </table>
      </div>
    </details>

    <p class="note" style="margin-top:2rem"><strong>検証の原則。</strong> 「たぶんそうだ」は確認済みではない。「有名な話」は証拠ではない。「専門家が言った」は一次資料ではない。本書はその原則を守ろうとしたが、完全には守れていない。読者は、本書を出発点に、自分で一次資料を確かめてほしい。</p>
  </div>
</main>

{footer("design-notes.html", "THE SYSTEM", "設計を、開く。")}
<script src="assets/app.js" defer></script>
</body>
</html>
"""
    (BASE / "method.html").write_text(page, encoding="utf-8")
    print(f"wrote method.html: {len(page):,} chars, myths={len(myths)}, corrections={len(corrections)}, checks={len(rows)}")


if __name__ == "__main__":
    main()
