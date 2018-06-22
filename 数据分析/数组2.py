#author:WeiminLee
#-*-coding:utf-8-*-
#date:''
#function=''

import numpy as np
import pandas as pd
from pandas import *
"""
Series学习

"""
##法1
series = pd.Series([1,2,3,4,5],index=['first','second','third','fourth','fifth']) ###自己构造索引
print series.index
print series['third']

##法2 字典
mydict = {'first':1,'second':2,'third':3,'fourth':4}
series_mydict = pd.Series(mydict)
print series_mydict
print series_mydict.count() ##返回非空值的数量