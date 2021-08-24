
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/7/28 19:04
# !/usr/bin/python3
# -*- coding:utf-8 -*-


# name = input("请输入你的名字：")
#
# if name == "alex":
#     print("恭喜，登录成功！")
# else:
#     print("对不起，登录失败！")


# print(1 > "string")

# int(6)
# int(9)
# a=int(6+9)
# print(a)
# type(6)


# int("这是一个字符串内容")

# int(True)
# int(False)

# a=str(6)+str(9)
# print(a)


# str("true")
# str("false")
#
# str(True)
# str(False)

# print((int(50)*int(10))/int(5))
# print(50*10/5)

# print(int(8) > int(10))a

# print(int(30)/2)


# print(int(30)%int(2))a


# print(3*str("我爱我的祖国",end=","))a


# print("wupeiqi" == "alex" )

# print(int(666)==int(666))

# # print(str(666)==int(666))
#
# def =
# ciossfang =
# help("keywords")

# name = "wupeiqi"
# name_new = name
# print(name_new)
# print(name)
#
# name = "alex"
# print(name_new)
# print(name)
#
# name = 18
# age = str(name)
# print(type(name))

# number1 = input("请输入第一个数字：")
# number2 = input("请输入第二个数字：")
# # 计算两者之和，但是要声明为整数型
# sum = int(number1) + int(number2)
# print(sum)


# name = input("请输入你的用户名：")
# password = input("请输入你的密码：")
#
# if name == "wupeiqi" and password == "uuu":
#     print("恭喜，登录成功！")
# else:
#     print("抱歉，登录失败！")


# # print(“猜数字游戏开始”)
# num = input("请输入一个数字：")
#
# if int(num) > int(10):
#     print("猜错了！")
# else:
#     print("猜对了！")


# num = input("请输出一个数字：")
# if int(num) % 2 == 0:
#     print("偶偶偶数")
# else:
#     print("奇奇奇数")


# score = input("请输入分数：")
# data = int(score)
#
# if data > 90:
#     print("优秀")
# elif data > 80:
#     print("良好")
# elif data > 70:
#     print("及格")
# elif data > 60:
#     print("差")
# else:
#     print("不及格！")


# 实现一个10086的语音服务平台流程
# print("欢迎拨打10086热线，话费业务请按1，业务办理请按2，投诉建议请按3，人工线路请按0:")
#
# num = input("请输入按办理的业务代码：")
# if  num == '1':
#     print("话费业务")
#     num_sub = input("请输入话费业务的子业务，话费查询请按1，话费充值请按2，返回请按#号键:")
#     if num_sub == '1':
#         print("话费查询")
#     elif num_sub == '2':
#         print("话费充值")
#     else:
#         print("返回上一层")
# elif num == '2':
#     print("业务办理")
# elif num == '3':
#     print("投诉建议")
# else:
#     print("人工线路")


# print('''文能提笔安天下，
# 武能上马定乾坤。
# 心存谋略何人姓，
# 古今英雄唯是君。''')


# while True:
#     print("如果祖国遭受了侵犯，热血男儿当自强。喝干这碗家乡的酒，壮士一去不复还。")


# 实现一个用户密码登录检验系统

# print("开始登录系统")
#
# retry = 1
# while retry < 6:
#     name = input("请输入你的用户名：")
#     password = input("请输入你的密码：")
#     if name == "ciossfang" and password == "123456":
#         print("恭喜你，登录成功！")
#         break
#     else:
#         if retry < 5:
#             print("抱歉，登录失败。请重新输入用户名密码登录")
#             retry = retry + 1
#         else:
#             print("5次大限已过，滚蛋吧！")
#             exit(504)
#
# print("系统登录成功，请享受您的冲浪之旅吧！")


# data = True
# while data:
#     num = input("请输入数字：")
#     num = int(num)
#     if num > 66:
#         print(" 大了")
#     elif num < 66:
#         print("小了")
#     else:
#         print("正确")
#         data = False


# n = 1
# while n < 101:
#     print(int(n))
#     n = n + 1
#结束")


# n = 1
# while n < 11:
#     if n != 7:
#         print(int(n))
#         n = n + 1
#     else:
#         break
# print("结束")


# n = 0
# while n < 10:
#     n = n + 1
#     if n != 7:
#         print(int(n))
#     else:
#         continue
# print("结束")


# n = 0
# while n < 100:
#     n = n + 1
#     print(n)
#     sum
# print("结束")
#
# n = 0
# while n < 100:
#     if n % 2 != 0:
#         print(n)
#     n = n + 1
# print("结束")
#
#
# n = 10
# while n < 11:
#     print(n)
#     n = n - 1
#     if n == 0:
#         break
#
#
# sum = 0
# n = 0
# while n < 100:
#     n = n + 1
#     sum = sum + n
# print(sum)


