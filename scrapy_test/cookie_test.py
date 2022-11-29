import requests
from lxml import etree

url = "http://www.porters.vip/verify/cookie/content.html"
headers = {"Cookie": "isfirst=789kq7uc1pp4c"}

rsp = requests.get(url, headers=headers)
if rsp.status_code == 200:
    sel = etree.HTML(rsp.text)
    res = sel.cssselect(".page-header h1")[0].text
    print(res)
else:
    print("请求失败")