'''
@file :  get_response.py
@author : 张福卫
@date : 2022/08/01 15:59
'''
import json

def get_response(res):
    # 获取请求结果
    m = json.dumps(res.json(),
                   ensure_ascii=False, #将接口返回的Unicode格式字符串转换成中文
                   sort_keys=True,
                   indent=4,    # 缩进
                   separators=(',', ':')) #分割符号
    print(m)
