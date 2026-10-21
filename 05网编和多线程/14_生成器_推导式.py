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

my_generator = (i for i in range(1, 11))
print(my_generator)
print('-----------------')

my_gt2 = (i for i in range(1, 11) if i % 2 == 0)
print(my_gt2)
print('-----------------')

# 从生成器中获取数据

print(next(my_generator))
print(next(my_gt2))
print(next(my_gt2))
for i in my_gt2:
    print(i)