# -*- coding: utf-8 -*-
"""Build atlas.html: thirteen annotated plates, drawn as inline SVG."""
from pathlib import Path

from build_read import head, rail, footer

BASE = Path(__file__).resolve().parent


def frame(pid: str, title: str, desc: str, art: str, tl: str, tr: str, bl: str, br: str, vb: str = "0 0 640 420") -> str:
    return f'''<svg class="plate" viewBox="{vb}" role="img" aria-labelledby="{pid}t {pid}d">
  <title id="{pid}t">{title}</title>
  <desc id="{pid}d">{desc}</desc>
  <g fill="none" stroke="var(--rule-strong)" stroke-width="0.7">
    <path d="M20 20 H46 M20 20 V46 M594 20 H620 M620 20 V46 M20 400 H46 M20 374 V400 M594 400 H620 M620 374 V400"/>
    <path d="M20 210 H26 M614 210 H620 M320 20 V26 M320 394 V400" opacity="0.55"/>
  </g>
  {art}
  <g font-family="IBM Plex Mono, monospace" font-size="9" fill="var(--ink-3)" letter-spacing="0.07em">
    <text x="40" y="44">{tl}</text>
    <text x="600" y="44" text-anchor="end">{tr}</text>
    <text x="40" y="396">{bl}</text>
    <text x="600" y="396" text-anchor="end">{br}</text>
  </g>
</svg>'''


def p01() -> str:
    art = '''
  <g fill="none" stroke="var(--ink)" stroke-width="1.6">
    <path d="M320 62 C356 108 405 170 411 212 C417 257 377 311 341 341 C331 351 324 360 320 368 C316 360 309 351 299 341 C263 311 223 257 229 212 C235 170 284 108 320 62 Z" fill="var(--paper-3)" fill-opacity="0.45"/>
  </g>
  <path d="M320 55 V375" stroke="var(--rule-strong)" stroke-width="0.8" stroke-dasharray="4 5"/>
  <g fill="none" stroke="var(--ink)" stroke-width="0.85" opacity="0.62">
    <path d="M320 98 C301 122 287 151 284 181"/>
    <path d="M320 132 C302 158 291 187 289 216"/>
    <path d="M320 166 C305 190 297 216 296 242"/>
    <path d="M320 200 C309 220 303 242 302 263"/>
    <path d="M320 234 C312 250 308 267 307 283"/>
    <path d="M320 98 C339 122 353 151 356 181"/>
    <path d="M320 132 C338 158 349 187 351 216"/>
    <path d="M320 166 C335 190 343 216 344 242"/>
    <path d="M320 200 C331 220 337 242 338 263"/>
    <path d="M320 234 C328 250 332 267 333 283"/>
  </g>
  <circle cx="320" cy="62" r="3.2" fill="var(--signal)"/>
  <g fill="none" stroke="var(--rule-strong)" stroke-width="0.7">
    <path d="M66 116 H274"/>
    <path d="M66 306 H264"/>
    <path d="M500 116 H372"/>
    <path d="M500 306 H380"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="9" fill="var(--ink-3)" letter-spacing="0.07em">
    <text x="40" y="108">SYMMETRY</text>
    <text x="40" y="322">FLAKE SCARS</text>
    <text x="508" y="108">CUT / DIG</text>
    <text x="508" y="322">GRIP</text>
  </g>
  <g fill="none" stroke="var(--ink)" stroke-width="0.8">
    <path d="M60 380 H120 M60 374 V386 M120 374 V386"/>
  </g>
  <text x="126" y="384" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">10 CM</text>
'''
    return frame("p01", "握斧 — 最初のデザイン", "左右対称の握斧。切る、掘る、叩くための機能と、見せるための形が、まだ分かれていない。", art, "PL. 01 / HANDAXE", "1.7M BCE", "FORM + FUNCTION", "ACHEULEAN")


def p02() -> str:
    art = '''
  <g>
    <path d="M235 96 C225 132 218 178 222 224 C226 284 260 330 300 338 C340 330 374 284 378 224 C382 178 375 132 365 96 Z" fill="var(--yellow)" fill-opacity="0.10" stroke="var(--ink)" stroke-width="1.5"/>
    <path d="M235 96 C255 88 345 88 365 96 C345 104 255 104 235 96 Z" fill="var(--paper-2)" stroke="var(--ink)" stroke-width="1.2"/>
    <g fill="none" stroke="var(--ink)" stroke-width="0.8" opacity="0.65">
      <path d="M232 128 C260 120 340 120 369 128"/>
      <path d="M229 158 C260 150 340 150 371 158"/>
      <path d="M226 190 C258 182 342 182 374 190"/>
      <path d="M226 222 C258 214 342 214 374 222"/>
      <path d="M230 254 C260 246 340 246 370 254"/>
      <path d="M238 286 C264 278 336 278 362 286"/>
    </g>
    <g stroke="var(--ink)" stroke-width="0.7" opacity="0.5">
      <path d="M248 138 l8 14 M268 136 l8 14 M288 135 l8 14 M308 135 l8 14 M328 136 l8 14 M348 138 l8 14"/>
      <path d="M246 202 l8 14 M266 200 l8 14 M286 199 l8 14 M306 199 l8 14 M326 200 l8 14 M346 202 l8 14"/>
      <path d="M250 266 l8 14 M270 264 l8 14 M290 263 l8 14 M310 263 l8 14 M330 264 l8 14 M350 266 l8 14"/>
    </g>
    <path d="M300 338 L300 354 M278 350 H322" stroke="var(--ink)" stroke-width="1"/>
    <g fill="none" stroke="var(--signal)" stroke-width="1.4">
      <path d="M92 352 C88 338 96 326 104 318 C106 332 112 342 104 352 Z"/>
      <path d="M116 352 C112 336 122 322 132 314 C134 330 140 342 132 352 Z"/>
      <path d="M140 352 C136 340 144 328 152 320 C154 334 160 344 152 352 Z"/>
    </g>
    <text x="84" y="368" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">OPEN FIRE 600–900°C</text>
    <g fill="none" stroke="var(--rule-strong)" stroke-width="0.8">
      <path d="M470 110 H520 V322 H470"/>
      <path d="M470 110 L520 322 M470 140 L520 352 M470 80 L520 292" opacity="0.5"/>
    </g>
    <text x="540" y="214" font-family="IBM Plex Mono, monospace" font-size="9" fill="var(--ink-3)">WALL</text>
    <text x="540" y="228" font-family="IBM Plex Mono, monospace" font-size="9" fill="var(--ink-3)">8 MM</text>
    <g fill="none" stroke="var(--rule-strong)" stroke-width="0.7">
      <path d="M365 96 H430 V72"/>
      <path d="M300 338 H430 V360"/>
    </g>
    <text x="436" y="68" font-family="IBM Plex Mono, monospace" font-size="9" fill="var(--ink-3)">RIM</text>
    <text x="436" y="364" font-family="IBM Plex Mono, monospace" font-size="9" fill="var(--ink-3)">BASE</text>
  </g>
'''
    return frame("p02", "土器 — 最初の容器", "粘土を成形し、火で焼く。土器は、人間が化学変化で作った最初の素材の一つ。縄目は装飾か、機能か。", art, "PL. 02 / JOMON POT", "20,000 BCE", "MATERIAL + MEMORY", "CORD MARK")


