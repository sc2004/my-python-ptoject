"""
无参无返回值的装饰器
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致
    原函数是无参无返回的，装饰器的内部函数也必须是无参无返回的
    原函数是有参有返回的，装饰器的内部函数也必须是有参有返回的
"""

# 定义无参无返回的get_sum()求和函数，在不改变源代码的基础上，增加友好提示

def hint(fn_name):
    def inner(a, b):
        print("正在努力计算中...")
        fn_name()
    return inner


@hint
def get_sum():
    a = 10
    b = 20
    print(a + b)

get_sum()
