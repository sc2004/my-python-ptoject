"""
类内:self.   类外：对象名.
"""
# 定义汽车类 类内有run(),在work()调用run()

class Car:
    def run(self):
        print(f'{self}汽车再跑')

    def work(self):
        print(f'是work函数，我的self是{self}')
        # 通过self调用类内的run函数
        self.run()

c1 = Car()
c1.work()