def p03() -> str:
    wedges = []
    for r in range(6):
        for c in range(8):
            if (r * 3 + c * 5) % 7 == 0:
                continue
            x = 150 + c * 44
            y = 108 + r * 33
            if (r + c) % 3 == 0:
                wedges.append(f'<path d="M{x} {y} l-4 14 l8 0 z" fill="var(--ink)" opacity="0.85"/>')
            else:
                wedges.append(f'<path d="M{x} {y} l15 4 l-15 4 z" fill="var(--ink)" opacity="0.85"/>')
    wedge_html = "\n      ".join(wedges)
    art = f'''
  <rect x="120" y="72" width="400" height="250" rx="10" fill="var(--paper-2)" stroke="var(--ink)" stroke-width="1.4"/>
  <g stroke="var(--rule)" stroke-width="0.6">
    <path d="M132 100 H508 M132 133 H508 M132 166 H508 M132 199 H508 M132 232 H508 M132 265 H508 M132 298 H508"/>
    <path d="M190 84 V310 M260 84 V310 M330 84 V310 M400 84 V310 M470 84 V310"/>
  </g>
  <g>
      {wedge_html}
  </g>
  <path d="M340 175 l15 4 l-15 4 z" fill="var(--signal)"/>
  <g fill="none" stroke="var(--ink)" stroke-width="1.2">
    <circle cx="92" cy="352" r="10"/>
    <path d="M120 342 L136 362 L120 362 Z"/>
    <path d="M154 342 C166 342 170 352 166 360 C162 368 150 368 146 360 C143 353 147 344 154 342 Z"/>
  </g>
  <g fill="none" stroke="var(--signal)" stroke-width="1.3">
    <path d="M178 352 H226"/>
    <path d="M218 346 L226 352 L218 358"/>
  </g>
  <text x="78" y="380" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">TOKENS → SIGNS</text>
  <g fill="none" stroke="var(--rule-strong)" stroke-width="0.7">
    <path d="M508 140 H548"/>
    <path d="M508 260 H548"/>
  </g>
  <text x="552" y="144" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">ACCOUNTING</text>
  <text x="552" y="264" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">LAW / MYTH</text>
'''
    return frame("p03", "楔形文字 — 数えることから書くことへ", "羊や穀物の数を表すトークンが、粘土板の印になり、楔形文字になる。会計が、文学の母になった。", art, "PL. 03 / CUNEIFORM", "3,200 BCE", "TOKEN → TABLET → TEXT", "SUMER")


def p04() -> str:
    star = "M320 60 L353.7 128.7 L426.1 103.9 L401.3 176.3 L470 210 L401.3 243.7 L426.1 316.1 L353.7 291.3 L320 360 L286.3 291.3 L213.9 316.1 L238.7 243.7 L170 210 L238.7 176.3 L213.9 103.9 L286.3 128.7 Z"
    octagon = "M320 60 L426.1 103.9 L470 210 L426.1 316.1 L320 360 L213.9 316.1 L170 210 L213.9 103.9 Z"
    diamonds = []
    pts = [(320, 60), (426.1, 103.9), (470, 210), (426.1, 316.1), (320, 360), (213.9, 316.1), (170, 210), (213.9, 103.9)]
    for i in range(8):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % 8]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        diamonds.append(f'<path d="M{mx:.1f} {my-14:.1f} L{mx+14:.1f} {my:.1f} L{mx:.1f} {my+14:.1f} L{mx-14:.1f} {my:.1f} Z"/>')
    diamond_html = "\n      ".join(diamonds)
    art = f'''
  <g fill="none" stroke="var(--rule-strong)" stroke-width="0.7">
    <circle cx="320" cy="210" r="158" stroke-dasharray="3 6"/>
    <rect x="170" y="60" width="300" height="300" stroke-dasharray="3 6"/>
    <rect x="170" y="60" width="300" height="300" transform="rotate(45 320 210)" stroke-dasharray="3 6"/>
    <path d="M320 40 V380 M140 210 H500" stroke-dasharray="2 5"/>
  </g>
  <path d="{star}" fill="var(--paper-2)" stroke="var(--ultra)" stroke-width="1.7"/>
  <g fill="var(--ultra)" fill-opacity="0.10" stroke="var(--ultra)" stroke-width="0.8">
      {diamond_html}
  </g>
  <path d="{octagon}" fill="none" stroke="var(--ink)" stroke-width="0.9"/>
  <circle cx="320" cy="210" r="62" fill="var(--yellow)" fill-opacity="0.24" stroke="var(--ink)" stroke-width="0.8"/>
  <circle cx="320" cy="210" r="37" fill="none" stroke="var(--ultra)" stroke-width="0.8" stroke-dasharray="2 4"/>
  <circle cx="320" cy="210" r="4" fill="var(--signal)"/>
  <g fill="none" stroke="var(--ink)" stroke-width="0.7">
    <circle cx="92" cy="340" r="16"/>
    <path d="M92 324 V300 M92 356 V376"/>
    <path d="M76 340 H108"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)" letter-spacing="0.06em">
    <text x="120" y="330">COMPASS</text>
    <text x="120" y="342">&amp; STRAIGHTEDGE</text>
    <text x="520" y="340">ONE TILE</text>
    <text x="520" y="352">8-FOLD</text>
  </g>
'''
    return frame("p04", "イスラームの幾何学 — 無限を描く", "円と定規から、八回対称の星が生まれる。数学であり、祈りであり、職人の技術である。", art, "PL. 04 / GIRIH", "1200–", "INFINITY / PATTERN", "ISLAMIC WORLD")


