# -*- coding:utf-8 -*-
__author__ = 'weimin lee'
__date__ = ''
__function__ = ''

"""
1.URLError
首先解释下URLError可能产生的原因：

    网络无连接，即本机无法上网
    连接不到特定的服务器
    服务器不存在
"""
import urllib2

requset = urllib2.Request('http://www.xxxxx.com')
try:
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason

"""
2.HTTPError

HTTPError是URLError的子类，在你利用urlopen方法发出一个请求时，服务器上都会对应一个应答对象response，
其中它包含一个数字”状态码”。
举个例子，假如response是一个”重定向”，需定位到别的地址获取文档，urllib2将对此进行处理。
其他不能处理的，urlopen会产生一个HTTPError，对应相应的状态吗，HTTP状态码表示HTTP协议所返回的响应的状态。
"""
import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason