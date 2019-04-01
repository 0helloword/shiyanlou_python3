#-*-coding:utf-8-*-

import sqlite3

def create_table():#创建表
    try:
        create_tb_cmd='''
        CREATE TABLE IF NOT EXISTS HighScore
        (ID  INT PRIMARY KEY   NOT NULL,
        SCORE  INT DEFAULT 0,
        REMARK  CHAR(50));
        '''
        conn.execute(create_tb_cmd)
        print('Create table success')
    except:
        print ("Create table failed")
        return False
    conn.commit()
     
#连接数据库,有则直接连接，无则创建一个数据库
conn = sqlite3.connect('2048.db')
print ("Opened database successfully") 
    

#插入数据
conn.execute("INSERT INTO HighScore (ID,SCORE,REMARK) VALUES (1, 100, '')")
conn.commit()
print ("Records created successfully")
 
#查询数据
score=conn.execute("select SCORE from HighScore")
for score in score:
    print (score[0])
 
#更新数据
score=99
conn.execute("update HighScore set SCORE ={0} where ID=1".format(score))
conn.commit()
print('update success')
conn.close()



# class sqliteOperate():
#     def __init__(self):
#         self.conn=sqlite3.connect('2048.db')
#     def select(self):
#         score=self.conn.execute("select SCORE from HighScore")
#         for row in score:            
#             return row[0]
#             
#     def update(self,score):
#         self.conn.execute("update HighScore set SCORE ={0} where ID=1".format(score))
#         self.conn.commit()
#         self.conn.close()
#     
# a=sqliteOperate()      
# print(a.select())




