
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/23 21:04
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入numpy模块
import numpy as np
#使用array函数创建一维数组
a=np.array([1,2,3,4])
print(a)
print(type(a))

#使用array函数创建二维数组
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(type(b))

#使用array函数创建三维数组
c=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(c)
print(type(c))

#array函数中dtype的使用
d=np.array([3,4,5],dtype=float)
print(d)
print(type(d))

#array函数中ndim的使用
e=np.array([5,6,7],dtype=float,ndmin=3)
print(e)

