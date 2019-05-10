'''
设计队列的实现( 在这里我们要求用之前介绍的链表形式实现 )
在队列中实现这些步骤：
1.初始化创建 Node, Queue 类
2.依次添加 21 35 58 13 进队列
3.返回队列头部元素
4.删除此时队列头部元素
5.返回此时队列头部元素
'''

class Node():
    def __init__(self,elem):
        self.elem=elem
        self.next=None
        
class Queue(object):
    def __init__(self):
        self.head=None
        self.rear=None
    
    def is_empty(self):
        return self.head is None
       
    def add(self,elem):
        p=Node(elem)
        if self.is_empty():
            self.head=p
            self.rear=p
        else:
            self.rear.next=p
            self.rear=p
     
    def dequeue(self):
        if self.is_empty():
            print('the queue is empty')
        else:
            temp=self.head.next
            self.head=temp
            
        
    def print_queue(self):
        list=[]
        temp=self.head
        while temp is not None:
            list.append(temp.elem)
            temp=temp.next
        print(list)
    
    def peek(self):
        if self.is_empty():
            print('the queue is empty')
        else:
            result=self.head.elem
            return result
    
myqueue=Queue()
myqueue.add(21)
myqueue.add(35)
myqueue.add(58)
myqueue.add(13)
myqueue.print_queue()
print(myqueue.peek())
myqueue.dequeue()
myqueue.print_queue()
print(myqueue.peek())