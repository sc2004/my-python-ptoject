# 设置汽车类，颜色为红色，4个轮胎， 可以跑
class Car:
    # 属性

    # 行为
    def run (self):
        print(f'{self}的汽车再跑')

c1 = Car()
c1.brand = '奔驰'
c1.color = '红色'
c1.tire = 4
print(f"c1的品牌是{c1.brand}")
print(f"c1的颜色是{c1.color}")
print(f"c1的轮胎是{c1.tire}")
c1.run()

c2 = Car()
print(f"c2的颜色是{c2.color}")
print(f"c2的轮胎是{c2.tire}")
c2.run()
