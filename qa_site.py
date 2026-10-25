import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

BASE = Path(r"design-history-research/site").resolve()
PAGES = ["index.html","read.html","timeline.html","atlas.html","method.html","design-notes.html"]
WIDTHS = [320, 390, 768, 1024, 1440]
AXE = "https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js"

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="chrome", headless=True)
        results = {}
        for page_name in PAGES:
            results[page_name] = {}
            for w in WIDTHS:
                page = await b.new_page(viewport={"width": w, "height": 900})
                errors=[]
                page.on("pageerror", lambda e: errors.append(str(e)))
                await page.goto((BASE/page_name).as_uri(), wait_until="networkidle")
                await page.wait_for_timeout(400)
                sw = await page.evaluate("document.documentElement.scrollWidth")
                iw = await page.evaluate("window.innerWidth")
                overflow = sw > iw + 1
                # elements beyond viewport (excluding scroll containers)
                bad = await page.evaluate("""() => {
                  const iw = window.innerWidth;
                  return [...document.querySelectorAll('body *')].filter(el => {
                    const s = getComputedStyle(el);
                    if (s.display === 'none' || s.visibility === 'hidden') return false;
                    if (el.closest('.table-wrap, .fc-table-wrap, .tl-full, .read-main, .plate-dialog')) return false;
                    const r = el.getBoundingClientRect();
                    return r.width > 0 && r.right > iw + 2;
                  }).slice(0, 5).map(el => el.tagName + '.' + (el.className && el.className.baseVal !== undefined ? el.className.baseVal : el.className));
                }""")
                results[page_name][w] = {"scrollWidth": sw, "overflow": overflow, "bad": bad, "errors": errors}
                await page.close()
        for page_name, widths in results.items():
            print("\n==", page_name)
            for w, r in widths.items():
                if r["overflow"] or r["bad"] or r["errors"]:
                    print(" ", w, "OVERFLOW" if r["overflow"] else "", r["bad"], r["errors"][:2])
                else:
                    print(" ", w, "ok")
        # axe on a subset
        for page_name in PAGES:
            page = await b.new_page(viewport={"width": 1440, "height": 900})
            await page.goto((BASE/page_name).as_uri(), wait_until="networkidle")
            await page.wait_for_timeout(300)
            try:
                await page.add_script_tag(url=AXE)
                axe = await page.evaluate("""async () => {
                  const r = await axe.run(document, {runOnly: {type:'tag', values:['wcag2a','wcag2aa','wcag22aa']}});
                  return r.violations.map(v => ({id:v.id, impact:v.impact, nodes:v.nodes.length, target:v.nodes[0] && v.nodes[0].target}));
                }""")
                print("\nAXE", page_name, "violations", len(axe))
                for v in axe[:10]: print("  ", v)
            except Exception as e:
                print("\nAXE", page_name, "FAILED", e)
            await page.close()
        await b.close()

asyncio.run(main())
