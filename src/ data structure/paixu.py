#冒泡法

# def maopao(list):
#     for i in range(0,len(list)-1):
#         for j in range(i+1,len(list)):
#             if list[i]>list[j]:
#                 list[i],list[j]=list[j],list[i]
#             
#     return list
# list=[12, 27, 46, 16, 25, 37, 22, 29, 15, 47, 48, 34]
# a=maopao(list)
# print(a)
    
    
#选择排序
# 首先在未排序序列中找到最小元素，存放到排序序列的起始位置；
# 再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾；
# 重复第二步，直到所有元素均排序完毕
def xuanze(list):
    for i in range(0,len(list)-1):
        minIndex=i
        for j in range(i+1,len(list)):
            if list[minIndex]>list[j]:
                minIndex=j
            list[minIndex],list[i]=list[i],list[minIndex]           
    return list
list=[12, 27, 46, 16, 25, 37, 22, 29, 15, 47, 48, 34]
a=xuanze(list)
print(a)

