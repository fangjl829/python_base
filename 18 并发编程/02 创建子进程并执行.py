
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 15:08
# !/usr/bin/python3
# -*- coding:utf-8 -*-

from multiprocessing import Process
def run_test():
    print('。。。test.....')
if __name__=='__main__':
    print('主进程执行')
    #创建子进程 target接收执行的任务
    p=Process(target=run_test)
    #调用子进程
    p.start()

