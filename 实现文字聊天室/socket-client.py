#-*-coding:utf-8-*-
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',1111))
#接受欢迎消息
print(s.recv(1024).decode('utf-8'))

data=[b'fsf',b'xiaowanzi',b'cyj',b'xiaola']

for data in data:
    #发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()