"""
对象属性和类属性。
属性介绍：
    对象属性：对象的属性，是对象的特征。
        只能通过对象名.属性名 来访问对象属性。
    类属性：类的属性，是类的特征。所有对象共享的属性。
        能通过类名.属性名 和 对象名.属性名 来访问类属性。
"""

# 演示对象属性和类属性。
class Student:

    #· 定义类属性。
    school = "清华大学"
    
    #· 定义对象属性。在类的内部，使用self.属性名 = 属性值 来定义对象属性。
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}，学校：{self.school}"

if __name__ == "__main__":
    #· 创建对象。
    stu1 = Student("张三", 18)
    stu2 = Student("李四", 19)
    print(stu1)
    print(stu2)
    #修改对象属性。
    stu2.age = 20
    stu2.school = "北京大学"
    print(stu2)
    Student.school = "中国大学"
    print(stu2.school)
    #修改类属性。
    print(Student.school)
    print(stu1.school)
