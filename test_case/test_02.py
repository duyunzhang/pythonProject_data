"""
@file :  test_02.py
@author : 张福卫
@date : 2022/09/04 15:23
"""
# from selenium import webdriver
# import unittest
# from ddt import ddt, data, unpack
#
#
# @ddt
# class add_g(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         print('打开浏览器')
#         cls.driver = webdriver.Chrome()
#         cls.driver.implicitly_wait(10)
#
#     @data(['test01', 'test01'])
#     @unpack
#     def test_2login(self, username, password):
#         print('%s登录' % username)
#         self.driver.get('http://newecshop.longtest.cn/admin/privilege.php')
#         self.driver.find_element('name', 'username').send_keys(username)
#         self.driver.find_element('name', 'password').send_keys(password)
#         self.driver.find_element('class name', 'button2').click()
#
#     @data(['商品管理', '添加新商品'])
#     @unpack
#     def test_3click_menu(self, menu, sub_menu):
#         print('点击%s-%s' % (menu, sub_menu))
#         self.driver.switch_to.frame('menu_frame')
#         self.driver.find_element('link text', menu).click()
#         self.driver.find_element('link text', sub_menu).click()
#         self.driver.switch_to.default_content()
#
#     @data(['dell电脑hzc', '电脑', '3999'])
#     @unpack
#     def test_4add_goods(self, goods_name, cat_name, shop_price):
#         print('添加商品%s-%s-%s' % (goods_name, cat_name, shop_price))
#         self.driver.switch_to.frame('main_frame')
#         self.driver.find_element('name', 'goods_name').send_keys(goods_name)
#         print('输入商品名称')
#         self.driver.find_element('name', 'cat_name').send_keys(cat_name)
#         print('输入商品分类')
#         # self.driver.find_element('name', 'goods_name').click()
#         print('点击商品名称')
#         self.driver.find_element('name', 'shop_price').send_keys(shop_price)
#         print('输入价格')
#         # self.driver.find_element('name', 'goods_img').send_keys(goods_img)
#         # self.driver.find_element('name', 'goods_img').send_keys(goods_img)
#         self.driver.find_element('id', 'goods_info_submit').click()
#         assert '添加商品成功' in self.driver.page_source
#
#
# if __name__ == '__main__':
#     unittest.main()

# def main():
#     add_g().open_browser()
#     add_g().login('test01', 'test01')
#     add_g().click_menu('商品管理', '添加新商品')
#     add_g().add_goods('dell电脑hzc', '电脑', '3999', )
# def qie_kuangjia():
#     from selenium import webself.driver
#     self.driver = webself.driver.Chrome()
#     self.driver.get("https://www.w3school.com.cn/tiy/t.asp?f=html_frame_rows")
#     self.driver.switch_to.frame("iframeResult")  # 使用节点id 或name,切换到第一层iframe
#     self.driver.switch_to.frame(0)  # 根据索引,切换到第二层第1 个frame
#     frame_a = self.driver.find_element_by_tag_name("h3")
#     print(frame_a.text)
#     self.driver.switch_to.parent_frame()  # 切换到父框架
#     self.driver.switch_to.frame(1)  # 根据索引,切换到第二层第2 个frame
#     frame_b = self.driver.find_element_by_tag_name("h3")
#     print(frame_b.text)
#     self.driver.quit()

# qie_kuangjia()
# open_browser()
# login('test01', 'test01')
# main()