# name = "ciossfang"
# age = 34
# # text = "我的姓名叫%s" %name
# text = "我的姓名叫%s，年龄是%s" %(name,age)
# print(text)

# text = "%s, 这个电影我已经下载了90%%了，居然断网了" %"xiongdi"
# print(text)


# text = "我叫{0},今年{1}岁"
# data1 = text.format("ciossfang",34)
# data2 = text.format("dong",31)
# print(data1)
# print(data2)


# text = "我叫{n1},今年{n2}岁，真实姓名也叫{n1}".format(n1="ciossfang",n2=34)
# # print(text)
#
# action = "跑步"
# line1 = f"嫂子喜欢{action},运动完后满身大汗"
# print(line1)



# action = "跑步"
# drink = "茶"
# line2 = f"嫂子喜欢{action},喜欢喝{drink}"
# print(line2)
#
# # 十进制
# v1 = f"我的年龄是{22}岁"
# print(v1)
#
# # 二进制
# v2 = f"我的年龄是{22:#b}岁"
# print(v2)
#
# # 八进制
# v3 = f"我的年龄是{22:#o}岁"
# print(v3)
#
# # 十六进制
# v4 = f"我的年龄是{22:#x}岁"
# print(v4)

# name = "ciossfang"
# text = f"我的名字是{ name.upper() }"
# print(text)
#
# count = 0
# while count < 3:
#     count = count + 1
#     user = input("请输入用户名：")
#     password = input("请输入密码:")
#     if user == "ciossfang" and  password == "123456":
#         print("恭喜，登录验证通过！")
#         break
#     else:
#         count_remind = f"验证失败，您还可以登录{3-count}次"
#         print(count_remind)



# v1 = bin(25)
# print(v1)
#
# v2 = oct(25)
# print(v2)
#
# v3 = hex(25)
# print(v3)
#
# v1 = int("0b101010",base=2)
# print(v1)
# # 二进制转换为十进制
#
# v2 = int("0o45",base=8)
# print(v2)
# # 八进制转换成十进制
#
# v3 = int("0x45",base=16)
# print(v3)
# # 十六进制转换成十进制


# name = "举头望明月，低头思故乡"
# data = name.encode("utf-8")
#
# file_object = open("/Users/ucloud/Downloads/poet.txt",mode="wb")
# file_object.write(data)
# file_object.close()

# v1 = int("186",base=10)
# # 看成十进制的值，转换成整数型
# print(v1)

# v2 = int("0b1001",base=2)
# print(v2)
# # 看成二进制的值，转换成整数型
#
# v3 = int("0o144",base=8)
# print(v3)
# # 看成八进制的值，转换成整数型
#
# v4 = int("0x59",base=16)
# print(v4)
# # # 看成十六进制的值，转换成整数型


# v1 = True + True
# print(v1)
#
# v1 = input("请输入居住地信息：")
# result = v1.startswith("北京")
# # result = v1.startswith("忙忙叨叨")
#
# if result = "北京":
#     print("你是北京人")
# else:
#     print("你是非北京人")
#
#
# lifezone = input("请输出居住地详细地址：")
#
# if lifezone.endswith("村"):
#     print("农村户口")
# else:
#     print("非农村户口")

# # 判断输入的字符串是否为数值，否则给出重新输入的提示
# data1 = input("请输入字符串：")
# data2 = input("请输入字符串：")
#
# if data1.isdecimal() and data2.isdecimal():
#     data = int(data1) + int(data2)
#     print(data)
# else:
#     print("输入非数值字符串，请重新输入！")


# talk = input("请输入拍马信息：")
# # 输入拍马信息："   各位老大老姐们晚上好啊   "
#
# # talk_new = talk.strip()
# if talk.lstrip() == " 各位老大老姐们晚上好啊":
#     print("左边有空格！开关不成功！")
# elif talk.rstrip() == "各位老大老姐们晚上好啊":
#     print("左边有空格！开关不成功！")
# elif talk == " 各位老大老姐们晚上好啊 ":
#     print("啥也不是！")
# else:
#     print("恭喜，验证通过！")
#
# data = input("请输入指定的内容：")
# # 内容是 “哥，原来你是树哥”
#
# data_new = data.strip("哥")
# print(data_new)
#
# data_new_left = data.lstrip("哥")
# print(data_new_left)
#
# data_new_right = data.rstrip("哥")
# print(data_new_right)
#
# data = input("请输入验证内容：")
# # 输入内容“ciossfang”
#
# data_new = data.upper()
# print(data_new)
#
# peple = "你是个好人，但是好人不适合我"
#
# peple_new =  peple.replace("好人","坏人")
# print(peple_new)
#
# dirty_word = ["草","fuck","草泥马","混蛋"]
# comment = input("请输入您的评论信息：")
#
# for i in dirty_word:
#     comment_replace = comment.replace(i,"棒~")
#
# print(comment_replace)


