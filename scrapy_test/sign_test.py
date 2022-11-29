import hashlib
import time
from random import randint, sample

import requests


def hex5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def uri():
    action = "".join([str(randint(0, 9)) for _ in range(5)])
    tim = round(time.time())
    randstr = "".join(sample([chr(_) for _ in range(65, 91)], 5))
    hexs = hex5(action + str(tim) + randstr)
    return f"?actions={action}&tim={tim}&randstr={randstr}&sign={hexs}"

url = "http://www.porters.vip/verify/sign/fet" + uri()
print(">>> url:", url)
rsp = requests.get(url)
print(rsp.status_code, rsp.text)