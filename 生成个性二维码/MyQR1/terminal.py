#!/user/bin/env python3
#-*-coding:utf-8-*-

import os
from myqr import run

def main():#???作用是什么
    import argparse#argparse是python标准库里面用来处理命令行参数的库
    argparser=argparse.ArgumentParser()# 创建一个解析对象
    #向该对象中添加你要关注的命令行参数和选项
    argparser.add_argument('Words',help='the words to product you QR-code picture,like a url or a sentence,please read the readme file for the supported characters.')
    argparser.add_argument('-v','--version',type=int,choices=range(1,41),default=1,help='the version means the length of a side of the QR-Code picture,from little size to large is 1 to 40.')
    argparser.add_argument('-l','--lever',choices=list('LMQH'),default='H',help='use this argument to choose an error-correction-lever:L(low),m(medium)or q(quartile),h(high).otherwise,just use the default one:h')
    argparser.add_argument('-p','--picture',help='the picture e.g example.jpg')
    argparser.add_argument('-c','--colorized',action='store_true',help = "Produce a colorized QR-Code with your picture. Just works when there is a correct '-p' or '--picture'.")
    argparser.add_argument('-con','--contrast',type=float,default=1.0,help = 'A floating point value controlling the enhancement of contrast. Factor 1.0 always returns a copy of the original image, lower factors mean less color (brightness, contrast, etc), and higher values more. There are no restrictions on this value. Default: 1.0')
    argparser.add_argument('-bri','--brightness',type=float,default = 1.0, help = 'A floating point value controlling the enhancement of brightness. Factor 1.0 always returns a copy of the original image, lower factors mean less color (brightness, contrast, etc), and higher values more. There are no restrictions on this value. Default: 1.0')
    argparser.add_argument('-n','--name',help="the filename of output tailed with one of {'.jpg', '.png', '.bmp', '.gif'}")
    argparser.add_argument('-d','--directory',default=os.getcwd(),help='the directory of output')
    args=argparser.parse_args()#进行解析
    
    if args.picture and args.picture[-4:]=='.gif':
        print('it may take a while,please wait for minutes……')
    try:
        ver,ecl,qr_name=run(
            args.Words,
            args.version,
            args.level,
            args.picture,
            args.colorized,
            args.contrast,
            args.brighness,
            args.name,
            args.directory
                            )
        print('Succeed!\ncheck out your',str(ver)+'-'+str(ecl),'QR-code:',qr_name)
    except:
        raise

    