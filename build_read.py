# -*- coding: utf-8 -*-
"""Build the reading edition (read.html) from the book manuscript."""
import re
from pathlib import Path

import markdown

BASE = Path(__file__).resolve().parent          # design-history-research/site
ROOT = BASE.parent                              # design-history-research
SOURCE = ROOT / "DESIGN_HISTORY_BOOK.md"

TITLE = "デザイン全史 — 本文 / THE CATALOGUE"
DESC = "『デザイン全史』の全文。15章、122,000字。読みやすさのための組版と、章ごとの図版リンク付き。"

SHORT = {
    "prologue": ("序", "序章 当たり前の集積"),
    "ch-01": ("01", "言葉の迷宮"),
    "ch-02": ("02", "５万年前のデザイン"),
    "ch-03": ("03", "西洋の外のデザイン"),
    "ch-04": ("04", "中世・ルネサンス・印刷"),
    "ch-05": ("05", "産業革命とデザイン"),
    "ch-06": ("06", "モダニズムの爆発"),
    "ch-07": ("07", "戦後のデザイン"),
    "ch-08": ("08", "デジタルの転回"),
    "ch-09": ("09", "デザインの現在"),
    "ch-10": ("10", "日本のデザイン全史"),
    "ch-11": ("11", "対象を読む方法"),
    "ch-12": ("12", "デザイン全史 年表"),
    "ch-13": ("13", "20の神話を壊す"),
    "ch-14": ("14", "読書案内"),
    "ch-15": ("15", "デザインの未来"),
    "app-a": ("A", "ファクトチェック記録"),
    "app-b": ("B", "参考文献"),
    "app-c": ("C", "謝辞"),
}

PLATES = {
    "ch-02": [("plate-01", "PL.01 握斧"), ("plate-02", "PL.02 土器")],
    "ch-03": [("plate-03", "PL.03 楔形文字"), ("plate-04", "PL.04 イスラーム"), ("plate-05", "PL.05 明式家具")],
    "ch-04": [("plate-06", "PL.06 活版印刷")],
    "ch-06": [("plate-07", "PL.07 バウハウス")],
    "ch-08": [("plate-08", "PL.08 グリッド")],
    "ch-09": [("plate-11", "PL.11 サーキュラー"), ("plate-12", "PL.12 AI")],
    "ch-10": [("plate-13", "PL.13 茶碗")],
    "ch-15": [("plate-12", "PL.12 AI")],
}


