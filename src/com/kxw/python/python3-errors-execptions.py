#!/usr/bin/python

# Python有两种错误很容易辨认：语法错误和异常。
import sys
'''
try语句按照如下方式工作；
首先，执行try子句（在关键字try和关键字except之间的语句）
如果没有异常发生，忽略except子句，try子句执行后结束。
如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
'''

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

'''
try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。
'''
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

'''
使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到的、而except又没有捕获的异常。
异常处理并不仅仅处理那些直接发生在try子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。
'''
def this_fails():
    x = 1/0

try:
   this_fails()
except ZeroDivisionError as err:
        print('Handling run-time error:', err)


# 抛出异常
''' Python 使用 raise 语句抛出一个指定的异常。'''
raise NameError('HiThere')

'''raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

'''
用户自定义异常
你可以通过创建一个新的exception类来拥有自己的异常。异常应该继承自 Exception 类，或者直接继承，或者间接继承
'''


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2 * 2)
except MyError as e:
    print('My exception occurred, value:', e.value)

'''在这个例子中，类 Exception 默认的 __init__() 被覆盖。
当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类'''


'''
定义清理行为
try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。
'''
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

'''
以上例子洪不管try子句里面有没有发生异常，finally子句都会执行。
如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后再次被抛出。
'''

'''预定义的清理行为'''
'''关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法'''
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
