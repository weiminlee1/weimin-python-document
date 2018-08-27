# -*- coding:utf-8 -*-
__author__ = 'weimin lee'
__date__ = ''
__function__ = ''
#python version:3

print('hello world')

python 学习笔记

1.可哈希（hashable）和不可改变性（immutable）

如果一个对象在自己的生命周期中有一哈希值（hash value）是不可改变的，那么它就是可哈希的（hashable）的，
因为这些数据结构内置了哈希值，每个可哈希的对象都内置了__hash__方法，所以可哈希的对象可以通过哈希值进行对比，
也可以作为字典的键值和作为set函数的参数。所有python中所有不可改变的的对象（imutable objects）都是可哈希的，
比如字符串，元组，也就是说可改变的容器如字典，列表不可哈希（unhashable）。
我们用户所定义的类的实例对象默认是可哈希的（hashable），它们都是唯一的，而hash值也就是它们的id()。

2.  哈希
