# -*- coding:utf-8 -*-
__author__ = 'weimin lee'
__date__ = ''
__function__ = ''

"""
1 设置Headers
如果识别有问题，那么站点根本不会响应，
所以为了完全模拟浏览器的工作，我们需要设置一些Headers 的属性

agent就是请求的身份，
如果没有写入请求身份，那么服务器不一定会响应，
所以可以在headers中设置agent
"""
import urllib
import urllib2
url = 'https://www.baidu.com'
values = {}
values['username']='13283665746@163.com'
values['password']="xxx"
data = urllib.urlencode(values)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User_Agent':user_agent}
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
print response.read()

"""
2 代理（proxy）的设置
urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。
假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，
它会禁止你的访问。所以你可以设置一些代理服务器来帮助你做工作，
每隔一段时间换一个代理
"""

import urllib2
enable_proxy =True
proxy_handle = urllib2.ProxyHandler({'http':'http://some-proxy.com:8080'})
null_proxy = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handle)
else:
    opener = null_proxy
urllib2.install_opener(opener) ##设置全局
url = 'https://www.baidu.com'
values = {}
values['username']='xxx'
values['password']='xxx'
data = urllib.urlencode(values)
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
request = urllib2.Request(url,data, headers)
response = urllib2.urlopen(request,timeout=10)
##response = urllib2.opener(request)