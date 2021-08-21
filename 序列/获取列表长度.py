
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/21 22:14
# !/usr/bin/python3
# -*- coding:utf-8 -*-

# 根据索引值，依次取出列表中的每一个元素
user_list = [ "范德彪","刘华强","尼古拉赵四","宋小宝","刘能" ]

for index in range( len(user_list) ):
  item = user_list[index]
  print(item)