# 常量（不会发生变化的量，常量的名称全部为大写）
PI = 3.14
NAME = "zhp"

# 00函数+面向对象
def log_seperator1():
    print("-" * 30)

def log_seperator2():
    print("*" * 30)

def log_seperator3():
    print("+" * 30)

def log_seperator4():
    print("#" * 30)
# 测试函数
# __name__: python的内置变量，表示当前模块的名字（直接运行当前模块，__name__的值为 “__main__" ;当该模块被导入时，__name__的值就是模块名称
# 执行当前文件，则会执行如下代码，如果被当作模块导入，如下代码不执行
if __name__ == "__main__":
    log_seperator1()

