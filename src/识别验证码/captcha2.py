#-*-coding:utf-8-*-
'''
首先针对一个验证码图片进行像素颜色统计检测，并人工验证哪些颜色组成了验证码的字符。
利用上一步得到的颜色，通过判断该颜色所在的横坐标，将验证码中每个数字所在的横坐标范围确定下来,。
利用实验楼提供的单数字图片与Pillow的Image.getdata()方法,得到每种数字或小写字母的有效像素的集合，作为“训练集”。
最后，利用上两步得到的“验证码的数字坐标集”与“训练集”，在VectorCompare.relation()算法下，
比较验证码每一位与训练集中每一个字符的数据，选最相似（相同坐标值相同的次数最多）的那个返回，这样就得到了验证码中数字的内容。
'''

from PIL import Image
import math, os, string, hashlib, time

#基本向量空间搜索
class VectorCompare:
    #计算矢量大小
    def magnitude(self, concordance):
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)
    #计算矢量之间的cos值
    def relation(self, concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
       
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


class CrackCaptcha(object):
    def __init__(self, fp):
        self.im = Image.open(fp)
        #将图片转换为8位像素模式
        self.im.convert("P")

        #根据im图片生成一个白底的图片im2
        self.im2 = Image.new("P", self.im.size, 255)
        self.v = VectorCompare()#实例化向量空间

    def cut_single_number(self):#纵向切割，获取单个字符的像素集合
        inletter = False
        foundletter = False
        start = 0
        end = 0

        letters = []

        '''
        y is width, x is height.
        these code find every number where start and end.
        '''
        for y in range(self.im2.size[0]):
            for x in range(self.im2.size[1]):
                pix = self.im2.getpixel((y,x))#该函数检索指定坐标点的像素的RGB颜色值
                if pix !=255:
                    inletter = True
            if foundletter == False and inletter == True:
                foundletter = True
                start = y

            if foundletter == True and inletter == False:
                foundletter = False
                end = y
                letters.append((start, end))
            inletter = False
        return letters

    def convert_two_color(self, pixes=[], fp=None):       
        for x in range(self.im.size[1]):
            for y in range(self.im.size[0]):
                pix = self.im.getpixel((y, x))#该函数检索指定坐标点的像素的RGB颜色值
                if pix in pixes:
                    self.im2.putpixel((y,x),0)#在指定位置画一像素，像素颜色值为黑色

        if fp != None:
            self.im2.save(fp + ".gif")
        self.im2.show()

    def find_most_color(self):
        '''
        find feature color in human eye
        '''    
        his = self.im.histogram()
        print (self.im.histogram())#打印直方图，直方图的每一位数字都代表了在图片中含有对应位的颜色的像素的数量

        values = {}
        
        for i in range(256):
            values[i] = his[i]
        #通过排序得到最多的前10个颜色
        for j,k in sorted(values.items(), key=lambda x:x[1], reverse=True)[:10]:
            print (j,k)

    #将图片转换为矢量,得到每种数字或小写字母的有效像素的集合
    def buildvector(self, im):
        d1 = {}
        count = 0
        for i in im.getdata():
            d1[count] = i
            count += 1
        return d1
    
    #加载训练营
    def train(self):
        iconset = [i for i in (string.digits + string.ascii_lowercase)]
        #iconset = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        imageset = []
        for letter in iconset:
            for img in os.listdir('./iconset/%s/'%(letter)):#iconset目录下是训练集，包含1-0，a-z的图片
                temp = []
                if img != "Thumbs.db" and img != ".DS_Store":
                    t_img = Image.open("./iconset/%s/%s"%(letter,img))
                    temp.append(self.buildvector(t_img))
                imageset.append({letter:temp})
        return imageset
    
    #对验证码图片进行切割
    def cut_captcha(self, letters, imageset, build_pic=False):
        count = 0
        for letter in letters:
            m = hashlib.md5()
            im3 = self.im2.crop((letter[0], 0, letter[1], self.im2.size[1]))#根据图片返回一个矩形区域
            if build_pic:
                m.update("%s%s"%(time.time(),count))
                im3.save("./%s.gif"%(m.hexdigest()))

            guess = []
            #将切割得到的验证码小片段与每个训练片段进行比较
            for image in imageset:
                for x,y in image.items():
                    if len(y) != 0:
                        guess.append((self.v.relation(y[0], self.buildvector(im3)),x))
            guess.sort(reverse=True)
            print ("",guess[0])

            count += 1


    def run(self, make_img=False):
        self.find_most_color()#通过排序找到有用的颜色
        self.convert_two_color([6,8])#6和8是需要的红色和灰色,方法是依次查看前10个的编号，找出对比度最大的两个编号，即组合起来验证码数字最清晰的两个编号
        letters = self.cut_single_number()#获取单个字符的像素集合
        imageset = self.train()#获取训练营字符数据
        self.cut_captcha(letters,imageset,make_img)


if __name__ == '__main__':
    cc = CrackCaptcha("./pic/7S9T9J.gif")#当前目录中的pic目录下的7S9T9J.gif图片
    cc.run()