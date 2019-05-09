##python3
##--*--coding:utf-8--*--

##类的学习
class Calculator: ##通用类的定义为首字母大写
  name = 'good calculator' ##定义类的属性
  price = 18 ##定义类的属性
  def add(self,x,y): ##在类中起传递作用，self是沟通类和函数之间的参数
    result = x + y
    print(self.name)
    print(result)
  def minus(self,x,y):
    result = x - y
    print(result)
   def times(self,x,y):
     result = x*y
      print(result)
   def divide(self,x,y):
     result = x/y
     print(result)
 

x = 10
y = 20 
result = Calculator() ####*****
result.add(x,y)
result.minus(x,y)
result.times(x,y)
result.divide(x,y)


#################################################################################
#init 初始initial类定义
class Calculator:
def __init__ (self,name,price,height,width,length,weight):
  self.name = name
  self.price = price
  self.height = height
  self.width = width
  self.length = lenght
  self.weight = weight

cacl = Calculator(name='good',price=13,height=32,width=45,length=23,weight=33) ##f赋予类的初始属性
print(cacl.name)
print(cacl.price)




