"""
网编案例_文件上传_服务器端
    创建客户端Socket对象.
    绑定ip 和 端口号.
    滚动数据源文件，上传到服务器端
    读取客户端上传的(文件)数据，写到目的地文件
    释放资源.
"""
import socket

# 创建服务器端Socket对象.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip 和 端口号.
client_socket.connect(('127.0.0.1', 5025))
# 滚动数据源文件，上传到服务器端
with open("C:\\Users\\36298\\Desktop\\test.txt", "rb") as f:
    while True:
        data = f.read(8192)
        client_socket.send(data)
        if not data:
            break

# 释放资源.
client_socket.close()
