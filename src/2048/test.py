# -*- coding:utf-8 -*-
import wx  
import wx.lib.buttons as buttons  
import random


#未解决问题：按向上箭头后，不知道如何更新gridBox中的数值，(gridBox一直保存了初始化时候的数值)针对2048_win_test的测试

class Frame(wx.Frame):
  
    def __init__(self, title):
        super().__init__(None, title=title, size=(300, 400))   
        self.InitUI()
        
        panel = wx.Panel(self)
        panel.SetFocus()#设置窗口焦点
#         panel.Bind(wx.EVT_CHAR_HOOK, self.onKeyDown)
        self.Centre()
#         self.Show()     
        
    def InitUI(self):  
        self.curScore = 0
        self.bstScore = 0
        self.win=False
#         self.win_value=win
#         self.loadScore()#读取最高分
        
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.label = wx.StaticText(self,label="Tips:Merge the same numbers to 2048 ") 
        self.scorelabel=wx.StaticText(self,label='                 Score:{}    Best:{}'.format(self.curScore,self.bstScore))       
        self.gridBox = wx.GridSizer(4,4,10,10)#创建一个4行4列的网格 rows行数,cols列数,vgap格子之间垂直间隔 ,hgap格子之间水平间隔

        self.datas=['2', ' ', ' ', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '4', ' ', ' ', ' ', ' ']
 
   
        for data in self.datas:
            buttonIterm = wx.Button(self,label=data)
            self.gridBox.Add(buttonIterm,1,wx.EXPAND)
        
          
        self.vbox.Add(self.label,proportion=1, flag=wx.EXPAND, border=1)
        self.vbox.Add(self.scorelabel,proportion=1, flag=wx.EXPAND, border=10)       
        self.vbox.Add(self.gridBox, proportion=7, flag=wx.EXPAND,border=100)
        
        
        
#         self.SetSizer(self.vbox)  
#         self.Show()     
#         self.gridBox = wx.GridSizer(4,4,10,10)
        self.gridBox.ev
        self.datas=['9', ' ', ' ', '2', ' ', ' ', ' ', '9', ' ', ' ', ' ', '4', ' ', ' ', ' ', ' ']
  
    
        for data in self.datas:
            buttonIterm = wx.Button(self,label=data)
            self.gridBox.Add(buttonIterm,1,wx.EXPAND)
                      
         
        self.vbox.Add(self.gridBox, proportion=7, flag=wx.EXPAND,border=10)
         
        
        
        self.SetSizer(self.vbox)  
        self.Show()     
         
        
if __name__ == '__main__':
    app = wx.App(redirect=False)
    Frame(title='2048')
    app.MainLoop()