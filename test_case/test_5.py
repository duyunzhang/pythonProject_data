'''
@file :  test_5.py
@author : 张福卫
@date : 2022/08/09 16:43
'''

import time
from time import sleep
def test(func):
    def test_1():
        s1 = time.time()
        func()
        s2 = time.time()
        print('耗时:',s2-s1)

    return test_1


@test  # test_2 = test(tets_2)
def test_2():

    print('开始')
    sleep(4)
    print('结束')


if __name__ == '__main__':
    test_2()