def p05() -> str:
    art = '''
  <g fill="none" stroke="var(--ink)" stroke-width="1.4">
    <path d="M200 142 C216 88 424 88 440 142"/>
    <path d="M216 148 C231 104 409 104 424 148"/>
    <path d="M300 120 C306 154 306 216 300 256 L340 256 C334 216 334 154 340 120 Z" fill="var(--yellow)" fill-opacity="0.10"/>
    <path d="M220 272 L420 272 L400 302 L240 302 Z" fill="var(--yellow)" fill-opacity="0.08"/>
    <path d="M250 302 L240 386 M390 302 L400 386 M265 302 L260 376 M375 302 L380 376"/>
    <path d="M244 346 H396 M258 336 H382"/>
    <path d="M200 142 C205 182 220 222 240 252 M440 142 C435 182 420 222 400 252"/>
    <path d="M240 302 L250 302 M400 302 L390 302"/>
  </g>
  <g fill="none" stroke="var(--ink)" stroke-width="0.6" opacity="0.45">
    <path d="M235 280 C280 275 340 275 405 280"/>
    <path d="M312 128 C317 165 317 210 312 248"/>
    <path d="M322 128 C327 165 327 210 322 248"/>
  </g>
  <g fill="none" stroke="var(--rule-strong)" stroke-width="0.8">
    <circle cx="500" cy="310" r="58"/>
    <path d="M420 296 L450 300"/>
  </g>
  <g fill="none" stroke="var(--ink)" stroke-width="1.1">
    <rect x="470" y="284" width="22" height="52" fill="var(--paper-2)"/>
    <rect x="492" y="296" width="36" height="28" fill="var(--paper-2)"/>
    <path d="M470 296 H492 M470 310 H492 M470 324 H492"/>
    <path d="M480 290 V330 M488 290 V330" stroke-width="0.6"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)" letter-spacing="0.05em">
    <text x="452" y="384">MORTISE &amp; TENON</text>
    <text x="40" y="100">HUANGHUALI</text>
    <text x="500" y="100">NO NAILS</text>
  </g>
'''
    return frame("p05", "明式家具 — 木のミニマリズム", "黄花梨の椅子。釘を使わず、ほぞと仕口で組む。曲線は装飾ではなく、身体と構造の応答である。", art, "PL. 05 / MING CHAIR", "1600", "JOINERY / STRUCTURE", "CHINA")


def p06() -> str:
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
    sorts = []
    for i, ch in enumerate(letters):
        col = i % 5
        row = i // 5
        x = 52 + col * 27
        y = 100 + row * 38
        fill = "var(--ink)" if i in (0, 6, 12, 18) else "var(--paper-2)"
        color = "var(--paper-2)" if fill == "var(--ink)" else "var(--ink)"
        sorts.append(
            f'<rect x="{x}" y="{y}" width="22" height="30" fill="{fill}" stroke="var(--ink)" stroke-width="0.8"/>'
            f'<text x="{x+11}" y="{y+21}" text-anchor="middle" font-family="Archivo, sans-serif" font-size="13" font-weight="700" fill="{color}">{ch}</text>'
        )
    sorts_html = "\n      ".join(sorts)
    art = f'''
  <g>
    <rect x="40" y="82" width="158" height="252" fill="var(--paper-2)" stroke="var(--rule-strong)" stroke-width="0.8"/>
    <g>
      {sorts_html}
    </g>
    <text x="40" y="356" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">SORTS / TYPE CASE</text>
  </g>
  <g>
    <rect x="232" y="100" width="150" height="170" fill="var(--paper-2)" stroke="var(--rule-strong)" stroke-width="0.8"/>
    <g transform="translate(614,0) scale(-1,1)">
      <text x="240" y="205" font-family="Archivo, sans-serif" font-size="34" font-weight="800" fill="var(--signal)">DESIGN</text>
    </g>
    <text x="232" y="356" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">FORME / REVERSED</text>
  </g>
  <g>
    <rect x="420" y="100" width="160" height="170" fill="var(--paper-2)" stroke="var(--rule-strong)" stroke-width="0.8"/>
    <text x="430" y="150" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">IMPRESSION</text>
    <text x="430" y="205" font-family="Archivo, sans-serif" font-size="34" font-weight="800" fill="var(--ultra)">DESIGN</text>
    <path d="M430 220 H560 M430 230 H520" stroke="var(--rule-strong)" stroke-width="1"/>
    <text x="420" y="356" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">PRINTED SHEET</text>
  </g>
  <g fill="none" stroke="var(--signal)" stroke-width="1.3">
    <path d="M198 185 H228 M220 179 L228 185 L220 191"/>
    <path d="M386 185 H416 M408 179 L416 185 L408 191"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)" letter-spacing="0.05em">
    <text x="520" y="72">MIRROR / REVERSE</text>
  </g>
'''
    return frame("p06", "活版印刷 — 複製のシステム", "活字を組み、版面を作り、紙に押す。印刷は、知識を複製し、標準化し、公共圏を作った。", art, "PL. 06 / MOVABLE TYPE", "1455", "REPRODUCTION", "EUROPE")


