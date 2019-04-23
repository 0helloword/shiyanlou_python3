#-*- coding:utf-8 -*-

import curses
from random import randrange, choice # generate and place new tile
from collections import defaultdict
from itertools import chain
import sqlite3
from colorama import init

class Action():
    #有效健值列表
    letter_codes = [ord(ch) for ch in 'WASDRQYwasdrqy']
    #print(letter_codes)#打印结果为WASDRQwasdrq对应的ascii码
    letter_list=[259,260,258,261,10,27,121]#上左下右EscEnterY键对应的ascii码，通过get_user_action中的char来获取
    letter_codes=letter_codes+letter_list
    
    #用户行为
    actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit','Continue']
    #将输入与行为进行关联
    actions_dict = dict(zip(letter_codes, actions * 3))
    
    def __init__(self):
        pass
    
    #用户输入处理
    def get_user_action(self,keyboard):    
        char = "N"
        #阻塞+循环，直到获得用户有效输入才返回对应行为
        while char not in self.actions_dict:    
            char = keyboard.getch()#从控制台读取一个字符，但不显示在屏幕上
    #         print(char)#通过这里打印对应按键的数字找到上下左右等按键的对应的ascii码
        return self.actions_dict[char]

#sqlite数据库操作，读取最高分数
class sqliteOperate():
    def __init__(self):
        self.conn=sqlite3.connect('2048.db')
        
    def select(self):
        score=self.conn.execute("select SCORE from HighScore")
        for row in score:
            return row[0]
            
    def update(self,score):
        self.conn.execute("update HighScore set SCORE ={0} where ID=1".format(score))
        self.conn.commit()
        self.conn.close() 
        
