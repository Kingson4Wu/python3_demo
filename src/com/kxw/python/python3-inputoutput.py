#!/usr/bin/python
print()
# 输出格式美化
'''Python两种输出值的方式: 表达式语句和 print() 函数。(第三种方式是使用文件对象的 write() 方法; 标准输出文件可以用 sys.stdout 引用。)
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
str() 函数返回一个用户易读的表达形式。
repr() 产生一个解释器易读的表达形式。'''

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

'''在第一个例子中, 每列间的空格由 print() 添加。
这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
另一个方法 zfill(), 它会在数字的左边填充 0'''

print('12'.zfill(5))
# '00012'
print('-3.14'.zfill(7))
# '-003.14'
print('3.14159265359'.zfill(5))
# '3.14159265359'

# str.format() 的基本使用
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"

'''括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
在括号中的数字用于指向传入对象在 format() 中的位置'''
print('{1} and {0}'.format('spam', 'eggs'))
# eggs and spam

'''如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。'''
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.

'''位置及关键字参数可以任意的结合'''
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))
# The story of Bill, Manfred, and Georg.

# import math
''''!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化'''
# print('The value of PI is approximately {!r}.'.format(math.pi))
# The value of PI is approximately 3.141592653589793.

# ...

'''通过在 table 变量前使用 '**' 来实现相同的功能'''
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

'''旧式字符串格式化
% 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串'''


# 读和写文件
'''open() 将会返回一个 file 对象，基本语法格式如下:
open(filename, mode)'''

f = open('/tmp/workfile', 'w')
'''
第一个参数为要打开的文件名。
第二个参数描述文件如何使用的字符。 mode 可以是 'r' 如果文件只读, 'w' 只用于写 (如果存在同名文件则将被删除), 和 'a' 用于追加文件内容;
所写的任何数据都会被自动增加到末尾. 'r+' 同时用于读写。 mode 参数是可选的; 'r' 将是默认值。'''

'''
f.read()
为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
'''

'''
f.readline()
f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
'''
'''
f.readlines()
f.readlines() 将返回该文件中包含的所有行。
如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
'''
'''迭代一个文件对象然后读取每行'''
for line in f:
    print(line, end='')

'''
f.write()
f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
'''
'''如果要写入一些不是字符串的东西, 那么将需要先进行转换'''
value = ('the answer', 42)
s = str(value)
f.write(s)

'''
f.tell()
f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
'''
'''
f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
from_what 值为默认为0，即文件开头。
'''
f = open('/tmp/workfile', 'rb+')
f.write(b'0123456789abcdef')
# 16
f.seek(5)     # 移动到文件的第六个字节
# 5
f.read(1)
# b'5'
f.seek(-3, 2)  # 移动到文件的倒数第三字节
f.read(1)

'''
f.close()
在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
'''

'''
当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:</p>
'''
with open('/tmp/workfile', 'r') as f:
    read_data = f.read()
f.closed

'''文件对象还有其他方法, 如 isatty() 和 trucate(), 但这些通常比较少用。'''

'''
pickle 模块
python的pickle模块实现了基本的数据序列和反序列化。
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
'''

'''基本接口：
pickle.dump(obj, file, [,protocol])
'''
# 有了 pickle 这个对象, 就能对 file 以读取的形式打开:
'''x = pickle.load(f)
注解：从 file 中读取一个字符串，并将它重构为原来的python对象。
file: 类文件对象，有read()和readline()接口。
'''

# 实例1：
# 使用pickle模块将数据对象保存到文件

import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         #'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()


# 实例2：
# 使用pickle模块从文件中重构python对象

import pprint, pickle

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
