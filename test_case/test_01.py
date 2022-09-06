"""
@file :  test_01.py
@author : 张福卫
@date : 2022/09/04 14:37
"""
import jsonpath
import requests, unittest, json

from lib.get_key import get_key
from lib.get_response import get_response
from ddt import ddt, file_data, unpack
import urllib3
from selenium import webdriver
import unittest, time

from selenium.webdriver.common.by import By

urllib3.disable_warnings()


class ceshi(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     wb = webdriver.Chrome()
    #     wb.get('https://newecshop.longtest.cn/admin/index.php')
    #     wb.find_element(By.NAME, 'username').send_keys('test01')
    #     wb.find_element(By.NAME, 'password').send_keys('test01')
    #     wb.find_element(By.CLASS_NAME, 'button2').submit()

    def test_1addgoods(self):
        print('')

        url = 'http://newecshop.longtest.cn/admin/privilege.php?act=login'
        data = {'username': 'test01',
                'password': 'test01'
                }
        res = requests.get(url=url, params=data)
        print(res)

    def test_2addgoods(self):
        data = {
            "code": 0,
            "message": "Success",
            "zpData": {
                "messages": [{
                    "uncount": 1,
                    "flag": 0,
                    "mid": 330633154163,
                    "received": True,
                    "securityId": "QJchP9pZpouUr-h1Vk02EKA0aXLf5EVjBlWLcumifzBVhFv8nTPiVHZBsqTgQcQXMurjDcmMAJ67m45vOLvxsfzKJNd-xKXMdZ-wXH12pC2I96JCu1SzJjP-ojwZR47Xs1gA92QFcnFEuZCnofIJj6RAJN3qk443e2c_2l8kVJ0rd3YzyEIGNz7CdJSeGMG4gdlJSBnSZ-2JvS8p327DSoTm0ZPMhoY4-Qk6Oin4tzecnoYcVMoBL_CPkZxpENUJgErxVl3F6gcjvPnLZCq_cciIAVHG1VsuP8VFi-9P4ZmScdADmmnJCV0MDe2M2NQY96_aQDuY9JfOrs8nHOg3IqArn6zIjnkahuARPjT_y6dskHlfv1K3oNXqvT-EGEh-d0kwh7yzi5RtrpqgeoPlX1cf_8ZChMXqhPjnYVa9xpq-lMWGvYtlfoJuhfUcqLiRngTMjTLnQ4t53gMgzxnTCRNzT5yJqvt53sLCS9Zn6A~~",
                    "cmid": 0,
                    "type": 3,
                    "body": {
                        "type": 8,
                        "templateId": 1,
                        "jobDesc": {
                            "education": "本科",
                            "boss": {
                                "uid": 39764630,
                                "headImg": 0,
                                "name": "杨先生",
                                "company": "",
                                "avatar": "https://img.bosszhipin.com/beijin/upload/avatar/20201023/0f7c089c21c374dd65e3cefbd70c68e9695acc5906eaee8c59e75ee980faf37c_s.png",
                                "source": 0,
                                "certification": 0
                            },
                            "distance": "",
                            "city": "北京 大兴区 亦庄",
                            "lid": "",
                            "partTimeDesc": "",
                            "expectId": 0,
                            "title": "测试工程师（学信网可查）",
                            "salary": "1.1-1.3万元",
                            "experience": "1-3年",
                            "bottomText": "9月5日 18:39 向你发起的沟通",
                            "content": "1. 接口根据产品需求设计，理解功能测试点，包括使用场景、上下游链路，接口的影响范围（如db、中间件、网络协议、请求方法等等，与工具无关）\n2. Linux常用的命令，mysql 单表、多表查询使用，索引（使用场景、影响范围）\n3. python 能知道基础的功能使用，自带的一些方法理解\n岗位属于车载类型的测试，无车载经验也可\n民办学历勿扰，谢谢",
                            "jobLabel": "",
                            "latlon": "",
                            "expectPosition": "",
                            "company": "武汉佰钧成",
                            "url": "bosszp://bosszhipin.app/openwith?type=jobview&jid=236660548&uid=39764630&securityId=QJchP9pZpouUr-h1Vk02EKA0aXLf5EVjBlWLcumifzBVhFv8nTPiVHZBsqTgQcQXMurjDcmMAJ67m45vOLvxsfzKJNd-xKXMdZ-wXH12pC2I96JCu1SzJjP-ojwZR47Xs1gA92QFcnFEuZCnofIJj6RAJN3qk443e2c_2l8kVJ0rd3YzyEIGNz7CdJSeGMG4gdlJSBnSZ-2JvS8p327DSoTm0ZPMhoY4-Qk6Oin4tzecnoYcVMoBL_CPkZxpENUJgErxVl3F6gcjvPnLZCq_cciIAVHG1VsuP8VFi-9P4ZmScdADmmnJCV0MDe2M2NQY96_aQDuY9JfOrs8nHOg3IqArn6zIjnkahuARPjT_y6dskHlfv1K3oNXqvT-EGEh-d0kwh7yzi5RtrpqgeoPlX1cf_8ZChMXqhPjnYVa9xpq-lMWGvYtlfoJuhfUcqLiRngTMjTLnQ4t53gMgzxnTCRNzT5yJqvt53sLCS9Zn6A~~",
                            "labels": ["功能测试", "性能测试"],
                            "extend": "",
                            "jobId": 236660548,
                            "stage": "未融资",
                            "geek": {
                                "uid": 121605517,
                                "headImg": 0,
                                "name": "",
                                "company": "",
                                "avatar": "",
                                "source": 0,
                                "certification": 0
                            },
                            "iconFlag": 0,
                            "positionCategory": "测试工程师",
                            "bossTitle": "招聘",
                            "expectSalary": ""
                        },
                        "headTitle": "Boss杨先生希望就如下职位与您沟通"
                    },
                    "offline": False,
                    "pushSound": 0,
                    "from": {
                        "uid": 39764630,
                        "headImg": 0,
                        "name": "杨先生",
                        "company": "",
                        "avatar": "https://img.bosszhipin.com/beijin/upload/avatar/20201023/0f7c089c21c374dd65e3cefbd70c68e9695acc5906eaee8c59e75ee980faf37c_s.png",
                        "source": 0,
                        "certification": 0
                    },
                    "to": {
                        "uid": 121605517,
                        "headImg": 0,
                        "name": "V. V.",
                        "company": "",
                        "avatar": "https://img.bosszhipin.com/beijin/upload/avatar/20220721/607f1f3d68754fd0187cfb2b40e02a66e988d927cb7f95ca081bd69e6ea39a02d059265c50886792_s.png",
                        "source": 0,
                        "certification": 0
                    },
                    "time": 1662374371207,
                    "taskId": 0,
                    "status": 1
                }, {
                    "uncount": 1,
                    "flag": 0,
                    "mid": 330633154244,
                    "received": True,
                    "securityId": "ASmCMm3GLp-zF-j1wMtG47iG8lmRh0YZphIla1nWMMepV-3mNnwmSnMk_8Z8Dt0gk3l1qIxakjrXy-z4-JbSD5lsBDN4Hv_FyVpO",
                    "cmid": 0,
                    "type": 3,
                    "body": {
                        "action": {
                            "extend": "{\"expectId\":368028083}",
                            "aid": 51
                        },
                        "type": 4,
                        "templateId": 1,
                        "headTitle": ""
                    },
                    "offline": False,
                    "pushSound": 0,
                    "from": {
                        "uid": 39764630,
                        "headImg": 0,
                        "name": "杨先生",
                        "company": "",
                        "avatar": "https://img.bosszhipin.com/beijin/upload/avatar/20201023/0f7c089c21c374dd65e3cefbd70c68e9695acc5906eaee8c59e75ee980faf37c_s.png",
                        "source": 0,
                        "certification": 0
                    },
                    "to": {
                        "uid": 121605517,
                        "headImg": 0,
                        "name": "V. V.",
                        "company": "",
                        "avatar": "https://img.bosszhipin.com/beijin/upload/avatar/20220721/607f1f3d68754fd0187cfb2b40e02a66e988d927cb7f95ca081bd69e6ea39a02d059265c50886792_s.png",
                        "source": 0,
                        "certification": 0
                    },
                    "time": 1662374371213,
                    "taskId": 0,
                    "status": 1
                }, {
                    "uncount": 0,
                    "flag": 0,
                    "bizType": 101,
                    "mid": 330633154348,
                    "received": True,
                    "securityId": "ChRgNl67GtfXa-p1axqXnMFtP6ErPtm4UmGThybF7awY6GbufwNXyOFfChgefKeQVVV9BJVzvhhD7e08rynbB4LzRzUmNvGlHaCC",
                    "cmid": 0,
                    "type": 3,
                    "body": {
                        "extend": "",
                        "text": "请问在考虑新的工作机会吗？",
                        "type": 1,
                        "templateId": 1,
                        "headTitle": ""
                    },
                    "offline": False,
                    "pushSound": 0,
                    "from": {
                        "uid": 39764630,
                        "headImg": 0,
                        "name": "杨先生",
                        "company": "",
                        "avatar": "https://img.bosszhipin.com/beijin/upload/avatar/20201023/0f7c089c21c374dd65e3cefbd70c68e9695acc5906eaee8c59e75ee980faf37c_s.png",
                        "source": 0,
                        "certification": 0
                    },
                    "to": {
                        "uid": 121605517,
                        "headImg": 0,
                        "name": "V. V.",
                        "company": "",
                        "avatar": "https://img.bosszhipin.com/beijin/upload/avatar/20220721/607f1f3d68754fd0187cfb2b40e02a66e988d927cb7f95ca081bd69e6ea39a02d059265c50886792_s.png",
                        "source": 0,
                        "certification": 0
                    },
                    "time": 1662374371217,
                    "pushText": "杨先生:请问在考虑新的工作机会吗？",
                    "taskId": 0,
                    "status": 1
                }],
                "type": 1
            }
        }
        data = json.dumps(data,ensure_ascii=False,indent=4)
        value = jsonpath.jsonpath(data, '$..pushText')
        print(value)
        print(data)



if __name__ == '__main__':
    unittest.main()
