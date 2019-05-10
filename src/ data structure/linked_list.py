class Node():#链点
    def __init__(self,data):
        self.data=data#表示对应的元素值
        self.next=None#表示下一个链接的链点
        
class Linked_List:
    def __init__(self):
        self.head=None#表示链表的头部元素
    
    def initlist(self,data_list):#链表初始化函数
        self.head=Node(data_list[0])  #创建头结点
        temp=self.head
        for i in data_list[1:]:#逐个为data内的数据创建结点，建立链表
            node=Node(i)
            temp.next=node
            temp=temp.next
    
    def is_empty(self):#判断链表是否为空    
        if self.head.next==None:
            print("Linked_list is empty")
            return True
        else:
            return False
        
    def get_length(self):#获取链表的长度
        temp=self.head#临时变量指向队列头部
        length=0#计算链表的长度变量
        while temp!=None:
            length=length+1
            temp=temp.next
        return length  #返回链表的长度
    
    def insert(self,key,value):#链表插入数据
        if key<0 or key>self.get_length()-1:
            print('insert error')
        temp=self.head
        i=0
        while i<=key:#遍历找到索引值为key的结点后，在其后面插入结点
            pre=temp
            temp=temp.next
            i=i+1
        node=Node(value)
        pre.next=node
        node.next=temp

        
    def print_list(self):#遍历链表，并将元素依次打印出来
        print('linked_list:')
        temp=self.head
        new_list=[]
        while temp is not None:
            new_list.append(temp.data)
            temp=temp.next
        print(new_list)
       
    def remove(self,key):#链表删除数据
        if key<0 or key>self.get_length()-1:
            print('delete error')
        i=0
        temp=self.head
        while temp!=None:#遍历找到索引值为key的结点
            pre=temp
            temp=temp.next
            i=i+1
            if i==key:
                pre.next=temp.next
                temp=None
                return True
        pre.next=None 

    def reverse(self):#将链表反转
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev
        
    def swap_nodes(self,d1,d2):#交换单链表里的两个链点
        prevD1=None#d1的前链点
        prevD2=None#d2的前链点
        if d1==d2:#如果两个链点的值相等则不需要做任何处理
            return
        else:
            D1=self.head#通过循环找到d1的链点D1和前链点prevD1
            while D1 is not None and D1.data!=d1:
                prevD1=D1
                D1=D1.next
            D2=self.head#通过循环找到d2的链点D2和前链点prevD2
            while D2 is not None and D2.data!=d2:
                prevD2=D2
                D2=D2.next
            if D1 is None and D2 is None:
                return
            if prevD1 is not None:#将d1的前链点的后链点改为D2
                prevD1.next=D2
            else:
                self.head=D2
            if prevD2 is not None:#将d2的前链点的后链点改为D1
                prevD2.next=D1
            else:
                self.head=D1
            temp=D1.next#交换D1和D2的后链点
            D1.next=D2.next
            D2.next=temp
                  
        
l=Linked_List()
datalist=[1]
l.initlist(datalist)
print(l.is_empty())
l.print_list() 
print('the length is '+str(l.get_length()))
l.insert(0, 5)        
l.print_list() 
l.remove(1)
l.print_list()
l.reverse()
l.print_list()
l.insert(0, 2)
l.insert(1, 3)
l.insert(2, 4)
l.insert(3, 5)
l.swap_nodes(3, 5)
l.print_list()