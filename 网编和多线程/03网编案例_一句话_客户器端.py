"""
网编案例_一句话_服务器端
    概述：
        服务器端负责接收客户端发送的数据，进行处理，最后将处理结果返回给客户端
    实现：
        1. 创建服务器端socket对象
        2. 绑定ip和端口
        3. 接收服务器端端发送的数据，打印出来
        4. 给服务器端端发送数据
        5. 释放资源
    细节：
        客户端和服务器端通过字节流的形式进行通信
"""

# 导入socket模块
import socket

# 1. 创建socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定ip和端口
client_socket.connect(('127.0.0.1', 10086))
# 3. 接收服务器端端发送的数据，打印出来
data = client_socket.recv(1024).decode('utf-8')
print('客户端收到', data)
#4. 给服务器端端发送数据
client_socket.send('你好，服务器！'.encode('utf-8'))
# 7. 释放资源
client_socket.close()
