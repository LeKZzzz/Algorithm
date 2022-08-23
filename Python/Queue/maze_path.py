# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/22

import basic

# 建立迷宫
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 设置下一步的方向
dirs = [
    lambda x, y: (x - 1, y),  # 向上进一步
    lambda x, y: (x + 1, y),  # 向下进一步
    lambda x, y: (x, y - 1),  # 向左进一步
    lambda x, y: (x, y + 1)  # 向右进一步
]


def print_f(path):  # 打印路径
    realpath = []  # 实际路径
    curNode = path[-1]  # 从传入的路径最后一个元素(终点坐标)开始往前找实际路径
    while curNode[2] != -1:  # 如果坐标不是起点坐标，则继续往前查找
        realpath.append((curNode[0], curNode[1]))
        curNode = path[curNode[2]]
    realpath.append((curNode[0], curNode[1]))
    realpath.reverse()  # 将逆序的实际路径反转获得从起点到终点的实际路径
    for i in realpath:  # 打印输出
        print(i)


def maze_path(x1, y1, x2, y2):  # x1 y1为起点坐标，x2 y2为终点坐标
    queue = basic.queue(21)  # 实例化队列
    queue.push((x1, y1, -1))  # 设置起始坐标，将起点入队
    path = []  # 设置路径列表，元素为含有三个数据的元组，第一个元素为路径结点的x坐标，第二个元素为路径结点的y坐标，第三个元素为该路径结点的上一个结点在路径列表path中的索引
    while not queue.is_empty():  # 若队列不为空，则说明仍然可以寻找路径
        curNode = queue.pop()  # 队首出队，作为查找路径的结点
        path.append(curNode)  # 将出队的队首放入路径列表path中
        for dir in dirs:  # 查找curNode的四个方向是否可以前进一步
            nextNode = dir(curNode[0], curNode[1])  # 可前进的下一步的坐标
            if nextNode == (x2, y2):  # 查找到终点，说明有路径可以到达，打印输出
                path.append((x2, y2, len(path) - 1))
                print_f(path)
                return True
            if maze[nextNode[0]][nextNode[1]] == 0:  # 如果下一个结点的坐标可前进
                queue.push((nextNode[0], nextNode[1],
                            len(path) - 1))  # 将该坐标加入队列中作为之后查找的起始结点，len(path)-1为上一个结点在路径列表path中的索引(即列表终点最后一个元素)
                maze[nextNode[0]][nextNode[1]] = 2  # 将该已查找过的坐标进行标记
    else:  # 若队列为空，说明没有路径到达终点
        return False


print(maze_path(1, 1, 8, 8))
