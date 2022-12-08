import asyncio

from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    script = "() => {Object.defineProperty(navigator, 'webdriver', {get: () => undefined})}"
    await page.evaluateOnNewDocument(script)
    await page.goto("http://www.porters.vip/features/webdriver.html")
    # 因为navigator.webdriver是一个只读属性，所以需要通过js来修改 不然会被检测出是自动化爬虫
    await asyncio.sleep(1)
    await page.click(".btn.btn-primary.btn-lg")

    rsp = await page.xpath('//*[@id="content"]')
    print(">>> rsp: ", await (await rsp[0].getProperty("textContent")).jsonValue())
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
