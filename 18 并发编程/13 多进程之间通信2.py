
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 16:42
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入模块
from multiprocessing import Process,Pool,Manager
from time import sleep
#定义写入的方法
def write(q):
    a=['a','b','c','d']
    for i in a:
        print('开始写入的值：%s'%i)
        q.put(i)
        sleep(1)

def reader(q):
    for i in range(q.qsize()):
        print('读取到的值：%s'%q.get())
        sleep(1)

if __name__ == '__main__':
    #创建队列
    q=Manager().Queue()
    #创建进程
    pool=Pool(3)
    pool.apply(write,(q,))
    pool.apply(reader,(q,))
    pool.close()
    pool.join()
