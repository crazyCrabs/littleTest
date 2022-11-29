import requests
from parsel import Selector

url = "http://www.porters.vip/verify/uas/index.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

rsp = requests.get(url, headers=headers)
if rsp.status_code == 200:
    sel = Selector(rsp.text)
    res = sel.css(".list-group-item::text").extract()
    print(res)
else:
    print("请求失败")