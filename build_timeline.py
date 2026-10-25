# -*- coding: utf-8 -*-
"""Build timeline.html from the book's 128-row chronology."""
import json
import math
import re
from pathlib import Path

from build_read import head, rail, footer

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
SOURCE = ROOT / "05_part5.md"

ERAS = [
    {
        "id": "prehistory", "no": "01", "name": "先史", "years": "2.6M BCE–3,000 BCE",
        "span": 2_600_000, "chapter": "ch-02",
        "question": "最初のデザインは、美しさのためだったのか、生き延びるためだったのか。",
    },
    {
        "id": "ancient", "no": "02", "name": "古代", "years": "3,000–500 BCE",
        "span": 2_500, "chapter": "ch-02",
        "question": "文字は、誰の記憶を保存し、誰の記憶を消したのか。",
    },
    {
        "id": "medieval", "no": "03", "name": "古典・中世", "years": "500 BCE–1400",
        "span": 1_900, "chapter": "ch-03",
        "question": "職人の身体知は、どこで生まれ、どこで失われたのか。",
    },
    {
        "id": "print", "no": "04", "name": "印刷・ルネサンス", "years": "1400–1750",
        "span": 350, "chapter": "ch-04",
        "question": "複製は、知識を民主化したのか、それとも新しい管理を生んだのか。",
    },
    {
        "id": "industrial", "no": "05", "name": "産業革命", "years": "1750–1900",
        "span": 150, "chapter": "ch-05",
        "question": "機械は、美しさを殺したのか、それとも新しい美しさを生んだのか。",
    },
    {
        "id": "modern", "no": "06", "name": "モダニズム", "years": "1900–1945",
        "span": 45, "chapter": "ch-06",
        "question": "普遍の名の下で、何が地方の特殊として切り捨てられたのか。",
    },
    {
        "id": "postwar", "no": "07", "name": "戦後", "years": "1945–1970",
        "span": 25, "chapter": "ch-07",
        "question": "豊かさのデザインは、誰の労働の上に建っていたのか。",
    },
    {
        "id": "postmodern", "no": "08", "name": "ポストモダン", "years": "1970–1990",
        "span": 20, "chapter": "ch-07",
        "question": "装飾の復権は、自由の回復か、消費の加速か。",
    },
    {
        "id": "digital", "no": "09", "name": "デジタル", "years": "1990–2010",
        "span": 20, "chapter": "ch-08",
        "question": "使いやすさは、民主化か、依存か。",
    },
    {
        "id": "now", "no": "10", "name": "現在", "years": "2010–2026",
        "span": 16, "chapter": "ch-09",
        "question": "AIが形を作るとき、誰が「良い」を決めるのか。",
    },
]

ERA_BY_ID = {e["id"]: e for e in ERAS}


def parse_year(label: str) -> int:
    s = label.replace("ごろ", "").replace("約", "")
    m = re.search(r"紀元前\s*(\d[\d,]*)", s)
    if m:
        return -int(m.group(1).replace(",", ""))
    m = re.search(r"(\d+)\s*万\s*(\d+)\s*年前", s)
    if m:
        return 2026 - (int(m.group(1)) * 10000 + int(m.group(2)))
    m = re.search(r"(\d+(?:\.\d+)?)\s*万年前", s)
    if m:
        return 2026 - int(float(m.group(1)) * 10000)
    m = re.search(r"(\d[\d,]*)\s*年前", s)
    if m:
        return 2026 - int(m.group(1).replace(",", ""))
    m = re.search(r"(\d{3,4})\s*年代", s)
    if m:
        return int(m.group(1))
    m = re.search(r"(\d{3,4})\s*年", s)
    if m:
        return int(m.group(1))
    return 2026


