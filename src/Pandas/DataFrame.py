#-*-coding:utf-8-*-
import pandas as pd
import numpy as np
#通过NumPy数组创建DataFrame
dates=pd.date_range('today',periods=5)#定义时间序列为index
num_arr=np.random.randn(5,4)#生成随机数组5行4列，randn是从标准正态分布中返回一个或多个样本值
columns=['A','B','C','D']
df1=pd.DataFrame(num_arr,index=dates,columns=columns)
print(df1)
#通过字典数组创建DataFrame
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
index=[1,2,3,4,5,6,7,8,9,10]
df2=pd.DataFrame(data,index=index)
print(df2)
#查看dataframe的数据类型
print(df2.dtypes)
#dataframe基本操作
print(df2.head())#默认显示前5行，可根据需要填入需要预览的行数
print(df2.tail(3))#默认显示后5行
print(df2.index)#查看索引
print(df2.columns)#查看列名
print(df2.values)#查看数值
#查看dataframe的统计数据
print(df2.describe())
print(df2.T)#转置
print(df2.sort_values(by='age'))#按列排序
print(df2[1:3])#切片
print(df2.loc[2:3])#基于label的索引,通过行标签索引行数据
print([df2.loc[:,'age']>6])
print(df2.iloc[1:3])#完全基于位置的索引,通过行号索引行数据 
print(df2['age'])#通过标签查询单列
print(df2.age)
print(df2[['age','animal']])#通过标签查询多列

#dataframe副本拷贝
df3=df2.copy()
print(df3)
print(df3.isnull())#为空则返回true
#添加列数据
num=pd.Series([11,22,33,44,55,66,77,88,99,98],index=df3.index)
df3['No.']=num
print(df3)
#根据下标值更改内容
df3.iat[1,0]=3#更改第二行第一列的值
print(df3)
#根据标签对数据进行修改
df3.loc[2,'age']=100
print(df3)
#dataframe求平均值操作
print(df3.mean())
#对任意列做求和操作
print(df3['visits'].sum())
#字符串操作
string = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca',
                    np.nan, 'CABA', 'dog', 'cat'])
print(string.str.lower())#转换为小写字母
print(string.str.upper())#转换为大写字母
#对缺失值进行填充
df4=df3.copy()
print(df4.fillna(value='abc'))
#删除存在缺失值的行
df5=df3.copy()
print(df5.dropna(how='any'))#任何存在NaN的行都将被删除
#dataframe文件操作
df3.to_csv('animal.csv')
print("写入成功")
df_animal=pd.read_csv('animal.csv')
print(df_animal)

import openpyxl,xlrd
df3.to_excel('animal.xlsx',sheet_name='Sheet1')
print("写入成功")
df_animal2=pd.read_excel('animal.xlsx','Sheet1')
print(df_animal2)