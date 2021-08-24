
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 16:25
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#导入模块
from socket import *
#创建服务器端套接字对象
server_socket=socket(AF_INET,SOCK_STREAM)
#绑定端口
server_socket.bind(('',8989))
#监听
server_socket.listen()
#接收客户端的连接
client_socket,client_info=server_socket.accept()
#接收客户端发送的消息
recv_data=client_socket.recv(1024)
print('接收到%s的消息%s'%(client_info,recv_data.decode('gb2312')))
#关闭连接
client_socket.close()
server_socket.close()