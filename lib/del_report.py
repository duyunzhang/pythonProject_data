"""
@file :  del_report.py
@author : 张福卫
@date : 2022/09/01 15:38
"""

import os


def del_report():
    path = '../html_report'
    list_f = os.listdir(path)
    print(path,list_f[-1])


del_report()
