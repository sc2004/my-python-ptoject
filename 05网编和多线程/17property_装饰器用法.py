"""
property_装饰器用法
property_装饰器：
    用于将方法转换为属性，调用时不需要加括号
    方式一：装饰器
    方式二：类属性

property_装饰器的用法：
    @property
    def 方法名(self):
        方法体
        return 返回值
"""

# 定义学生类
class Student:
    def __init__(self):
        self.__age = 18
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        #实际开发中数据是从前端传过来的，需要进行校验，属于二次校验
        self.__age = age

if __name__ == '__main__':
    s1 = Student()
    s1.age = 20
    print(s1.age)


