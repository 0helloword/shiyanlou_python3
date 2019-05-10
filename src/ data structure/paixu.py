#冒泡法

# def maopao(list):
#     for i in range(1,len(list)):
#         for j in range(0,len(list)-i):
#             if list[j]>list[j+1]:
#                 list[j],list[j+1]=list[j+1],list[j]
#     return list
# 
# list=[12, 27, 46, 16, 25, 37, 22, 29, 15, 47, 48, 34]
# a=maopao(list)
# print(a)
    
    
#选择排序
def xuanze(list):
    newlist=[]
    while list:
        for i in range(1,len(list)-1):
            min=list[i-1]
            if min>list[i]:
                min=list[i]
                newlist.append(min)
                list[i-1],list[i]=list[i],list[i-1]
            else:
                newlist.append(min)


    return newlist

list=[12, 27, 46, 16, 25, 37, 22, 29, 15, 47, 48, 34]
a=xuanze(list)
print(a)