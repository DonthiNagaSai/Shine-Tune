import asyncio, pathlib,json,sys,os,math
from playwright.async_api import async_playwright

CHROME = pathlib.Path('/usr/bin/google-chrome')
LAUNCH = {'args': ['--no-sandbox']}
if CHROME.exists():
    LAUNCH['executable_path'] = str(CHROME)

PAGE = 'file://' + str(pathlib.Path(__file__).resolve().parent.parent / 'index.html')
TARGET=5.5
plazas=json.loads(sys.argv[1]); gs=json.loads(sys.argv[2])
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(**LAUNCH)
        pg=await b.new_page(viewport={'width':800,'height':600})
        await pg.goto(PAGE); await pg.wait_for_timeout(400)
        async def run(pi,g,m,n=2):
            hs=[];last=None
            for _ in range(n):
                r=await pg.evaluate('([pi,g,m])=>window.__paceSim(pi,g,40,m)',[pi,g,m]); hs.append(r['hours']); last=r
            return sum(hs)/len(hs),last
        res={}
        for pi in plazas:
            for g in gs:
                lo,hi=1.0,60.0
                for _ in range(10):
                    mid=math.sqrt(lo*hi); h,_r=await run(pi,g,mid)
                    if h<TARGET: lo=mid
                    else: hi=mid
                m=round(math.sqrt(lo*hi),2); h,r=await run(pi,g,m,3)
                log=r['log']; gaps=[log[0][0]]+[log[i][0]-log[i-1][0] for i in range(1,len(log))]
                dec=[round(sum(gaps[int(len(gaps)*k/10):int(len(gaps)*(k+1)/10)])/60) for k in range(10)]
                print(f"plaza {pi}: g={g} m={m} -> {h:.2f}h, buys={len(log)}, max gap {max(gaps)/60:.0f} min, per tenth: {dec}, first: {[x[0] for x in log[:6]]}")
                res[(pi,g)]=m
        await b.close()
asyncio.run(main())
