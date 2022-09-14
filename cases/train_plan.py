import unittest

import pymysql
import requests


class TrainPlain(unittest.TestCase):

    # 获取实训计划页面
    def get_plan_page_ok(self):

        plan_url = "http://192.168.108.210/etp-api/plan/pages"
        resp = requests.get(url=plan_url)

        # 打印响应结果
        print("响应结果为 =", resp)

        # 连接数据库
        conn = pymysql.Connect(host="",
                               port=3306,
                               database="",
                               user="",
                               password="",
                               charset="utf8")
        # 获取游标
        cursor = conn.cursor()

        #执行SQL查询语句
        cursor.execute("select * from plan")

        #获取查询显示的数量并赋值

        # 断言
        self.assertEqual("", resp.json().get("count"))
        self.assertEqual("1", resp.json().get("pageIndex"))
        self.assertEqual("20", resp.json().get("pageSize"))

    # 根据计划名称查询
    def find_by_plan_name(self):
        plan_url = "http://192.168.108.210/etp-api/plan/pages"
        json_data = {"planName": "1"}
        resp = requests.post(url=plan_url,
                             data=json_data)
        #打印响应结果
        print("响应结果 =", resp.json())

        #断言响应结果

    # 根据考试模式查询(模式为：考试)
    def find_by_plan_mode(self):
        plan_url = "http://192.168.108.210/etp-api/plan/pages"
        json_data = {"examModel": "1"}
        resp = requests.post(url=plan_url,
                             data=json_data)
        # 打印响应结果
        print("响应结果 =", resp.json())

        #断言


    # 根据计划状态查询
    def find_by_plan_status(self):
        plan_url = "http://192.168.108.210/etp-api/plan/pages"
        json_data = {"isPublish": "0"}
        resp = requests.post(url=plan_url,
                             data=json_data)
        # 打印响应结果
        print("响应结果 =", resp.json())

        # 断言

    # 根据实训日期查询
    def find_by_plan_time(self):
        plan_url = "http://192.168.108.210/etp-api/plan/pages"


    #重置页面
    def reset_plan_page(self):
        plan_url = "http://192.168.108.210/etp-api/plan/pages"
        json_data = {"time": []}
        resp = requests.post(url=plan_url,
                             data=json_data)
        # 打印响应结果
        print("响应结果 =", resp.json())

        # 断言


    #新建计划
    def create_plan_ok(self):
        plan_url = "http://192.168.108.210/etp-api/plan"
        json_data = {"planName": "",
                     "examModel": "2",
                     "time": ""}
        resp = requests.post(url=plan_url,
                             data=json_data)

        #打印响应结果
        print("响应结果 =", resp.json())

        #断言

    #修改计划


    #删除计划
    def delete_plan_ok(self):
        plan_url = "http://192.168.108.210/etp-api/plan/"
        #获取计划的ID
        id = ""
        requests.delete(url=plan_url+id)
        