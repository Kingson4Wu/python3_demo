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
    'name': 'Runoob',
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