# name = "fangshengshan,donglijie,xiaoer"
# name_new = name.split(',')
# print(name_new)
# print(name)
#
# name = ["fangshengshan","donglijie","xiaoer"]
# name_new = "_".join(name)
# print(name_new)
#
# name = "嫂子"
# name_new1 = name.encode("utf8")
# name_new2 = name.encode("gbk")
# print(name_new1)
# print(name_new2)
#
#
# name = "王老汉"
# name_new = name.center(20,"*")
# print(name_new)
#
#
# name = "101"
# name_new = name.zfill(10)
# print(name_new)
#
#
# name1 = "come on~"
# name2 = name1 * 3
# print(name2)
#
# name1 = "ciossfang"
# name2 = len(name1)
# print(name2)
#
# name1 = "ciossfang"
# print(name1[2])
#
# name1 = "ciossfang"
# name2 = name1[0:3]
# print(name2)
#
# name = "ciossfang"
# name1 = name[0:4:2]
# print(name1)
#
# name = "ciossfang"
# name1 = name[4:0:-1]
# print(name1)


# v1 = 675
# v1_new = bin(v1)
# print(v1_new)
# 请把v1转换为二进制（字符串类型）

# v2 = "0b11000101"
# v2_new = int(v2,base=2)
# print(v2_new)
# # 请把二进制v2 转换成十进制（整数型）
#

# v3 = "11000101"
# v3_new = int(v3,base=2)
# print(v3_new)
# 请把二进制v3 转换成十进制（整数型）






# 现有 `v1=123` 和 `v2=456`，请将这两个值转换为二进制，并将其二进制后的前缀 0b 去掉。然后将两个二进制拼接起来，最终再转换成整型（十进制）
#
# user_list = []
#
# while True:
#     user = input("请输入用户名（Q退出）：")
#     if user == "Q":
#         break
#     user_list.append(user)
#
# print(user_list)


# 输出提醒开始信息
# welcome = "欢迎使用智趣游戏".center(30,'*')
# print(welcome)

# 输入游侠的参与人数
# user_count = 0
# while True:
#     count = input("请输入游戏人数：")
#     if count.isdecimal():
#         user_count = int(count)
#         break
#     else:
#         print("输入格式错误，人数必须是数字")
#
# message = "{}人参加游戏".format(user_count)
# print(message)
#
# user_name_list = []
# for i in range(1, user_count + 1):
#     tips = "请输入玩家的姓名({}/{}):".format(i, user_count)
#     name = input(tips)
#     user_name_list.append(name)
#
# print(user_name_list)
#
# tool = ['菜刀','剪刀','镰刀']
# tool_new = ['1','2','3']
# tool.extend(tool_new)
# print(tool)
#
#
# av_people = ['苍老师','宫野明美','马蓉']
# av_people.insert(1,'大桥未久')
# print(av_people)

# 导入随机生成模块
# import random
#
# data_list = ['二手充气女友','机器猫','macpro笔记本','电动牙刷']
# name = input('请输入您的名字：')
#
# # 建立一个循环，由于非空列表为True，这一句相当于 while True:
# while data_list:
#     value = random.choice(data_list)
#     info = "恭喜{0},您的奖品是{1}".format(name,value)
#     print(info)
#     data_list.remove(value)
#     print(data_list)
#     break
# # break 允许抽奖单次结束，否则上面的while会一直循环下去

# # 排队买火车票
# # '李杰','张三','五斗米道人','方胜山','小核桃''老妖','小和尚','董丽杰'
# buy_ticket = []
# ticket = 0
#
#
# while ticket < 5:
#     name = input("北京-上海高铁火车票开始发售，请输入购买车票人名：")
#     if name == 'Q':
#         print("请输入正确的购买人名！")
#     else:
#         buy_ticket.append(name)
#     name = buy_ticket.pop(0)
#     ticket = ticket + 1
#     info = '恭喜{0},您的火车票已经购买完成！'.format(name)
#     print(info)
#
# # 没有买到票的人：'老妖','小和尚','董丽杰'
# fail_user = ['老妖','小和尚','董丽杰']
# fail_user_new = ','.join(fail_user)
# info = "对不起：{0}票已经售完，麻烦选择其他的出行方式。".format(fail_user_new)
# print(info)
#
# name = ['李杰','张三','五斗米道人']
#
# name_new = name.index('五斗米道人')
# print(name_new)
#
# num = ['100','22','21','56','32','200']
# print(num)
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)
#
# name  = ['老妖','小和尚','董丽杰']
# if 'alex' in name:
#     print("删除alex")
#     name.remove('alex')
# else:
#     print('alex 用户不在')


