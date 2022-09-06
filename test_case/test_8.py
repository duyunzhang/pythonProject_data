"""
@file :  test_8.py
@author : 张福卫
@date : 2022/08/24 11:09
"""
from lib.get_response import *
import requests, unittest
from ddt import ddt, data, unpack
from lib.get_mysql import *  # 导入封装的数据库方法
# 插入测试数据
from lib.get_url import *

s = "INSERT INTO `test_1`.`a_cp` (`type`, `postid`) VALUES " \
    "('济南', '山东'),('青岛', '山东'),('日照', '山东'),('聊城', '山东')"
get_mysql(s)
s = get_mysql('select * from a_cp')


# print(s)

@ddt
class api_test(unittest.TestCase):
    """
    注意一个参数跟两个参数的区别
    """

    @classmethod
    def setUpClass(cls) -> None:

        print('测试数据准备：\n', s)

    @data(*s)  # * 表示不计长度
    @unpack  # 将入参分离依次给city，province传值
    def test_1_login(self, city, province):
        # 2个参数
        url = url_1
        data = {'city': city,
                'province': province
                }
        res = requests.get(url=url, params=data)
        get_response(res)  # 打印接口返回数据

    def test_2(self):
        """
        验证测试数据
        :return:
        """
        s = get_mysql('select * from a_cp')
        print('测试数据验证:\n',s)

    @data(*s)  # * 表示不计长度
    @unpack  # 将入参分离依次给city，province传值
    def test_3_login(self, city, province):
        # 2个参数
        url = url_1
        data = {'city': city,
                'province': province
                }
        res = requests.get(url=url, params=data)
        get_response(res)  # 打印接口返回数据
        print(data)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.sql = "delete from a_cp where type in ('济南','青岛','日照','聊城')"
        get_mysql(cls.sql)
        print('测试完成，清除以下测试数据：\n', s)


if __name__ == '__main__':
    unittest.main()
    # time.sleep(2)
