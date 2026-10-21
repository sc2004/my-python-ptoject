"""
创建socket对象
    概述：
        网络编程也叫socket编程，双方都有自己的socket对象，用于进行网络通信
        数据在socket对象之间通过udp协议和tcp协议进行传递
"""

# 导入socket模块
import socket

# 创建socket对象 
# AF_INET 表示ipv4协议（默认ipv4协议）
# SOCK_STREAM 表示tcp协议，SOCK_DGRAM 表示udp协议
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket_obj)