# user_list = ['李杰','张三','五斗米道人','方胜山','小核桃''老妖','小和尚','董丽杰']
# user_list_new = user_list[::-1]
# print(user_list_new)

# data = '方胜山'
# data_new = list(data)
# print(data_new)

# user_list = [['李杰','张三'],'五斗米道人','方胜山',['小核桃''老妖','小和尚','董丽杰']]
# print(user_list[0])
# print(user_list[1])
# print(user_list[0][1])
# print(user_list[1][-1])
# user_list.append(666)
# # print(user_list)
# user_list[0].append('张三丰')
# print(user_list)
# user_list[0][0] = "李连杰"
# print(user_list)

# 定义列表 li
# li = ['alex','WuSir','ritian','barry','武沛齐']
# 计算列表的长度并输出
# list_len = len(li)
# print(list_len)
# 输出结果
# 5

# 列表中追加元素"seven"并输出添加后的列表
# li.append('seven')
# print(li)
# ['alex', 'WuSir', 'ritian', 'barry', '武沛齐', 'seven']


# 请在列表的第一索引位置插入元素“Tony”，并输出添加后的列表
# li.insert(1,'Tony')
# print(li)
# ['alex', 'Tony', 'WuSir', 'ritian', 'barry', '武沛齐']


# 请修改列表第二个索引位置的元素为“Kelly”，并输出修改后的列表
# li[2] = "Kelly"
# print(li)
# ['alex', 'WuSir', 'Kelly', 'barry', '武沛齐']

# 请将列表中的第三个索引位置的值修改为“妖怪” 并输出修改后的列表
# li[3] = '妖怪'
# print(li)
# ['alex', 'WuSir', 'ritian', '妖怪', '武沛齐']

# 请将列表`data=[1,"a",3,4,"heart"]` 的每一个元素追加到列表 `li`中，并输出添加后的列表。
# data=[1,"a",3,4,"heart"]
# li_new = list(li) + list(data)
# print(li_new)
# ['alex', 'WuSir', 'ritian', 'barry', '武沛齐', 1, 'a', 3, 4, 'heart']

# 请将字符串 `s = "qwert"`的每一个元素增加到表`li`中。
# s = "qwert"
# s_new = list(s)
# print(s_new)
# li.append(s_new)
# print(li)
# ['alex', 'WuSir', 'ritian', 'barry', '武沛齐', ['q', 'w', 'e', 'r', 't']]



# 请删除列表中的元素“barry” 并输出删除元素后的列表
# li.remove("barry")
# print(li)
# ['alex', 'WuSir', 'ritian', '武沛齐']

# + 请删除列表中的第二个元素，并输出删除元素后的列表
# li.pop(2)
# print(li)
# ['alex', 'WuSir', 'barry', '武沛齐']

# 请删除列表中的第二到4个元素，并输出删除元素后的列表。
# del li[1:4]
# print(li)
# ['alex', '武沛齐']

# 创建列表 li
li = [1,3,2,"a",4,"b",5,"c"]

# 通过对 li 列表的切片形成新的列表[1,3,2]
# li_new = li[0:3]
# print(li_new)
# [1, 3, 2]

# 通过对li 列表的切片形成新的列表 ["a",4,"b"]
# li_new = li[3:6]
# print(li_new)
# ['a', 4, 'b']

# 通过对 li 列表的切片形成新的列表[1,2,4,5]
# li_new = li[0:8:2]
# print(li_new)
# [1, 2, 4, 5]


# 通过对 li 列表的切片形成新的列表 [3,"a","b"]
# li_new = li[1:6:2]
# print(li_new)
# [3, 'a', 'b']

# 通过对 li 列表的切片形成新的列表 [3,"a","b","c"]
# li_new = li[1::2]
# print(li_new)
# [3, 'a', 'b', 'c']

# 通过对li 列表的切片，形成新的列表["c"]
# li_new = li[-1]
# print(li_new)
# c

# 通过对 li 列表的切片，形成新的列表 ["b","a",3]
# li_new = li[1:6:2]
# print(li_new)
# li_new.sort(reverse=True)
# print(li_new)

# li = [1,3,2,"a",4,"b",5,"c"]
#
# a = (1)
# print(type(a))
# b = (1,)
# print(type(b))
#
# data = {'方胜山','董丽杰','二姐'}
# data.add('大姐')
# print(data)

