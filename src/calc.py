# -*- coding: utf-8 -*-
import wx

class CalcFrame(wx.Frame):
  
    def __init__(self, title):
        super(CalcFrame, self).__init__(None, title=title, 
            size=(350, 300))
            
        self.InitUI()
        self.Centre()
        self.Show()     
        
    def InitUI(self):     
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.textprint = wx.TextCtrl(self, -1,style=wx.TE_RIGHT|wx.TE_READONLY)#-1表示不支持键盘输入
        self.equation=""#用来存储textprint的内容。通过self.textprint.SetValue(self.equation)就可以把equation的内容显示在textprint上

        vbox.Add(self.textprint, 2, flag=wx.EXPAND, border=4)
        
        gridBox = wx.GridSizer(5,4,5,5)#创建一个5行4列的网格 rows行数,cols列数,vgap格子之间垂直间隔 ,hgap格子之间水平间隔


        labels=['AC','DEL','pi','CLOSE','7','8','9','/','4','5','6',
                '*','1','2','3','-','0','.','=','+']
        for label in labels:
            buttonIterm = wx.Button(self,label=label)
            self.createHandler(buttonIterm,label)
            gridBox.Add(buttonIterm, 1, wx.EXPAND)
           
        vbox.Add(gridBox, proportion=7, flag=wx.EXPAND)
        self.SetSizer(vbox)

    #创建按钮处理方法
    def createHandler(self,button,labels):
        item = "DEL AC = CLOSE"
        if labels not in item:
            self.Bind(wx.EVT_BUTTON,self.OnAppend,button)
        elif labels == 'DEL':
            self.Bind(wx.EVT_BUTTON,self.OnDel,button)
        elif labels == 'AC':
            self.Bind(wx.EVT_BUTTON,self.OnAc,button)
        elif labels == '=':
            self.Bind(wx.EVT_BUTTON,self.OnTarget,button)
        elif labels == 'CLOSE':
            self.Bind(wx.EVT_BUTTON,self.OnExit,button)
            
    #添加运算符与数字
    def OnAppend(self,event):
        eventbutton = event.GetEventObject()
        label = eventbutton.GetLabel()
        self.equation += label
        self.textprint.SetValue(self.equation)
    def OnDel(self,event):
        self.equation = self.equation[:-1]#删掉最后一个字符
        self.textprint.SetValue(self.equation)
    def OnAc(self,event):
        self.textprint.Clear()
        self.equation=""
    def OnTarget(self,event):
        string = self.equation
        try:
            target = eval(string)#eval返回传入字符串的表达式的结果
            self.equation = str(target)
            self.textprint.SetValue(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'格式错误，请输入正确的等式!',
                                u'请注意', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            
    def OnExit(self,event):
        self.Close()
        
if __name__ == '__main__':
  
    app = wx.App()
    CalcFrame(title='Calculator')
    app.MainLoop()