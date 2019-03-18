#!/usr/bin/env python3
#-*-coding:utf-8-*-

# Positional parameters
#   words: str
#
# Optional parameters
#   version: int, from 1 to 40
#   level: str, just one of ('L','M','Q','H')
#   picutre: str, a filename of a image
#   colorized: bool
#   constrast: float
#   brightness: float
#   save_name: str, the output filename like 'example.png'
#   save_dir: str, the output directory
import os
from MyQR.mylibs import theqrmodule
from PIL import Image

#os.getcwd()函数获得当前的路径
def run(words,version=1,level='H',picture=None,colorized=False,contrast=1.0,brightness=1.0,save_name=None,save_dir=os.getcwd()):
    supported_chars = r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ··,.:;+-*/\~!@#$%^&`'=<>[]()?_{}|"
    
    #check every parameter
    #isinstance() 函数来判断一个对象是否是一个已知的类型
    #any(x)判断x对象是否为空对象，如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true
    if not isinstance(words, str) or any(i not in supported_chars for i in words):
        raise ValueError('cyj-Wrong words!Make sure the words are supported!')
    if not isinstance(version, int) or version not in range(1,41): 
        raise ValueError('cyj-Wrong version!Please choose a int type value from 1 to 40!')
    if not isinstance(level, str) or len(level)>1 or level not in 'LMQH' :
        raise ValueError("cyj-Wrong level!Please choose a str type from {'L','M','Q','H'}!")
    if picture:
        if not isinstance(picture, str) or not os.path.isfile(picture) or picture[-4:] not in ('.jpg','.png','.bmp','.gif'):
            raise ValueError("cyj-Wrong picture!Input a filename that exists and be tailed with one of {'.jpg','.png','.bmp','.gif'}!")
        if picture[-4:]=='.gif' and save_name and savd_name[-4:]!='.gif':
            raise ValueError('cyj-Wrong save_name!If the picture is .gif format,the output filename should be .gif format,too!')   
        if not isinstance(colorized, bool):
            raise ValueError('cyj-Wrong colorized!Input a bool type value!')
        if not isinstance(contrast, float):
            raise ValueError('cyj-Wrong contrast!input a float type value!')
        if not isinstance(brightness, float):
            raise ValueError('cyj-Wrong brightness!input a float type value!')
    if save_name and (not isinstance(save_name, str)or save_name[-4:]not in ('.jpg','.png','.bmp','.gif')):
         raise ValueError("cyj-Wrong save_name!Input a save_name  tailed with one of {'.jpg','.png','.bmp','.gif'}!")
    if not os.path.isdir(save_dir):
        raise ValueError('cyj-Wrong save_dir!Input a existing-directory!')

    def combine(ver,qr_name,bg_name,colorized,contrast,brightness,save_dir,save_name=None):#图片处理
        from MyQR.mylibs.constant import alig_location
        from PIL import ImageEnhance,ImageFilter
        
        qr=Image.open(qr_name)#在PIL中，使用Image模块的open()函数打开后，返回的图像对象的模式都是“RGB”。而对于灰度图像，不管其图像格式是PNG，还是BMP，或者JPG，打开后，其模式为“L”。
    #     print (qr.mode)
        qr=qr.convert('RGBA') if colorized else qr#判断二维码是否有色colorized为真则将图片转为RGBA格式，否则不转
    #     print (qr.mode)
        
        bg0=Image.open(bg_name).convert('RGBA')#将图片转为RGBA格式
    #     print (bg0.mode)
        bg0=ImageEnhance.Contrast(bg0).enhance(contrast)#ImageEnhance对比度增强类:Contrast用于调整图像的对比度
        bg0=ImageEnhance.Brightness(bg0).enhance(brightness)#brightness用于调整图片的亮度
        print(bg0.size[0],bg0.size[1])#打印bg0图片的长宽
        if bg0.size[0]<bg0.size[1]:#resize(width, height)，图片缩放
            bg0=bg0.resize((qr.size[0]-24,(qr.size[0]-24)*int(bg0.size[1]/bg0.size[0])))
        else:
            bg0=bg0.resize(((qr.size[1]-24)*int(bg0.size[0]/bg0.size[1]), qr.size[1]-24))
            
        bg=bg0 if colorized else bg0.convert('1')#colorized为False,将bg0格式转为1？？？
    #     print (bg)
        
        aligs=[]
        if ver>1:
            aloc=alig_location[ver-2]#(6,18)
    #         print(aloc)
    #         print(len(aloc))
            for a in range(len(aloc)):
                for b in range(len(aloc)):
                    if not ((a==b==0)or(a==len(aloc)-1 and b==0)or(a==0 and b==len(aloc)-1)):
                        for i in range(3*(aloc[a]-2),3*(aloc[a]+3)):
                            for j in range(3*aloc[b]-2,3*(aloc[b]+3)):
                                aligs.append((i,j))
    #         print(aligs)#根据alig_location生成一个数组，作用？？？
        
    #     print (qr.size)
       
        for i in range(qr.size[0]-24):#将目标图片按照规律替换为背景图片的像素点颜色
            for j in range(qr.size[1]-24):
    #             print(bg0.getpixel((i,j))[3])
                if not ((i in(18,19,20)) or (j in (18,19,20)) or (i<24 and j<24) or(i<24 and j>qr.size[1]-49) or(i>qr.size[0]-49 and j<24)or ((i,j)in aligs)or (i%3==1 and j%3==1)or(bg0.getpixel((i,j))[3]==0)):#im.getpixel((x,y)) --返回(x,y)处的像素值
                    qr.putpixel((i+12,j+12),bg.getpixel((i,j)))#putpixel(xy, color) 改变单个像素点颜色
                    #os.path.splitext()将文件名和扩展名分开#os.path.basename返回path最后的文件名称
        print(save_dir,os.path.splitext(os.path.basename(bg_name))[0])
        #如果没有设置save_name,qr_name=source/123_qrcode.png,否则qr_name=save_dir+save_name
        qr_name=os.path.join(save_dir,os.path.splitext(os.path.basename(bg_name))[0]+'_qrcode.png')if not save_name else os.path.join(save_dir,save_name)
