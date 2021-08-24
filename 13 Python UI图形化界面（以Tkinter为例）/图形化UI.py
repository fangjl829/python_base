# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/13 13:35
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#
# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
# root.title("我的第一个GUI程序")
# root.geometry("400x600+100+200")
#
# btn01 = Button(root)
# btn01["text"] = "点我就送花"
# btn01.pack()
#
# def songhua(e):
#     messagebox.showinfo("Message", "送你一朵玫瑰花")
#     print("送你99朵玫瑰花~")
#
#
# btn01.bind("<Button-1>", songhua)
# # 设置窗口界面，执行主循环
# root.mainloop()


# 测试经典的面对对象的GUI写法
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的 GUI 程序的类的写法"""

    def __init__(self, master=None):
        super().__init__(master)
        # super()代表的是父类的定义，而不是父类对象 self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):
        """创建组件"""
        self.label01 = Label(self,text="输入用户名")
        self.label01.pack()

        # stringvar 变量绑定到指定的组件
        # stringvar 变量的值发生变化，组件内容也变化；
        # 组件内容发生变化，stringvar 变量的值也发生变化。
        v1 = StringVar()
        self.entry01 = Entry(self,textvariable=v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get());print(self.entry01.get())

        # 创建密码框
        self.label02 = Label(self,text="密码")
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self,textvariable=v2,show="*")
        self.entry02.pack()
        v2.set("123456")

        Button(self, text="登录", command=self.login).pack()


    def login(self):
        username = self.entry01.get()
        password = self.entry02.get()
        print("用户名：" + username)
        print("密码：" + password)
        if username == "ciossfang" and password == "123456":
            messagebox.showinfo("学习系统","登录成功，欢迎进入学习系统！")
        else:
            messagebox.showinfo("学习系统","登录失败，不能进入学习系统！")

    def songhua(self):
        messagebox.showinfo("送花", "送你 99 朵玫瑰花")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个经典的 GUI 程序类的测试")
    app = Application(master=root)
    root.mainloop()

# class Application(Frame):
#     """一个经典的GUI程序的类的写法"""
#     def __init__(self):
#         pass
#     def createWidget(self):
#         pass
# root = Tk()
# root.geometry("400x600+100+200")
# root.title("这是一个经典的GUI程序类写法")
# app = Application(master=root)

