
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/23 20:57
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入模块
import matplotlib.pyplot as plt
import numpy as np
#生成1000个标志的正太分布随机数
x=np.random.randn(1000)
# plt.hist(x)
#修改柱的宽度  使用bins
plt.hist(x,bins=100)#10个柱装在一起
plt.show()
