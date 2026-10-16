"""
魔法方法_init()
特点:
1. 方法名必须是__init__()
2. 方法中必须有self参数
3. 方法中可以有其他参数
4. 会自动调用，不需要手动调用
"""
class Car:
    def __init__(self, color, tire):
        print('init方法被调用')
        self.color = color
        self.tire = tire
        # 在init方法中可以设置属性，每个对象都有自己的属性

    def show(self):
        print(f'{self}的颜色是{self.color}，轮胎是{self.tire}')

c1 = Car('红色', 4)
c1.show()
# 修改c1的颜色为黄色
c1.color = '黄色'
c1.show()

c2 = Car('蓝色', 4)
c2.show()
