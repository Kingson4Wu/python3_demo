#!/usr/bin/python

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

a = 2 / 4  # 除法，得到一个浮点数
b = 2 // 4  # 除法，得到一个整数
c = 17 % 3  # 取余
d = 2 ** 5  # 乘方

a, b = 1, 2  # Python可以同时为多个变量赋值

''' String '''
s = 'Yes,he doesn\'t'
print(s, type(s), len(s))

print('C:\some\name')
print(r'C:\some\name')

print('str' + 'ing', 'my' * 3)

'''Python中的字符串有两种索引方式，第一种是从左往右，从0开始依次增加；第二种是从右往左，从-1开始依次减少。'''
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])

'''可以对字符串进行切片，获取一段子串。用冒号分隔两个索引，形式为变量[头下标:尾下标]。'''
word = 'ilovepython'
print(word[1:5])
print(word[5:])
print(word[-10:-6])

'''与C字符串不同的是，Python字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。'''

'''List（列表）'''
a = ['him', 25, 100, 'her']
print(a)

a = [1, 2, 3, 4, 5]
a + [6, 7, 8]

'''与Python字符串不一样的是，列表中的元素是可以改变的'''
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
a[2:5] = []  # 删除

'''List内置了有很多方法，例如append()、pop()等等'''

'''Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号里，元素之间用逗号隔开。
元组中的元素类型也可以不相同'''
tup = (1, 2, 3, 4, 5, 6)
print(tup[0], tup[1:5])

tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号

'''元组也支持用+操作符'''
tup1, tup2 = (1, 2, 3), (4, 5, 6)
print(tup1 + tup2)

'''string、list和tuple都属于sequence（序列）'''

'''Sets（集合）
集合（set）是一个无序不重复元素的集。
基本功能是进行成员关系测试和消除重复元素。
可以使用大括号 或者 set()函数创建set集合，注意：创建一个空集合必须用 set() 而不是 { }，因为{ }是用来创建一个空字典。'''

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 重复的元素被自动去掉
'Rose' in student  # membership testing（成员测试）
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素

'''Dictionaries（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。
字典是一种映射类型（mapping type），它是一个无序的键 : 值对集合。
关键字必须使用不可变类型，也就是说list和包含可变类型的tuple不能做关键字。
在同一个字典中，关键字还必须互不相同。'''

dic = {}  # 创建空字典
tel = {'Jack': 1557, 'Tom': 1320, 'Rose': 1886}
print(tel)
print(tel['Jack'])  # 主要的操作：通过key查询
del tel['Rose']  # 删除一个键值对
tel['Mary'] = 4127  # 添加一个键值对
print(tel)
print(list(tel.keys()))  # 返回所有key组成的list
print(sorted(tel.keys()))  # 按key排序
print('Tom' in tel)  # 成员测试
print('Mary' not in tel)  # 成员测试

'''构造函数 dict() 直接从键值对sequence中构建字典，当然也可以进行推导'''
tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(tel)

tel ={x: x**2 for x in (2, 4, 6)}
print(tel)
tel = dict(sape=4139, guido=4127, jack=4098)
print(tel)

'''另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等'''
