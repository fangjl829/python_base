
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/23 20:57
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入模块
import matplotlib.pyplot as plt
import numpy as np
#使用np.random.normal()指定期望和均值的正太分布
x=np.random.normal(0,0.8,1000)
y=np.random.normal(-2,1,1000)
z=np.random.normal(3,2,1000)

kwargs=dict(bins=100,alpha=0.2)
#alpha是透明度
plt.hist(x,**kwargs)
plt.hist(y,**kwargs)
plt.hist(z,**kwargs)
plt.show()