def p07() -> str:
    art = '''
  <g stroke="var(--rule)" stroke-width="0.55" opacity="0.55">
    <path d="M40 90 H600 M40 140 H600 M40 190 H600 M40 240 H600 M40 290 H600 M40 340 H600"/>
    <path d="M80 60 V370 M160 60 V370 M240 60 V370 M320 60 V370 M400 60 V370 M480 60 V370 M560 60 V370"/>
  </g>
  <circle cx="240" cy="210" r="105" fill="var(--bauhaus-yellow)" fill-opacity="0.90"/>
  <rect x="325" y="105" width="175" height="175" fill="var(--bauhaus-blue)" fill-opacity="0.86" transform="rotate(12 412 192)"/>
  <path d="M300 340 L398 160 L496 340 Z" fill="var(--bauhaus-red)" fill-opacity="0.88"/>
  <g fill="none" stroke="var(--ink)" stroke-width="1.5">
    <circle cx="240" cy="210" r="105"/>
    <rect x="325" y="105" width="175" height="175" transform="rotate(12 412 192)"/>
    <path d="M300 340 L398 160 L496 340 Z"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="9" fill="var(--ink-3)" letter-spacing="0.08em">
    <text x="40" y="72">VORKURS / FORM + COLOUR</text>
    <text x="40" y="386">CIRCLE · SQUARE · TRIANGLE</text>
    <text x="600" y="386" text-anchor="end">BAUHAUS</text>
  </g>
'''
    return frame("p07", "バウハウス — 造形の文法", "円、四角、三角。色彩と形態を、感覚から体系へ。バウハウスの基礎課程は、デザイン教育の原型になった。", art, "PL. 07 / BAUHAUS", "1919–1933", "FORM + COLOUR", "WEIMAR / DESSAU")


def p08() -> str:
    cols = []
    for i in range(1, 12):
        x = 70 + i * (500 / 12)
        cols.append(f'<path d="M{x:.1f} 60 V360"/>')
    baselines = []
    for y in range(80, 361, 20):
        baselines.append(f'<path d="M70 {y} H570"/>')
    art = f'''
  <rect x="70" y="60" width="500" height="300" fill="var(--paper-2)" stroke="var(--ink)" stroke-width="1.2"/>
  <g fill="none" stroke="var(--ultra)" stroke-width="0.55" opacity="0.20">
    {''.join(cols)}
  </g>
  <g fill="none" stroke="var(--rule-strong)" stroke-width="0.4" opacity="0.45">
    {''.join(baselines)}
  </g>
  <text x="90" y="250" font-family="Archivo, sans-serif" font-size="150" font-weight="800" fill="var(--ink)" letter-spacing="-0.06em">Aa</text>
  <text x="555" y="120" text-anchor="end" font-family="Archivo, sans-serif" font-size="48" font-weight="800" fill="var(--ultra)">1957</text>
  <g fill="var(--ink-3)" opacity="0.32">
    <rect x="335" y="150" width="130" height="8"/>
    <rect x="335" y="166" width="180" height="8"/>
    <rect x="335" y="182" width="150" height="8"/>
    <rect x="335" y="198" width="200" height="8"/>
    <rect x="335" y="214" width="120" height="8"/>
  </g>
  <rect x="335" y="250" width="80" height="80" fill="none" stroke="var(--ink)" stroke-width="0.8"/>
  <circle cx="375" cy="290" r="24" fill="none" stroke="var(--signal)" stroke-width="2"/>
  <circle cx="545" cy="332" r="4" fill="var(--signal)"/>
  <g font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)" letter-spacing="0.05em">
    <text x="40" y="386">ORDER IS NOT NEUTRAL</text>
    <text x="600" y="386" text-anchor="end">HELVETICA / 1957</text>
  </g>
'''
    return frame("p08", "グリッド — 秩序の骨格", "スイス・スタイルは、グリッドで情報を整理した。秩序は自由を減らすのではなく、判断の数を減らす。", art, "PL. 08 / GRID", "1957", "INFORMATION / ORDER", "SWITZERLAND")


def p09() -> str:
    art = '''
  <g fill="none" stroke="var(--rule-strong)" stroke-width="0.55" opacity="0.5">
    <path d="M80 80 V340 M160 80 V340 M240 80 V340 M320 80 V340 M400 80 V340 M480 80 V340 M560 80 V340" stroke-dasharray="2 6"/>
  </g>
  <g fill="none" stroke="var(--cyan)" stroke-width="1.1">
    <path d="M30 160 H170 M20 182 H130 M30 204 H110 M40 226 H90"/>
  </g>
  <path d="M50 280 C90 220 170 195 310 195 C430 195 530 215 590 255 L590 290 L50 290 Z" fill="var(--paper-3)" fill-opacity="0.55" stroke="var(--ink)" stroke-width="1.6"/>
  <path d="M60 280 C100 232 180 208 310 208 C420 208 510 224 570 254" fill="none" stroke="var(--ultra)" stroke-width="2"/>
  <g fill="none" stroke="var(--ink)" stroke-width="1.2">
    <path d="M330 218 H410 V250 H330 Z"/>
    <path d="M430 222 H500 V250 H430 Z"/>
    <circle cx="180" cy="290" r="28"/>
    <circle cx="180" cy="290" r="12"/>
    <circle cx="470" cy="290" r="28"/>
    <circle cx="470" cy="290" r="12"/>
  </g>
  <g fill="none" stroke="var(--signal)" stroke-width="1.4">
    <path d="M50 280 H590" stroke-dasharray="1 5"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="9" fill="var(--ink-3)" letter-spacing="0.07em">
    <text x="600" y="72" text-anchor="end">Cd = ?</text>
    <text x="40" y="386">SPEED OR DESIRE?</text>
    <text x="600" y="386" text-anchor="end">AIR RESISTANCE</text>
  </g>
  <g fill="none" stroke="var(--ink)" stroke-width="0.8">
    <path d="M520 150 H580 M572 144 L580 150 L572 156"/>
  </g>
  <text x="520" y="140" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">100 KM/H</text>
'''
    return frame("p09", "流線型 — 速度の記号", "空気抵抗の合理性と、未来への欲望。流線型は、冷蔵庫にまで速度をまとわせた。", art, "PL. 09 / STREAMLINE", "1930s", "SPEED / DESIRE", "USA")


