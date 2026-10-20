"""
一个装饰器装饰多个函数
    一个装饰器的参数有且只能有一个
    有多个参数，要多包裹一层，当成内部函数返回
"""

def logging(flag):
    def my_decorator(fn_name):
        def inner(a, b):
            if flag == '+':
                print('努力计算加法中')
            else:
                print('努力计算减法中')
            return fn_name(a, b)
        return inner
    return my_decorator

@logging('+')
def get_sum(a, b):
    return a + b

@logging('-')
def get_diff(a, b):
    return a - b

print(get_sum(10, 20))
print(get_diff(10, 20))