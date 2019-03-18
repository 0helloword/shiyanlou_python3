#-*-coding:utf-8-*-
import pandas as pd
import numpy as np

# #建立一个以 2018年1月的每一天为索引，值为随机数的 Series
# index=pd.date_range(start='2018-01-01',end='2018-01-31',freq='D')
# data=np.random.rand(len(index))
# s1=pd.Series(data,index)
# print(s1)
# #统计s1中每一个周三对应值的和
# print(s1[s1.index.weekday==2].sum())
# #统计s1中每个月值的平均值
# print(s1.resample('M').mean())
# #将时间转换为分钟
# s=pd.date_range('today',periods=10,freq='S')
# s2=pd.Series(np.random.randint(0,500,len(s)),index=s)#生成10个在0-500间的随机数
# print(s2)
#不同时间表示方式的转换
# rng=pd.date_range('1/1/2018',periods=5,freq='M')
# ts=pd.Series(np.random.randn(len(rng)),index=rng)
# print(ts)
# ps=ts.to_period()
# print(ps)
# ps.to_timestamp()
# print(ps)
#创建多重索引Series
# letters=['A','B','C']
# numbers=list(range(5))
# data=np.random.rand(15)
# mi=pd.MultiIndex.from_product([letters,numbers])#设置多重索引
# s=pd.Series(data,index=mi)
# print(s)
# #多重索引Series查询
# print(s.loc[:,[1,3]])
# print(s.loc[pd.IndexSlice[:'B',4:]])#切片
#创建多索引dataframe
# ni=[list('AAABBB'),list('123123')]
# data=np.arange(12).reshape(6,2)#reshape调整矩阵的行数，列数
# columns=['hello','shiyanlou']
# s=pd.DataFrame(data,index=ni,columns=columns)
# print(s)
# #多重索引设置列名称
# s.index.names=['first','second']
# print(s)
# print(s.groupby('first').sum())#多重索引分组求和
# print(s.stack())#dataframe行列名称转换
# print(s.unstack())#索引转换
#dataframe条件查找
# data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
#         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
# 
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(data, index=labels)
# print(df)
# print(df[df['age']>3])#查找age大于3的全部信息
# print(df[df.loc[:,'age']>3])
# print(df.iloc[2:4,1:3])#根据行列索引切片
# print(df[(df['age']<3) & (df['animal']=='cat')])#查找age<3且为cat的全部数据
# print(df[df['animal'].isin(['cat'])])
# print(df.loc[df.index[[1,2]],['age','visits']])#按标签及列名查询
# print(df.sort_values(by=['age','visits'],ascending=[False,True]))#按照 age 降序，visits 升序排列
# print(df['priority'].map({'yes':True,'no':False}))#将 priority 列的 yes 值替换为 True，no 值替换为 False
# print(df.groupby('animal').sum())#分组求和
# #使用列表拼接多个dataframe
# temp1=pd.DataFrame(np.random.randn(5,4))
# temp2=pd.DataFrame(np.random.randn(5,4))
# temp=[temp1,temp2]
# print(temp)
# print(temp1.sum().idxmax())#找出表中和最大的列
# #dataframe中每个元素减去每一行的平均值
# print(temp1.sub(temp1.mean(axis=1),axis=0))#axis=1表示按行求平均值
#DataFrame 分组，并得到每一组中最大2个数之和
df=pd.DataFrame({'A':list('abad'),'B':[11,33,44,22]})
print(df)
print(df.groupby('A')['B'].nlargest(2).sum(level=0))

