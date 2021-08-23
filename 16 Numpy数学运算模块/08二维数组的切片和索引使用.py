
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/23 21:05
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入numpy模块
import numpy as np
#创建一维数组
a=np.arange(1,13)
print(a)
#对一维数组进行修改形状  (4,3)
a=a.reshape((4,3))
print(a)
#索引的使用
#获取第三行
print(a[2])
#获取第二行 第3列
print(a[1][2])

#切片的使用 [行进行切片,列进行切片]   [start:stop:step,start:stop:step]
#获取所有行所有列
print(a[:,:])
#获取所有行部分列   所有行第2列
print(a[:,1])
#获取所有行部分列   所有行第1,2列
print(a[:,0:2])

#获取部分行 所有列  获取奇数行所有列
print(a[::2,:])

#获取部分行 部分列   获取奇数行  第1,2列
print(a[::2,0:2])

#坐标获取 [行,列]
#获取第2行第3列的元素
print(a[1][2])
print(a[1,2])

#同时获取不同行不同列   获取第2行第3列  第3行第1列
print(a[1,2],a[2][0])
print(np.array([a[1,2],a[2][0]]))
#使用坐标
print(a[(1,2),(2,0)])

#负索引的使用
print('最后一行')
print(a[-1])
print('行倒序')
print(a[::-1])
print('行列倒序')
print(a[::-1,::-1])