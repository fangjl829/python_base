
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 15:08
# !/usr/bin/python3
# -*- coding:utf-8 -*-

from time import sleep
def sing():
    for i in range(3):
        print('正在唱歌...%d'%i)
        dance()
        sleep(1)

def dance():
    for i in range(3):
        print('正在跳舞...%d'%i)
        sleep(1)

if __name__=='__main__':
    sing()
    dance()
