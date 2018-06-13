#-*- conding:utf-8 -*-
"""
1,Proxy的设置
urllib2默认会使用环境变量http_proxy来设置HTTP Proxy。
如果想在程序中明确控制Proxy而不受环境变量的影响，可以使用代理。

"""
##例子

import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({'http':'http://some-proxy.com:2222'})
null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
  opener = urllib2.build_opener(proxy_handler)
else:
  opener = urllib2.build_opener(null_proxy_handler)
  
urllib2.install_opener(opener)
