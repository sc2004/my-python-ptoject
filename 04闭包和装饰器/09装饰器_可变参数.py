"""
可变参数的装饰器
"""


def hint(fn_name):
    def inner(*args, **kwargs):
        print("正在努力计算中...")
        return (fn_name(*args, **kwargs))
    return inner

@hint
def get_sum(*args, **kwargs):
    """
    该函数用于计算数字列表和字典value值
    :param args: 数字列表
    :param kwargs: 字典,键是字符串，值是数字 **kwargs 接收所有关键字参数
    :return: 数字列表和字典value值的和
    """

    #定义求和变量
    sum = 0
    # 遍历元组
    for i in args:
        sum += i
    # 遍历字典
    for i in kwargs.values():
        sum += i
    return sum


sum = get_sum(13, 27, a=0, b=20)
print(sum)

