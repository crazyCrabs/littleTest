import re

import requests
from parsel import Selector

url = "http://www.porters.vip/confusion/flight.html"

rsp = requests.get(url)
sel = Selector(rsp.text)
em = sel.css("em.rel").extract()
# print(">>> em: ", em)

for element in em:
    element = Selector(element)
    element_b = element.css("b").extract()
    # print(">>> element_b: ", element_b)
    b1 = Selector(element_b.pop(0))
    # 提取i标签里面基础的数据
    b1_style = b1.css("b::attr(style)").get()
    print(">>> b1_style: ", b1_style)
    b1_width = "".join(re.findall(r"width:(.*?)px", b1_style))
    print(">>> b1_width: ", b1_width)
    number = int(int(b1_width) / 16)
    base_price = b1.css("i::text").extract()[:number]
    print(">>> base_price: ", base_price)

    alternate_price = []
    for eb in element_b:
        eb = Selector(eb)
        style = eb.css("b::attr('style')").get()
        position = "".join(re.findall(r"left:(.*?)px", style))
        # print(">>> position: ", position)
        value = eb.css("b::text").get()
        # print(">>> value: ", value)
        alternate_price.append({"position": position, "value": value})
    print(">>> alternate_price: ", alternate_price)

    for al in alternate_price:
        position = int(al.get("position"))
        value = al.get("value")
        plus = position >= 0
        index = int(position / 16)
        base_price[index] = value
    print(">>> base_price: ", base_price)