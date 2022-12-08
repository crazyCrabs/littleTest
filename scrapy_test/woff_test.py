# 安装 pip install fonttools 来解析字体文件
# from fontTools.ttLib import TTFont
# font = TTFont("littleTest/scrapy_test/movie.woff")
# font.saveXML("littleTest/scrapy_test/movie.xml")
import hashlib
import re

import requests
from urllib import parse
from fontTools.ttLib import TTFont
from parsel import Selector

# 取字形信息来当作hex值
base_font = {
    "font": [
        {"name": "uniE339", "value": "6", "hex": hashlib.md5(
            "uniE339".encode("utf-8")).hexdigest()},
        {"name": "uniE624", "value": "9", "hex": "704362b6e0feb6cd0b1303f10c000f95"},
        {"name": "uniE7DF", "value": "2", "hex": hashlib.md5(
            "uniE7DF".encode("utf-8")).hexdigest()},
        # uniE9C7->7 uniEA16->5 uniEE76->0 uniEFD4->8 uniF19A->3 uniF57B->1 uniF593->4
        {"name": "uniE9C7", "value": "7", "hex": "4aa5ac9a6741107dca4c5dd05176ec4c"},
        {"name": "uniEA16", "value": "5", "hex": hashlib.md5(
            "uniEA16".encode("utf-8")).hexdigest()},
        {"name": "uniEE76", "value": "0", "hex": hashlib.md5(
            "uniEE76".encode("utf-8")).hexdigest()},
        {"name": "uniEFD4", "value": "8", "hex": hashlib.md5(
            "uniEFD4".encode("utf-8")).hexdigest()},
        {"name": "uniF19A", "value": "3", "hex": hashlib.md5(
            "uniF19A".encode("utf-8")).hexdigest()},
        {"name": "uniF57B", "value": "1", "hex": hashlib.md5(
            "uniF57B".encode("utf-8")).hexdigest()},
        {"name": "uniF593", "value": "4", "hex": hashlib.md5(
            "uniF593".encode("utf-8")).hexdigest()},
    ]
}

url = "http://www.porters.vip/confusion/movie.html"
rsp = requests.get(url)
sel = Selector(rsp.text)
# 提取css路径
css_path = sel.css("link[rel=stylesheet]::attr(href)").extract()
woffs = []
for c_link in css_path[1:]:
    css_url = parse.urljoin(url, c_link)
    print(">>> css_url: ", css_url)
    css_rsp = requests.get(css_url)
    woff_path = re.findall(
        r"src:url\('..(.*.woff)'\) format\('woff'\);", css_rsp.text)
    print(">>> woff_path: ", woff_path)
    if woff_path:
        woffs.extend(woff_path)

    woff_url = parse.urljoin(url, f".{woffs.pop()}")
    print(">>> woff_url: ", woff_url)
    woff = requests.get(woff_url)
    filename = "target.woff"
    with open(filename, "wb") as f:
        f.write(woff.content)
    font = TTFont(filename)


    web_code = "&#xe624.&#xe9c7"
    woff_code = [i.upper().replace('&#X', "uni") for i in web_code.split(".")]
    result = []
    for w in woff_code:
        print(">>> w: ", w)
        content = font['glyf'].glyphs.get(w).data
        hex = hashlib.md5(content).hexdigest()
        for b in base_font.get("font"):
            if hex == b.get("hex"):
                result.append(b.get("value"))
                break
    print(">>> result: ", ".
          ".join(result))