'''
@file :  test_case1.py
@author : 张福卫
@date : 2022/08/01 18:42
'''

from lib.get_response import *
from lib.get_key import *
import requests, unittest
from ddt import ddt, data, unpack
from lib.get_mysql import *  # 导入封装的数据库方法

s = get_mysql('select * from a_cp')  # 将结果实例化
print(s)


@ddt
class api(unittest.TestCase):
    """
    注意一个参数跟两个参数的区别
    """

    @data('泰安', '日照', '聊城', '青岛', '济南')  # * 表示不计长度
    # @unpack  # 将入参分离依次给city，province传值
    def test_1_login(self, city):
        # 1个参数
        url = 'http://wthrcdn.etouch.cn/weather_mini'
        data = {'city': city,
                'province': '山东'
                }
        res = requests.get(url=url, params=data)
        # get_key(res, 'date')  # 获取关键字

        get_response(res)  # 打印接口返回数据

    @data(('泰安', '山东'), ('聊城', '山东'), ('济南', '山东'), ('青岛', '山东'))  # * 表示不计长度
    @unpack  # 将入参分离依次给city，province传值
    def test_2_login(self, city, province):
        # 2个参数
        url = 'http://wthrcdn.etouch.cn/weather_mini'
        data = {'city': city,
                'province': province
                }
        res = requests.get(url=url, params=data)
        c = get_key(res, 'city')  # 获取关键字
        print(f'city ：{c}')  # 打印关键字
        get_response(res)  # 打印接口返回数据

    @data(*s)  # * 表示不计长度
    @unpack  # 将入参分离依次给city，province传值
    def test_3_login(self, city, province):
        # 2个参数
        url = 'http://wthrcdn.etouch.cn/weather_mini'
        data = {'city': city,
                'province': province
                }
        res = requests.get(url=url, params=data)
        # c = get_key(res, 'city')  # 获取关键字
        # print(f'city ：{c}')  # 打印关键字
        get_response(res)  # 打印接口返回数据


if __name__ == '__main__':
    unittest.main()
