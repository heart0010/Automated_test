import unittest

import requests


class GetHomePage(unittest.TestCase):

    #获取首页成功
    def get_home_page_ok(self):
        home_url = "http://192.168.108.210/etp-api/home-page"
        resp = requests.get(url=home_url)
        #打印响应结果
        print(resp.json())