#创建棋盘
class GameField(object):
    
    def __init__(self, height=4, width=4,win=0):
        self.height=height #高
        self.width=width  #宽
        self.win_value=win  #过关分数
        self.score=0   #当前分数
        self.highscore=Highscore  #从数据库获取最高分
        self.reset()   #棋盘重置
        self.action=Action()
    
    #如果该方法没有引用对象的资源，可以采用静态方法，并且不需要传入self
    @staticmethod
    #矩阵转置,行和列的转换
    def transpose(field):
        return [list(row) for row in zip(*field)]
    
    @staticmethod
    #矩阵逆转，每行倒着排列
    def invert(field):
        return [row[::-1] for row in field]
        
    #重置棋盘
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            sqliteoperate.update(self.highscore) #更新数据库中的最高分
        self.score = 0        
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]#创建一个4*4值全为0的二维数组
        self.spawn()#棋盘上初始状态显示2个数字，随机生成两个数字，调两次spawn方法
        self.spawn()
    
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2#9:1的比例生成2或4
        #通过choice随机选择一个未被占领的位置来放置new_element
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element
    
    def move(self, direction):
        #一行向左合并   
        def move_row_left(row):
            def tighten(row): #squeese non-zero elements together
                #把零散的非零单元挤到一块,先打印出非零的元素，然后在后面空白位置补0
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):#对邻近元素进行合并
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)#assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假
                return new_row
            #先挤到一块再合并再挤到一起
            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left']  = lambda field:                              \
                [move_row_left(row) for row in field]
        moves['Right'] = lambda field:                              \
                self.invert(moves['Left'](self.invert(field)))
        moves['Up']    = lambda field:                              \
                self.transpose(moves['Left'](self.transpose(field)))
        moves['Down']  = lambda field:                              \
                self.transpose(moves['Right'](self.transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False
    
    def move_is_possible(self, direction):
        def row_is_left_movable(row): 
            def change(i): # true if there'll be change in i-th tile
                if row[i] == 0 and row[i + 1] != 0: # Move
                    return True
                if row[i] != 0 and row[i + 1] == row[i]: # Merge
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))#判断是否有任意一行可以向左移动
        
        check = {}
        check['Left']  = lambda field:                              \
                any(row_is_left_movable(row) for row in field)

        check['Right'] = lambda field:                              \
                 check['Left'](self.invert(field))

        check['Up']    = lambda field:                              \
                check['Left'](self.transpose(field))

        check['Down']  = lambda field:                              \
                check['Right'](self.transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False       
        
    def is_win(self):
        #any(x)判断x对象是否为空对象，如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true
        #遍历每个元素查看是否大于win_value
#         return any(any(i >= self.win_value for i in row) for row in self.field)
        #找出当前二维数组中的最大值与win_value比较
        #chain把二维数组转化成序列
#         print(max(chain(*self.field)),self.win_value)
        return max(chain(*self.field))>=self.win_value        
        
    def is_gameover(self):
        #所有的行都不能移动则游戏结束
        return not any(self.move_is_possible(move) for move in self.action.actions)

    def draw(self, screen):     
        def set_color():#设置颜色
            #使用颜色首先需要调用这个方法
            curses.start_color()    
            #文字和背景色设置，设置了三个color pair,分别为1,2,3
            curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
            curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
            curses.init_pair(3,curses.COLOR_RED,curses.COLOR_BLACK)
                
        def cast(string):#绘制字符串      
#             screen.addstr(string+ '\n')     
            set_color()
            screen.addstr(string+ '\n',curses.color_pair(1))
            
        def cast2(string):#绘制字符串 ，成功时显示绿色的提示语     
            set_color()
            screen.addstr(string+ '\n',curses.color_pair(2))

        def cast3(string):#将分数和最高分显示为红色   
            set_color()
            screen.addstr(string+ '\n',curses.color_pair(3))

        def draw_row(row):#绘制包含数字的行
            #^是居中显式，<是左对齐，>是右对齐，冒号后面有一个空格，意思是空格填充
            #如果单元格中数字大于0，则将该数字格式化为居中显示，否者仅打印斜杠和空格
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')
   
        help_string1 = '(↑)Up(↓)Down(←)Left(→)Right'
        help_string2 = '   (Enter)Restart (Esc)Exit'
        help_string3 = '(Enter)Restart(Y)Continue(Esc)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'      

        screen.clear()
        cast3('SCORE: ' + str(self.score))#绘制当前分数
        cast3('HIGHSCORE: ' + str(self.highscore))#绘制当前最高分数
        for row in self.field:
            cast('+------' * self.width + '+')
            draw_row(row)
        cast('+------' * self.width + '+')        
        
        if self.is_win():
            cast2(win_string)
            cast(help_string3)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
            cast(help_string2)
        
def main(stdscr):#stdscr由curses传入，主要用于命令行的操作
    def init():
        #重置游戏棋盘
        game_field.reset()
        return 'Game'

    def not_game(state):#胜利或失败的状态
        #画出 GameOver 或者 Win 的界面
        game_field.draw(stdscr)
        #读取用户输入得到action，判断是重启游戏还是结束游戏
        action = actionoperate.get_user_action(stdscr)
        responses = defaultdict(lambda: state) #默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'],responses['Continue'] = 'Init', 'Exit','Continue' #对应不同的行为转换到不同的状态
        return responses[action]

    def game():
        #画出当前棋盘状态
        game_field.draw(stdscr)
        #读取用户输入得到action
        action = actionoperate.get_user_action(stdscr)
        
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action): # move successful
            if game_field.is_win():
                if action=='Continue':
                    return 'Continue'
                else:
                    return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'    
    
    def game_suc():
        #画出游戏成功后当前棋盘状态
        game_field.draw(stdscr)
        #读取用户输入得到action
        action = actionoperate.get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action): # move successful            
            return 'GameSuc'
        return 'GameSuc'
    
    def game_continue():#达到胜利分数值选择继续游戏
        game_field.draw(stdscr)
#         #读取用户输入得到action
        action = actionoperate.get_user_action(stdscr)
        
        if game_field.move(action): # move successful
            if game_field.is_gameover():
                return 'Gameover'
            else: 
                return 'GameSuc'
        return 'GameSuc'
                
    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game,
            'Continue':game_continue,
            'GameSuc':game_suc            
        }
   

#     curses.use_default_colors()

    # 设置终结状态最大数值为 8
    game_field = GameField(win=8)
    actionoperate=Action()

    state = 'Init'

    #状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()

sqliteoperate=sqliteOperate()              
Highscore=sqliteoperate.select()
#curses库提供了控制字符屏幕的独立于终端的方法
#不能用任何IDE来运行有curses包的python文件,否则提示Redirection is not supported.
curses.wrapper(main) #初始化curses

'''
#拓展：
1.支持方向键  已完成
2.达到胜利分数值可以选择继续游戏或者结束游戏  已完成
3.为不同的分数值添加颜色,在控制台输出不同的颜色
4.链接sqlite，将最好成绩存入其中，每次启动游戏时读取   已完成

'''