def p10() -> str:
    art = '''
  <g fill="none" stroke="var(--ink)" stroke-width="1.4">
    <rect x="70" y="80" width="300" height="280"/>
    <path d="M70 173 H370 M70 266 H370 M170 80 V360 M270 80 V360"/>
  </g>
  <g fill="none" stroke="var(--ink)" stroke-width="1.1">
    <rect x="90" y="108" width="60" height="48"/>
    <path d="M90 122 H150"/>
    <rect x="190" y="104" width="12" height="58"/>
    <rect x="207" y="110" width="12" height="52"/>
    <rect x="224" y="100" width="12" height="62"/>
    <path d="M285 112 H335 V150 H285 Z M285 118 H335"/>
    <path d="M100 240 H130 V270 H100 Z M100 246 C108 240 122 240 130 246"/>
    <path d="M112 240 C112 226 106 218 100 214 M112 240 C112 226 118 218 124 214 M112 240 C116 228 126 224 132 226"/>
    <path d="M190 250 H250 M190 260 H250 M190 270 H240"/>
  </g>
  <g fill="none" stroke="var(--rule-strong)" stroke-width="1" stroke-dasharray="4 4">
    <rect x="285" y="230" width="65" height="70"/>
  </g>
  <text x="302" y="270" font-family="Shippori Mincho B1, serif" font-size="18" fill="var(--ink-3)">空</text>
  <g fill="none" stroke="var(--ink)" stroke-width="1.2">
    <rect x="450" y="105" width="120" height="120" fill="var(--paper-2)"/>
    <circle cx="510" cy="165" r="34"/>
    <circle cx="510" cy="165" r="8"/>
    <path d="M510 225 V300"/>
    <path d="M500 300 H520"/>
  </g>
  <circle cx="560" cy="115" r="3" fill="var(--signal)"/>
  <g fill="none" stroke="var(--rule-strong)" stroke-width="0.7">
    <path d="M370 150 H450"/>
    <path d="M440 144 L450 150 L440 156"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="9" fill="var(--ink-3)" letter-spacing="0.06em">
    <text x="600" y="72" text-anchor="end">CD PLAYER / 1999</text>
    <text x="40" y="386">EMPTY = MA</text>
    <text x="600" y="386" text-anchor="end">LESS, BUT BETTER?</text>
  </g>
'''
    return frame("p10", "無印良品 — 引き算のデザイン", "素材、機能、価格。余分なブランドを削ぎ、空いた余白に意味を置く。だが「引き算」もまた、一つの主張である。", art, "PL. 10 / MUJI", "1980–", "RESTRAINT / MA", "JAPAN")


def p11() -> str:
    nodes = [
        (320, 80, "DESIGN"),
        (430, 140, "MAKE"),
        (430, 260, "USE"),
        (320, 320, "REPAIR"),
        (210, 260, "REMAKE"),
        (210, 140, "RECYCLE"),
    ]
    node_html = []
    for x, y, label in nodes:
        node_html.append(f'<circle cx="{x}" cy="{y}" r="18" fill="var(--paper-2)" stroke="var(--ink)" stroke-width="1.2"/>')
        node_html.append(f'<text x="{x}" y="{y+4}" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="7" fill="var(--ink-3)">{label}</text>')
    art = f'''
  <g fill="none" stroke="var(--ultra)" stroke-width="1.4">
    <path d="M320 98 A112 112 0 0 1 422 156"/>
    <path d="M438 176 A112 112 0 0 1 438 224"/>
    <path d="M422 244 A112 112 0 0 1 320 302"/>
    <path d="M320 302 A112 112 0 0 1 218 244"/>
    <path d="M202 224 A112 112 0 0 1 202 156"/>
    <path d="M218 136 A112 112 0 0 1 320 98"/>
  </g>
  <g fill="var(--signal)" stroke="none">
    <path d="M416 150 L426 160 L412 162 Z"/>
    <path d="M440 218 L430 230 L442 236 Z"/>
    <path d="M326 302 L314 310 L322 318 Z"/>
    <path d="M214 238 L204 226 L216 220 Z"/>
    <path d="M200 162 L212 150 L202 144 Z"/>
    <path d="M314 98 L326 106 L316 112 Z"/>
  </g>
  {''.join(node_html)}
  <g fill="none" stroke="var(--green)" stroke-width="1.5">
    <path d="M320 160 C348 160 364 182 364 204 C364 228 344 242 320 242 C296 242 276 228 276 204 C276 182 292 160 320 160 Z"/>
    <path d="M320 242 C320 218 320 196 320 172"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)" letter-spacing="0.05em">
    <text x="40" y="72">CIRCULAR / 3 PRINCIPLES</text>
    <text x="40" y="386">WASTE = DESIGN ERROR</text>
    <text x="600" y="386" text-anchor="end">ELLEN MACARTHUR FDN.</text>
  </g>
  <g fill="none" stroke="var(--signal)" stroke-width="1.2">
    <path d="M70 360 H280"/>
    <path d="M92 352 L70 360 L92 368"/>
    <path d="M290 350 L310 370 M310 350 L290 370"/>
  </g>
  <text x="70" y="346" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">TAKE → MAKE → WASTE</text>
'''
    return frame("p11", "サーキュラー — 廃棄物は設計の失敗", "まず出さない。長く使う。直す。再製造する。リサイクルは最後の手段。循環は、素材ではなく関係の問題である。", art, "PL. 11 / CIRCULAR", "2024", "CIRCULATE / REGENERATE", "GLOBAL")


