# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/21


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


def maze_path(x1, y1, x2, y2):  # x1 y1为起点坐标，x2 y2为终点坐标
    stack = []  # 建立栈
    stack.append((x1, y1))  # 添加起点进栈
    while len(stack) > 0:  # 若栈不空，则对栈顶进行操作
        curNode = stack[-1]  # 当前坐标为栈顶
        if curNode[0] == x2 and curNode[1] == y2:  # 如果当前坐标为终点坐标则输出栈(路径)
            for i in stack:
                print(i)
            return True
        for dir in dirs:  # 对栈顶进行下一步的方向进行操作
            nextNode = dir(curNode[0], curNode[1])  # 下一步的方向
            if maze[nextNode[0]][nextNode[1]] == 0:  # 如果下一步在maze中为0，说明这一步可行
                stack.append(nextNode)  # 将可行的下一步坐标加入栈中
                maze[nextNode[0]][nextNode[1]] = 2  # 标记下一步已走过
                break  # 跳出当前循环，开始下一次的方向选择
        else:  # 如果所有方向都是1或2(已走过)
            maze[curNode[0]][curNode[1]] = 2  # 标记当前坐标为2(已走过)
            stack.pop()  # 栈顶出栈，回退一步
    else:  # 如果栈空，则说明无法到达终点
        return False


print(maze_path(1, 1, 8, 8))
