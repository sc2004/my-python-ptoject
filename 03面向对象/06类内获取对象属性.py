"""
类内:self.   类外：对象名.

类内设置属性:__init__()
"""

# 创建汽车类 ，设置属性颜色，轮胎
class Car:
    def __init__(self, color, tire):
        self.color = color
        self.tire = tire
    def run(self):
        print(f'{self}的汽车再跑')
    def show(self):
        print(f'{self}的颜色是{self.color}，轮胎是{self.tire}')
c1 = Car('红色', 4)
c1.show()
c1.run()