def p12() -> str:
    layers = [
        (190, [140, 190, 240, 290]),
        (270, [115, 160, 205, 250, 295]),
        (350, [140, 190, 240, 290]),
        (430, [160, 220, 280]),
    ]
    lines = []
    for i in range(len(layers) - 1):
        x1, ys1 = layers[i]
        x2, ys2 = layers[i + 1]
        for y1 in ys1:
            for y2 in ys2:
                lines.append(f'<path d="M{x1+9} {y1} L{x2-9} {y2}"/>')
    line_html = "\n    ".join(lines)
    nodes = []
    for x, ys in layers:
        for y in ys:
            nodes.append(f'<circle cx="{x}" cy="{y}" r="7" fill="var(--paper-2)" stroke="var(--ultra)" stroke-width="1"/>')
    node_html = "\n    ".join(nodes)
    art = f'''
  <g fill="none" stroke="var(--ultra)" stroke-width="0.45" opacity="0.55">
    {line_html}
  </g>
  {node_html}
  <g fill="none" stroke="var(--ink)" stroke-width="1.2">
    <rect x="40" y="170" width="100" height="80" fill="var(--paper-2)"/>
    <path d="M40 190 H140 M40 210 H140 M40 230 H140" stroke-width="0.6"/>
  </g>
  <text x="52" y="160" font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)">PROMPT</text>
  <g fill="none" stroke="var(--rule-strong)" stroke-width="0.8">
    <path d="M140 210 H176"/>
    <path d="M168 204 L176 210 L168 216"/>
    <path d="M446 210 H486"/>
    <path d="M478 204 L486 210 L478 216"/>
  </g>
  <g fill="none" stroke="var(--ink)" stroke-width="1.1">
    <rect x="486" y="120" width="56" height="56" fill="var(--paper-2)"/>
    <rect x="550" y="120" width="56" height="56" fill="var(--paper-2)"/>
    <rect x="486" y="184" width="56" height="56" fill="var(--paper-2)"/>
    <rect x="550" y="184" width="56" height="56" fill="var(--paper-2)"/>
    <circle cx="514" cy="148" r="14"/>
    <rect x="576" y="134" width="28" height="28"/>
    <path d="M572 212 L590 184 L608 212 Z" fill="var(--yellow)" fill-opacity="0.7"/>
    <path d="M500 222 C510 206 522 206 532 222" stroke="var(--signal)" stroke-width="1.4"/>
  </g>
  <g fill="none" stroke="var(--signal)" stroke-width="1.2" stroke-dasharray="4 4">
    <circle cx="320" cy="366" r="26"/>
    <path d="M346 366 C400 366 470 340 470 300"/>
    <path d="M300 366 C220 366 160 330 140 250"/>
  </g>
  <text x="320" y="370" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="7" fill="var(--signal)">HUMAN</text>
  <text x="320" y="378" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="7" fill="var(--signal)">JUDGEMENT</text>
  <g font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)" letter-spacing="0.05em">
    <text x="40" y="72">GENERATION / JUDGEMENT</text>
    <text x="40" y="386">WHO DECIDES?</text>
    <text x="600" y="386" text-anchor="end">RESPONSIBILITY</text>
  </g>
'''
    return frame("p12", "AI — 生成のあとに残るもの", "プロンプト、モデル、出力。生成は自動化できる。だが、何を良しとするか、誰が責任を負うかは、まだ人間の仕事である。", art, "PL. 12 / AI", "2022–", "GENERATE / JUDGE", "GLOBAL")


def p13() -> str:
    art = '''
  <path d="M420 92 C370 48 250 48 190 104 C120 168 126 292 196 346 C266 400 386 392 432 322 C456 286 456 248 438 220" fill="none" stroke="var(--ink)" stroke-width="1.8"/>
  <path d="M420 92 C414 86 408 80 400 74" fill="none" stroke="var(--paper)" stroke-width="5"/>
  <g>
    <path d="M240 168 C232 200 230 244 246 278 C262 312 356 318 382 284 C400 260 400 210 392 168 Z" fill="var(--paper-2)" stroke="var(--ink)" stroke-width="1.5"/>
    <path d="M240 168 C260 160 374 160 394 168 C374 176 260 176 240 168 Z" fill="var(--paper-3)" stroke="var(--ink)" stroke-width="1.1"/>
    <path d="M286 300 C290 310 310 314 320 314 C330 314 350 310 354 300" fill="none" stroke="var(--ink)" stroke-width="1"/>
    <path d="M270 178 C264 206 262 242 274 270 C286 296 354 300 370 274 C382 246 380 208 374 178" fill="none" stroke="var(--ink)" stroke-width="0.6" opacity="0.4"/>
    <path d="M258 188 L278 206 L266 228 L292 244 L282 266 L310 282" fill="none" stroke="var(--yellow)" stroke-width="3"/>
    <path d="M278 206 L300 196 M292 244 L314 238 M282 266 L266 280" fill="none" stroke="var(--yellow)" stroke-width="1.8"/>
    <path d="M250 292 C270 302 290 306 310 306 C330 306 350 302 370 292" fill="none" stroke="var(--ink)" stroke-width="1.2"/>
  </g>
  <g fill="none" stroke="var(--rule-strong)" stroke-width="0.8">
    <rect x="480" y="270" width="70" height="70"/>
    <circle cx="515" cy="305" r="16"/>
    <circle cx="515" cy="305" r="2.5" fill="var(--signal)" stroke="none"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="8" fill="var(--ink-3)" letter-spacing="0.05em">
    <text x="484" y="262">MA / 間</text>
    <text x="40" y="72">WABI-SABI IS NOT ALL OF JAPAN</text>
    <text x="40" y="386">KINTSUGI / REPAIR</text>
    <text x="600" y="386" text-anchor="end">THE BOWL IS A BODY</text>
  </g>
'''
    return frame("p13", "茶碗 — 侘寂は、日本全体ではない", "歪み、厚み、景色。茶の湯が磨いた美学は、日本文化の一部であって全体ではない。金継ぎは、欠けを消さずに残す。", art, "PL. 13 / TEA BOWL", "16TH C.", "WABI-SABI / REPAIR", "JAPAN")


