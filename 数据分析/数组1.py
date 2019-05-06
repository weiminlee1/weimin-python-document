#author:WeiminLee
#-*-coding:utf-8-*-
#date:''
#function=''

import numpy as np

np1 = np.arange(10)
print np1 ##顺序输出数组
print np1[::-1] ##逆序输出数组
#############################################
"""
数组的构造
1,列表
2,array()函数
"""

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10,11,12]
np_from_list = np.array(list1)
print np_from_list
print np_from_list.shape
print np_from_list.ndim
print np_from_list.size
print np_from_list.dtype
"""
切片
"""
np_from_list12 = np.array([list1,list2])

print np_from_list12[0] ##输出这个数组的第一行
print np_from_list12[:,1] ##输出这个数组的所有行中的第二列

np_from_list1234 = np.array([list1,list1,list2,list2])

print np_from_list1234[:2,:2] ##输出这个数组的前二行和前二列

"""
计算数组
"""

np_from_list12[0].mean()
np_from_list1234[0].std()
np_from_list1234[0].sum()
np_from_list1234[0].prod()

"""
数组的性质
np.shape
np.ndim
np.type
"""
arr.T ##转置，行变成列

A = np.array([1,2,3])
B = np.array([4,5,6])

C = np.vstack([A,B]) ##垂直方向，上下方向合并
D = np.hstack([A,B]) ##水平方向，左右方向合并
E = np.concatenate((A,B,B,A),axis=0/1) ##0代表上下维度，1代表左右维度合并数组

np.split(arr,2,axis=1) ##数组arr进行分裂
np.vsplit(arr,3) ##垂直分割
np.hsplit(arr,2) ##水平分割




