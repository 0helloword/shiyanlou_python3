# -*- coding:utf-8 -*-

import wx
import random
import os
import copy
from random import choice, randrange
import operator
from functools import reduce

class Frame(wx.Frame):
  
    def __init__(self, title):
        super().__init__(None, title=title, size=(300, 400))   
        self.InitUI()
        
        panel = wx.Panel(self)
        panel.SetFocus()#设置窗口焦点
        panel.Bind(wx.EVT_CHAR_HOOK, self.onKeyDown)
        self.Centre()
        self.Show()     
        
    def InitUI(self):  
        self.curScore = 0
        self.bstScore = 0
        self.win=False
#         self.win_value=win
        self.loadScore()#读取最高分
        
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.label = wx.StaticText(self,label="Tips:Merge the same numbers to 2048 ") 
        self.scorelabel=wx.StaticText(self,label='                 Score:{}    Best:{}'.format(self.curScore,self.bstScore))       
        self.gridBox = wx.GridSizer(4,4,10,10)#创建一个4行4列的网格 rows行数,cols列数,vgap格子之间垂直间隔 ,hgap格子之间水平间隔

        self.datas=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']#一维数组
        self.datas_new=[[],[],[],[]]#二维数组
 
        count = 0          
        #初始化生成2个数字
        while count < 2:
            i = random.randint(0, 15)#随机生成行列号
            if self.datas[i] != ' ':
                continue
            self.datas[i] =str(2) if random.randint(0, 1) else str(4)
            count += 1
        for data in self.datas:
            buttonIterm = wx.Button(self,label=data)
            self.gridBox.Add(buttonIterm,1,wx.EXPAND)
        
          
        self.vbox.Add(self.label,proportion=1, flag=wx.EXPAND, border=1)
        self.vbox.Add(self.scorelabel,proportion=1, flag=wx.EXPAND, border=10)       
        self.vbox.Add(self.gridBox, proportion=7, flag=wx.EXPAND,border=100)
        
        self.SetSizer(self.vbox)

    def show(self): 
        print(self.datas)
        self.gridBox = wx.GridSizer(4,4,10,10)
        for data in self.datas:
            print(data)
            buttonIterm = wx.Button(self,label=data)
            self.gridBox.Add(buttonIterm,1,wx.EXPAND) 

        self.vbox.Add(self.gridBox, proportion=7, flag=wx.EXPAND,border=100)
        
        self.SetSizer(self.vbox)  
        self.Show()      



    def onKeyDown(self, event):
        '与按键事件中得到对应的键码'
        keyCode = event.GetKeyCode()
        if keyCode == wx.WXK_UP:#doMove的参数是slideUpDown或者slideLeftRight方法返回的元组。 *代表元组，**代表字典,返回true(false)和score
            self.doMove(*self.slideUpDown(True))
#         elif keyCode == wx.WXK_DOWN:
#             self.doMove(*self.slideUpDown(False))
#         elif keyCode == wx.WXK_LEFT:
#             self.doMove(*self.slideLeftRight(True))
#         elif keyCode == wx.WXK_RIGHT:
#             self.doMove(*self.slideLeftRight(False))
#         elif keyCode == 27:#点击esc，关闭退出游戏
#             self.Close()
#         elif keyCode == 13:#点击enter，重新开始游戏
#             self.initGame(self.win_value)
#             self.drawAll()

    def loadScore(self):
        if os.path.exists('bestScore.ini'):
            ff = open('bestScore.ini')
            self.bstScore = int(ff.read())
            ff.close()
            
    def slideUpDown(self, up):
        self.datas_new=self.turnTwoDimensionalList(self.datas)
        print(self.datas_new)
        score = 0
        numCols = len(self.datas_new[0])
        numRows = len(self.datas_new)
        '复制列表中的所有结构与数据'
        oldData = copy.deepcopy(self.datas_new)
 
        for col in range(numCols):
            '得以列值为序且不为0的列表'
            cvl = [self.datas_new[row][col] for row in range(numRows) if
                   self.datas_new[row][col] != ' ']
            '改变score以及对列中的值进行合并，删除cvl中合并前可合并的两个数中的一个，另一个翻倍改变'
#             if len(cvl) >= 2:
#                 score += self.update(int(cvl), up)
            '通过cvl中的个数来添加或是插入0值，保持cvl中列表个数为4个'
            for i in range(numRows - len(cvl)):
                if up:
                    cvl.append(' ')
                else:
                    cvl.insert(' ',' ')
            '将改变后的数据放入原始变量中'
            for row in range(numRows):
                self.datas_new[row][col] = cvl[row]
 
        '比较当前数据与原始数据是否发生变化'
        print(oldData != self.datas_new, score)
        return oldData != self.datas_new, score

    def update(self, vlist, direct):
        score = 0
        '向up或left移动则执行'
        if direct:
            i = 1
            '最多判断执行一次，如果相邻的两位数相等，则删掉后一位，前一位分数翻倍'
            while i < len(vlist):
                if vlist[i-1] == vlist[i]:
                    del vlist[i]
                    vlist[i-1] *= 2
                    score += vlist[i-1]
                    i += 1
                i += 1
        else:#'向down或right移动则执行'
            i = len(vlist) - 1
            while i > 0:
                if vlist[i-1] == vlist[i]:
                    del vlist[i]
                    vlist[i-1] *= 2
                    score += vlist[i-1]
                    i -= 1
                i -= 1
        print(score)
        return score

    def turnTwoDimensionalList(self,datas):
        def partition(lst, partition_size):
            if partition_size < 1:
                partition_size = 1
            return [
                lst[i:i + partition_size]
                for i in range(0, len(lst), partition_size)
                        ]
        newlist=partition(datas, 4)
        return newlist
    
    
    def turnList(self,datas):
        return reduce(operator.add, datas)

    def doMove(self, move, score):
        if self.win==False:#先判断游戏是否胜利
            if move:           
                self.putTile()#'每移动一次则生成一个2或4'
#                 self.drawChange(score)
#                 if self.curScore>=self.win_value:
#                     self.winGame(move, score)
#                 if self.isGameOver():
#                     if wx.MessageBox('游戏结束，是否重新开始?', '(*^▽^*)',
#                                      wx.YES_NO|wx.ICON_INFORMATION) == wx.YES:
#                         bstScore = self.bstScore
#                         self.initGame(self.win_value)
#                         self.bstScore = bstScore
#                         self.drawAll()
#         else:
#             if move:           
#                 self.putTile()#'每移动一次则生成一个2或4'
#                 self.drawChange(score)
#                 if self.isGameOver():
#                     if wx.MessageBox('游戏结束，是否重新开始?', '(*^▽^*)',
#                                      wx.YES_NO|wx.ICON_INFORMATION) == wx.YES:
#                         bstScore = self.bstScore
#                         self.initGame(self.win_value)
#                         self.bstScore = bstScore
#                         self.drawAll()
                
    def putTile(self):
        new_element = 4 if randrange(100) > 89 else 2#9:1的比例生成2或4
        #通过choice随机选择一个未被占领的位置来放置new_element
#         print(self.datas_new)
        (row,col) = choice([(row,col) for row in range(len(self.datas_new)) for col in range(len(self.datas_new[0])) if self.datas_new[row][col] == ' '])
        self.datas_new[row][col] = str(new_element)
#         print(self.datas_new)
        self.datas=self.turnList(self.datas_new)

        print(self.datas)
        self.show()

       
if __name__ == '__main__':
    app = wx.App(redirect=False)
    Frame(title='2048')
    app.MainLoop()