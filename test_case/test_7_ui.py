'''
@file :  test_7_ui.py
@author : 张福卫
@date : 2022/08/11 15:28
'''

# import time
# from appium import webdriver
# from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support.wait import WebDriverWait
#
# des = {
#     "platformName": "Android",
#     "platformVersion": "7.1",
#     "appPackage": "com.baidu.yuedu",
#     "deviceName": "127.0.0.1:62001",
#     "appActivity": "com.baidu.yuedu.base.ui.MainActivity",
#     "skipDeviceInitialization": True,
#     "skipServerInstallation": True,
#     "noSign": False,
# }
#
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=des)
# driver.implicitly_wait(10)
#
#
# def get_elements_by_text(driver, text):
#     elements = driver.find_elements(MobileBy.XPATH, f'//*[@text="{text}"]')
#     return elements
#
#
# def deal_with_arleat():
#     elements = get_elements_by_text(driver, '同意')
#     if len(elements) > 0:
#         elements[0].click()
#         time.sleep(3)
#
#     elements = get_elements_by_text(driver, '允许')
#     if len(elements) > 0:
#         elements[0].click()
#         time.sleep(3)
#
#     elements = get_elements_by_text(driver, '继续')
#     if len(elements) > 0:
#         elements[0].click()
#
#     elements = get_elements_by_text(driver, '跳过')
#     if len(elements) > 0:
#         elements[0].click()
#
#     for i in range(1):
#         elements = get_elements_by_text(driver, "关闭应用")
#         if len(elements) > 0:
#             elements[0].click()
#
#     for i in range(4):
#         wait = WebDriverWait(driver, 20, 1)
#         elements = wait.until(lambda k: driver.find_elements(MobileBy.CLASS_NAME, "android.widget.ImageView"))
#         if len(elements) == 2:
#             elements[1].click()
#             break
#         if len(elements) == 1:
#             elements[0].click()
#             driver.back()
#             break
#
#
# deal_with_arleat()
#
# versions = '宜人v9.6'
# jql_bugdata = f'affectedVersion = {versions} order by created DESC'
#
# '''bug类型列表'''
# jql_BugType = [f'affectedVersion = {versions}  order by created DESC',
#                f'affectedVersion = {versions}  AND BUG类型 = 代码优化   order by created DESC',
#                f'affectedVersion = {versions}  AND BUG类型 = 代码错误   order by created DESC',
#                f'affectedVersion = {versions}  AND BUG类型 = 安全相关   order by created DESC',
#                f'affectedVersion = {versions}  AND BUG类型 = 界面优化   order by created DESC',
#                f'affectedVersion = {versions}  AND BUG类型 = 需求问题   order by created DESC',
#                f'affectedVersion = {versions}  AND BUG类型 = 安装部署   order by created DESC',
#                f'affectedVersion = {versions}  AND BUG类型 = 性能问题   order by created DESC',
#                f'affectedVersion = {versions}  AND BUG类型 = 标准规范   order by created DESC',
#                f'affectedVersion = {versions}  AND BUG类型 = 测试脚本   order by created DESC',
#                f'affectedVersion = {versions}  AND BUG类型 = 环境相关   order by created DESC',
#                f'affectedVersion = {versions}  AND BUG类型 = 设计方案变更 order by created DESC',
#                ]
# # **********************************************************************************************************************
#
# '''bug等级列表'''
# jql_dengji = [f'affectedVersion = {versions}  AND BUG严重程度 = 1级严重 order by created DESC',
#               f'affectedVersion = {versions}  AND BUG严重程度 = 2级重要 order by created DESC',
#               f'affectedVersion = {versions}  AND BUG严重程度 = 3级一般 order by created DESC',
#               f'affectedVersion = {versions}  AND BUG严重程度 = 4级微小 order by created DESC',
#               ]
#
#
# # ***********************************************************************************************************************
#
# '''bug状态列表'''
#
# jql_status = [f'affectedVersion = {versions} order by created DESC',
#               f'status = NEW         AND affectedVersion = {versions}  order by created DESC',
#               f'status = Resolved    AND affectedVersion = {versions}  order by created DESC',
#               f'status = In Progress AND affectedVersion = {versions}  order by created DESC',
#               f'status = CLOSED      AND affectedVersion = {versions}  order by created DESC',
#               f'status = Reopened    AND affectedVersion = {versions}  order by created DESC',
#               f'status = 延期处理     AND affectedVersion = {versions}  order by created DESC'
#               ]
# # **********************************************************************************************************************
# '''bug状态条件'''
#
# # bug_sum = 'affectedVersion = {versions} order by created DESC'
# # bug_new = 'status = NEW AND affectedVersion = {versions}  order by created DESC'  # 【新建】
# # bug_Resolved = 'status = Resolved AND affectedVersion = {versions}  order by created DESC'  # 【已解决，未验证】
# # bug_InProgress = 'status = "In Progress" AND affectedVersion = {versions}  order by created DESC'  # 【处理中】
# # bug_CLOSED = 'status = CLOSED AND affectedVersion = {versions}  order by created DESC'  # 【已经关闭】
# # bug_Reopened = 'status = Reopened AND affectedVersion = {versions}  order by created DESC'  # 【重新打开】
# # bug_YanQi = 'status = 延期处理 AND affectedVersion = {versions}  order by created DESC'  # 【延期处理】
#
# # ***********************************************************************************************************************
#
# # **********************************************************************************************************************
# '''bug归属列表'''
#
# jql_BugOwn = [f'affectedVersion = {versions} AND bug归属 = IOS       order by created DESC',
#               f'affectedVersion = {versions} AND bug归属 = Android   order by created DESC',
#               f'affectedVersion = {versions} AND bug归属 = H5        order by created DESC',
#               f'affectedVersion = {versions} AND bug归属 = AppServer order by created DESC',
#               f'affectedVersion = {versions} AND bug归属 = 底层       order by created DESC',
#               f'affectedVersion = {versions} AND bug归属 = PM        order by created DESC',
#               f'affectedVersion = {versions} AND bug归属 = PC        order by created DESC']

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

wb = webdriver.Chrome()
wb.get('https://www.baidu.com')

wb.find_element(By.ID,'kw').send_keys('图片')
time.sleep(1)
wb.find_element(By.ID,'kw').clear()
wb.find_element(By.CLASS_NAME,'soutu-btn').click()
wb.find_element(By.CLASS_NAME,'upload-pic').send_keys(r'D:\桌面壁纸\123.jpg')
# wb.find_element(By.CSS_SELECTOR,'upload-pic').send_keys(r'D:\桌面壁纸\123.jpg')
# wb.find_element(By.ID,'su').submit()
# wb.find_element(By.ID,'su').click()
# wb.close()
# wb.maximize_window()