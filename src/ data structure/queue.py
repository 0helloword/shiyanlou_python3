#队列 (queue) 是一种特殊的线性表，特殊之处在于它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作
#和栈一样，队列是一种操作受限制的线性表。进行插入操作的端称为队尾，进行删除操作的端称为队头。符合先进先出[FIFO]的原则
#以下将以链表的形式实现队列

# class Node():
#     def __init__(self,elem,next=None):
#         self.elem=elem#表示对应的元素值
#         self.next=next#表示下一个链接的链点
#         
# class Queue(object):
#     def __init__(self):
#         self.head=None#头部链接为None
#         self.rear=None#尾部链接为None
# 
#     def is_empty(self):
#         return self.head is None#判断队列是否为空
#     
#     def enqueue(self,elem):#往队列中添加元素
#         p=Node(elem)
#         if self.is_empty():
#             self.head=p
#             self.rear=p
#         else:
#             self.rear.next=p#队列尾部的后继是新节点
#             self.rear=p#使队列尾部指针指向新节点
#             
#     def dequeue(self,elem):#从队列头部删除元素
#         p=Node(elem)
#         if self.is_empty():
#             print('the queue is empty')
#         else:
#             result=self.head.elem#resutl为队列头部元素
#             self.head=self.head.next#将头部指针指向下一个元素
#             return result
#         
#     def peek(self):#查看队列头部元素
#         if self.is_empty():
#             print('the queue is empty')
#         else:
#             result=self.head.elem
#             return result
#     
#     def print_queue(self):
#         print('queue:')
#         myqueue=[]
#         temp=self.head
#         while temp is not None:
#             myqueue.append(temp.elem)
#             temp=temp.next
#         print(myqueue) 
# 
# myqueue=Queue()  
# print(myqueue.is_empty()) 
# myqueue.enqueue(1)
# myqueue.enqueue(2) 
# myqueue.enqueue(3) 
# myqueue.print_queue() 
# print(myqueue.peek())
# myqueue.dequeue(1)
# myqueue.print_queue() 

#以下将以数组的形式实现队列
class Queue():
    def __init__(self):
        self.elems=[]#队列中的参数
        self.front=0#队列头部位置
        self.length=0#队列长度
        
    def enqueue(self,elem):
        self.elems.append(elem)
    
    def dequeue(self):
        self.elems=self.elems[1:]
        return self.elems        
    
    def print_queue(self):
        print(self.elems)
    
    def peek(self):
        return self.elems[0]
    
myqueue=Queue()
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.print_queue()
myqueue.dequeue()
myqueue.print_queue()
print(myqueue.peek())

        



