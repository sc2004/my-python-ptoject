"""
多态入门
    概述：同一个函数，不同的对象，不同的行为
    多态的条件：
        1. 要有继承关系
        2. 子类重写父类方法
        3. 父类引用指向子类对象、
"""

# 动物类案例
class Animal: #抽象类，也叫接口
    def speak(self):
        print('动物在说话')
class Dog(Animal):
    def speak(self):
        print('汪汪汪')
class Cat(Animal):
    # def speak(self):
    #     print('喵喵喵')
    pass
class Car:
    def speak(self):
        print('嘟嘟嘟')

def make_sound(an: Animal):
    an.speak()

if __name__ == '__main__':
    d1 = Dog()
    c1 = Cat()
    car1 = Car()
    make_sound(d1)
    make_sound(c1)
    make_sound(car1)

