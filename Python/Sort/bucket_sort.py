# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/15


def bucket_sort(list, max_num=10000, n=100):  # max_num为数据最大范围，n为桶数
    tmp = [[] for _ in range(n)]  # 建立桶
    for i in list:
        j = min(i // (max_num // n), n - 1)  # 确定数据i应在编号为j的桶，max_num//n为单个桶存储的数据范围，超过最大数据范围的放入最后一个桶
        tmp[j].append(i)  # 将数据存入桶中
        for t in range(len(tmp[j]) - 1, 0, -1):  # 对桶中进行排序
            if tmp[j][t] < tmp[j][t - 1]:
                tmp[j][t], tmp[j][t - 1] = tmp[j][t - 1], tmp[j][t]
            else:
                break
    list.clear()
    for i in range(n):
        list.extend(tmp[i])  # 将tmp中的数据覆盖原列表
