
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/17 21:59
# !/usr/bin/python3
# -*- coding:utf-8 -*-


#coding=utf-8
#记事本软件,练习主菜单的设计

from tkinter.filedialog import *

root = Tk();root.geometry("400x400")

#创建主菜单栏
menubar = Menu(root)

#创建子菜单
menuFile = Menu(menubar)
menuEdit = Menu(menubar)
menuHelp = Menu(menubar)

#将子菜单加入到主菜单栏
menubar.add_cascade(label="文件(F)",menu=menuFile)
menubar.add_cascade(label="编辑(E)",menu=menuEdit)
menubar.add_cascade(label="帮助(H)",menu=menuHelp)

filename = ""


def openfile():
    global filename
    w1.delete('1.0', 'end')         # 先把Text控件中的内容清空
    with askopenfile(title="打开文件") as f:
        content = f.read()
        w1.insert(INSERT, content)
        filename = f.name
        print(f.name)


def savefile():
    with open(filename, "w") as f:
        content = w1.get(1.0, END)
        f.write(content)


def exit():
    root.quit()



# 添加菜单项
menuFile.add_command(label="打开", accelerator="ctrl+o", command=openfile)
menuFile.add_command(label="保存", command=savefile)
menuFile.add_separator()  # 添加分割线
menuFile.add_command(label="退出", command=exit)
# 将主菜单栏加到根窗口
root["menu"] = menubar

w1 = Text(root, width=50, height=30)
w1.pack()


root.mainloop()