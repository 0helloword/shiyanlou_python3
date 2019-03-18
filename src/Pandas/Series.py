#-*-coding:utf-8-*-
#Pandas 的数据结构：Pandas 主要有 Series（一维数组），DataFrame（二维数组），Panel（三维数组），Panel4D（四维数组），PanelND（更多维数组）等数据结构

import pandas as pd
import abc
#查看pandas版本信息
print(pd.__version__)

#创建serise数据类型 s=pd.Series(data,index=index)
#从列表创建series（一维数组）
arr=[11,22,33,44]
s1=pd.Series(arr)#不指定索引，则默认从0开始
print(s1)
index=['a','b','c','d']
s2=pd.Series(arr,index)
print(s2)
#从Ndarray创建Series
import numpy as np
n=np.random.randn(5)
index2=[1,2,3,4,5]
s3=pd.Series(n,index2)
print(s3)
#从字典创建Series
d={'a':5,'b':2,'c':9}
s3=pd.Series(d)
print(s1[1])
#修改Series索引
s1.index=['aa','bb','cc','d']
print(s1)
#Series纵向拼接
s4=s2.append(s3)
print(s4)
#Series按指定索引删除元素
s5=s4.drop('a')
print(s5)
#修改Series索引元素
s5['b']=10
print(s5)
#Series按指定索引查找元素
print(s5['b'])
print(s5.b)
print(s1[1])
#Series切片操作
print(s1[:2])
#Series加减乘除法运算
print(s1,s2)
print(s1+s2)#索引不同，值为NaN
print(s1-s2)
print(s1*s2)
print(s1/s2)
#Series求中位数
print(s1.median())
#Series求和,最大值，最小值
print(s1.sum())
print(s1.max())
print(s1.min())

