
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 16:26
# !/usr/bin/python3
# -*- coding:utf-8 -*-


from socket import *
#创建客户端套接字对象
client_socket=socket(AF_INET,SOCK_STREAM)
#调用connect方法与服务器建立连接
client_socket.connect(('192.168.121.1',8888))
while True:
    #客户端发送消息
    msg=input('>')
    client_socket.send(msg.encode('utf-8'))
    if msg == 'bye':
        break
    #客户端接收消息
    recv_data=client_socket.recv(1024)
    print('服务器端说：',recv_data.decode('utf-8'))
client_socket.close()