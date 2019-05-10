##set的去重复功能

char_list = ['a','b','c','d','c','d','a']
char_list1 = set(char_list) #返回的是没有重复元素

char_list1.add('x') 添加新元素
char_list.remove('x') 删除存在的元素
char_list.discard('y') 删除元素y，不存在也不报错

set1=['a','b','c']
set2=['a','c','e']

set1.difference(set2)

##pickle存储数据

import pickle
a_dict = {'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}

file = open('pickle_example.pickle','wb')
pickle.dump(a_dict,file) ##pickle把a_dict存入file
file.close()

file = open('pickle_example.pickle','rb')
a_dict1 = pickle.load(file) ##读取文件
file.close()

print（a_dict1）

###with 语句可以自动关闭文件
with open('pickle_example.pickle', 'rb') as file:
  a_dict1 = pickle.load(file)
  
  
  
 ##copy，deepcopy
 import copy
 a = [1,2,3]
 b = a
 id(a)
 id(b) ##id(a)与id(b)一样，改变任一个，两者多改变
 
 c = copy.copy(a)
 id(c) != id(a) ##改变其中一个，另一个并不改变
 
 e = copy.deepcopy(a) ##完全改变id,存储位置改变
 
 
  
  ##多线程
