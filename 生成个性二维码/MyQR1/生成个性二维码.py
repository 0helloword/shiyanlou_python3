#-*-coding:utf-8-*-

#1.pip3 install MyQR
#2.生成普通二维码
# from MyQR import myqr
# myqr.run('https://www.baidu.com', 10, 'H', '', '', '1.0', '1.0', 'qrcode.png')
# #3.生成带图片的二维码
# myqr.run(
#          words='http://jzsit.9fchaoneng.cn:8805/#/',
#          picture='source/1.png',
#          colorized=True,
#          save_name='artistic.png',
#          )
# #4.生成动态二维码
# myqr.run(
#          words='http://jzsit.9fchaoneng.cn:8805/#/',
#          picture='source/wm.gif',
#          colorized=True,
#          save_name='Animated.gif',
#          )


num=2
qrmatrix=[[None]*num for i in range(num)]
print(qrmatrix)


