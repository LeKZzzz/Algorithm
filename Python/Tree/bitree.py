# -*- coding: UTF-8 -*- 
# Creator：LeK
# Date：2022/8/30


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


def pre_order(root):  # 前序遍历
    if root != None:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)


def in_order(root):  # 中序遍历
    if root != None:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)


def post_order(root):  # 后序遍历
    if root != None:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data)


import Queue.basic


def level_order(root, size):  # 层次遍历
    queue = Queue.basic.queue(size)
    queue.push(root)
    while not queue.is_empty():
        node = queue.pop()
        print(node.data, end=',')
        if node.lchild != None:
            queue.push(node.lchild)
        if node.rchild != None:
            queue.push(node.rchild)
