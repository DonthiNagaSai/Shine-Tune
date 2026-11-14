import asyncio, pathlib,json,sys,os
from playwright.async_api import async_playwright

CHROME = pathlib.Path('/usr/bin/google-chrome')
LAUNCH = {'args': ['--no-sandbox']}
if CHROME.exists():
    LAUNCH['executable_path'] = str(CHROME)

PAGE = 'file://' + str(pathlib.Path(__file__).resolve().parent.parent / 'index.html')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(**LAUNCH)
        pg=await b.new_page(viewport={'width':800,'height':600})
        errs=[]
        pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto(PAGE)
        await pg.wait_for_timeout(400)
        args=json.loads(sys.argv[1])
        for pi,g in args:
            r=await pg.evaluate('([pi,g])=>{const t0=performance.now();const r=window.__paceSim(pi,g,16);r.ms=performance.now()-t0;return r}',[pi,g])
            log=r['log']
            print(f"plaza {pi} g={g}: {r['hours']:.2f}h done={r['done']} buys={r['n']} rate={r['rate']:.1f} ({r['ms']:.0f}ms)")
            if len(sys.argv)>2:
                print('  first:',[(x[0],x[1],x[2]) for x in log[:8]])
                q=[log[int(len(log)*f)-1] for f in (.25,.5,.75,1)] if log else []
                print('  quartiles:',[(round(x[0]/60),x[1],x[2]) for x in q])
        print('errors',errs)
        await b.close()
asyncio.run(main())