#         print(qr_name)
#         print(qr.size)
        qr.resize((qr.size[0]*3,qr.size[1]*3)).save(qr_name)#图片尺寸放大3倍
        return qr_name
    
    
    
    
    #os.path.expanduser(path)  #把path中包含的"~"和"~user"转换成用户目录    
    # tempdir=os.path.join(os.path.expanduser('~'),'.myqr')   #定义临时文件夹 
    nowpwd = os.getcwd()   
    tempdir=os.path.join(nowpwd,'myqr')
    
    try:
        if not os.path.exists(tempdir):
            os.makedirs(tempdir)
             
#         version=1
#         level='M'
#         words='http://jzsit.9fchaoneng.cn:8805/#/'
#         picture='source/wm.gif'
#         save_name='test1.jpg'
        ver,qr_name=theqrmodule.get_qrcode(version,level,words,tempdir)#生成一张3*3像素的二维码图片
        print(ver,qr_name)
           
        if picture and picture[-4:]=='.gif':
            import imageio
                
            im=Image.open(picture)
            print(im.info)#打印gif图片的信息
            duration=im.info.get('duration',0)#获取GIF图片每帧的时长
            print(duration)
            im.save(os.path.join(tempdir,'0.png'))
            while True:
                try:
                    seq=im.tell()#tell()方法返回文件的当前位置，即文件指针当前位置。
#                     print(seq)
                    im.seek(seq+1)#seek() 方法用于移动文件读取指针到指定位置。
                    im.save(os.path.join(tempdir,'%s.png' %(seq+1)))#依次共保存15张图片
                except EOFError:
                    break
            
            imsname=[]
            for s in range(seq+1):
                bg_name=os.path.join(tempdir,'%s.png' %s)
#                 print (bg_name)
                imsname.append(combine(ver,qr_name,bg_name,colorized,contrast,brightness,tempdir))#跳到combine方法，和背景图片合成二维码
                print (imsname)
            ims=[imageio.imread(pic) for pic in imsname]#imread用于读取图片文件中的数据
            #在项目当前目录生成一张背景为wm.gif的动态二维码
            qr_name=os.path.join(save_dir,os.path.splitext(os.path.basename(picture))[0]+'_qrcode.gif') if not save_name else os.path.join(save_dir, save_name)
            imageio.mimwrite(qr_name,ims,'.gif',**{'duration':duration/1000})#mimwrite用于将图像数据写入到图像文件中
        elif picture:
            qr_name=combine(ver,qr_name,picture,colorized,contrast,brightness,save_dir,save_name)  
        elif qr_name:
            qr=Image.open(qr_name)
            qr_name=os.path.join(save_dir,os.path.basename(qr_name)) if not save_name else os.path.join(save_dir,save_name)
            qr.resize((qr.size[0]*3,qr.size[1]*3)).save(qr_name) 
            
        return ver,level,qr_name                 
    except:
        raise
#     finally:
#         import shutil
#         if os.path.exists(tempdir):
#             shutil.rmtree(tempdir)#递归删除文件夹下的所有子文件夹和子文件
    
    
    
    
# B=run(words='https://www.baidu.com', version=1, level='M',picture='source/wm.gif')
# A=combile(2, qr_name='source/1.png', bg_name='source/123.jpg', colorized=False, contrast=1.0, brightness=1.0, save_dir='source/', save_name='test.jpg')
