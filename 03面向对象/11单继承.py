"""
单继承
    子类只能继承一个父类

故事：摊煎饼的老师傅将技术传给徒弟

分析：
    1. 定义一个父类，表示老师傅 Master
        属性：kongfu
        方法：make_cake()
    2. 定义一个子类，表示徒弟 Prentice
    3. 子类可以继承父类的属性和方法
"""
# 定义一个父类
class Master:
    def __init__(self, ):
        self.kongfu = '[古法配方]'
    def make_cake(self):
        print(f'采用{self.kongfu}，做煎饼')

class Prentice(Master):
    pass

# 实例化对象
p1 = Prentice()
p1.make_cake()
        
