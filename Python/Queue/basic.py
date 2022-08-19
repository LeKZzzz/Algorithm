# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/18


class queue:
    def __init__(self, size):
        self.queue = [None for _ in range(size)]
        self.rear = 0
        self.front = 0
        self.size = size

    def push(self, element):
        if not self.is_filled():  # 队列满则无法入队
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            return False

    def pop(self):
        if not self.is_empty():  # 队列空则无法出队
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            return None

    def is_empty(self):
        if self.front == self.rear:
            return 1
        else:
            return 0

    def is_filled(self):
        if (self.rear + 1) % self.size == self.front:
            return 1
        else:
            return 0
