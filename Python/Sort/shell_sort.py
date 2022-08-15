# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/15

def insert_sort(list, gap):  # gap为步长
    for i in range(gap, len(list)):
        for j in range(i - gap, -1, -gap):
            if list[j] > list[j + gap]:
                t = list[j]
                list[j] = list[j + gap]
                list[j + gap] = t


def shell_sort(list):
    gap = len(list) // 2
    while gap >= 1:
        insert_sort(list, gap)
        gap = gap // 2
