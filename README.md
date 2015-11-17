###python basic
<http://www.runoob.com/python3/python3-tutorial.html>

+ python中数有四种类型：整数、长整数、浮点数和复数。
+ Python中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在Python中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
Python 3中有六个标准的数据类型： <br/>
Numbers（数字）  <br/>
String（字符串） <br/>
List（列表）  <br/>
Tuple（元组）  <br/>
Sets（集合）  <br/>
Dictionaries（字典）  <br/>

---

+ 网络编程 socket库  (select/poll函数)  <br/>
事件驱动的Python网络框架 Twisted
urllib ,urllib2 <br/>
+ 获取网页信息 urllib 
+ 解析HTML Tidy库, HTMLParser, Beautiful Soup
+ CGI 运行服务器创建动态网页 cgi和cgitb模块  
+ mod_python Apache服务器
+ Web应用程序框架和服务器  Zope, Django, Pylon, TurboGears
+ 配置文件 ConfigParser
+ 日志记录 logging

---
+ 测试: doctest, unittest(基于Java的流行框架JUnit),
+ 检查源代码 : Pychecker, PyLint
+ 分析 找到代码的瓶颈 profile模块, hotshot模块

---
+ Python使用命令行工具的方式: subprocess模块
+ 扩展Python : Jython(java), IronPython(C#), CPython(C)
+ 使用Python/C API
+ 程序打包 Distutils (setup.py), 可执行二进制文件Py2exe


---
###pip & easy_install
<http://www.2cto.com/kf/201309/246889.html>
easy_insall的作用和perl中的cpan, ruby中的gem类似，都提供了在线一键安装模块的傻瓜方便方式，而pip是easy_install的改进版, 提供更好的提示信息，删除package等功能。老版本的python中只有easy_install, 没有pip。

+ easy_install的用法：
 
1） 安装一个包
 $ easy_install <package_name>
 $ easy_install "<package_name>==<version>"
 
2) 升级一个包
 $ easy_install -U "<package_name>>=<version>"
 
+ pip的用法
 
1) 安装一个包
 $ pip install <package_name>
 $ pip install <package_name>==<version>
 
2) 升级一个包 (如果不提供version号，升级到最新版本）
 $ pip install --upgrade <package_name>>=<version>
 
3）删除一个包
 $ pip uninstall <package_name> 