def head(title: str, desc: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#e7e8e0">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="ja_JP">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800;900&family=IBM+Plex+Mono:wght@400;500;600&family=Noto+Serif+JP:wght@400;500;600;700&family=Shippori+Mincho+B1:wght@400;600;700;800&family=Zen+Kaku+Gothic+New:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script>
(function () {{
  try {{
    var t = localStorage.getItem("dh-theme");
    if (t === "dark") {{
      document.documentElement.setAttribute("data-theme", "dark");
      var m = document.querySelector('meta[name="theme-color"]');
      if (m) m.setAttribute("content", "#0d0f0e");
    }}
  }} catch (e) {{}}
}})();
</script>
</head>"""


def rail(active: str = "") -> str:
    items = [
        ("01", "入口", "index.html#orientation", "home"),
        ("02", "定義", "index.html#definition", "definition"),
        ("03", "15章", "index.html#rooms", "rooms"),
        ("04", "年表", "timeline.html", "timeline"),
        ("05", "図版", "atlas.html", "atlas"),
        ("06", "検証", "method.html", "method"),
        ("07", "設計", "design-notes.html", "design"),
    ]
    links = []
    for num, label, href, key in items:
        cur = ' aria-current="page"' if key == active else ""
        links.append(
            f'<a class="rail__link" href="{href}"{cur}>'
            f'<span class="rail__num">{num}</span><span class="rail__label">{label}</span></a>'
        )
    read_cur = ' aria-current="page"' if active == "read" else ""
    return f"""<aside class="rail" aria-label="サイト">
  <a class="rail__brand" href="index.html" aria-label="デザイン全史 ホーム">
    <span class="rail__mark">D<span>/</span>H</span>
    <span class="rail__name">デザイン全史</span>
  </a>
  <nav class="rail__nav" id="site-nav" aria-label="主要">
    {''.join(links)}
    <a class="rail__link rail__link--read" href="read.html"{read_cur}>
      <span class="rail__num">08</span><span class="rail__label">本文</span>
    </a>
  </nav>
  <div class="rail__bottom">
    <button class="rail__toggle theme-toggle" type="button" data-theme-toggle aria-pressed="false" aria-label="照明を暗くする">
      <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg>
      <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4 6.5 6.5 0 0 0 20 14.5Z"/></svg>
    </button>
    <a class="rail__read" href="read.html"{read_cur}>本文</a>
  </div>
  <div class="rail__mobile">
    <button class="rail__toggle theme-toggle" type="button" data-theme-toggle aria-pressed="false" aria-label="照明を暗くする">
      <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg>
      <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4 6.5 6.5 0 0 0 20 14.5Z"/></svg>
    </button>
    <button class="nav-toggle" type="button" data-nav-toggle aria-controls="site-nav" aria-expanded="false">
      <span class="nav-toggle__label">メニュー</span>
      <span class="nav-toggle__bars" aria-hidden="true"><span></span><span></span></span>
    </button>
  </div>
</aside>
<div class="nav-scrim" data-nav-scrim aria-hidden="true"></div>
<noscript>
  <nav class="nojs-nav" aria-label="メニュー（JavaScriptなし）">
    <a href="index.html">入口</a>
    <a href="index.html#definition">定義</a>
    <a href="index.html#rooms">15章</a>
    <a href="timeline.html">年表</a>
    <a href="atlas.html">図版</a>
    <a href="method.html">検証</a>
    <a href="design-notes.html">設計</a>
    <a href="read.html">本文</a>
  </nav>
</noscript>"""


def footer(next_href: str, next_label: str, next_title: str) -> str:
    return f"""<footer class="footer">
  <div class="shell">
    <div class="footer__cta">
      <div>
        <p class="eyebrow"><span class="eyebrow__no">NEXT</span> {next_label}</p>
        <h2>{next_title}</h2>
      </div>
      <a class="btn btn--solid" href="{next_href}">開く <span class="btn__arrow" aria-hidden="true">↗</span></a>
    </div>
    <div class="colophon mono">
      <span>デザイン全史 / WEB EDITION · 2026.10.25</span>
      <span>OPENCODE RESEARCH · BUILT WITHOUT FRAMEWORKS</span>
    </div>
  </div>
</footer>"""


def main() -> None:
    raw = SOURCE.read_text(encoding="utf-8")
    total_chars = len(raw)

    # Epigraph
    epi_match = re.search(r"^---\n\n(> .*?)\n\n---", raw, re.MULTILINE | re.DOTALL)
    epigraph = epi_match.group(1) if epi_match else ""
    epigraph = re.sub(r"^> ", "", epigraph, flags=re.MULTILINE).strip()

    # Body begins at the reader's promise; drop the cover and the printed TOC.
    body = raw[raw.index("## 読者への約束"):]
    body = re.sub(r"\n## 目次\n.*?(?=\n# 第I部)", "", body, flags=re.DOTALL)

    # Assign stable ASCII ids and collect the TOC.
    lines = body.splitlines()
    heading_info = []
    h2_counter = 0
    h3_counter = 0
    h4_counter = 0
    part_counter = 0
    current_h1 = None
    chapter_chars = {}
    current_lines = []

    def flush_chapter() -> None:
        nonlocal current_h1, current_lines
        if current_h1 and current_lines:
            chapter_chars[current_h1] = len("\n".join(current_lines))
        current_lines = []

    out_lines = []
    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if m:
            level = len(m.group(1))
            text = m.group(2)
            hid = None
            if level == 1:
                flush_chapter()
                if text.startswith("第") and "部" in text[:6]:
                    part_counter += 1
                    hid = f"part-{part_counter}"
                elif text.startswith("序章"):
                    hid = "prologue"
                else:
                    cm = re.match(r"第(\d+)章", text)
                    if cm:
                        hid = f"ch-{int(cm.group(1)):02d}"
                    elif text.startswith("付録A"):
                        hid = "app-a"
                    elif text.startswith("付録B"):
                        hid = "app-b"
                    elif text.startswith("付録C"):
                        hid = "app-c"
                    else:
                        hid = f"h1-{len(heading_info) + 1:02d}"
                current_h1 = hid
                current_lines = [line]
            elif level == 2:
                h2_counter += 1
                if "１ページ要約" in text:
                    hid = "summary"
                else:
                    hid = f"sec-{h2_counter:03d}"
            elif level == 3:
                h3_counter += 1
                hid = f"sub-{h3_counter:03d}"
            else:
                h4_counter += 1
                hid = f"ssub-{h4_counter:03d}"
            heading_info.append((level, text, hid))
            out_lines.append(f"{line} {{#{hid}}}")
        else:
            if current_h1:
                current_lines.append(line)
            out_lines.append(line)
    flush_chapter()

    body = "\n".join(out_lines)

    html = markdown.markdown(
        body,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
        output_format="html5",
    )

    # Headings: page h1 is in the header; parts/chapters become h2.
    def h1_repl(m: re.Match) -> str:
        hid, inner = m.group(1), m.group(2)
        if hid.startswith("part-"):
            return f'<h2 class="part-title" id="{hid}">{inner}</h2>'
        if hid == "prologue":
            return f'<h2 class="chapter-title" id="{hid}" data-no="PROLOGUE">{inner}</h2>'
        if hid.startswith("ch-"):
            no = hid.split("-")[1]
            return f'<h2 class="chapter-title" id="{hid}" data-no="{no}">{inner}</h2>'
        if hid.startswith("app-"):
            no = hid.split("-")[1].upper()
            return f'<h2 class="chapter-title" id="{hid}" data-no="APPENDIX {no}">{inner}</h2>'
        return f'<h2 class="chapter-title" id="{hid}">{inner}</h2>'

    html = re.sub(r'<h1 id="([^"]+)">(.*?)</h1>', h1_repl, html, flags=re.DOTALL)
    html = re.sub(r'<h2 id="([^"]+)">(.*?)</h2>', r'<h3 class="section-title-read" id="\1">\2</h3>', html, flags=re.DOTALL)
    html = re.sub(r'<h3 id="([^"]+)">(.*?)</h3>', r'<h4 id="\1">\2</h4>', html, flags=re.DOTALL)
    html = re.sub(r'<h4 id="([^"]+)">(.*?)</h4>', r'<h5 id="\1">\2</h5>', html, flags=re.DOTALL)

    # Blockquote callouts.
    def bq_repl(m: re.Match) -> str:
        inner = m.group(1)
        text = re.sub(r"<[^>]+>", "", inner)
        cls = ""
        if "赤ちゃんでもわかる一言" in text:
            cls = " callout--kid"
        elif "一歩深く" in text:
            cls = " callout--deep"
        elif "歴史の教訓" in text:
            cls = " callout--lesson"
        elif "注意" in text:
            cls = " callout--note"
        return f'<blockquote class="callout{cls}">{inner}</blockquote>'

    html = re.sub(r"<blockquote>(.*?)</blockquote>", bq_repl, html, flags=re.DOTALL)

    # Tables: horizontal scroll + accessible region.
    html = re.sub(
        r"<table>(.*?)</table>",
        lambda m: (
            '<div class="table-wrap" role="region" aria-label="表" tabindex="0">'
            f"<table>{m.group(1)}</table></div>"
            '<p class="table-hint">横にスクロールできます →</p>'
        ),
        html,
        flags=re.DOTALL,
    )
    html = html.replace("<th>", '<th scope="col">')

    # Chapter metadata and plate links.
    def chapter_meta_repl(m: re.Match) -> str:
        hid = m.group(1)
        block = m.group(0)
        if not (hid == "prologue" or hid.startswith("ch-")):
            return block
        chars = chapter_chars.get(hid, 0)
        minutes = max(1, round(chars / 500))
        meta = (
            f'<p class="ch-meta mono"><span>{chars:,} CHARACTERS</span>'
            f"<span>約 {minutes} 分</span></p>"
        )
        plate_html = ""
        if hid in PLATES:
            links = " ".join(
                f'<a href="atlas.html#{pid}">{label}</a>' for pid, label in PLATES[hid]
            )
            plate_html = (
                '<aside class="ch-plate">'
                '<span class="mono">PLATES IN THIS CHAPTER</span>'
                f"{links}</aside>"
            )
        return block + meta + plate_html

    html = re.sub(
        r'<h2 class="chapter-title" id="([^"]+)"[^>]*>.*?</h2>',
        chapter_meta_repl,
        html,
        flags=re.DOTALL,
    )

    # TOC.
    toc_rows = []
    mobile_rows = []
    for level, text, hid in heading_info:
        if level != 1:
            continue
        if hid.startswith("part-"):
            label = text
            toc_rows.append(f'<p class="read-toc__part">{label}</p>')
            mobile_rows.append(f'<p class="read-toc__part">{label}</p>')
            continue
        if hid not in SHORT:
            continue
        num, label = SHORT[hid]
        toc_rows.append(
            f'<a class="read-toc__link" href="#{hid}" data-toc-link>'
            f'<span>{num}</span>{label}</a>'
        )
        mobile_rows.append(
            f'<a class="read-toc__link" href="#{hid}">{label}</a>'
        )

    toc_html = "\n".join(toc_rows)
    mobile_toc_html = "\n".join(mobile_rows)
    total_minutes = max(1, round(total_chars / 500))

    page = f"""{head(TITLE, DESC)}
<body data-page="read">
<a class="skip" href="#main">本文へスキップ</a>
{rail("read")}
<div class="read-progress" data-progress aria-hidden="true"></div>

<main id="main" class="page">
  <div class="shell">
    <header class="read-head">
      <p class="eyebrow"><span class="eyebrow__no">FULL TEXT</span> THE CATALOGUE</p>
      <h1 class="read-title">デザイン全史</h1>
      <p class="read-sub">人類が「かたち」にこめた知恵の５万年</p>
      <p class="read-epigraph">{epigraph.replace(chr(10), '<br>')}</p>
      <div class="read-meta mono">
        <span>{total_chars:,} CHARACTERS</span>
        <span>15 CHAPTERS</span>
        <span>ABOUT {total_minutes} MIN</span>
        <span>3 ROUTES</span>
      </div>
      <div class="read-tools" aria-label="読書設定">
        <span class="read-tool read-tool--label">文字サイズ</span>
        <button class="read-tool" type="button" data-font-size="small" aria-pressed="false" aria-label="文字を小さくする">A−</button>
        <button class="read-tool" type="button" data-font-size="normal" aria-pressed="true" aria-label="文字サイズを標準に戻す">A</button>
        <button class="read-tool" type="button" data-font-size="large" aria-pressed="false" aria-label="文字を大きくする">A＋</button>
        <span class="read-tool read-tool--label" data-font-status aria-live="polite">標準</span>
        <a class="read-tool" href="デザイン全史.pdf" download>PDF</a>
      </div>
      <noscript><style>.read-tools button, .read-tool--label {{ display: none; }}</style></noscript>
    </header>

    <div class="read-layout">
      <aside class="read-toc" aria-label="目次">
        <div class="read-toc__title mono"><span>CONTENTS</span><span>15 CHAPTERS</span></div>
        {toc_html}
      </aside>

      <article class="read-main" data-read>
        <details class="read-toc-mobile">
          <summary>章一覧 / 15章</summary>
          <nav aria-label="モバイル目次">{mobile_toc_html}</nav>
        </details>
        {html}
        <section class="read-end">
          <p class="eyebrow"><span class="eyebrow__no">END</span> THE TEXT</p>
          <h2>本文は、ここまで。</h2>
          <p>次は、図版で考え、検証で疑い、年表でつなぐ。読んだあとに開くと、違うものが見えます。</p>
          <div class="read-end__links">
            <a class="btn btn--solid" href="atlas.html">図版室へ <span class="btn__arrow" aria-hidden="true">↗</span></a>
            <a class="btn" href="method.html">検証室へ <span class="btn__arrow" aria-hidden="true">↗</span></a>
            <a class="btn" href="timeline.html">年表へ <span class="btn__arrow" aria-hidden="true">↗</span></a>
          </div>
        </section>
      </article>
      <div aria-hidden="true"></div>
    </div>
  </div>
</main>

{footer("method.html", "THE EVIDENCE", "検証で、疑う。")}
<script src="assets/app.js" defer></script>
</body>
</html>
"""

    (BASE / "read.html").write_text(page, encoding="utf-8")
    print(f"wrote read.html: {len(page):,} chars, headings={len(heading_info)}")
    print("chapters:", len(chapter_chars), "total:", total_chars)


if __name__ == "__main__":
    main()
