'''
@file :  test_1.py
@author : 张福卫
@date : 2022/08/02 10:16
'''

import unittest

import requests
import json

from lib.get_key import get_key
from lib.get_response import get_response
from ddt import ddt, file_data, unpack


@ddt
class ceshi(unittest.TestCase):

    def assignment(self, kwargs):
        for key, value in kwargs.items():
            if type(value) is dict:
                self.assignment(value)
            else:
                if value:
                    pass
                else:
                    kwargs[key] = getattr(self, key)
        return kwargs

    @classmethod
    def setUpClass(cls) -> None:
        cls.city = None
        cls.ganmao = None
        cls.wendu = None
        cls.status = None

    def test_1_login(self):
        """
        :return: 1个参数
        """
        url = 'http://wthrcdn.etouch.cn/weather_mini'
        data = {'city': '济南',
                'province': '山东'
                }
        res = requests.get(url=url, params=data)
        get_response(res)
        print(type(res))
        ceshi.city = get_key(res, 'city')  # 获取关键字
        ceshi.ganmao = get_key(res, 'ganmao')  # 获取关键字
        ceshi.wendu = get_key(res, 'wendu')  # 获取关键字
        ceshi.status = get_key(res, 'status')  # 获取关键字

    # @file_data('F:\\pythonProject_data\\data\\123.yaml')
    def test_2(self):
        """
        :return: 接口关联
        """
        data = {'city': self.city,
                'ganmao': self.ganmao,
                'wendu': self.wendu,
                'status': self.status
                }
        print(data)

    @file_data('F:\\pythonProject_data\\data\\123.yaml')
    def test_3(self, **kwargs):
        """
        :return: 赋值函数
        """
        a = self.assignment(kwargs)
        data = a['data']
        data = json.dumps(data,ensure_ascii=False,indent=4)
        print(data)


if __name__ == '__main__':
    unittest.main()
