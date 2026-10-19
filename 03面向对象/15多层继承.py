"""
多层继承
    a继承b，b继承c，这就是多层继承

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

class Tusun(Prentice):
    pass

if __name__ == '__main__':
    t1 = Tusun()
    t1.make_cake()
