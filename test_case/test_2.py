'''
@file :  test_2.py
@author : 张福卫
@date : 2022/08/02 14:24
'''
import json

d = {'name': '张三',
     'ganmao': '感冒低发期，天气舒适，请注意多吃蔬菜水果，多喝水哦。',
     'sex': '女',
     'age': 18,
     'nide': 'aa'}

# print(type(d))
d['sex']='男'
print(d)

s = json.dumps(d,ensure_ascii=False,sort_keys=True,indent=4)
print('dump的类型',type(s))
print(s)
print('*'*10)

s_d = json.loads(s)
print(type(s_d))
print(s_d)
print('*'*20)
# a = set()
#
#
for key, value in d.items():

    print(key,':',value,end=', ')


print('*'*20,'\n\n')
for i in d.items():
       print(i)
print('*'*20,'\n\n')
print(d.items())
print('*'*20,'\n\n')
for key in d.keys():
     print(key)
for value in d.values():
     print(value)
     print(type(value))

# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# z = dict(zip(key, value))
# print(z)  # Holds an iterator object


# print(a)
# a={'wendu', 'city', 'nide', 'ganmao', 'status'}
# b=a.pop()
# print(b)
# print(a)

# def file_cope(source_file, tatget_file):
#     with open(source_file, 'rb') as source:
#         with open(tatget_file, 'wb') as target:
#             data = source.read(512)
#             while data:
#                 target.write(data)
#                 data = source.read(512)
#
# if __name__ == '__main__':
#
#         file_cope("C:\\Users\\15723\\Desktop\\小结.xmind",
#                   "C:\\Users\\15723\\Desktop\\小结1.xmind")


a='1223344556'
b=list(a)
print(b)
b.pop()
print(b)

a = ['name',2,3]
b = ['张三',5,6]

print(dict(zip(a,b)))