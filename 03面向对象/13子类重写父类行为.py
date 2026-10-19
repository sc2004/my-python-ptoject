"""
子类重写父类行为
    子类可以重写父类的方法，实现自定义的行为

重写解释：
    重写也叫做方法覆盖，子类出现与父类相同的方法，也叫重写
    调用层次：先调用子类的方法，再调用父类的方法，就近原则
"""

class Master:
    def __init__(self, ):
        self.kongfu = '[古法配方]'
    def make_cake(self):
        print(f'采用{self.kongfu}，做煎饼')

class Master2:
    def __init__(self, ):
        self.kongfu = '[新配方配方]'
    def make_cake(self):
        print(f'采用{self.kongfu}，做煎饼')

class Prentice(Master, Master2):
    def __init__(self, ):
        self.kongfu = '[独创配方]'
    def make_cake(self):
        print(f'采用{self.kongfu}，做煎饼')


if __name__ == '__main__':
    p1 = Prentice()
    p1.make_cake()
