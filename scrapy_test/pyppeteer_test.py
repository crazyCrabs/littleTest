import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://www.porters.vip/verify/sign')
    await page.click('#fetch_button')
    rsp = await page.xpath('//*[@id="content"]')
    text = await (await rsp[0].getProperty('textContent')).jsonValue()
    print(text)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())