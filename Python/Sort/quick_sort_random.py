# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/11

import random


def sort(list, left, right):
    if left >= right:
        return

    mid = random.randint(left, right)
    while mid == left:
        mid = random.randint(left, right)
    tmp = list[mid]
    t = 0
    leftpoint = left
    rightpoint = right
    while leftpoint != rightpoint:
        while list[leftpoint] <= tmp and leftpoint < mid:
            leftpoint += 1
        if leftpoint != rightpoint:
            if t == 0:
                list[mid] = list[leftpoint]
                t = 1
            else:
                list[rightpoint] = list[leftpoint]
                rightpoint -= 1
        while list[rightpoint] >= tmp and leftpoint < rightpoint:
            rightpoint -= 1
        if leftpoint != rightpoint:
                list[leftpoint] = list[rightpoint]
                leftpoint += 1
    list[leftpoint] = tmp
    print(list)
    sort(list, rightpoint + 1, right)
    sort(list, left, leftpoint - 1)
