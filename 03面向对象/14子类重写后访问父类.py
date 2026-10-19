"""
案例：子类重写父类功能后，继续访问父类的功能

思路：
    1.父类名.父类函数名(self) 精准查找
    super().父类函数名() 只能访问最近的，有就用，没有往后走
   """

class Master:
    # def __init__(self):
    #     self.kongfu = '[古法配方]'
    # def make_cake(self):
    #     print(f'采用{self.kongfu}，做煎饼')
    pass

class Master2:
    def __init__(self):
        self.kongfu = '[新配方配方]'
    def make_cake(self):
        print(f'采用{self.kongfu}，做煎饼')

class Prentice(Master, Master2):
    def __init__(self):
        self.kongfu = '[独创配方]'
    def make_master_cake(self):
        super().__init__()
        super().make_cake()
        


if __name__ == '__main__':
    p1 = Prentice()
    print(p1.kongfu)
    p1.make_master_cake() 
    p1.make_cake() 
    print(p1.kongfu)
