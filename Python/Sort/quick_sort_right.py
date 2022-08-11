# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/11


def sort(list, left, right):
    if left >= right:
        return

    mid = right
    tmp = list[mid]
    leftpoint = left
    rightpoint = right
    while leftpoint != rightpoint:
        while list[leftpoint] <= tmp and leftpoint < rightpoint:
            leftpoint += 1
        if leftpoint != rightpoint:
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