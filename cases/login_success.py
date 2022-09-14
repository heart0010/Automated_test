import unittest

import requests


class TestLogin(unittest.TestCase):

    # 测试登录成功
    def test01_login_success(self):
        # 创建session实例
        session = requests.Session()

        # 使用实例，调用get发送获取验证码请求
        session.get(url="http://192.168.108.210/SSOServer/validata/code/259e69e4-ca8d-453b-867c-458c4d474b0f")

        # 使用实例，调用post发送登录请求
        resp = session.post(url="http://192.168.108.210/etp/login/1",
                            headers={"Content-Type": "application/x-www-form-urlencoded",
                                     "Authorization": "Authorized"},
                            data={"username": "13620202020", "password": "123",
                                  "deviceId": "259e69e4-ca8d-453b-867c-458c4d474b0f",
                                  "validCode": "4"})

        print("响应结果 =", resp.json())

        # 断言响应结果
        self.assertEqual(200, resp.status_code)
        self.assertEqual("true", resp.json().get("success"))
        self.assertEqual("登录成功!", resp.json().get("message"))
