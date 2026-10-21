"""
生成器_推导式

概述：
    基于数据规则，先生成一部分，在生成一部分
目的：
    节约大量内存
实现方式：
    推导式
    yield关键字

"""

# 生成1-10得整数
# 定义函数，存储到生成器
def my_fun():
    # my_list = []
    # for i in range(1, 11):
    #     my_list.append(i)
    # return my_list
    for i in range(1, 11):
        yield i

my_g1 = my_fun()
print(my_g1)
print('-----------------')
for i in my_g1:
    print(i)