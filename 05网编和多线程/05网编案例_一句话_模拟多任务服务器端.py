"""
网编案例_一句话_服务器端
    概述：
        服务器端负责接收客户端发送的数据，进行处理，最后将处理结果返回给客户端
    实现：
        1. 创建socket对象
        2. 绑定ip和端口
        3. 设置最大连接数为5
        4. 等待建立连接
        5. 给客户端发送数据
        6. 接收客户端发送的数据
        7. 释放资源
    细节：
        客户端和服务器端通过字节流的形式进行通信
"""

# 导入socket模块
import socket

# 1. 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定ip和端口
server_socket.bind(('127.0.0.1', 10086))
# 3. 设置最大连接数为5
server_socket.listen(5)

while True:
    try:
        # 4. 等待建立连接
        print('等待客户端连接...')
        accept_socket, client_info = server_socket.accept()
        print('客户端连接成功', client_info)
        # 5. 给客户端发送数据
        accept_socket.send(b'Welcome to the server!')
        # 6. 接收客户端发送的数据
        data = accept_socket.recv(1024).decode('utf-8')
        print('客户端发送的数据', data)
        # 7. 释放资源
        accept_socket.close() # 关闭客户端连接
        # server_socket.close() #  服务器端连接一般不关闭
    except:
        pass


# 扩展：设置端口号重用，目的是：快速重启服务器（服务器关闭后，立即释放端口）
# 参1: SOL_SOCKET 表示socket选项
# 参2: SO_REUSEADDR 表示端口号重用
# 参3: True 该
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
