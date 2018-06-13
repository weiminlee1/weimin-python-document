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
openers使用处理器handlers，所以的工作由handlers处理。
每个handlers知道如何通过特定协议打开URls,或者如何处理URL打开时的各个方面。
例如获取一个能处理cookie的opener，或者获取一个不重定向的opener。

4.2.1
要创建一个opener，可以实例化一个openerdirector
然后调用.add_handler
4.2.2
同样，可以使用build_opener,这是一个更加方便的函数，用来创建opener对象，只需要一次函数调用。
install_opener用来创建（全局）默认opener。这个表示调用URLopen将使用你安装的opener
Opener对象有一个open方法
该方法可以像URLopen函数那样直接用来获取urls:通常不必调用install_opener。
4.2.3
为了展示创建和安装一个Handler,我们将使用HTTPBasicAuthHandle(基本验证）。
'''
# -*-conding:utf-8 -*-
import urllib2

#创建一个密码管理者

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

#添加用户名和密码

top_level_url = "http://example.com/foo/"

#如果知道realm,我们可以使用它代替“None”
#password_mgr.add_password(None,top_level_url,username,password)

password_mgr.add_password(None,top_level_url,'weimin','lee123')

#创建了一个新的handler
handler = urllib2.HTTPBasicAuthHandler(password_mgr)

#创建“opener”
opener = urllib2.build_opener(handler)
a_url = 'http://www.baidu.com/'

#使用opener获取一个URL
opener.open(a_url)

#安装 opener
#现在所有调用urllib2.urlopen()将使用我们定义的opener，而不是默认的。
urllib2.install_opener(opener)
