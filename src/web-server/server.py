#-*- coding:utf-8 -*-
import sys, os
from http.server import BaseHTTPRequestHandler,HTTPServer
import subprocess

class ServerException(Exception):
    '''服务器内部错误'''
    pass
class base_case(object):
    #条件处理基类
    def handle_file(self,handler,full_path):
        try:
            with open(full_path,'rb') as reader:
                content=reader.read()
            handler.send_content(content)
        except IOError as msg:
            msg="'{0}' unable to read".format(full_path,msg)
            handler.handle_error(msg)    

    def index_path(self,handler):
        return os.path.join(handler.full_path,'index.html')
    
    def test(self, handler):
        assert False, 'Not implemented.'

    def act(self, handler):
        assert False, 'Not implemented.'

    
class case_no_file(base_case):
    '''该路径不存在'''
    def test(self,handler):
        return not os.path.exists(handler.full_path)
    def act(self,handler):
        raise ServerException("'{0}' not found".format(handler.path))

class case_existing_file(base_case):
    '''该路径是文件'''
    def test(self,handler):
        return os.path.isfile(handler.full_path)
    def act(self,handler):
        self.handle_file(handler,handler.full_path)

class case_always_fail(base_case):
    '''所有情况都不符合时的默认处理类'''
    def test(self,handler):
        return True
    def act(self,handler):
        raise ServerException("unknow object '{0}'".format(handler.path))



class case_directory_index_file(base_case):
    #在根目录下返回主页文件
    #判断目标路径是否是目录&&目录下是否有index.html
    def test(self,handler):
        return os.path.isdir(handler.full_path) and  os.path.isfile(self.index_path(handler))#self总是指调用时的类的实例。

    #响应index.html的内容
    def act(self,handler):
        self.handle_file(handler,self.index_path(handler))

class case_cgi_file(base_case):
    #脚本文件处理
    def run_cgi(self,handler):
        data=subprocess.check_output(['python3',handler.full_path],shell=False)
        handler.send_content(data)
            
    def test(self,handler):
        return os.path.isfile(handler.full_path) and handler.full_path.endswith('.py')
    
    def act(self,handler):
        self.run_cgi(handler.full_path)

class RequestHandler(BaseHTTPRequestHandler):
    '''
    请求路径合法则返回相应处理
    否则返回错误页面
    '''

    Cases = [case_no_file(),
             case_cgi_file(),#注意这里的顺序，需要先判断是否是需要执行的脚本文件，再判断是否为普通文件
             case_existing_file(),
             case_directory_index_file(),
             case_always_fail()
             ]

    # 错误页面模板
    Error_page="""
    <html>
    <head>Error Page</head>
    <body>
    <h1>Error access<path></h1>
    <p>{msg}</p>
    </body>
    </html>
    
    """


        


    def do_GET(self):
        try:
            # 得到完整的请求路径
            self.full_path=os.getcwd()+self.path
            # 遍历所有的情况并处理
            for case in self.Cases:
                if case.test(self):
                    case.act(self)
                    break

        # 处理异常
        except Exception as msg:
            self.handle_error(msg)

    def handle_error(self, msg):
        content=self.Error_page.format(path=self.path,msg=msg)
        self.send_content(content.encode('utf-8'), 404)

    # 发送数据到客户端
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-length',str(len(content)))
        self.end_headers()
        self.wfile.write(content)

 

if __name__ == '__main__':
    serverAddress=('',8080)
    server=HTTPServer(serverAddress,RequestHandler)
    server.serve_forever()

