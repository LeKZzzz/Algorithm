# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/15


def radix_sort(list):
    i = 0
    max_num = max(list)  # 通过最大元素确定需要获取基数的次数
    while 10 ** i <= max_num:
        tmp = [[] for _ in range(10)]
        for val in list:
            j = (val // (10 ** i)) % 10  # 根据val的基数放入对应的桶
            tmp[j].append(val)
        list.clear()
        for val in tmp:
            list.extend(val)  # 将桶中数据按照顺序覆盖原列表
        i += 1
