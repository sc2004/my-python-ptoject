# # 定义类 --> 不推荐 动态的为对象添加属性
# class Car:
#     pass
# # 创建对象
# c1 = Car()
# c2 = Car()
#
# # 动态的为对象添加属性
# c1.color = 'red'
# c1.brand = "BMW"
# c1.name = "X5"
# c1.price = 50000
# print(c1)
# print(c1.__dict__)
# print(c1.color)
# print(c1.brand)
# print(c1.name)

# 定义类
class Car:
    # 类属性
    wheel = 4 #轮胎数量
    tax_rate = 0.1 # 购置税的税率
    # 初始化的方法，会在对象创建的时候自动调用，可以在该方法中为对象设置对应的属性
    # self: 是第一个参数，表示当前所创建的实例对象
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel = 3
        print("Car 类型的对象初始化完毕，对象属性已经添加完毕")

# 创建对象
# c1 = Car("red", "BMW", "X7", 50000)
# print(c1.__dict__)
#
# c2 = Car("黄色", "奔驰", "X7", 50000)
# print(c2.__dict__)

    # 定义实例方法
    def running(self):
        print(f"{self.brand}{self.name}正在高速行驶中...")
    def total_cost(self, discount, rate):
        """
        计算提车的总费用，包含两个部分车的价格，税费
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        """
        total_cost = rate * self.price * discount + rate * self.price
        return total_cost

    # 魔法方法
    def __str__(self):
        return f"{self.color}, {self.brand}, {self.name}, {self.price}"
    def __eq__(self, other: object):
        return self.color == other.color and self.brand == other.brand
    def __lt__(self, other: object):
        return self.price < other.price

c1 = Car("黄色", "奔驰", "X7", 50000)
print(c1.brand)
print(c1.wheel) # 通过实例对象查找属性，会先查找实例属性，在查找类属性

# 通过类名访问类属性
print(Car.wheel)

# c2 = Car("黄色", "奔驰", "X7", 50000)
# print(c2)
#
# print(c1 == c2)
# print(c1 > c2)
