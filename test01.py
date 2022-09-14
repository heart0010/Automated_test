# 定义全局变量
import requests

URL = "http://192.168.108.210/etp-api/plan/pages"
header = {
    "Content-Type": "application/json;charset=UTF-8",
    "Authorization": "bearer be2537ac-997c-4b55-8326-87117ba0ea27"
}


# 查询实训计划_默认
def query_default():
    json_data = {"isPublish": "", "time": [], "planName": "", "pageable": {"pageIndex": 1, "pageSize": 20}}
    resp = requests.post(url=URL, headers=header, data=json_data)
    print(resp.status_code)
    print(resp.json())


if __name__ == '__main__':
    query_default()
