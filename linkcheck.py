from pathlib import Path
from html.parser import HTMLParser
import re, urllib.parse

BASE = Path("design-history-research/site")
pages = ["index.html","read.html","timeline.html","atlas.html","method.html","design-notes.html"]

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=set(); self.hrefs=[]; self.imgs=[]; self.buttons=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if "id" in a: self.ids.add(a["id"])
        if tag=="a" and "href" in a: self.hrefs.append(a["href"])
        if tag=="img": self.imgs.append(a)
        if tag=="button": self.buttons.append(a)

all_ids={}
for page in pages:
    p=P(); p.feed((BASE/page).read_text(encoding="utf-8")); all_ids[page]=p.ids

problems=[]
for page in pages:
    p=P(); p.feed((BASE/page).read_text(encoding="utf-8"))
    dup = []
    seen=set()
    for tag in re.findall(r'id="([^"]+)"', (BASE/page).read_text(encoding="utf-8")):
        if tag in seen: dup.append(tag)
        seen.add(tag)
    if dup: problems.append(f"{page}: duplicate ids {sorted(set(dup))}")
    for href in p.hrefs:
        if href.startswith(("http://","https://","mailto:","javascript:","tel:")): continue
        parts=urllib.parse.urlsplit(href)
        target=parts.path or page
        frag=parts.fragment
        if target not in pages and not (BASE/target).exists():
            problems.append(f"{page}: missing file {href}")
            continue
        if frag:
            if target in all_ids and frag not in all_ids[target]:
                problems.append(f"{page}: missing anchor {href}")
    for img in p.imgs:
        if "alt" not in img: problems.append(f"{page}: img missing alt {img}")
    for b in p.buttons:
        if not (b.get("aria-label") or b.get("title") or b.get("data-nav-toggle") or b.get("data-theme-toggle") or b.get("data-font-size") or b.get("data-tl-mode") or b.get("data-era") or b.get("data-filter") or b.get("data-open-plate") or b.get("data-close-plate") or b.get("data-tl-prev") or b.get("data-tl-next") or b.get("data-term")):
            # text content unknown here; only report if no common hook
            pass

print("problems:", len(problems))
for x in problems[:50]: print(" -", x)
print("ids per page:", {k:len(v) for k,v in all_ids.items()})
