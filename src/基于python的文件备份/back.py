#-*-coding:utf-8-*-

import os
import time

source = ["E:/auto"]
target_dir = "E:/zip"



today_dir = target_dir + time.strftime('%Y%m%d')
time_dir = time.strftime("%H%M%S")

touch = today_dir + os.sep + time_dir + '.zip'
command_touch = "7z" + touch +' '+ ' '.join(source)

#逻辑思路判断
if os.path.exists(today_dir)==0:
    os.mkdir(today_dir)
if os.system(command_touch)==0:
    print("Success backup Up")
else:
    print("Failed backup")

