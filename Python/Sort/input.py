# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/11

import random
import merge_sort

list = [i for i in range(21)]
random.shuffle(list)
merge_sort.sort(list,0,len(list)-1)
print(list)
