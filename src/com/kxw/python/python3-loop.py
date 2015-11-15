#!/usr/bin/python

# Python中的循环语句有 for 和 while。
n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("Sum of 1 until %d: %d" % (n, sum))

# for语句
edibles = ["ham", "spam", "eggs", "nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")

# range()函数
'''如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列 '''

for i in range(5):
    print(i)

'''使用range指定区间的值 '''
for i in range(5, 9):
    print(i)

'''使range以指定数字开始并指定不同的增量(甚至可以是负数;有时这也叫做'步长)'''
for i in range(0, 10, 3):
    print(i)

for i in range(-10, -100, -30):
    print(i)

'''结合range()和len()函数以遍历一个序列的索引'''
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

'''使用range()函数来创建一个列表'''
tel = list(range(5))
print(tel)

'''break和continue语句及循环中的else子句'''

'''pass语句什么都不做。它只在语法上需要一条语句但程序不需要任何操作时使用.'''
while True:
    pass  # 等待键盘中断 (Ctrl+C)
