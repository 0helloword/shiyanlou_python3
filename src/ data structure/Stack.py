#-*-coding:utf-8-*-

class stack(object):
    def __init__(self,limit):
        self.stack=[]#存放元素
        self.limit=limit
        
    def push(self,data):
        if len(self.stack)>=self.limit:#判断栈是否溢出
            print('StackOverflowError')
            pass       
        self.stack.append(data)
        return self.stack
            
    def pop(self):
        if self.stack:
            self.stack.pop()
            return self.stack
        else:
            raise IndexError('SackEmpty')

    def peek(self):#查看堆栈的最上面的元素
        if self.stack:
            return self.stack[-1]
        
    def is_empty(self):
        if self.stack:
            return not bool(self.stack)
    def size(self):
        return len(self.stack)
    
    
    def check_parenthesesd(self,data):
        for i in range (int(len(data))):
            print(i)
            if data[i]=='(':
                if data[len(data)-i-1]==')':
                    continue
                else:
                    return False
                    break
        return True

                
                

     
data='())'
a=stack(10)
b=a.check_parenthesesd(data)
print(b)