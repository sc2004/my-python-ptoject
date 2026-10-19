"""
多继承
    子类可以继承多个父类
    子类可以继承多个父类的属性和方法
故事：摊煎饼的老师傅将技术传给徒弟，徒弟学习多个配方

扩展：MRO机制
    解释：Method Resolution Order
    作用：解决多继承时，方法调用顺序的问题
    格式：子类名.__mro__ 
        类名.mro()

"""
# 定义一个师傅
class Master:
    def __init__(self, ):
        self.kongfu = '[古法配方]'
    def make_cake(self):
        print(f'采用{self.kongfu}，做煎饼')

# 定义第二个师傅
class Master2:
    def __init__(self, ):
        self.kongfu = '[新配方配方]'
    def make_cake(self):
        print(f'采用{self.kongfu}，做煎饼')

# 定义徒弟
class Prentice(Master, Master2): #从左到右，先调用Master，再调用Master2
    pass

# 实例化对象
p1 = Prentice()
p1.make_cake()
print(Prentice.__mro__)
print(Prentice.mro())
        
