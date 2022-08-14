# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/14


def merge(list, start, mid, end):
    i = start
    j = mid + 1
    tmp = []
    while i <= mid and j <= end:  # 当两个子序列其中一个触碰到自身边界时退出
        if list[i] < list[j]:
            tmp.append(list[i])
            i += 1
        else:
            tmp.append(list[j])
            j += 1
    #   将剩余的有序部分依次添加到tmp数组中存储
    while i <= mid:
        tmp.append(list[i])
        i += 1
    while j <= end:
        tmp.append(list[j])
        j += 1
    list[start:end + 1] = tmp  # 将tmp列表覆盖原列表


def sort(list, start, end):
    if start < end:  # 当传入的子序列元素数为1时即退出递归
        mid = (start + end) // 2
        # 递归分割该序列，直至符合递归退出条件
        sort(list, start, mid)
        sort(list, mid + 1, end)
        merge(list, start, mid, end)  # 下层递归返回即说明返回的为相邻的两个有序子序列，对这两个子序列进行归并
    else:
        return