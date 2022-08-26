# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/26


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def create_head_insert(list):  # 头插法创建列表
    head = Node(list[0])
    for item in list[1:]:
        node = Node(item)
        node.next = head
        head = node
    return head


def create_tail_insert(list):  # 尾插法创建列表
    head = Node(list[0])
    tail = head
    for item in list[1:]:
        node = Node(item)
        tail.next = node
        tail = node
    return head


def traverse(head):  # 遍历
    point = head
    while point:
        print(point.item, end=' ')
        point = point.next
    print('\n')


def insert(head, num, item):  # 在num节点后插入数据item
    curNode = head
    for _ in range(num - 1):
        curNode = curNode.next
    nextNode = Node(item)
    nextNode.next = curNode.next
    curNode.next = nextNode


def delete(head, num):  # 删除num节点
    curNode = head
    for _ in range(num - 2):
        curNode = curNode.next
    nextNode = curNode.next
    curNode.next = nextNode.next


linklist = create_tail_insert([i for i in range(11)])
traverse(linklist)
insert(linklist, 5, 100)
traverse(linklist)
delete(linklist, 6)
traverse(linklist)
