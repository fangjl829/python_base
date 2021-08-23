
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/23 20:55
# !/usr/bin/python3
# -*- coding:utf-8 -*-


#导入matplotlib模块
import matplotlib.pyplot as plt
#准备x y
x=[1,2,3,4,5]
y=[1,4,9,16,25]
#绘制折线
#linewidth属性设置线条的宽度
plt.plot(x,y,linewidth=5)
#添加x y轴名称
plt.xlabel('x')
plt.ylabel('y=x^2')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#给图标添加标题
plt.title('多个点绘制折线图')
plt.show()