import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x,y1)

plt.figure(num=3, figsize=(8,5)) ##设置figure的名字和画布大小
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--') ##一个画布显示两个数据
plt.xlim((-1,2)) ##设置坐标轴x的取值范围
plt.ylim((-2,3))
plt.xlabel('x轴') ##设置坐标轴的名称
plt.ylabel('y轴')

new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks) ##设置x轴的刻度
plt.yticks([-2,-1.8,-1,1.22,3],['really bad','bad','normal','good','really good'])

##gca = 'get current axis'
##改变坐标轴的位置
ax = plt.gca()
ax.spines['right'].set_color('none') ##去掉右边框
ax.spines['top'].set_color('none') ##去掉顶部边框
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data',0)) ##移动底部边框的位置
ax.spines['left'].set_position(('data',0))   ##移动左边框的位置
plt.show()

