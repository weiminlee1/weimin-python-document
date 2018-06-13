#author:WeiminLee
#-*-coding:utf-8-*-
#date:''
#function=''
'''利用urllib2通过指定的URL抓取网页内容
1,urllib 和 urllib2的区别：
urllib 和 urllib2 多是接受URL请求的相关模块，但是urllib2可以接受一个Request类的实例来设置URL请求的headers, urllib
仅可以接受URL
urllib2.Request()的功能是构造一个请求信息，
urllib2.urlopen()的功能是发送构造好的请求信息，并返回一个文件类Respones。
Response.read()可以读取到response里面的HTML，通过response.info()可以读到一些额外的信息。

2,HTTPError:
服务器上每一个HTTP应答对象response包含一个数字：状态码 urllib.URLError as e: e.code
404-页面无法找到
403-请求禁止
401-待验证请求

3,urllib2中的两个方法：info 和 geturl
urllib2.urlopen()返回的应答对象response有两个很有用的方法info()和geturl()

3.1 response.geturl()
这个返回获取的真实的URL,这个很有用，因为urlopen或许有重定向。获取的URL或许跟请求的URL不同。

3.2 response.info()
这个返回对象的字典对象，该字典描述了获取的页面的情况。通常是服务器发送的特定头headers。
经典的headers包含‘content-length’,‘content-type’

4, urllib2中的两个重要概念：openers和handers。

4.1 Openers
当你获取一个URL你使用一个opener
正常情况下，我们使用默认opener：通过urlopen
但你能够创建个性的openers。
4.2 Handles

'''
