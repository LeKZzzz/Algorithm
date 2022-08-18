# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/18


import basic


def brace_match(s):
    stack = basic.stack()
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif match[ch] == stack.gettop():
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False