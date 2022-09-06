'''
@file :  get_key.py
@author : 张福卫
@date : 2022/08/01 15:58
'''
import jsonpath

def get_key(res, key):
    # 获得接口返回字段数据
    if res != '':
        try:
            res = res.json()
            value = jsonpath.jsonpath(res, f'$..{key}')
            if value:
                if len(value) == 1:
                    return value[0]
                elif len(value) != 1:
                    for i in value:
                        print(f'{key}-->：{i}')
            else:
                return value
        except Exception as e:
            return e
    else:
        return None