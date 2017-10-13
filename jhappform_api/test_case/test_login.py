#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:22-09-2017
#Author:jhinno
#Version=.3



import sys
sys.path.append("..")
from tools.tools import *
import unittest
import os


class TestLogin(unittest.TestCase):
    """测试 appform 登录 case:"""
    

    def setUp(self):
        print("start test login ...")
     
    def clear(self):
        #some cleanup code
        pass

    def actions(self, arg1, arg2):
        data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
        datas = Tools().readi_test_data(data_json)
        url = datas['other_param'][0]['baseUrl'] + "login?username=" + arg1 + "&password=" + arg2       
        s = Tools().access_web(url)
        self.assertEqual(s["result"],'success', msg = "用户名或密码错误，没有获取到token值。登录appform失败！")


    @staticmethod
    def getTestFunc(arg1, arg2, arg3):
        def func(self):
            self.actions(arg1, arg2)
        return func

    def tearDown(self):
        print("test end login...")

def generateTestCases():
    data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
    data_case = Tools().readi_test_data(data_json)
    print(type(data_case))
    arglists = []
    lenth = len(data_case['login'][0])
    for i in range(lenth):
        no = i + 10
        cse = "case" + str(i + 1)
        unm = data_case['login'][0][cse][0]['data']['username']
        pwd = data_case['login'][0][cse][0]['data']['password']
        arglists.append((unm,pwd,no))
    for args in arglists:
        setattr(TestLogin, 'test_login_%s_%s_%s'%(args[0], args[1], args[2]),TestLogin.getTestFunc(*args))

s = generateTestCases()



if __name__ =='__main__':
    unittest.main()



