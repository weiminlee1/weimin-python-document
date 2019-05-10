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
 
 
  
  ##多线程，同一时间分批量运行任务
  import threading
  def thread_job():
    print('this is an added thread, number is %s' % threading.current_thread())
  def main(): ##主函数
    thread_added = threading.Thread(target=thread_job) ##添加线程
    thread_added.start() #执行添加的线程
    print(threading.active_count()) ##显示当前激活的threading数目
    print(threading.enumerate())  ##显示具体的threading
    print(threading.current_thread()) ##显示正在运行的线程
  
  if __name__=='__main__':
    main()
  
  ##################
import threading
import time
def thread_job():
  print('T1 start\n')
  for i in range(10):
      time.sleep(0.1)
  print('T1 finish\n')
 
def main():
  added_thread = threading.Thread(target=thread_job, name = 'T1') ##name 命名
  added_thread.start()
  print('all done\n') ##print这个任务与上面的任务同时进行
  
  added_thread.join() ##join()使T1任务完成后，在进行下一步的print('all done\n')
  pirnt('all done\n')
  
           
