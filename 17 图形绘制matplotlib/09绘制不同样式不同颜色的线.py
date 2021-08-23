
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/23 20:56
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入模块
import matplotlib.pyplot as plt
import numpy as np
#创建x
x=np.linspace(0,10,100)
plt.plot(x,x+0,'--g')
plt.plot(x,x+1,'-.r')
plt.plot(x,x+2,':b')
plt.plot(x,x+3,'.k')
plt.plot(x,x+4,',c')
plt.plot(x,x+5,'*y')
plt.show()