data1 = {'二姐', '方胜山', '大姐'}
data2 = {'大姐', '董丽杰'}

# 方式1、intersection
# data3 = data1.intersection(data2)
# print(data3)

# 方式2、&
# data3 = data1 & data2
# print(data3)

# 方式1、union
# data3 = data1.union(data2)
# print(data3)

# 方式2、|
# data3 = data1 | data2
# print(data3)

# 方式1、差集difference
# data3 = data1.difference(data2)
# print(data3)
# data3 = data2.difference(data1)
# print(data3)

#方式1、-
# data3 = data1 - data2
# print(data3)
# data3 = data2 - data1
# print(data3)
#
#
# data1 = {'二姐', '方胜山', '大姐'}
# data2 = {'大姐', '董丽杰'}
# data3 = data1 - data2
# print(data3)
#
# data1 = {1,True}

#
#
# print("我是你二大爷")
#
#
# print("看这风景美如画",end=",")
# print("本想吟诗走天下",end=".")
#
#
#
#
# print("看这风景美如画")
# print("本想吟诗走天下")
#
# print("我是alice")
# print(我是alice)
#
# # 加法
# print(3+4)
# # 乘法
# print(3*4)
# print(3*"你大爷还是你大爷")
# # 除法
# print(9/3)
# # 求余
# print(9//4)
# # 幂等运算
# print(3**4)

# a = "c_abcd3456"
# b = "c_abcd3456"
# print(a is b)
#
# c = "dd#"
# d = "dd#"
# print(c is d)
#
# print(id(c))
# print(id(d))
#
#
# # 字符串的格式化
# # string_1 = "{0}是一个好小伙子，他在{1}公司上班。职位是{2}.{0}的wx是x.".format("方胜山","UCloud","云计算工程师")
# # print(string_1)
# string_1 = "{name}是一个好小伙子，他在{company}公司上班。职位是{job}.{name}的wx是x.".format(name="方胜山",company="UCloud",job="云计算")
# print(string_1)


# "{:*>8}".format("右对齐")
# print("{:#>8}".format("name"))
# # ####name
# left = "{:&<10}".format("左对齐")
# print(left)
# 左对齐&&&&&&&

# square = "{:#^10}".format("square")
# print(square)
# ##square##


# string_1 = "{0}拥有大量存款，他的存款金额是{1:.2f}"
# print(string_1.format("方胜山",40000.1234))
# 方胜山拥有大量存款，他的存款金额是40000.12
# string_1 = "{0}拥有大量存款，他的存款金额是{1:-.2f}"
# print(string_1.format("方胜山",-40000.1234))
# 方胜山拥有大量存款，他的存款金额是-40000.12
#
#
# a = list()
# a=list(range(10))
# print(a)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# a = range(0,10,2)
# print(list(a))
# [0, 2, 4, 6, 8]
#
# a = [ x*2 for x in range(100) if x%9==0]
# print(a)
# [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198]
# print(id(a))
# b = [10,20]
# a = a+b
# print(id(a))
# print(a)
#
# # 输出结果
# [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198]
# 140467736491264
# 140467738030656
# [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 10, 20]

a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
# print(a)
# print(a['name'])
#
#
# print(a.get('age'))
# print(a.get('sex'))
#
#
# print(a.items())
#
# print(a.keys())
# print(a.values())

# print(len(a))
#
# print("sex" in dict(a))
#
# a = {'name':'fangshengshan','sex':'girl','age':'18'}
# print(a)
# a['class'] = 'class3'
# print(a)
# a['salary'] = '1800000'
# print(a)
# a = {'name':'fangshengshan','sex':'girl','age':'18'}
# # b = {'class':'class3','salary':'1800000'}
# b = {'name':'fangshengshan','salary':'1800000'}
# a.update(b)
# print(a)
# a = {'name':'fangshengshan','sex':'girl','age':'18'}
# a.clear()
# print(a)
# a = {'name':'fangshengshan','sex':'girl','age':'18'}
# del a['name']
# del a['sex']
# print(a)
# a.pop('name')
# print(a)

# 把表格的各栏目内容转换为字典定义
# t1 = {"name":"高小一","age":'18','salaxy':'30000','city':"北京"}
# t2 = {"name":"高小二","age":'19','salaxy':'20000','city':"上海"}
# t3 = {"name":"高小五","age":'20','salaxy':'10000','city':"深圳"}
# t4 = {"name":"高小六","age":'21','salaxy':'40000','city':"广州"}
#
# # 尝试打出t1 的薪水
# # print(t1["salaxy"])
#
# # 循环
# table = [t1,t2,t3,t4]
# for i in range(4):
#     salaxy_new = table[i].get('salaxy')
#     print(salaxy_new)



