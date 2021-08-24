
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 16:24
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入模块
from socket import socket,AF_INET,SOCK_DGRAM
#创建UDP套接字
udp_socket=socket(AF_INET,SOCK_DGRAM)
#创建接收信息的地址
addr=('192.168.121.1',8080)
#键盘接收发送的消息
data=input('请输入要发送信息：')
#调用sendto方法发送信息
udp_socket.sendto(data.encode('gb2312'),addr)
#关闭套接字
udp_socket.close()