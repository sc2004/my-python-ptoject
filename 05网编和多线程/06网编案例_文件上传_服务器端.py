"""
网编案例_文件上传_服务器端
    创建服务器端Socket对象.
    绑定ip 和 端口号.
    设置最大监听数.
    等待客户端申请建立连接
    读取客户端上传的(文件)数据
    把读取到的数据写到目的地文件中.
    释放资源.
"""
import socket

# 创建服务器端Socket对象.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip 和 端口号.
server_socket.bind(('127.0.0.1', 5025))
# 设置最大监听数.
server_socket.listen(5)
# 等待客户端申请建立连接
accept_socket, client_info = server_socket.accept()
print('客户端连接成功', client_info)
# 读取客户端上传的(文件)数据，写到目的地文件
#   循环读取
with open('D:\\code\python\\05网编和多线程\\data\\my.txt', 'wb') as f:
    # 循环读取数据
    while True:
        # 接受文件数据
        data = accept_socket.recv(8192)
        # 无数据，结束循环
        if not data:
            break
        # 把读取到的数据写到目的地文件中.
        f.write(data)
# 释放资源
accept_socket.close()
