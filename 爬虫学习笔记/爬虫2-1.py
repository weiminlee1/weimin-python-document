# -*- coding:utf-8 -*-
__author__ = 'weimin lee'
__date__ = ''
__function__ = ''

"""
1 urllib2.urlopen(url,data,timeout)

url为网址，协议可以是https,ftp,file,http
data是访问url时要传送的数据
timeout设置超时的时间

response = urllib2.urlopen(url).read()
read()为一个方法，可以返回获取到的网页内容
"""
import urllib2
response = urllib2.urlopen('https://www.baidu.com')
print(response.read())


"""
2 构造Request
request请求，构造时需要传入url和data

request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
"""

request = urllib2.Request('https://www.baidu.com')
response = urllib2.urlopen(request)
print(response.read())

"""
3 Post和Get数据传送
3.1 Post
引入urllib的urlencode方法将data编码，构建request时传入两个参数
url和data，运行程序，返回的便是Post后呈现的页面内容
"""
##法一

import urllib
values = {'username':"13283665746@163.com",'password':"xxx"}
data = urllib.urlencode(values)
url = "https://xxxx.com"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()

##法二

values = {}
values['username']='13283665746@163.com'
values['password']='xxx'
data = urllib.urlencode(values)
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()


"""
3.2 Get方式
可以直接把参数写到网址上面，直接构建一个带参数的url出来即可
"""
values = {}
values['username']='13283665746@163.com'
values['password']='xxx'
data = urllib.urlencode(values)

geturl = url + "?" + data

request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.geturl()
print response.read()



