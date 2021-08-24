
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/24 16:25
# !/usr/bin/python3
# -*- coding:utf-8 -*-


#导入模块
from socket import *
#创建UDP套接字
udp_socket=socket(AF_INET,SOCK_DGRAM)
#绑定一个端口
udp_socket.bind(('',8989)) #绑定的是本机，端口是8989
addr=('192.168.121.1',8080)
data=input('请输入要发送的信息：')
#发送数据
udp_socket.sendto(data.encode('gb2312'),addr)
recv_data=udp_socket.recvfrom(1024) #表示本次接收的最大字节数1024
print('接收到%s的消息是%s'%(recv_data[1],recv_data[0].decode('gb2312')))
#关闭套接字
udp_socket.close()
