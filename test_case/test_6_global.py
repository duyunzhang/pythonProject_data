'''
@file :  test_6_global.py
@author : 张福卫
@date : 2022/08/11 14:26
'''

import unittest

import requests
from pytest_html.extras import json

from lib.get_key import get_key
from lib.get_response import get_response
from ddt import ddt, file_data, unpack
import json


class ceshi(unittest.TestCase):

    def test_1_login(self):
        # 1个参数
        global city
        url = 'http://wthrcdn.etouch.cn/weather_mini'
        data = {'city': '济南',
                'province': '山东'
                }
        res = requests.get(url=url, params=data)
        m = json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=4)
        print(m)
        city = get_key(res, 'city')  # 获取关键字
        # global city

    def test_2_login(self):
        # 1个参数
        url = 'http://wthrcdn.etouch.cn/weather_mini'
        data = {'city': city,
                'province': '山东'
                }
        res = requests.get(url=url, params=data)

        get_response(res)


if __name__ == '__main__':
    unittest.main()
