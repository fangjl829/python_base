
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 16:17
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入模块
import multiprocessing
import time
#定义执行任务的函数
def colck(interval):
    for i in range(3):
        print('当前时间：{}'.format(time.ctime()))
        time.sleep(interval)

if __name__=='__main__':
    #创建子进程
    p=multiprocessing.Process(target=colck,args=(1,))
    p.start()
    p.join()
    print('p.pid:',p.pid)
    print('p.name:',p.name)
    print('p.is_alive:',p.is_alive())