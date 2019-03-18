#9.self的属性，名称前加上两个下划线，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
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