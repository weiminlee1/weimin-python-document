#-*- conding:utf-8 -*-
"""
1,Proxy的设置
urllib2默认会使用环境变量http_proxy来设置HTTP Proxy。
如果想在程序中明确控制Proxy而不受环境变量的影响，可以使用代理。

"""
##例1

import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({'http':'http://some-proxy.com:2222'})
null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
  opener = urllib2.build_opener(proxy_handler)
else:
  opener = urllib2.build_opener(null_proxy_handler)
  
urllib2.install_opener(opener)
'''使用urllib2.install_opener(opener)会设置urllib2的全局opener，
比较好的办法是不使用install_opener去更改全局的设置，而只是直接调用opener.open(url)
的方法代替全局的urlopen()方法'''

"""
2,Timeout设置
urllib2的API并没有暴露Timeout的设置，要设置Timeout值，只能更改Socket的全局Timeout值。

"""
##例2
import urllib2
import socket
socket.setdefaulttimeout(10) #法一：10 seconds后超时
urllib2.socket.setdefaulttimeout(10) #另一方法

response = urllib2.urlopen(url, timeout=10) ##python2.6以后的方法

"""
3,在HTTP Request 中加入特定的Header
要加入header,需要使用Request对象：
对有些header要特别注意，服务器会针对这些header做检查

User-Agent:有些服务器或Proxy会通过该值来判断是否是浏览器发出的请求
Content-Type:在使用REST接口时，服务器会检查该值，用来确定HTTP Body中的内容该怎样解析。
application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
application/json ： 在 JSON RPC 调用时使用
application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
"""

##例3
improt urllib2
request = urllib2.Request('url')
request.add_header('User_Agent','fake-client')
response = urllib2.urlopen(request)
print response.read()
