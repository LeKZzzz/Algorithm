# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/13


def sift(list, start, end):  # 向下调整函数，start为堆顶，end为堆的最后一个元素的位置
    i = start
    j = 2 * i + 1
    tmp = list[start]
    while j <= end:
        if j + 1 <= end and list[j] < list[j + 1]:  # 比较根节点的两个子结点，最大的子结点和根结点之间进行比较
            j = j + 1
        if tmp < list[j]:   # 比较子结点与根结点大小，如果子结点比根节点大，则子结点上移一层
            list[i]= list[j]
            i = j
            j = 2 * i + 1
        else:
            list[i] = tmp   # 若子结点均比根结点小，则说明根结点已找到它的位置
            break
    else:
        list[i] = tmp   # 根结点位于叶子结点，则该位置为根结点所应处的位置


def heap(list):
    n = len(list) - 1   # 完全二叉树最下一层的最右端的叶子结点
    #   构建堆
    for i in range((n - 1) // 2, -1, -1):   # 从最小的堆开始构建，i为每个根结点的索引
        sift(list, i, n)
    #   依次出数
    for j in range(n, -1, -1):  # 将最后一个元素与首元素交换位置，堆底end往前进1，向下调整新的堆，重复此操作最终成为一个有序列表
        list[0], list[j] = list[j], list[0]
        sift(list, 0, j-1)