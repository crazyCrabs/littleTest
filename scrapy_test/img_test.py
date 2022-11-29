import io
from urllib.parse import urljoin

import pytesseract
import requests
from parsel import Selector
from PIL import Image

url = "http://www.porters.vip/confusion/recruit.html"


rsp = requests.get(url)
sel = Selector(rsp.text)
company = sel.css('h1.jumbotron::text').get()
image_name = sel.css('img.pn::attr(src)').get()
print(">>> image_name: ", image_name)
image_url = urljoin(url, image_name)
image_body = requests.get(image_url).content
print(">>> image_body: ", image_body)
image_stream = Image.open(io.BytesIO(image_body))
phone_number = pytesseract.image_to_string(image_stream)
print(">>> company: ", company, "phone_number: ", phone_number)