"""
继承入门
    子类可以继承父类的属性和方法
    叫法：
        子类，派生类
        父类，基类
        父类，超类
    好处：
        1. 代码复用
        2. 代码维护性
    弊端：
        耦合性增加
    开发原则：
        高内聚，低耦合
"""

# 定义一个父类
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name}的年龄是{self.age}'

# 定义一个子类
class Dog(Animal):
    pass
        
# 实例化对象
d1 = Dog('旺财', 1)
print(d1)