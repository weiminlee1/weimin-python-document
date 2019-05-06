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

dates = pd.date_range('20190101',periods=5)
df = pd.DataFrame(np.random.randn(5,2),index=dates, columns=['a','b'])
df.index ##输出df的索引
df.columns ##输出df的列名
df.dtype ##输出df的数据类型
df.values ##输出df的数值
df.describe() ##输出df的count,mean,min,max,std等

df.sort_index(axis=1,ascending=False) ##按行进行倒序排列
df.sort_index(axis=0,ascending=False) ##按列索引进行倒序排列
df.sort_values(by='a') ##安某列值进行排列

######################################################################################
pandas 选择数据

df['a']/df.a ##输出a列
df[0:3] ##输出前三行
df['20190101':'20190101'] ##
df.loc['20190101']
df.loc[:,['a','b']] ##输出a,b两列
df.loc['20190101',['a','b']]
df.iloc[3:5,:2] ##输出3:5行，前两列
df.iloc[[1,3,5],1:2] ##输出1,3,5行的第1列
df.ix[:3,['a','b']] ##混合模式
df[df.a < 1] ##布尔型筛选数据

df.iloc[2,2] = 111 ##改变df坐标为2,2的值为111

df['c'] = df.a + df.b ##添加新列
df['d'] = np.nan

####################################################################
处理丢失的数据NaN
df.dropna(axis=0, how='all/any') ##all表示这行所有为NaN时丢掉，any则表示这行有NaN就丢掉这行。
df.isnull() ##判断df是否有NaN
np.any(df.isnull()==True) ##判断df是否有NaN,有的话是True,没有的话是False


###########################################################################
读取和存储数据
pd.read_csv(options)
  file=''
  sep=''
 
pd.to_csv(options)

res = pd.concat([df1,df2,df3],axix=0/1) #数组合并，index,columns要一样



