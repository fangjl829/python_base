
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 16:42
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入模块
import _thread
import time
def fun1():
    print('开始运行fun1')
    time.sleep(4)
    print('运行fun1结束')

def fun2():
    print('开始运行fun2')
    time.sleep(2)
    print('运行fun2结束')

if __name__ == '__main__':
    print('开始运行')
    #创建线程
    _thread.start_new_thread(fun1,())
    _thread.start_new_thread(fun2,())
    time.sleep(7)
