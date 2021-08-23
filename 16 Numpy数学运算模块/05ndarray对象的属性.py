
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/23 21:04
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入numpy
import numpy as np
#创建一维的数组
a=np.array([1,2,3,4])
print(a)
#创建二维数组
b=np.random.randint(4,10,size=(2,3))
print(b)
#创建三维数组
c=np.random.randn(2,3,4)
print(c)
#ndim属性
print('ndim:',a.ndim,b.ndim,c.ndim)
#shape属性
print('shape:',a.shape,b.shape,c.shape)
#dtype属性
print('dtype:',a.dtype,b.dtype,c.dtype)
#size 元素的总个数
print('size:',a.size,b.size,c.size)
#itemsize  每个元素所占的字节
print('itemsize:',a.itemsize,b.itemsize,c.itemsize)
