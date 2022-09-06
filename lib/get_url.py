"""
@file :  get_url.py
@author : 张福卫
@date : 2022/08/24 15:27
"""
import configparser

con = configparser.ConfigParser()
con.read("F:\\pythonProject_data\\data\\config.ini",encoding='utf-8')
url_1=con.get('DEFAULT','url')
url_11=con.get('DEFAULT','url11')
