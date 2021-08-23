
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/23 16:41
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入numpy
import numpy as np
#创建数组
a=np.arange(10)
print(a)
print(type(a))

#对ndarray对象类型进行向量处理
print(np.sqrt(a))


#对列表中的元素开平方
import math
b=[3,4,9]
#定义存储开平方结果的列表
result=[]
#遍历列表
for i in b:
    result.append(math.sqrt(i))
print(result)




