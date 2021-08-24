
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/17 19:46
# !/usr/bin/python3
# -*- coding:utf-8 -*-

"""askcolor 颜色选择框的测试，改变背景色"""
from tkinter import *
from tkinter.colorchooser import *
root = Tk()
root.geometry("400x150")


def test1():
    # 这里的askcolor中的red为默认颜色
    s1 = askcolor(color="red", title="选择背景色")
    print(s1)
    # s1 的值是：((0.0, 0.0, 255.99609375), '#0000ff')
    root.config(bg=s1[1])


Button(root, text="选择背景色", command=test1).pack()

root.mainloop()
