'''
@file :  test_1.py
@author : 张福卫
@date : 2022/08/02 10:16
'''

import requests, unittest, json

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
        # 1个参数
        url = 'http://wthrcdn.etouch.cn/weather_mini'
        data = {'city': '济南',
                'province': '山东'
                }
        res = requests.get(url=url, params=data)

        get_response(res)
        print((res))
        ceshi.city = get_key(res, 'city')  # 获取关键字
        ceshi.ganmao = get_key(res, 'ganmao')  # 获取关键字
        ceshi.wendu = get_key(res, 'wendu')  # 获取关键字
        ceshi.status = get_key(res, 'status')  # 获取关键字

    # @file_data('F:\\pythonProject_data\\data\\123.yaml')
    def test_2(self):
        data = {'city': self.city,
                'ganmao': self.ganmao,
                'wendu': self.wendu,
                'status': self.status
                }
        data = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)
        print(data)

    @file_data('F:\\pythonProject_data\\data\\123.yaml')
    def test_3(self, **kwargs):
        a = self.assignment(kwargs)
        data = a['data']
        data = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)
        print(data)

    @file_data('F:\\pythonProject_data\\data\\123.yaml')
    # @unpack
    def test_4(self, **kwargs):
        data = kwargs['data']
        data['city'] = self.city
        data['wendu'] = self.wendu
        data['ganmao'] = self.ganmao
        data['status'] = self.status

        print(data)

    @file_data('F:\\pythonProject_data\\data\\123.yaml')
    def test_5(self, **kwargs):
        data = kwargs['data']
        print(data)

    @unittest.skipIf(1 == 1, "条件1=1符合，跳过")
    @file_data('F:\\pythonProject_data\\data\\123.yaml')
    def test_6(self, **kwargs):
        data = kwargs['data']
        print(data)

    @file_data('F:\\pythonProject_data\\data\\123.json')
    def test_7_login(self, city, province):
        # 1个参数
        url = 'http://wthrcdn.etouch.cn/weather_mini'
        data = {'city': city,
                'province': province
                }
        res = requests.get(url=url, params=data)

        get_response(res)


if __name__ == '__main__':
    unittest.main()
