# # 异常处理
# try:
#     print("-" * 30)
#     print(my_name)
#     print("-" * 30)
# except NameError as e: # 捕获的是 NameError错误
#     print("程序运行出错,异常信息：", e)

try:
    print("-" * 30)
    print(1/0)
    print("-" * 30)
except ZeroDivisionError as e: # 捕获的是 NameError错误
    print("程序运行出错,异常信息：", e)

