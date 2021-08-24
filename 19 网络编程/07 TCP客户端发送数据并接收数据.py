
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 16:25
# !/usr/bin/python3
# -*- coding:utf-8 -*-

from socket import *
#创建客户端套接字对象
client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect(('192.168.121.1',8989))
#客户端发送消息
client_socket.send('haha'.encode('gb2312'))
#客户接收服务器端消息
recv_data=client_socket.recv(1024)
print('接收到消息：',recv_data.decode('gb2312'))
#关闭套接字
client_socket.close()