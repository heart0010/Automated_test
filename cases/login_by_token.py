import requests
import unittest


class LoginByToken(unittest.TestCase):
    URL = "http://192.168.108.210/etp/index"
    header = {
        "Authorization": "bearer be2537ac-997c-4b55-8326-87117ba0ea27"
    }
    resp = requests.get(url=URL, headers=header)
    print(resp)
    print(resp.status_code)
    print(resp.cookies)
    print(resp.headers)
    print(resp.raw)
    print(resp.request)
    print(resp.request.url)
    print(resp.text)

