
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/26 08:07
# !/usr/bin/python3
# -*- coding:utf-8 -*-

def sequence_search(alist,v):
    for i in range(len(alist)): #i指列表的索引下标
        if alist[i] == v:
            return i
    #没有找到
    return -1

if __name__ == '__main__':
    alist=[4,3,5,1,233,66,99]
    index=sequence_search(alist,199)
    if index != -1:
        print('找到了，索引值为：',index)
    else:
        print('没有找到')