
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 16:43
# !/usr/bin/python3
# -*- coding:utf-8 -*-

import time
from threading import Thread
num=0
def test1():
    global num
    for i in range(100000):
        num+=1
    print('执行test1函数num的值：',num)

def test2():
    global num
    for i in range(100000):
        num+=1
    print('执行test2函数num的值：',num)

if __name__ == '__main__':
    t1=Thread(target=test1)
    t2=Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()