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
备注：1代表左右方向的维度，0代表上下方向的维度
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

##############################################################################
数据框合并
res = pd.concat([df1,df2,df3],axix=0/1) #数组合并，index,columns要一样

res = pd.concat([df1,df2],join='inner',ignore_index=True) 合并df1,df2适合index不一样

res = pd.concat([df1,df2], axis=1, join_axes=[df1.index]) ##以df1的index为准，df2中缺失的
index由NaN填充

res = df1.append(df2, ignore_index=True) ##在上下方向添加
res = df1.append([df2,df3],ignore_index=True) ##上下方向添加

s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
res = df1.append(s1,ignore_index=True)

##########################################################################
left = pd.DataFrame({'key':['K0','K1','K2','K3'],'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']})

res = pd.merge(left,right,on='key') ##合并left，right两个数据框left.key=right.key
res = pd.merge(left,right,on=['key1','key2'],how='inner') ##left.key1/key2 = right.key1/key2
##how='inner','outer','left','right'
res = pd.merge(df1,df2,on='col1',how='outer',indicator=True) ##显示合并数据的动态过程

res = pd.merge(left,right,left_index=True,right_index=True,how='outer') ##按index进行合并

boys = pd.DataFrame({'k':['k0','k1','k2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['k0','k1','k3'],'age':[4,6,7]})

res = pd.merge(boys,girls, on='k',suffixes=['_boy','_girl'],how='inner')
##inner只显示共同项的，outer则显示全部的


 