def era_of(year: int) -> str:
    if year <= -3000:
        return "prehistory"
    if year <= -500:
        return "ancient"
    if year <= 1400:
        return "medieval"
    if year <= 1750:
        return "print"
    if year <= 1900:
        return "industrial"
    if year < 1945:
        return "modern"
    if year <= 1970:
        return "postwar"
    if year <= 1990:
        return "postmodern"
    if year <= 2010:
        return "digital"
    return "now"


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    start = text.index("| 年 | 出来事 | デザイン上の意味 |")
    rows = []
    for line in text[start:].splitlines():
        line = line.strip()
        if not line.startswith("|"):
            if rows:
                break
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 3:
            continue
        if cells[0] in ("年", "---") or "出来事" in cells[0]:
            continue
        rows.append(cells)

    events = []
    for i, (year_label, title, meaning) in enumerate(rows, 1):
        y = parse_year(year_label)
        era = era_of(y)
        events.append(
            {
                "id": f"ev-{i:03d}",
                "no": i,
                "year": year_label,
                "sort": y,
                "title": title,
                "meaning": meaning,
                "era": era,
            }
        )

    # Counts
    counts = {e["id"]: 0 for e in ERAS}
    for ev in events:
        counts[ev["era"]] += 1

    # JSON for the interaction
    payload = {
        "eras": [
            {**e, "count": counts[e["id"]]}
            for e in ERAS
        ],
        "events": events,
    }
    data_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))

    # Bar segments and era buttons
    bar_segments = []
    era_buttons = []
    for e in ERAS:
        bar_segments.append(
            f'<button class="tl-bar__seg" type="button" data-era="{e["id"]}" aria-pressed="false" style="--w:1" title="{e["name"]} {e["years"]}">'
            f'<span class="tl-bar__no">{e["no"]}</span>'
            f'<span class="tl-bar__name">{e["name"]}</span>'
            f'<span class="tl-bar__years">{e["years"]}</span></button>'
        )
        era_buttons.append(
            f'<button class="tl-era" type="button" data-era="{e["id"]}" aria-pressed="false">'
            f'<span class="tl-era__no">{e["no"]}</span>'
            f'<span class="tl-era__name">{e["name"]}</span>'
            f'<span class="tl-era__years">{e["years"]}</span>'
            f'<span class="tl-era__count">{counts[e["id"]]} EVENTS</span></button>'
        )

    # Event lists (one panel per era; the first is visible without JS)
    panels = []
    for e in ERAS:
        era_events = [ev for ev in events if ev["era"] == e["id"]]
        items = []
        for j, ev in enumerate(era_events):
            pressed = ' aria-pressed="true"' if e["id"] == "prehistory" and j == 0 else ' aria-pressed="false"'
            items.append(
                f'<button class="tl-ev" type="button" data-ev="{ev["id"]}" data-era="{e["id"]}"{pressed}>'
                f'<span class="tl-ev__year">{ev["year"]}</span>'
                f'<span class="tl-ev__dot" aria-hidden="true"></span>'
                f'<span><span class="tl-ev__title">{ev["title"]}</span>'
                f'<span class="tl-ev__meaning">{ev["meaning"]}</span></span>'
                f"</button>"
            )
        hidden = "" if e["id"] == "prehistory" else " hidden"
        panels.append(
            f'<div class="tl-list" data-tl-list="{e["id"]}"{hidden}>{"".join(items)}</div>'
        )

    first = events[0]
    first_era = ERA_BY_ID[first["era"]]

    # Full table
    trs = []
    for ev in events:
        trs.append(
            f'<tr data-tl-row data-era="{ev["era"]}"><td>{ev["year"]}</td><td>{ev["title"]}</td>'
            f'<td>{ev["meaning"]}</td><td>{ERA_BY_ID[ev["era"]]["name"]}</td></tr>'
        )

    page = f"""{head("年表 — デザイン全史 / THE RULER", "128の出来事を、等幅と対数の二つの尺度でたどるインタラクティブ年表。")}
<body data-page="timeline">
<a class="skip" href="#main">本文へスキップ</a>
{rail("timeline")}

<main id="main" class="page">
  <div class="shell">
    <header class="tl-head">
      <p class="eyebrow"><span class="eyebrow__no">04</span> THE RULER</p>
      <h1 class="tl-title">128の出来事を、<br>ひとつのものさしに。</h1>
      <p class="tl-lede">50,000年を等幅で並べると、嘘になる。実際の時間で並べると、20世紀が針の先になる。だから、二つの尺度を切り替えられるようにした。時代を選び、出来事を選ぶ。年号は、歴史の厚みを測る道具である。</p>
      <div class="tl-controls">
        <div class="segmented" role="group" aria-label="時間の尺度">
          <button type="button" data-tl-mode="equal" aria-pressed="true">等幅 / 時代の厚み</button>
          <button type="button" data-tl-mode="log" aria-pressed="false">対数 / 実際の時間</button>
        </div>
        <p class="tl-note">等幅は各時代を同じ幅で、対数は log10(年数) で圧縮して表示します。どちらも「正確な縮尺」ではありません。</p>
      </div>
    </header>
    <noscript><p class="note">JavaScriptを有効にすると、時代を切り替えて読めます。下の「全128件の年表を開く」は、JavaScriptなしでも読めます。</p></noscript>

    <section aria-label="時代の比率">
      <div class="tl-bar" data-tl-bar role="group" aria-label="時代の比率（クリックで選択）">
        {''.join(bar_segments)}
      </div>
      <div class="tl-scale mono">
        <span>EQUAL / LOG</span>
        <span>10 ERAS · 128 EVENTS</span>
        <span>NOW = 2026</span>
      </div>
      <div class="tl-eras" role="group" aria-label="時代を選ぶ">
        {''.join(era_buttons)}
      </div>
    </section>

    <section class="tl-stage" aria-label="時代の出来事">
      <div data-tl-lists>
        {''.join(panels)}
      </div>
      <aside class="tl-detail" data-tl-detail aria-live="polite">
        <div class="tl-detail__era mono"><span>{first_era["no"]} / {first_era["name"]}</span><span>{first_era["years"]}</span></div>
        <p class="tl-detail__year" data-tl-year>{first["year"]}</p>
        <h2 class="tl-detail__title" data-tl-title>{first["title"]}</h2>
        <p class="tl-detail__text" data-tl-text>{first["meaning"]}。</p>
        <div class="tl-detail__actions">
          <div class="tl-detail__nav">
            <button type="button" data-tl-prev aria-label="前の出来事">←</button>
            <button type="button" data-tl-next aria-label="次の出来事">→</button>
          </div>
          <a class="tl-detail__link" href="read.html#{first_era["chapter"]}" data-tl-link>第2章を読む ↗</a>
        </div>
      </aside>
    </section>

    <p class="tl-note" style="margin-top:1.2rem;max-width:62em">年号は考古学・文献学の進展で変わります。本書の年表は「読むための索引」であり、網羅的な学術年表ではありません。異説がある場合は、本文と付録Aの注記を参照してください。</p>

    <details class="tl-full">
      <summary>全128件の年表を開く <span class="mono">128 ROWS</span></summary>
      <div class="tl-search">
        <label class="sr-only" for="tl-search">年表を検索</label>
        <input id="tl-search" type="search" placeholder="出来事・意味・時代で検索（例: バウハウス）" data-tl-search>
        <span class="mono" data-tl-count>128 / 128</span>
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th scope="col">年</th><th scope="col">出来事</th><th scope="col">デザイン上の意味</th><th scope="col">時代</th></tr></thead>
          <tbody>{''.join(trs)}</tbody>
        </table>
      </div>
    </details>
  </div>
</main>

{footer("atlas.html", "THE PLATES", "図版で、見る。")}
<script type="application/json" id="timeline-data">{data_json}</script>
<script src="assets/app.js" defer></script>
</body>
</html>
"""

    (BASE / "timeline.html").write_text(page, encoding="utf-8")
    print(f"wrote timeline.html: {len(page):,} chars, {len(events)} events")
    for e in ERAS:
        print(e["id"], counts[e["id"]])


if __name__ == "__main__":
    main()
