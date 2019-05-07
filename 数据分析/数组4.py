import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x,y1)

plt.figure(num=3, figsize=(8,5)) ##设置figure的名字和画布大小
l1 = plt.plot(x,y2,label='up')
l2 = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down') ##一个画布显示两个数据
plt.legend(handles=[l1,l2],labels=['x','y'],loc='best') ##设置图例的位置,并且命名图例元素的名字,loc='best'自动设置图例位置最合理处
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


##添加标注
#找到添加标注的位置
x0 = 0.5
y0 = 2*xo + 1
plt.scatter(x0,y0,s=50, color='b') ##s=size
plt.plot([x0,x0],[y0,0],'k--',lw=2.5) ##k==black,--代表虚线

##法1
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='
             offset points',fontsize=16, arrowprops=dict(arrowstyle='->',connetionstyle
            ='arc3,rad=.2')) ##


##法2     
plt.text(-3.7,3,r'$This is the some text.\\mu\\sigma_i\\alpha_t$',fontdict={'size':16,'color':'r'})
plt.show()

