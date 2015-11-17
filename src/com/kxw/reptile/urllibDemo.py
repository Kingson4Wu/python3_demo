#!/usr/bin/python
#  http://obmem.info/?p=476

from urllib import request
import http.cookiejar

''' python 3.x中urllib库和urilib2库合并成了urllib库。。
其中urllib2.urlopen()变成了urllib.request.urlopen()
urllib2.Request()变成了urllib.request.Request() '''

# 1. 最基本的抓站

content = request.urlopen('https://www.baidu.com/').read()
print(content)

# 2.使用代理服务器
'''proxy_support = request.P.ProxyHandler({'http':'http://XX.XX.XX.XX:XXXX'})
opener = request.build_opener(proxy_support, request.HTTPHandler)
request.install_opener(opener)
content = request.urlopen('http://XXXX').read()'''


# 3.需要登录的情况

# 3.1 cookie的处理
cookie_support = request.HTTPCookieProcessor(http.cookiejar.CookieJar)
opener = request.build_opener(cookie_support, request.HTTPHandler)

request.install_opener(opener)

# content = request.urlopen('https://www.baidu.com/').read()

# 3.2 表单的处理

postdata = request.urlencode({
    'username': 'XXXXX',
    'password': 'XXXXX',
    'continueURI': 'http://www.verycd.com/',
    'fk': 'fk',
    'login_submit': '登录'
})

# 然后生成http请求，再发送请求：

req = request.Request(
    url='http://secure.verycd.com/signin/*/http://www.verycd.com/',
    data=postdata
)
result = request.urlopen(req).read()

# 3.3 伪装成浏览器访问
'''某些网站反感爬虫的到访，于是对爬虫一律拒绝请求。这时候我们需要伪装成浏览器，这可以通过修改http包中的header来实现'''
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
req = request.Request(
    url='http://secure.verycd.com/signin/*/http://www.verycd.com/',
    data=postdata,
    headers=headers
)

# 3.4 反”反盗链”
'''某些站点有所谓的反盗链设置，其实说穿了很简单，就是检查你发送请求的header里面，referer站点是不是他自己，所以我们只需要像3.3一样，把headers的referer改成该网站即可，以黑幕著称地cnbeta为例'''
headers = {
    'Referer': 'http://www.cnbeta.com/articles'
}
'''
headers是一个dict数据结构，你可以放入任何想要的header，来做一些伪装。
例如，有些自作聪明的网站总喜欢窥人隐私，别人通过代理访问，他偏偏要读取header中的X-Forwarded-For来看看人家的真实IP，没话说，
那就直接把X-Forwarde-For改了吧，可以改成随便什么好玩的东东来欺负欺负他，呵呵。
'''

# 3.5 终极绝招
'''
有时候即使做了3.1-3.4，访问还是会被据，那么没办法，老老实实把httpfox中看到的headers全都写上，那一般也就行了。
 再不行，那就只能用终极绝招了，selenium直接控制浏览器来进行访问，只要浏览器可以做到的，那么它也可以做到。
 类似的还有pamie，watir，等等等等。
'''

# 4.多线程并发抓取

