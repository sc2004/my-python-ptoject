"""
nonlocal关键字
    用于在闭包中修改外部变量
"""

# 1. 定义一个闭包
def outer(num1):
    def inner():
        nonlocal num1
        num1 += 10
        print(f'和是{num1}')
    return inner

inner = outer(50)
inner()
inner()
inner()