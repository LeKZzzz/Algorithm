# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/11


def sort(list):
    for i in range(1, len(list)):
        for j in range(i - 1, -1, -1):
            if list[j] > list[j + 1]:
                t = list[j]
                list[j] = list[j + 1]
                list[j + 1] = t
