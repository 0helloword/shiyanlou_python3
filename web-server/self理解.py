#-*- coding:utf-8 -*-

#self代表类的实例，而非类
class Stest:
    def p(self):#self就是指类本身
        print(self)#实例可理解为self为实例t，<__main__.Stest object at 0x00000000022A40F0>
        print(self.__class__)#类，<class '__main__.Stest'>

t = Stest()#t为Stest的实例
t.p()

#self总是指调用时的类的实例。
#在继承时，传入的是哪个实例，就是那个传入的实例，而不是指定义了self的类的实例。
class Parent:
    def p(self):
        print(self)

class Child(Parent):
    def c(self):
        print(self)
child = Child()
child.c()
child.p()
parent = Parent()
parent.p()
# parent.c()

#Python中的self用于类的方法中，不可省略
class Student():
    def __init__(self,name):
        self.name=name
    def pname(self):#如果去掉此处的self，提示pname() takes 0 positional arguments but 1 was given
        print('the student name is:',self.name)#如果去掉此处的self，会提示name 'name' is not defined       
s=Student('xiaola')
s.pname()
        
#self也可以换成其他的自己喜欢的词
class Student():
    def __init__(lucy,name):
        lucy.name=name
    def pname(lucy):
        print('the student name is:',lucy.name)        
s=Student('xiaola')
s.pname()

#一个独立的函数不需要加上self参数
def Teather(tname):
    print('the teacher name is:',tname)
Teather('dala')



#当然，加上self独立的函数也不影响，但是没有必要
def Teather(self,tname):
    print('the teacher name is:',tname)
Teather('','dala')#需传入一个空参数


#self的作用主要表示这个变量是类中的公共变量
#在类的一个方法定义了一个变量name1，这个变量就唯一的属于setname这个方法，其他方法无法使用这个变量
#使用self会告诉所有的方法，这个变量是我们共有的，可以随便用
class Student():
    def setname(self):
        name1='jay'            
        self.name='joly'
    def getname(self): 
        print('her name is:',self.name) 
#         print('his name is:',name1)#报错:name 'name1' is not defined
s=Student()
s.setname()
s.getname()

#self的属性，名称前加上两个下划线，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student2():
    def setname(self):  
        self.name1='jay'         
        self.__name2='joly'
    def getname(self): 
        print('her name is:',self.name1,self.__name2) 
s=Student2()
s.setname()
s.getname()
print(s.name1)
print(s.__name2)

#同一个类中调用其他的方法时需要加self
class Test():
    def test1(self):           
        print('this is test1')
    def test2(self): 
        self.test1()#不加self,报错：name 'test1' is not defined
        print('this is test2') 
t=Test()
t.test2()
   