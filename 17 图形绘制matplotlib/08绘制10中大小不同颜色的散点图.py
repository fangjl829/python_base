
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/23 20:55
# !/usr/bin/python3
# -*- coding:utf-8 -*-


#导入模块
import matplotlib.pyplot as plt
import numpy as np

#绘制10中大小 100种颜色的散点图
#创建x
np.random.seed(0)
#执行多次每次获取的随机数都是一样的
x=np.random.rand(20)
y=np.random.rand(20)
#生成10中大小
size=np.random.rand(20)*1000
#生成100中颜色
color=np.random.rand(20)
print(x)
print(y)
#绘制散点图
plt.scatter(x,y,s=size,c=color,alpha=0.7)
#s表示点的大小 c表示点的颜色 alpha表示透明度
plt.show()
'''
注意：点的个数和颜色的个数要相同
      点的个数和点大小的个数可以不同，如果点的个数大于大小的个数，则会循环获取大小
'''