# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/11

import random
import heap_sort

list = [i for i in range(21)]
random.shuffle(list)
heap_sort.heap(list)
print(list)
