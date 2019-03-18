#-*-coding:utf-8-*-

from PIL import Image
import os

def draw_qrcode(abspath,qrmatrix):#画一个33*33的图片
    unit_len=3
    x=y=4*unit_len
    pic=Image.new('1',[(len(qrmatrix)+8)*unit_len]*2,'White')#mode=1,size=33*33
#     print(pic)
    #循环矩阵中的单位，在需要涂黑的单位启用draw_a_black_unit函数涂黑
    for line in qrmatrix:
        for module in line:
            if module:
                draw_a_black_unit(pic,x,y,unit_len)
            x+=unit_len
        x,y=4*unit_len,y+unit_len
    print(x,y)    
    saving=os.path.join(abspath,'qrcode.png')
    pic.save(saving)
    return saving 

def draw_a_black_unit(p,x,y,ul):#画一个小黑块
    for i in range(ul):
        for j in range(ul):
            p.putpixel((x+i,y+j),0)#putpixel(xy, color) 改变单个像素点颜色，0为黑色，1为白色
            
a=draw_qrcode('F:/test/workspace/实验室/qrcode/MyQR1/source','123')#路径用斜杠/不用反斜杠\
print(a)