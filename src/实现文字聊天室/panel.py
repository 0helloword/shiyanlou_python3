#coding:utf-8
import wx
 
def openfile(event):     # 定义打开文件事件
    path = path_text.GetValue()
    with open(path,"r",encoding="utf-8") as f:  # encoding参数是为了在打开文件时将编码转为utf8
        content_text.SetValue(f.read())
 
app = wx.App()
frame = wx.Frame(None,title = "Gui Test Editor",pos = (1000,200),size = (500,400))
 
# path_text = wx.TextCtrl(frame,pos = (5,5),size = (350,24))
# open_button = wx.Button(frame,label = "打开",pos = (370,5),size = (50,24))

panel=wx.Panel(frame)
path_text=wx.TextCtrl(panel)
open_button=wx.Button(panel,label="打开")

open_button.Bind(wx.EVT_BUTTON,openfile)    # 绑定打开文件事件到open_button按钮上
 
# save_button = wx.Button(frame,label = "保存",pos = (430,5),size = (50,24))
save_button=wx.Button(panel,label="保存")

# content_text= wx.TextCtrl(frame,pos = (5,39),size = (475,300),style = wx.TE_MULTILINE)
#  wx.TE_MULTILINE可以实现以滚动条方式多行显示文本,若不加此功能文本文档显示为一行
content_text=wx.TextCtrl(panel,style=wx.TE_MULTILINE)

box=wx.BoxSizer()
box.Add(path_text,proportion=5,flag=wx.EXPAND | wx.ALL,border=3 )
box.Add(open_button,proportion=2,flag=wx.EXPAND | wx.ALL,border=3 )
box.Add(save_button,proportion=2,flag=wx.EXPAND | wx.ALL,border=3 )

v_box=wx.BoxSizer(wx.VERTICAL)
v_box.Add(box,proportion=1,flag=wx.EXPAND | wx.ALL,border=3)
v_box.Add(content_text,proportion=5,flag=wx.EXPAND | wx.ALL,border=3)


panel.SetSizer(v_box)

frame.Show()
app.MainLoop()