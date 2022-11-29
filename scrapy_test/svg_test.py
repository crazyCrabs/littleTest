import re

import requests
from parsel import Selector

css_url = "http://www.porters.vip/confusion/css/food.css"
svg_url = "http://www.porters.vip/confusion/font/food.svg"

css_resp  = requests.get(css_url).text
svg_resp = requests.get(svg_url).text

class_name = "vhkbvu"
pile = f".{class_name}{{background:-(\d+)px-(\d+)px;}}"
pattern = re.compile(pile)
css = css_resp.replace("\n", "").replace(" ", "")
print(">>> pile: ", pile)
if coord := pattern.findall(css):
    print(">>> coord: ", coord)
    x, y = coord[0]
    x, y = int(x), int(y)

    svg_data = Selector(svg_resp)
    texts = svg_data.xpath("//text")
    print(">>> texts: ", texts)
    axis_y = [i.attrib.get('y') for i in texts if y <= int(i.attrib.get("y"))]
    print(">>> axis_y: ", axis_y)
    svg_text = svg_data.xpath(f"//text[@y={axis_y[0]}]/text()").extract_first()
    print(">>> svg_text: ", svg_text)
    font_size = re.search(r"font-size:(\d+)px", svg_resp)[1]
    print(">>> font_size: ", font_size)
    position = x // int(font_size)
    number = svg_text[position]
    print(">>> number: ", number)