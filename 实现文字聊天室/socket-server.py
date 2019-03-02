#-*-coding:utf-8-*-
'''
Socket是网络编程的一个抽象概念。
通常我们用一个Socket表示“打开了一个网络链接”，
而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
'''
import socket
import threading
import time
#创建一个基于IPv4和TCP协议的Socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#AF_INET指定使用IPv4协议,SOCK_STREAM指定使用面向流的TCP协议
#绑定监听的地址和端口
s.bind(('127.0.0.1',1111))#参数是一个tuple,包含地址和端口号
#监听端口,传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection……')


#每个连接都必须创建新线程处理，否则单线程在处理连接过程中无法接受其他客户端的连接
def tcplink(sock,addr):
    #连接建立后服务器先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端
    #如果客户端发送了exit字符串，则关闭连接
    print('Accept new connection from %s:%s……' % addr)
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)#每次最多接收1k字节:
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))#decode的作用是将其他编码的字符串转换成unicode编码,encode反之
    sock.close()
    print('Connection from %s:%s closed.' % addr)

    
#服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接   
while True:
    #接受一个新连接
    sock,addr=s.accept()
    #创建新线程来处理TCP连接
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()    
    
    
    
    
    
    


