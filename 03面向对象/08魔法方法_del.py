class Car:
    def __init__(self, color, tire):
        self.color = color
        self.tire = tire
        # 在init方法中可以设置属性，每个对象都有自己的属性
    def __str__(self):
        return f'{self.color}的{self.tire}轮胎'
    
    def __del__(self):
        print(f'{self}被删除了')
       
c1 = Car('红色', 4)
print(c1)
# 手动删除对象
print("程序结束")