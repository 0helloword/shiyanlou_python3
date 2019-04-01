# #-*- coding:utf-8 -*-
# 
# # field=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# # 
# # def transpose(field):
# #     return [list(row) for row in zip(*field)]
# # 
# # def invert(field):
# #     return [row[::-1] for row in field]
# # 
# # print(transpose(field))
# # print(invert(field))
# # from collections import defaultdict
# # def draw():
# #     help_string1 = '(↑)Up(↓)Down(←)Left(→)Right'
# #     help_string2 = '   (Enter)Restart (Esc)Exit'
# #     gameover_string = '           GAME OVER'
# #     win_string = '          YOU WIN!'
# #     def cast(string):#绘制字符串
# #         print(string + '\n')
# 
# # def draw_hor_separator():#绘制分割线
# # #             line = '+' + ('+------' * self.width + '+')[1:]
# #     line =  ('+------' * 4 + '+')
# #     separator = defaultdict(lambda: line)
# #     if not hasattr(draw_hor_separator, "counter"):#判断draw_hor_separator对象中是否存在counter属性,有为True,没有False
# #         draw_hor_separator.counter = 0
# #     cast(separator[draw_hor_separator.counter])
# #     draw_hor_separator.counter += 1
# # line =  ('+------' * 4 + '+')
# # separator = defaultdict(lambda: line)
# # print(separator["fdf"])
# 
# 
# 
# 
# import curses
# 
# stdscr=curses.initscr()
# 
# def display_info1(str,colorpair=1):#x,y是横纵坐标
#     #使用指定的colorpair显示文字
#     global stdscr
#     stdscr.addstr(str,curses.color_pair(colorpair))
#     stdscr.refresh()
# 
# def display_info2(str,colorpair=2):#x,y是横纵坐标
#     #使用指定的colorpair显示文字
#     global stdscr
#     stdscr.addstr(str,curses.color_pair(colorpair))
#     stdscr.refresh()
# 
# def get_ch_and_continue():
#     #演示press any key to continue
#     global stdscr
#     #设置nodelay,为0时变成阻塞式等待
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
#     #控制台重置
#     global stdscr
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
#         string=''
#         if string=='hello':
#             display_info1(string+'\n')
#         else :
#             display_info2(string+'\n')
#         get_ch_and_continue()
#     except Exception as e:
#         raise e
#     finally:
#         unset_win()
#     
#   

row=[0,2,2,0]
print(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')


for num in row:
    if num>0:
        print(''.join('|{: ^5}'.format(num)), end=' ')
    else:
        print('|     ', end=' ')

print('|',end='')
