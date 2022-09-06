"""
@file :  get_report.py
@author : 张福卫
@date : 2022/08/22 16:24
"""

import unittest, time, BeautifulReport


class re:
    def get_report(self):
        # 用例路径
        case_path = 'F:\\pythonProject_data\\test_case'

        # 加载用例
        dis = unittest.defaultTestLoader.discover(case_path, 'test_case.py')

        # 生成报告时间
        now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())

        # 定义报告名称
        report_name = now + ' report.html'

        # 定义报告存储路径
        report_path = 'F:\\pythonProject_data\\html_report'

        BeautifulReport.BeautifulReport(dis).report(filename=report_name, report_dir=report_path, description='测试报告')

    def get_report1(self,py):
        # 用例路径
        case_path = 'F:\\pythonProject_data\\test_case'

        # 加载用例
        dis = unittest.defaultTestLoader.discover(case_path, py)

        # 生成报告时间
        now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())

        # 定义报告名称
        report_name = now + ' report.html'

        # 定义报告存储路径
        report_path = 'F:\\pythonProject_data\\html_report'

        BeautifulReport.BeautifulReport(dis).report(filename=report_name, report_dir=report_path, description='测试报告')


if __name__ == '__main__':
    re().get_report()
