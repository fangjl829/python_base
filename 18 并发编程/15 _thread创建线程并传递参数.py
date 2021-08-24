
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 16:43
# !/usr/bin/python3
# -*- coding:utf-8 -*-

import _thread
import time
def fun1(thread_name,delay):
    print('开始运行fun1，线程的名：',thread_name)
    time.sleep(delay)
    print('运行fun1结束')

def fun2(thread_name,delay):
    print('开始运行fun2，线程的名：',thread_name)
    time.sleep(delay)
    print('运行fun2结束')

if __name__ == '__main__':
    print('开始运行')
    #创建线程
    _thread.start_new_thread(fun1,('thread-1',3))
    _thread.start_new_thread(fun2,('thread-2',3))
    time.sleep(7)