PLATES = [
    {
        "id": "plate-01", "no": "PL. 01", "title": "握斧 — 最初のデザイン", "svg": p01,
        "tags": "form material", "span": "pc-7",
        "desc": "<p>左右対称の握斧。切る、掘る、叩くための機能と、見せるための形が、まだ分かれていない。</p><dl><div><dt>見る</dt><dd>左右の対称軸、刃先の摩耗、手に収まる厚み。</dd></div><div><dt>問う</dt><dd>機能と美は、いつ分かれたのか。そもそも分かれているのか。</dd></div><div><dt>出典</dt><dd>本書 第2章 / 対象: アシューリアン握斧（大英博物館ほか）</dd></div></dl>",
    },
    {
        "id": "plate-02", "no": "PL. 02", "title": "土器 — 最初の容器", "svg": p02,
        "tags": "material form", "span": "pc-5",
        "desc": "<p>粘土を成形し、火で焼く。土器は、人間が化学変化で作った最初の素材の一つ。縄目は装飾か、機能か。</p><dl><div><dt>見る</dt><dd>口縁の広がり、器壁の厚み、縄目のリズム、焼成の色むら。</dd></div><div><dt>問う</dt><dd>容器は、何を「持ち運ぶ」ことを可能にしたのか。記憶か、食べ物か。</dd></div><div><dt>出典</dt><dd>本書 第2章・第10章 / 対象: 縄文土器（十日町市博物館ほか）</dd></div></dl>",
    },
    {
        "id": "plate-03", "no": "PL. 03", "title": "楔形文字 — 数えることから書くことへ", "svg": p03,
        "tags": "meaning system", "span": "pc-5",
        "desc": "<p>羊や穀物の数を表すトークンが、粘土板の印になり、楔形文字になる。会計が、文学の母になった。</p><dl><div><dt>見る</dt><dd>くさび形の筆致、格子状の ruled lines、トークンからの矢印。</dd></div><div><dt>問う</dt><dd>文字は、誰の記憶を保存し、誰の記憶を消したのか。</dd></div><div><dt>出典</dt><dd>本書 第2章 / 対象: メソポタミアの粘土板（大英博物館ほか）</dd></div></dl>",
    },
    {
        "id": "plate-04", "no": "PL. 04", "title": "イスラームの幾何学 — 無限を描く", "svg": p04,
        "tags": "meaning form system", "span": "pc-7",
        "desc": "<p>円と定規から、八回対称の星が生まれる。数学であり、祈りであり、職人の技術である。</p><dl><div><dt>見る</dt><dd>八回対称の星、外接する八角形、中心のロゼット、作図の円。</dd></div><div><dt>問う</dt><dd>「無限」を、有限のタイルでどう表すか。装飾は、情報か。</dd></div><div><dt>出典</dt><dd>本書 第3章 / 対象: ギリーフ・タイル（イスファハン、アルハンブラほか）</dd></div></dl>",
    },
    {
        "id": "plate-05", "no": "PL. 05", "title": "明式家具 — 木のミニマリズム", "svg": p05,
        "tags": "material form power", "span": "pc-6",
        "desc": "<p>黄花梨の椅子。釘を使わず、ほぞと仕口で組む。曲線は装飾ではなく、身体と構造の応答である。</p><dl><div><dt>見る</dt><dd>背もたれのカーブ、座面の比例、脚の踏み込み、継ぎ手の精度。</dd></div><div><dt>問う</dt><dd>「簡素」は、誰の趣味か。文人の教養と、職人の労働の関係は。</dd></div><div><dt>出典</dt><dd>本書 第3章 / 対象: 明式黄花梨椅子（メトロポリタン美術館ほか）</dd></div></dl>",
    },
    {
        "id": "plate-06", "no": "PL. 06", "title": "活版印刷 — 複製のシステム", "svg": p06,
        "tags": "system meaning", "span": "pc-6",
        "desc": "<p>活字を組み、版面を作り、紙に押す。印刷は、知識を複製し、標準化し、公共圏を作った。</p><dl><div><dt>見る</dt><dd>活字ケース、鏡像の版面、印刷されたページ。左から右への変換。</dd></div><div><dt>問う</dt><dd>複製は、知識を民主化したのか。それとも、新しい管理を生んだのか。</dd></div><div><dt>出典</dt><dd>本書 第4章 / 対象: グーテンベルク42行聖書（各地）</dd></div></dl>",
    },
    {
        "id": "plate-07", "no": "PL. 07", "title": "バウハウス — 造形の文法", "svg": p07,
        "tags": "form meaning power", "span": "pc-8",
        "desc": "<p>円、四角、三角。色彩と形態を、感覚から体系へ。バウハウスの基礎課程は、デザイン教育の原型になった。</p><dl><div><dt>見る</dt><dd>三つの形、三つの色、12度傾いた四角、重なりの新しい色。</dd></div><div><dt>問う</dt><dd>「普遍の造形」は、誰の身体を標準にしたのか。学校は、なぜ政治化したのか。</dd></div><div><dt>出典</dt><dd>本書 第6章 / 対象: バウハウス基礎課程（Bauhaus-Archiv）</dd></div></dl>",
    },
    {
        "id": "plate-08", "no": "PL. 08", "title": "グリッド — 秩序の骨格", "svg": p08,
        "tags": "system form", "span": "pc-4",
        "desc": "<p>スイス・スタイルは、グリッドで情報を整理した。秩序は自由を減らすのではなく、判断の数を減らす。</p><dl><div><dt>見る</dt><dd>12カラム、ベースライン、非対称の配置、赤い円。</dd></div><div><dt>問う</dt><dd>グリッドは、誰の情報を読みやすくし、何をはみ出させたのか。</dd></div><div><dt>出典</dt><dd>本書 第7章 / 対象: スイス・スタイルのポスター（1950s）</dd></div></dl>",
    },
    {
        "id": "plate-09", "no": "PL. 09", "title": "流線型 — 速度の記号", "svg": p09,
        "tags": "form meaning power", "span": "pc-5",
        "desc": "<p>空気抵抗の合理性と、未来への欲望。流線型は、冷蔵庫にまで速度をまとわせた。</p><dl><div><dt>見る</dt><dd>涙形のボディ、速度線、クロームの帯、風洞のグリッド。</dd></div><div><dt>問う</dt><dd>その曲線は、空気のためか、欲望のためか。機能は、どこまで記号か。</dd></div><div><dt>出典</dt><dd>本書 第5章・第7章 / 対象: 1930年代の流線型製品</dd></div></dl>",
    },
    {
        "id": "plate-10", "no": "PL. 10", "title": "無印良品 — 引き算のデザイン", "svg": p10,
        "tags": "material meaning system", "span": "pc-7",
        "desc": "<p>素材、機能、価格。余分なブランドを削ぎ、空いた余白に意味を置く。だが「引き算」もまた、一つの主張である。</p><dl><div><dt>見る</dt><dd>棚のモジュール、空の区画、CDプレーヤーの引き紐、赤い点。</dd></div><div><dt>問う</dt><dd>「これでいい」は、誰の「これ」か。空白は、余白か、省略か。</dd></div><div><dt>出典</dt><dd>本書 第10章 / 対象: 無印良品の家具・壁掛けCDプレーヤー</dd></div></dl>",
    },
    {
        "id": "plate-11", "no": "PL. 11", "title": "サーキュラー — 廃棄物は設計の失敗", "svg": p11,
        "tags": "system power", "span": "pc-6",
        "desc": "<p>まず出さない。長く使う。直す。再製造する。リサイクルは最後の手段。循環は、素材ではなく関係の問題である。</p><dl><div><dt>見る</dt><dd>6つのノード、環状の矢印、中心の葉、下の直線経路と×。</dd></div><div><dt>問う</dt><dd>誰が修理し、誰が回収し、誰がその労働を負担するのか。</dd></div><div><dt>出典</dt><dd>本書 第9章 / Ellen MacArthur Foundation / EU ESPR 2024</dd></div></dl>",
    },
    {
        "id": "plate-12", "no": "PL. 12", "title": "AI — 生成のあとに残るもの", "svg": p12,
        "tags": "system power meaning", "span": "pc-6",
        "desc": "<p>プロンプト、モデル、出力。生成は自動化できる。だが、何を良しとするか、誰が責任を負うかは、まだ人間の仕事である。</p><dl><div><dt>見る</dt><dd>入力、層、出力、人間の判断への帰還線。生成と判断の境界。</dd></div><div><dt>問う</dt><dd>AIが形を作るとき、作者は誰か。責任は、どこに残るのか。</dd></div><div><dt>出典</dt><dd>本書 第8章・第9章 / EU AI Act 2024</dd></div></dl>",
    },
    {
        "id": "plate-13", "no": "PL. 13", "title": "茶碗 — 侘寂は、日本全体ではない", "svg": p13,
        "tags": "meaning material power", "span": "pc-12",
        "desc": "<p>歪み、厚み、景色。茶の湯が磨いた美学は、日本文化の一部であって全体ではない。金継ぎは、欠けを消さずに残す。</p><dl><div><dt>見る</dt><dd>轆轤目、厚みの不均一、金の修復線、背後の円相、空の四角。</dd></div><div><dt>問う</dt><dd>「侘寂」は、誰の美意識か。修復は、傷を隠すのか、歴史として残すのか。</dd></div><div><dt>出典</dt><dd>本書 第10章 / 対象: 楽焼茶碗・金継ぎ（諸博物館）</dd></div></dl>",
    },
]


