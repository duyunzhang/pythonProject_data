'''
@file :  test_case.py
@author : 张福卫
@date : 2022/08/01 15:50
'''

import unittest, requests
from lib.get_key import *
from lib.get_response import *
from lib.get_mysql import *
from ddt import ddt, file_data, data, unpack

s = get_mysql('select * from a_cp')


@ddt
class api(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://wthrcdn.etouch.cn/weather_mini'
        cls.city = None

    def test_1_login(self):
        url = self.url
        data = {'city': '青岛',
                'province': '山东'
                }
        res = requests.get(url=url, params=data)
        get_response(res)
        c = get_key(res, 'city')
        api.city = c  # 将接口返回‘city’的值做全局变量

    def test_2_login(self):
        '''
        接口关联
        '''
        url = self.url
        data = {'city': self.city,  # 第一个接口返回的数据做传参
                'province': '山东'
                }
        res = requests.get(url=url, params=data)
        get_response(res)

    @data(['青岛', '山东'], ['济南', '山东'], ['北京','北京'])
    @unpack
    def test_3_login(self, cit, p):
        '''
        :param p: data数据驱动
        '''
        url = self.url
        data = {'city': cit,
                'province': p
                }
        res = requests.get(url=url, params=data)
        get_response(res)

    @file_data('F:\\pythonProject_data\\data\\weather.yaml')
    def test_4_login(self, **kwargs):
        '''
        yaml文件驱动
        '''
        url = self.url
        data = kwargs['data']
        res = requests.get(url=url, params=data)
        print('用例描述', kwargs['data'])
        get_response(res)
        c = get_key(res,'date')
        print(c)

    @data(*s)  # * 表示不计长度
    @unpack  # 将入参分离依次给city，province传值
    def test_5_login(self, city, province):
        url = 'http://wthrcdn.etouch.cn/weather_mini'
        data = {'city': city,
                'province': province
                }
        res = requests.get(url=url, params=data)
        c = get_key(res, 'city')  # 获取关键字
        print(f'city ：{c}')  # 打印关键字
        get_response(res)  # 打印接口返回数据


if __name__ == '__main__':
    unittest.main()
