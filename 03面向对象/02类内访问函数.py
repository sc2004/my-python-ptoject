# 定义汽车类 类内有run(),在work()调用run()

class Car:
    def run(self):
        print(f'{self}汽车再跑')

    def work(self):
        print(f'是work函数，我的self是{self}')
        # 输出self地址
        print(f"self地址是{id(self)}")
        print("")
        # 通过self调用类内的run函数
        self.run(self)
c1 = Car()
c1.work()
print(f"")
