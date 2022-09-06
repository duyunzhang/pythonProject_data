'''
@file :  get_request.py
@author : 张福卫
@date : 2022/08/01 15:23
'''
import requests
import json,jsonpath

class apikey():



    def post(self,url,data=None,haesders=None,json_=None):
        #get请求
        return requests.post(url=url,data=data,headers=haesders,json=json_)


    def get(self,url,data=None,haesders=None):
        #post请求
        return requests.post(url=url,params=data,headers=haesders)



