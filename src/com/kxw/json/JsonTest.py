# coding=utf-8
# !/usr/bin/python3

from urllib import request
import json

# http://www.runoob.com/python3/python3-json.html

content = request.urlopen('http://baidu.com', timeout=60).read()
print(content)

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob始数',
    'url': 'http://www.runoob.com',
    'array': ["gg", "cc", "kk"]
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])
for str2 in data2['array']:
    print(str2 + "dddd")

# 写入 JSON 数据
'''
with open('data.json', 'w') as f:
    json.dump(data, f)
'''
# 读取数据

with open('data.json', 'r', encoding="UTF-8") as f:
    data = json.load(f)
print("message ", data['message'])
print("data ", data['data'])
for obj in data['data']:
    print(obj)
