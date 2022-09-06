"""
@file :  test_run.py
@author : 张福卫
@date : 2022/08/22 16:36
"""

from lib.get_report import *


def get_t(func):
    def shijian():
        t1 = time.time()
        func()
        t2 = time.time()
        print('测试耗时：', t2 - t1)

    return shijian


@get_t
def run():
    re().get_report()


if __name__ == '__main__':
    run()
