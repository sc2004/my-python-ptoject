"""
类方法和静态方法
类方法：
    类方法是类的特征，所有对象共享的特征。
    类方法的定义：
        @classmethod
        def 方法名(cls):
            方法体
    类方法的调用：
        类名.方法名()
        对象名.类名.方法名()
    类方法的参数：
        cls：类名，代表类的本身。
静态方法：
    静态方法是类的特征，所有对象共享的特征。
    静态方法的定义： 参数传不传都可以
        @staticmethod
        def 方法名():
            方法体
    静态方法的调用：
        类名.方法名()
        对象名.类名.方法名()
    静态方法的参数：
        @staticmethod
                   方法体
区别：
    类方法和静态方法的区别在于，类方法需要传入类参数cls，而静态方法不需要传入任何参数。
    如果函数用类对象，就用类方法，否则就是静态方法
"""

# 定义学生类
class Student:
    #· 定义类属性。
    school = "清华大学"
    
    # 定义类方法
    @classmethod
    def change_school(cls):
        print(cls)
        print("我是类方法")

    # 定义静态方法
    @staticmethod
    def print_school():
        print("我是静态方法")

# 测试
if __name__ == "__main__":
    #· 调用类方法。
    Student.change_school()
    #· 调用静态方法。
    Student.print_school()