# for i in range(10):
#     print(i**2)

# sum0 = 0
# for i in range(101):
#     sum0 = sum0 + i
# print(sum0)
#
# for i in range(5):
#     for m in range(5):
#         print(i,end='\t')
#     print('\n')

# 打印99乘法表，首先得定义两个循环，并且是嵌套的。先实现第一个循环
# 定义两个参数x，y
# for x in range(1,10):
#     for y in range(1,x+1):
#         print("{0}*{1}={2}".format(x,y,(x*y)),end='\t')
#     print()
#
#
# # 把表格的各栏目内容转换为字典定义，然后打印薪水大于20000的列表
# t1 = {"name":"高小一","age":'18','salaxy':'30000','city':"北京"}
# t2 = {"name":"高小二","age":'19','salaxy':'20000','city':"上海"}
# t3 = {"name":"高小五","age":'20','salaxy':'10000','city':"深圳"}
# t4 = {"name":"高小六","age":'21','salaxy':'40000','city':"广州"}
# t_new = [t1,t2,t3,t4]
#
# for i in t_new:
#     if i.get("salaxy") > '20000':
#         print(i)


# 录入薪资，求平均薪资水平，运用break 和continue 以及 else循环语句
# 先定义工资参数变量 salaxy，以及输入员工工资的综合 salaxy_sum
# salaxy = []
# salaxy_num = 0
#
# # 走for 循环，输入员工薪资
# for num in range(0,4):
#     s = input("请输出每一个员工的工资：")
#     if str(s.upper()) == "Q":
#         print("执行结束，退出")
#         break
#     elif int(s) < int(0):
#         print("工资数应该为大于0的数值，请重新输入：")
#         continue
#
#     salaxy.append(float(s))
#     salaxy_num += float(s)
#
# else:
#     print("您已录入4位工人的工资收入。")
#
# # 通过字符串的格式化手段，打印出工人人数，以及平均薪资水平
# print("录入的薪资分别是{0},平均工资是{1}".format(salaxy,salaxy_num/4))


# 导入时间模块
# import time
# # 优化前代码
# start1 = time.time()
# for i in range(1000):
#     result = []
#     for m in range(10000):
#         result.append(i*1000+m*100)
#
# end1 = time.time()
# print("耗时:{0}".format((end1-start1)))
#
# # 优化后代码
# start2 = time.time()
# for i in range(1000):
#     result = []
#     c = i*1000
#     for m in range(10000):
#         result.append(c+m*100)
#
# end2 = time.time()
# print("耗时:{0}".format((end2-start2)))


# 列表推导式范例1
# list = [ x for x in range(5)]
# print(list)
#
# # 创建列表推导式2
# list = [x**2 for x in range(5)]
# print(list)
#
# # 创建列表推导式3
# list = [x*2 for x in range(5)]
# print(list)
#
# # 实现满足条件的列表推导式创建
# list = [x**2 for x in range(100) if x%2==0]
# print(list)
#
# # 实现双元素嵌套循环
# list = [(x,y) for x in range(5) for y in range(5)]
# print(list)


# 字典推导式
# 采用字典推导式来实现对指定字符串字母出现次数的统计
# word = "i love you,i love dlj,i love ciossfang"
# 字典形式，以列表字母为key，出现的次数为value进行统计
# total = {c:word.count(c) for c in word}
# print(total)

# 生成器推导式（生成元组）
# 只能单次生效，第二次就会提示为空
# number = (x*2 for x in range(10) if x%2==0)
# print(number)
# for i in number:
#     print(i,end='\t')
# # 上面正常打印出来生成器中的每一个元素。再次执行
# for m in number:
#     print(m,end='\t')
# 空，这正是生成器的特性

# 综合小案例，画一个小海龟
# import  turtle
# t = turtle.Pen()
# t.circle(50)
# turtle.done()


# 函数的学习
# 定义的函数
# def number_list():
#     print("*"*15)
#     string_new = "这是一个测试函数"
#     print(string_new.center(10,'#'))
#     print("*"*15)
#     print()
#
# for i in range(5):
#     print(number_list())

# 形参&实参
# def function_new(a,b):
#     '''这个函数用来比较传入两个参数的大小，并且打印出其中比较大的那个'''
#     if a>b:
#         print(a,"较大者")
#     else:
#         print(b,"较大者")
#     return a+b
#
#
# print(function_new(10,15))
# print(function_new(12,30))
# print(help(function_new.__doc__))


# return 的作用1
# def function_new(a,b):
#     '''这个函数用来比较传入两个参数的大小，并且打印出其中比较大的那个'''
#     if a>b:
#         print(a,"较大者")
#     else:
#         print(b,"较大者")
#     return a+b
#
# print(function_new(30,40)/10)

