"""
迭代器
    概述：
        自定义得类，只要重写了__iter__方法和__next__方法，那么就叫迭代器了。
    目的：
        实现自定义迭代器，提高程序的可扩展性和灵活性。
        惰性加载：在需要时才加载数据，而不是在创建迭代器时就加载所有数据。
"""
# 模拟range(1, 6) 自定义，迭代器实现同等逻辑

for i in range(1, 6):
    print(i)
print('-----------------')

class MyIterator:
    
    # 自定义迭代器类
    def __init__(self, start, end):
        self.current_value = start
        self.end = end

    # 实现__iter__方法 迭代器对象
    def __iter__(self):
        return self

    # 实现__next__方法 迭代器对象
    def __next__(self):
        if self.current_value >= self.end:
            raise StopIteration
        self.current_value += 1
        return self.current_value - 1

for i in MyIterator(1, 6):
    print(i)
