
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 16:44
# !/usr/bin/python3
# -*- coding:utf-8 -*-

from threading import Thread,Lock
import time

#创建互斥锁
lock_a=Lock()
lock_b=Lock()
class MyThread1(Thread):
    def run(self):
        if lock_a.acquire():
            print(self.name,'执行')
            time.sleep(1)
            if lock_b.acquire():
                print(self.name, '执行')
                time.sleep(1)
                lock_b.release()
            lock_a.release()

class MyThread2(Thread):
    def run(self):
        if lock_b.acquire():
            print(self.name,'执行')
            time.sleep(1)
            if lock_a.acquire():
                print(self.name, '执行')
                time.sleep(1)
                lock_a.release()
            lock_b.release()

if __name__ == '__main__':
    t1=MyThread1()
    t2=MyThread2()
    t1.start()
    t2.start()

