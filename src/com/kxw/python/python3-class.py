#!/usr/bin/python

print()
'''
和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。
Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
'''
'''
类对象
类对象支持两种操作：属性引用和实例化。
属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
类对象创建后，类命名空间中所有的命名都是有效属性名
'''


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()

'''类定义了 __init__() 方法的话，类的实例化操作会自动调用 __init__() 方法。'''


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)

'''
类的方法
在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
'''
# 类定义


class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法

    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s is speaking: I am %d years old" % (self.name, self.age))


p = People('tom',10,30)
p.speak()

# 继承
'''
需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。
BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用
'''
# 单继承示例


class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g
    # 覆写父类的方法

    def speak(self):
        print("%s is speaking: I am %d years old,and I am in grade %d"%(self.name,self.age,self.grade))


s = Student('ken', 20, 60, 3)
s.speak()

# 多重继承
'''
需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
'''
# 另一个类，多重继承之前的准备


class Speaker():
    topic = ''
    name = ''

    def __init__(self,n,t):
        self.name = n
        self.topic = t

    def speak(self):
        print("I am %s,I am a speaker!My topic is %s"%(self.name,self.topic))

# 多重继承


class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法

'''
类属性与方法
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
类的方法
在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 slef.__private_methods。
类的专有方法：
__init__ 构造函数，在生成对象时调用
__del__ 析构函数，释放对象时使用
__repr__ 打印，转换
__setitem__按照索引赋值
__getitem__按照索引获取值
__len__获得长度
__cmp__比较运算
__call__函数调用
__add__加运算
__sub__减运算
__mul__乘运算
__div__除运算
__mod__求余运算
__pow__称方
'''

