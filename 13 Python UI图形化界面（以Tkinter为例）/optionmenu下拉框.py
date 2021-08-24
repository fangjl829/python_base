
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/17 19:36
# !/usr/bin/python3
# -*- coding:utf-8 -*-


"""optionmenu 的使用测试"""
from tkinter import *

root = Tk();root.geometry("200x100")

v = StringVar(root)
v.set("百战程序员")
om = OptionMenu(root, v, "尚学堂", "百战程序员", "卓越班[保底 18 万]")
om["width"] = 10
om.pack()

def test1():
    print("最喜爱的机构:", v.get())
    # v.set("尚学堂")
    # 直接修改了 optionmenu 中选中的值
    Button(root, text="确定", command=test1).pack()

root.mainloop()