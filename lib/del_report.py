"""
@file :  del_report.py
@author : 张福卫
@date : 2022/09/01 15:38
"""

import os, time


def del_report():
    path_f = '../html_report/'
    list_f = os.listdir(path_f)
    if list_f:
        for i in list_f:
            if i:
                file = path_f + i
                os.remove(file)
                print(f'{i} 已删除...')
    else:
        print(f'\n当前 {path_f} 文件夹没有测试报告文件')


if __name__ == '__main__':
    del_report()


# def get_report():
#     path = '../html_report'
#     list_f = os.listdir(path)
#     # print(list_f[-1])
#     return list_f[-1]
#
#
# # 将最新测试报告复制到桌面
# now = time.strftime('%H_%M_%S', time.localtime())
# path = "F:\\pythonProject_data\\html_report\\" + get_report()
# with open(path, 'r', encoding='utf-8') as f:
#     with open(f'C:\\Users\\15723\\Desktop\\测试报告\\{now}测试报告.html', 'a', encoding='utf-8') as f1:
#         data = f.read(512)
#         while data:
#             f1.write(data)
#             data = f.read(512)
