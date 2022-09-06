'''
@file :  get_mysql.py
@author : 张福卫
@date : 2022/08/01 19:52
'''

import pymysql


def get_mysql(sql):
    con = pymysql.connect(host='127.0.0.1',  # 数据库ip
                          port=3306,
                          user='test',
                          password='123456',
                          database='test_1')  # 数据库名称

    cur = con.cursor()  # 创建游标，用来执行或返回操作结果

    cur.execute(sql)  # 执行sql
    con.commit()  # 提交sql 除了查询，增删改都要执行
    # print("列名:\n", "  ".join([items[0] for items in cur.description]))
    res = cur.fetchall()  # 将结果实例化给data赋值
    # for i in res:
    #     print(i)

    return res
if __name__ == '__main__':


    # s = "INSERT INTO `test_1`.`a_cp` (`type`, `postid`) VALUES " \
    # "('济南', '山东'),('青岛', '山东'),('日照', '山东'),('聊城', '山东')"
    # get_mysql(s)
    get_mysql('select * from a_cp')

# print(s)
