import wx
import telnetlib
from time import sleep
import _thread as thread

class LoginFrame(wx.Frame):
    """
    登录窗口
    """
    def __init__(self, parent, id, title, size):
        # 初始化，添加控件并绑定事件
        wx.Frame.__init__(self, parent, id, title)
        self.SetSize(size)#自动调节窗口大小
        self.Center()#设置登录弹窗在桌面中心
        self.serverAddressLabel = wx.StaticText(self, label="Server Address", pos=(10, 50), size=(120, 25))
        self.userNameLabel = wx.StaticText(self, label="UserName", pos=(40, 100), size=(120, 25))
        self.serverAddress = wx.TextCtrl(self, pos=(120, 47), size=(150, 25))
        self.userName = wx.TextCtrl(self, pos=(120, 97), size=(150, 25))
        self.loginButton = wx.Button(self, label='Login', pos=(80, 145), size=(130, 30))
        # 绑定登录方法
        self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        self.Show()#显示以上控件

    def login(self, event):
        # 登录处理
        try:
            serverAddress = self.serverAddress.GetLineText(0).split(':')
            con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)
            response = con.read_some()
            if response != b'Connect Success':
                self.showDialog('Error', 'Connect Fail!', (200, 100))
                return
            con.write(('login ' + str(self.userName.GetLineText(0)) + '\n').encode("utf-8"))
            loginname=str(self.userName.GetLineText(0))
            print(loginname)
            response = con.read_some()
            if response == b'UserName Empty':
                self.showDialog('Error', 'UserName Empty!', (200, 100))
            elif response == b'UserName Exist':
                self.showDialog('Error', 'UserName Exist!', (200, 100))
            else:
                self.Close()
                ChatFrame(None, 2, title='ShiYanLou Chat Client - '+loginname, size=(500, 400))
        except Exception:
            self.showDialog('Error', 'Connect Fail!', (200, 150))

    def showDialog(self, title, content, size):
        # 显示错误信息对话框
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label=content)
        dialog.ShowModal()

class ChatFrame(wx.Frame):
    """
    聊天窗口
    """

    def __init__(self, parent, id, title, size):
        # 初始化，添加控件并绑定事件
        wx.Frame.__init__(self, parent, id, title)
        self.SetSize(size)
        self.Center()
        self.chatFrame = wx.TextCtrl(self, pos=(5, 5), size=(550, 310), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.message = wx.TextCtrl(self, pos=(5, 320), size=(300, 25))#设置文本输入框的位置和尺寸
        self.sendButton = wx.Button(self, label="Send", pos=(310, 320), size=(58, 25))
        self.usersButton = wx.Button(self, label="Online Users", pos=(373, 320), size=(90, 25))
        self.closeButton = wx.Button(self, label="Close", pos=(436, 320), size=(58, 25))
        # 发送按钮绑定发送消息方法
        self.sendButton.Bind(wx.EVT_BUTTON, self.send)
        # Users按钮绑定获取在线用户数量方法
        self.usersButton.Bind(wx.EVT_BUTTON, self.lookUsers)
        # 关闭按钮绑定关闭方法
        self.closeButton.Bind(wx.EVT_BUTTON, self.close)
        thread.start_new_thread(self.receive, ())#新增一个线程来处理接收服务器消息
        self.Show()

    def send(self, event):
        # 发送消息
        message = str(self.message.GetLineText(0)).strip()
        if message != '':
            con.write(('say ' + message + '\n').encode("utf-8"))#通过write写给服务器端
            self.message.Clear()

    def lookUsers(self, event):
        # 查看当前在线用户
        con.write(b'look\n')

    def close(self, event):
        # 关闭窗口
        con.write(b'logout\n')
        con.close()
        self.Close()

    def receive(self):
        # 接受服务器的消息
        while True:
            sleep(0.6)
            result = con.read_very_eager()#不断接收来自服务器的消息
            if result != '':
                self.chatFrame.AppendText(result)#将消息显示在聊天窗口中

if __name__ == '__main__':
    app = wx.App()
    con = telnetlib.Telnet()
    LoginFrame(None, -1, title="Login", size=(320, 250))
    app.MainLoop()

#拓展   
#3个用户，给指定的用户发送消息，其他人收不到
#python3.6使用asyncio+tkinter重写程序