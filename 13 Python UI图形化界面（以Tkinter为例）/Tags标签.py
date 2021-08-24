
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/16 20:30
# !/usr/bin/python3
# -*- coding:utf-8 -*-


from tkinter import *
import webbrowser


root = Tk();root.geometry("300x300+400+400")
w1 = Text(root,width=40,height=20)
#宽度 20 个字母(10 个汉字)，高度一个行高
w1.pack()

w1.insert(INSERT,"good good study,day day up!\n 北京尚学堂\n百战程序员\n 百度，搜一下就知道")
w1.tag_add("good",1.0,1.9)
w1.tag_config("good",background="yellow",foreground="red")
w1.tag_add("baidu",4.0,4.2)
w1.tag_config("baidu",underline=True)

def webshow(event):
    webbrowser.open("https://www.baidu.com")

w1.tag_bind("baidu","<Button-1>",webshow)
root.mainloop()