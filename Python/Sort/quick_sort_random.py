# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/11

import random


def sort(list, left, right):
    if left >= right:
        return

    mid = random.randint(left, right)
    tmp = list[mid]
    leftpoint = left
    rightpoint = right
    while leftpoint < rightpoint:
        while list[leftpoint] < tmp and leftpoint < rightpoint:
            leftpoint += 1
        while list[rightpoint] > tmp and leftpoint < rightpoint:
            rightpoint -= 1
        list[leftpoint], list[rightpoint] = list[rightpoint], list[leftpoint]
        if list[leftpoint] == list[rightpoint] == tmp:
            leftpoint += 1
    print(list)
    sort(list, rightpoint + 1, right)
    sort(list, left, leftpoint - 1)