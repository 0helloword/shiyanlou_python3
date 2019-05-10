class Stack(object):
    def __init__(self, limit=10):
        self.stack = [] #存放元素
        self.limit = limit #栈容量极限
        
    def push(self, data): #判断栈是否溢出
        if len(self.stack) >= self.limit:
            print('StackOverflowError')
            pass
        self.stack.append(data)
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack') #空栈不能被弹出
        
    def peek(self): #查看堆栈的最上面的元素
        if self.stack:
            return self.stack[-1]
        
    def is_empty(self): #判断栈是否为空
        return not bool(self.stack)
    
    def size(self): #返回栈的大小
        return len(self.stack)
    
def balanced_parentheses(parentheses):
    #判断是否为有效括号字符串
    #先判断正括号将其入栈，当遇到反括号时出栈
    #字符串遍历完后，非空则为无效括号字符串
    #字符串还未遍历完就已经为空，则为无效括号字符串
    stack=Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parenthesis)
        elif parenthesis == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

if __name__ == '__main__':
    examples = ['((()))', '((())', '(()))']
    print('Balanced parentheses demonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))