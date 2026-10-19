"""
创建类的格式:

class 类名:
    类体

class 类名():
    类体

class 类名(object):
    类体
"""
# 需求: 创建一个学生类
class Student:
    def name(self):
        print('学生类1')
class Student():
    def name(self):
        print('学生类2')
class Student(object): # 学生类继承自object类
    def name(self):
        print('学生类3')


s = Student()
s.name()
print(type(s))