#二分搜索
#要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列
# def binarysearch(sorted_list,target):
#     left=0
#     right=len(sorted_list)-1
#     while(left<=right):
#         midpoint=(right+left)//2
#         current_item=sorted_list[midpoint]
#         if target==current_item:
#             return midpoint
#         elif target<current_item:
#             right=midpoint-1
#         else:
#             left=midpoint+1
#     return None
# 
# sorted_list=[1,5,9,34,89,111]
# print(binarysearch(sorted_list, 34))
        
#三分搜索
# def ternary_search(sorted_list,target):
#     left=0
#     right=len(sorted_list)-1       
#     while (left<=right):
#         third1=(right-left)//3+left
#         third2=2*(right-left)//3+left
#         if target==sorted_list[third1]:
#             return third1
#         elif target==sorted_list[third2]:
#             return third2
#         elif target<sorted_list[third1]:
#             right=third1-1
#         elif target>sorted_list[third2]:
#             left=third2+1
#         else:
#             left=third1+1
#             right=third2-1
#     return None
# sorted_list=[1,5,9,34,89,111]
# print(ternary_search(sorted_list, 34))

#快速搜索
# import random
# def partition(sequence,left,right,pivot_index):
#     pivot_value=sequence[pivot_index]
#     sequence[pivot_index],sequence[right]=sequence[right],sequence[pivot_index] #交换两个元素，使pivot_index与最右边元素置换位置，即先将pivot移动到最右边
#     store_index=left
#     for i in range(left,right):
#         if sequence[i]<pivot_value:
#             sequence[store_index],sequence[i]=sequence[i],sequence[store_index] #交换两个元素，使当前遍历元素(小于pivot_value的元素)与store_index元素置换位置
#             store_index=store_index+1 #store_index索引增加1
#     sequence[store_index],sequence[right]=sequence[right],sequence[store_index] #交换两个元素，使store_index与最右边元素置换位置，即交换回来pivot最终应该在的位置
#     return store_index
# def quick_search(sequence,left,right,k):
#     if left==right: #如果只有一个元素
#         return sequence[left] #返回该元素
#     pivot_index=left+random.randint(0,right-left+1) #初始pivot_index，使pivot_index在无序表随机
#     pivot_index=partition(sequence,left,right,pivot_index) #pivot在已经排好序的位置
#     if k==pivot_index:
#         return sequence[k] #返回该位置元素
#     elif k<pivot_index:
#         return quick_search(sequence,left,pivot_index-1,k) #需要在[left,pivot_index-1]里面继续快速检索
#     else:
#         return quick_search(sequence,pivot_index+1,right,k) #需要在[pivot_index+1,right]里面继续快速检索
# if __name__=='__main__':
#     sequence=[12,99,21,34,25,15,35,13,45,100,234,521,2,16,16]
#     left=0
#     right=len(sequence)-1
#     k=int(input("Find the k'th smallest number in sequence,k="))-1
#     value=quick_search(sequence,left,right,k)
#     print("The %s 'th smallest number in sequence is : %s"%(k+1,value))
   
#哈希搜索
class HashTable:
    def __init__(self, size):
        self.elem = [None for i in range(size)] # 使用list数据结构作为哈希表元素保存方法
        self.count = size # 最大表长
    def hash(self, key):
        return key % self.count # 散列函数采用除留余数法
    def insert_hash(self, key):
    #插入关键字到哈希表内
        address = self.hash(key) # 求散列地址
        while self.elem[address]: # 当前位置已经有数据了，发生冲突。
            address = (address+1) % self.count # 线性探测下一地址是否可用
        self.elem[address] = key # 没有冲突则直接保存。
    def search_hash(self, key):
    #查找关键字，返回布尔值
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address + 1) % self.count
            if not self.elem[address] or address == star: # 说明没找到或者循环到了开始的位置
                return False
        return True,address #返回索引值
if __name__ == '__main__':
    list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    hash_table = HashTable(12)
    for i in list_a:
        hash_table.insert_hash(i)
    for i in hash_table.elem:
        if i:
            print((i, hash_table.elem.index(i)), end=" ")
    print("\n")
    print(hash_table.search_hash(15))
    print(hash_table.search_hash(33)) 
            