
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 15:09
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入模块
from multiprocessing import Process
from time import sleep
def worker(interval):
    print('work start')
    sleep(interval)
    print('work end')

if __name__=='__main__':
    print('主进程正在执行')
    #创建子进程
    p=Process(target=worker,args=(5,))
    #调用子进程
    p.start()
    #希望下面的输出语句，再子进程执行完才输出
    # sleep(4)
    #调用join方法 ：主进程等待调用join的子进程结束
    p.join()
    print('主进程执行完')
