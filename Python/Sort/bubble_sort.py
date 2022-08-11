# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/11


def sort(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] < list[j]:
                t = list[i]
                list[i] = list[j]
                list[j] = t
