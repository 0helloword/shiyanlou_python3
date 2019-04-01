#-*- coding:utf-8 -*-

# #案例一
# import curses
# 
# stdscr=curses.initscr()
# 
# def display_info1(str,x,y,colorpair=1):#x,y是横纵坐标
#     #使用指定的colorpair显示文字
#     stdscr.addstr(y,x,str,curses.color_pair(colorpair))
#     stdscr.refresh()
#     
#     
# def display_info2(str,x,y,colorpair=2):#x,y是横纵坐标
#     #使用指定的colorpair显示文字
#     stdscr.addstr(y,x,str,curses.color_pair(colorpair))
#     stdscr.refresh()
#     
# def get_ch_and_continue():
#     #演示press any key to continue
#     #设置nodelay为0时变成阻塞式等待
#     stdscr.nodelay(0)
#     #输入一个字符
#     ch=stdscr.getch()
#     #重置nodelay,使得控制台可以以非阻塞的方式接受控制台输入，超时1秒
#     stdscr.nodelay(1)
#     return True
# 
# def set_win():
#     #控制台设置
#     global stdscr
#     #使用颜色首先需要调用这个方法
#     curses.start_color()
#     #文字和背景色设置，设置了两个color pair,分别为1和2
#     curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
#     curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
#     #关闭屏幕回显
#     curses.noecho()
#     #输入时不需要回车确认
#     curses.cbreak()
#     #设置nodelay,使得控制台可以以非阻塞的方式接受控制台输入，超时1秒
#     stdscr.nodelay(1)
#     
# def unset_win():
#     #恢复控制台默认设置（若不恢复，会导致即使程序结束退出了，控制台仍然是没有回显的）
#     curses.nocbreak()
#     stdscr.keypad(0)
#     curses.echo()
#     #结束窗口
#     curses.endwin()
#     
# if __name__=='__main__':
#     try:
#         set_win()
#         display_info1('Hello,curses!',5,5)
#         display_info2('Press any key to continue...',0,10)
#         get_ch_and_continue()
#     except Exception as e:
#         raise e
#     finally:
#         unset_win()
    
# #案例二
# #-*- coding:utf-8 -*-
# from colorama import init
# 
# init(autoreset=True)
# 
# print("\033[0;30;40m\tHello World\033[0m") #黑色 
# print("\033[0;31;40m\tHello World\033[0m") #红色
# print("\033[0;32;40m\tHello World\033[0m") #绿色
# print("\033[0;33;40m\tHello World\033[0m") #黄色
# print("\033[0;34;40m\tHello World\033[0m") #蓝色 
# print("\033[0;35;40m\tHello World\033[0m") #紫色
# print("\033[0;36;40m\tHello World\033[0m") #浅蓝 
# print("\033[0;37;40m\tHello World\033[0m") #白色
    

#案例三
from colorama import init,Fore
init(autoreset=True)
print (Fore.YELLOW + "welcome to python !!")
print ("automatically back to default color again") 
print(Fore.RED+'SCORE: ' + str(100))

