"""
封装之私有属性
    私有属性：
        私有属性在类的内部使用，外部不能直接访问
        私有属性的前缀是下划线__
    概述：
        是面向对象的三大属性之一，隐藏了类的实现细节，保护了类的属性不被外部访问，仅提供公共方法访问私有属性
    怎么封装：
        函数，类就是封装的单位
    好处：
        1. 代码隐藏，保护了类的属性不被外部访问  安全性
        2. 代码维护性，方便了代码的维护和扩展   复用性
    弊端：
        代码量增加
"""
# 徒弟给技术给徒孙，不想给私房钱

#定义师傅类
class Master:
    def __init__(self, ):
        self.kongfu = '[古法配方]'
    def make_cake(self):
        print(f'采用{self.kongfu}，做煎饼')

#定义徒弟类
class Prentice(Master):
    def __init__(self, ):
        self.kongfu = '[独创配方]'
        self.__money = '私房钱'
    def make_cake(self):
        print(f'采用{self.kongfu}，做煎饼')
    def get_money(self):
        print(self.__money)
    def set_money(self, money):
        self.__money = money


#定义徒孙类
class Tusun(Prentice):
    pass

if __name__ == '__main__':
    t1 = Tusun()
    t1.make_cake()
    print(t1.kongfu)
    # print(t1.money)
    # print(t1.__money)  # 报错，私有属性不能直接访问
    t1.get_money()
    t1.set_money('1000元')
    t1.get_money()
