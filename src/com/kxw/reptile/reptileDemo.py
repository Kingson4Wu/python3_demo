#!/usr/bin/python
#  http://obmem.info/?p=476

from urllib import request
from gzip import GzipFile
from io import StringIO
# deflate support
#import zlib

# 5.验证码的处理

# 6 gzip/deflate支持
'''
现在的网页普遍支持gzip压缩，这往往可以解决大量传输时间，以VeryCD的主页为例，未压缩版本247K，压缩了以后45K，为原来的1/5。这就意味着抓取速度会快5倍。
然而python的urllib/urllib2默认都不支持压缩，要返回压缩格式，必须在request的header里面写明’accept-encoding’，
然后读取response后更要检查header查看是否有’content-encoding’一项来判断是否需要解码，很繁琐琐碎。如何让urllib2自动支持gzip, defalte呢？
'''
'''
<http://stackoverflow.com/questions/11914472/stringio-in-python3>
The StringIO and cStringIO modules are gone. Instead, import the io module and use io.StringIO or io.BytesIO for text and data respectively.
'''

# 其实可以继承BaseHanlder类，然后build_opener的方式来处理


class ContentEncodingProcessor(request.BaseHandler):
    # add headers to requests

    def http_request(self, req):
        req.add_header("Accept-Encoding", "gzip, deflate")
        return req

    # decode
    def http_response(self, req, resp):
        old_resp = resp
        # gzip
        if resp.headers.get("content-encoding") == "gzip":
            gz = GzipFile(
                fileobj=StringIO(resp.read()),
                mode="r"
            )
            resp = request.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)
            resp.msg = old_resp.msg
        # deflate
        if resp.headers.get("content-encoding") == "deflate":
            gz = StringIO(deflate(resp.read()))
            resp = request.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)  # 'class to add info() and
            resp.msg = old_resp.msg
        return resp



# def deflate(data):   # zlib only provides the zlib compress format, not the deflate format;
#   try:               # so on top of all there's this workaround:
#     return zlib.decompress(data, -zlib.MAX_WBITS)
#   except zlib.error:
#     return zlib.decompress(data)
