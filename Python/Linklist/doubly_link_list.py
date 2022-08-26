# -*- coding: UTF-8 -*- 
# Creator：LeK
# Date：2022/8/26


class Node:
    def __init__(self, item):
        self.item = item
        self.prior = None
        self.next = None