"""
@file :  get_rep.py
@author : 张福卫
@date : 2022/08/22 16:42
"""
import os

path = '../html_report'

list = os.listdir(path)
print(list[-1])
# for i in list:
#     print(i)
    # os.remove(i)