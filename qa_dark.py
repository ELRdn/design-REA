import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
BASE = Path(r"design-history-research/site").resolve()
AXE = "https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js"
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="chrome", headless=True)
        for name in ["index.html","read.html","timeline.html","atlas.html","method.html","design-notes.html"]:
            page = await b.new_page(viewport={"width":1440,"height":900})
            await page.add_init_script("localStorage.setItem('dh-theme','dark')")
            await page.goto((BASE/name).as_uri(), wait_until="networkidle")
            await page.wait_for_timeout(400)
            try:
                await page.add_script_tag(url=AXE)
                axe = await page.evaluate("""async () => {
                  const r = await axe.run(document, {runOnly: {type:'tag', values:['wcag2a','wcag2aa','wcag22aa']}});
                  return r.violations.map(v => ({id:v.id, impact:v.impact, nodes:v.nodes.length, target:v.nodes[0] && v.nodes[0].target}));
                }""")
                print("DARK AXE", name, len(axe))
                for v in axe[:8]: print("  ", v)
            except Exception as e:
                print("DARK AXE", name, "FAIL", e)
            await page.close()
        await b.close()
asyncio.run(main())
