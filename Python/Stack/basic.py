# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/18


class stack:
    def __init__(self):
        self.stack = []

    def push(self, element):  # 压栈
        self.stack.append(element)

    def pop(self):  # 出栈
        self.stack.pop()

    def gettop(self):  # 取栈顶
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        lenth = len(self.stack)
        if lenth > 0:
            return 0
        else:
            return 1