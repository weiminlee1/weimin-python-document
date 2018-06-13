#author:WeiminLee
#-*-coding:utf-8-*-
#date:''
#function=''
'''利用urllib2通过指定的URL抓取网页内容
1,urllib 和 urllib2的区别：
urllib 和 urllib2 多是接受URL 请求的相关模块，但是urllib2可以接受一个Request类的实例来设置URL请求的headers, urllib
仅可以接受URL
urllib2.Request()的功能是构造一个请求信息，
urllib2.urlopen()的功能是发送构造好的请求信息，并返回一个文件类Respones。
Response.read()可以读取到response里面的HTML，通过response.info()可以读到一些额外的信息。

2,HTTPError:
服务器上每一个HTTP应答对象response包含一个数字：状态码 urllib.URLError as e: e.code
404-页面无法找到
403-请求禁止
401-待验证请求
'''
