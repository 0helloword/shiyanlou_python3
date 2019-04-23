#-*- coding:utf-8 -*-


import wx #引入wx模块
app = wx.App() #实例化一个主循环
frame = wx.Frame(None,-1,title='test',pos=(300,400),size=(300,300)) #实例化一个窗口

"""
None: 当前窗口的父窗口parent，如果当前窗口是最顶层的话，则parent=None,如果不是顶层窗口，则它的值为所属frame的名字
-1: id值, -1的话程序会自动产生一个id
pos: 位置
size: 宽，高大小
还有风格参数style，不填默认是这样几个的组合
wx.MAXIMIZE_BOX| wx.MINIMIZE_BOX| wx.RESIZE_BORDER|wx.SYSTEM_MENU| wx.CAPTION| wx.CLOSE_BOX
你可以去掉几个看看效果，比如
style = wx.SYSTEM_MENU| wx.CAPTION| wx.CLOSE_BOX
"""


frame.Show()#调用窗口展示功能
app.MainLoop()#启动主循环