# return 的作用2
# def function_new(a,b):
#     '''这个函数用来比较传入两个参数的大小，并且打印出其中比较大的那个'''
#     if a>b:
#         print(a,"较大者")
#     else:
#         print(b,"较大者")
#     return
#     print("这事一个比较ab大小的函数")


# print(function_new(30,40))
#
# def function_new(a,b):
#     '''这个函数用来比较传入两个参数的大小，并且打印出其中比较大的那个'''
#     if a>b:
#         print(a,"较大者")
#     else:
#         print(b,"较大者")
#
# c = function_new(20,30)
# print(c)

# 测试局部变量和全局变量的效率比
# import math
# import time
#
# def sqrt_1():
#     start1 = time.time()
#     for i in range(100000000):
#         math.sqrt(30)
#     end1 = time.time()
#     print("耗时{0}".format((end1-start1)))
#
# print(sqrt_1())
#
#
# def sqrt_2():
#     c = math.sqrt
#     start2 = time.time()
#     for i in range(100000000):
#         c(30)
#     end2 = time.time()
#     print("耗时{0}".format((end2-start2)))
#
# print(sqrt_2())

#
# # 传递可变对象的变量
# a = [10,20]
#
# def number_1(b):
#     print(id(b))
#     b.append(30)
#     print(id(b))
#
# print(number_1(a))
# print(a)

# 传递不可变对象的变量
# str1 = "i love python~"
#
# def number_2(b):
#     print(id(b))
#     b = b + "i love c++ too"
#     print(id(b))
#     print(b)
#
# print(number_2(str1))
# print(str1)


# # 深拷贝和浅拷贝
# import copy
#
# def copy_2():
#     a  = [5,6,[10,20]]
#     b =  copy.deepcopy(a)
#     print("a" ,a)
#     print("b" ,b)
#     b.append(30)
#     b[2].append(7)
#     print("a" ,a)
#     print("b" ,b)
#
# print(copy_2())


# 定义传参时候的默认参数。参数不足进行补位

# def num_3(a=b=c=20,d=30):


# 传递默认的参数
# def num_03(a,b,c=30,d=40):
#     print(a,b,c,d)
#
# print(num_03(10,10))
# print(num_03(10,20,30))
# print(num_03(10,11,12,13))

# 顺序传参
# def num_04(a,b,c,d):
#     print(a,b,c,d)
#
# print(num_04(10,12,14,16))

# 变量传参
# a = 11
# def num_05(a,b,c,d):
#     print(a,b,c,d)
#     a = 9
#
# print(num_05(a=20,b=23,c=24,d=a+1))


# 可变参数传参
# def num_06(a,b,*c):
#     print(a,b,c)
# print(num_06(10,20,30,40,50,60))
#
#
# def num_07(a,b,**c):
#     print(a,b,c)
# print(num_07(10,20,name = "fangshengshan",sex = "fale"))
#
# def num_08(a,b,*c,**d):
#     print(a,b,c,d)
# print(num_08(10,20,34,40,name="ciossfang",class_01="stage-Four"))

# 强制命名参数
# def num_08(a,b,*c,d,e):
#     print(a,b,c,d,e)
# print(num_08(10,20,30,40,60,d=40,e=50))


# 穿件lambda 匿名函数
# f = lambda a,b : print(a+b)
# print(f(3,4))
#
# f = lambda i:i**2
# print(f(4))
#
#
# # eval 函数
# a = 8
# b = eval('a**3')
# print(b)
#
# c = 10
# d = eval('c*2+c/2+c+c')
# print(d)


# 递归函数-阶乘
# def factorial(n):
#     if n == 1:return 1
#     return n*factorial(n-1)
#
# print(factorial(1))
#
# def num_5(n):
#     print("####开始###")
#     print("test01:",n)
#     if n == 0:
#         print("结束")
#     else:
#         print(num_5(n-1))
#     print("test01",n)
#
# print(num_5(5))
#
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(10))
#
#
# # 分形几何函数
#
# import numpy as np
# import pylab as pl
# from matplotlib import cm
# import math
#
# def smooth_iter_point(c):
#     """计算迭代次数，返回当迭代结果的复数的模小于等于2的最大次数"""
#     z = c
#     for i in range(1, 100):
#         if abs(z) > 2: break
#         z = z ** 2 + c
#     absz = abs(z)
#     if absz > 2.0:
#         mu = i - math.log(math.log(abs(z), 2), 2)
#     else:
#         mu = i
#     return mu
#
#
# def draw_mandelbrot(cx, cy, d, filename):
#     """"""
#     x0, x1, y0, y1 = cx - d, cx + d, cy - d, cy + d
#     y, x = np.ogrid[y0:y1:400j, x0:x1:400j]
#     c = x + y * 1j
#     mandelbrot = np.frompyfunc(smooth_iter_point, 1, 1)(c).astype(np.float)
#     pl.imshow(mandelbrot,
#               cmap=cm.Blues_r,
#               extent=[x0, x1, y0, y1])
#     pl.gca().set_axis_off()
#
#
# x, y = 0.27322626, 0.595153338
# pl.subplot(241)
# draw_mandelbrot(-0.5, 0, 1, "1.png")
# for i in range(2, 9):
#     pl.subplot(240 + i)
#     draw_mandelbrot(x, y, 0.5 ** (i - 1), "{}.png".format(i))  # 逐步放大
# pl.subplots_adjust(0.01, 0, 0.99, 1, 0.02, 0)
# pl.show()


