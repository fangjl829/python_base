
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/17 21:35
# !/usr/bin/python3
# -*- coding:utf-8 -*-


"""文件对话框获取文件"""

from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry("400x100")


def test1():
    f = askopenfilename(title="上传文件",
                        initialdir="f:", filetypes=[("视频文件", ".mp4")])
    # print(f)
    show["text"] = f


Button(root, text="选择编辑的视频文件", command=test1).pack()

show = Label(root, width=40, height=3, bg="green")
show.pack()

root.mainloop()
