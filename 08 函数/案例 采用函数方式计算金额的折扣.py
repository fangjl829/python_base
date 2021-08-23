# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/22 19:03
# !/usr/bin/python3
# -*- coding:utf-8 -*-

# 定义一个函数，把输入的金额和折扣后的金额做处理，运用 if 判断
def fun_checkout(money):
    """
    这是一个函数，用于把可输入的金额通过逻辑判断的方式根据不同的折扣计算金额
    """
    money_old = sum(money)
    money_new = money_old
    if 500 <= money_old < 1000:
        money_new = '{:.2f}'.format(money_old * 0.9)
        # 在500到1000金额之间，享受9折优惠
    elif 1000 <= money_old < 2000:
        money_new = '{:.2f}'.format(money_old * 0.8)
        # 1000到2000之间，享受8折优惠
    elif 2000 <= money_old < 3000:
        money_new = '{:.2f}'.format(money_old * 0.7)
        # 2000到3000之间，享受7折优惠
    elif 3000 <= money_old:
        money_old = '{:.2f}'.format(money_old * 0.6)
        # 3000以上，享受6折优惠
    return money_old, money_new
    # 最后返回折扣前后的金额


# 采用列表，存储输入的金额，并调用函数
print("===开始计算折扣后的金额===")
money_list = []
while True:
    inmoney = float(input("请出入您的购物金额,按0退出:"))
    if int(inmoney) == 0:
        print("没有购物的话，不需要结账，可以直接离开！")
        break
        # 金额为0，直接退出程序
    else:
        money_list.append(inmoney)
        money = fun_checkout(money_list)
print("您的总金额是:", money[0], "您的应付金额是:",money[1])