# 嵌套函数，根据内部函数来判断输出中文名或者英文名

# def printname(ischinese,name,famliy_name):
#     def name_1(a,b):
#         print("{0} {1}".format(a,b))
#     if ischinese:
#         name_1(famliy_name,name)
#     else:
#         name_1(name,famliy_name)
# print(printname(True,"胜山","方"))
# print(printname(False,"David","smith"))



# 全局关键字 global
# count = 0
# def print_num():
#     # global count
#     count_new = 2
#     count_new += 1
#     print(count_new)
#
# print(print_num())
#
# class Student:
#     company = "SXT"  # 类属性
#     count = 0  # 类属性
#
#     def __init__(self, name, score):
#         self.name = name  # 实例属性
#         self.score = score
#         Student.count = Student.count + 1
#
#     def say_score(self):  # 实例方法
#         print("我的公司是：", Student.company)
#         print(self.name, '的分数是：', self.score)


# 第一个class类
# class StudentName:
#
# # 定义一个构造方法
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def say_score(self):
#         print("{0}的分数是：{1}".format(self.name,self.score))
#
# # 调用class类
# scoreperson = StudentName("方胜山","28")
# scoreperson.say_score()


# class Student():
#     commany = "德堂彤盛"
#     count = 2
#     # 定义类的属性
#
#     def __init__(self,name,score):
#         # 定义实例的属性
#         self.name = name
#         self.score = score
#         Student.count += 1
#
#     def say_score(self):
#         # 定义实例的方法
#         print("我的公司名称是：",Student.commany)
#         print(self.name,"的分数是：",self.score)
#
# s1 = Student("方胜山",80)
# s1.say_score()
# print("一共创建了{0}个对象".format(Student.count))


# 类方法 @classmethod
# class Student():
#     company = "sxt"
#
#     @classmethod
#     def printcompany(cls):
#         print(cls.company)
#
# Student.printcompany()

# 定义静态方法
# class Student():
#
#     @staticmethod
#     def add(a,b):
#         print("{0}+{1}={2}".format(a,b,(a+b)))
#         return a+b
#
# Student.add(100,210)

# python中没有重载的说法在，只有最后一个生效
# class Student():
#     def say_hi(self):
#         print("hello")
#     def say_hi(self,name):
#         print("{0}，hello".format(name))
#
# say_hi_1 = Student()
# say_hi_1.say_hi("方胜山")

# 私有属性的设置
# class Student():
#     __company = "德堂彤盛" # #私有类属性. 通过 dir 可以查到 _Employee__company
#
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age #私有实例属性
#     def say_company(self):
#         print("我的公司名字是{0}：".format(Student.__company))
#         # 类内部 可以直接访问私有属性
#         print("我的名字是：",self.name,"年龄是",self.__age,"岁")
#         self.__work()
#
#     def __work(self):
#         # 私有实例方法 通过 dir 可以查到 _Employee__work
#         print("好好学习，天天向上！")
#
# p1 = Student("方胜山",34)
# print(p1.name)
# print(p1.__dir__())
# print(p1.say_company())
# print(p1._Student__age)


# class Person:
#     # 默认继承 object 类
#     def __init__(self,name):
#         self.name = name
#
#     def __str__(self):
#         return "我的名字是{0}".format(self.name)
#
# p = Person("方胜山")
# print(p)
#
#
# class A:
#     def a(self):
#         print("aa")
# class B:
#     def b(self):
#         print("bb")
#
# class C(A,B):
#     def c(self):
#         print("cc")
#
# d = C()
# print(d.c())
# print(d.b())
# print(d.a())

#将 d:/a.txt 拷贝到 e:盘
# try:
#     copyFile("d:/a.txt", "e:/a.txt")
# except:
#     print("文件无法拷贝")

print(3/0)
