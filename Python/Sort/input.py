# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/8/11

import random
import quick_sort_right

list = [i for i in range(21)]
random.shuffle(list)
quick_sort_right.sort(list,0,len(list)-1)
print(list)
