# 定义全局变量
import requests

URL = 'http://192.168.108.210/etp/login/1'
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/105.0.0.0 "
#                   "Safari/537.36 Edg/105.0.1343.33 "
#     # "Cookie": "d2admin-0.0.1-lang=zh-chs; JSESSIONID=pK1qWjQt2riAQ1-SI5pFx-FmX6rFMSwPUdqDRk7v",
#     # "Upgrade-Insecure-Requests": "1"
# }


# 登录成功
def login_by_cookies():
    session = requests.Session()
    resp = session.get(url=URL)
    print(session)
    print(session.cookies)
    print(resp)
    print(resp.text)

    c = requests.cookies.RequestsCookieJar()
    c.set('JSESSIONID', 'slYtPvHZPFNbLht7jbPFOmBVxD6aVjx9gqS_nNfO')
    session.cookies.update(c)
    print(session.cookies)


if __name__ == '__main__':
    login_by_cookies()