def main() -> None:
    cards = []
    for p in PLATES:
        cards.append(
            f'''<article class="plate-card {p["span"]}" id="{p["id"]}" data-plate-card data-tags="{p["tags"]}">
  <div class="plate-card__visual">
    {p["svg"]()}
    <button class="plate-card__expand" type="button" data-open-plate aria-label="{p["title"]} を拡大">拡大 ＋</button>
  </div>
  <div class="plate-card__caption">
    <span class="plate-card__no">{p["no"]}</span>
    <div>
      <h2 class="plate-card__title">{p["title"]}</h2>
      <div class="plate-card__desc">{p["desc"]}</div>
    </div>
  </div>
</article>'''
        )

    page = f"""{head("図版室 — デザイン全史 / THE PLATES", "13の注釈つき図版で、デザイン史の構造を読む。見る・問う・出典の三点で構成。")}
<body data-page="atlas">
<a class="skip" href="#main">本文へスキップ</a>
<noscript><style>.atlas-filters{{display:none}}.plate-card__expand{{display:none}}</style></noscript>
{rail("atlas")}

<main id="main" class="page">
  <div class="shell">
    <header class="atlas-head">
      <p class="eyebrow"><span class="eyebrow__no">05</span> THE PLATES</p>
      <h1 class="atlas-title">図版は、<br>飾りではない。</h1>
      <p class="atlas-lede">一枚の図が、一章ぶんの考えを運ぶ。13の図版を、<strong>見る・問う・出典</strong>の三点で読む。図は、答えではなく、考えるための器具である。</p>
      <div class="atlas-controls">
        <div class="atlas-filters" data-filters role="group" aria-label="図版を絞り込む">
          <button class="filter" type="button" data-filter="all" aria-pressed="true">すべて <span>13</span></button>
          <button class="filter" type="button" data-filter="form" aria-pressed="false">形</button>
          <button class="filter" type="button" data-filter="material" aria-pressed="false">素材</button>
          <button class="filter" type="button" data-filter="meaning" aria-pressed="false">意味</button>
          <button class="filter" type="button" data-filter="system" aria-pressed="false">システム</button>
          <button class="filter" type="button" data-filter="power" aria-pressed="false">権力</button>
        </div>
        <p class="mono"><span data-filter-count>13</span> / 13 PLATES</p>
      </div>
    </header>

    <div class="atlas-grid">
      {''.join(cards)}
    </div>

    <p class="note" style="margin-top:2rem">図版は、対象の写真ではなく、構造を読むための作図です。寸法・比率・色は、説明のために単純化しています。対象の正確な形は、各博物館のコレクションで確認してください。</p>
  </div>
</main>

<dialog class="plate-dialog" id="plate-dialog" aria-labelledby="plate-dialog-title">
  <div class="plate-dialog__inner">
    <button class="plate-dialog__close" type="button" data-close-plate aria-label="閉じる">×</button>
    <div class="plate-dialog__art" data-dialog-art></div>
    <div class="plate-dialog__text">
      <span class="mono" data-dialog-no></span>
      <h2 id="plate-dialog-title" data-dialog-title></h2>
      <div class="plate-dialog__desc" data-dialog-text></div>
    </div>
  </div>
</dialog>

{footer("method.html", "THE EVIDENCE", "検証で、疑う。")}
<script src="assets/app.js" defer></script>
</body>
</html>
"""
    (BASE / "atlas.html").write_text(page, encoding="utf-8")
    print(f"wrote atlas.html: {len(page):,} chars, {len(PLATES)} plates")


if __name__ == "__main__":
    main()
