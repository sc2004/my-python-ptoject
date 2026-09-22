#学生类
from random import choice


class Student:
    def __init__(self, name, chinese_score, math_score, english_score):
        self.name = name
        self.chinese_score  = chinese_score
        self.math_score = math_score
        self.english_score = english_score

    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese_score} | 数学：{self.math_score} | 英语: {self.english_score}"

    # 修改学生成绩
    def update_score(self, chinese_score = None, math_score = None, english_score = None):
        if chinese_score is not None:
            self.chinese_score = chinese_score
        if math_score is not None:
            self.math_score = math_score
        if english_score is not None:
            self.english_score = english_score


#教务管理系统类：
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = [] # 记录在校学生的学生信息

    # 添加学生成绩
    def add_student(self):
        name = input("请输入学生的姓名：")

        #判断学生的姓名是否存在，如果存在则添加失败
        for s in self.student_list:
            if s.name == name:
                print("该学生已经存在，添加失败")
                return

        chinese_score = int(input("请输入学生的语文成绩："))
        math_score = int(input("请输入学生的数学成绩："))
        english_score = int(input("请输入学生的英语成绩："))

        # 判断分数是否在 0-100 之间
        if 0 <= chinese_score <= 100 and 0 <= math_score <= 100 and 0 <= english_score <= 100:
            stu = Student(name, chinese_score, math_score, english_score)
            self.student_list.append(stu)
            print("学生信息添加成功")
        else:
            print("学生各科成绩要在0-100之间")
            return

    # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生的姓名：")

        # 根据学生信息
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩{s}")

                chinese_score = int(input("请输入修改后的语文成绩："))
                math_score = int(input("请输入修改后的数学成绩："))
                english_score = int(input("请输入修改后的英语成绩："))

                # 判断分数是否在 0-100 之间
                if 0 <= chinese_score <= 100 and 0 <= math_score <= 100 and 0 <= english_score <= 100:
                    s.update_score(chinese_score,math_score, english_score)
                    print("成绩修改成功")
                    print(f"修改后的成绩{s}")
                else:
                    print("学生各科成绩要在0-100之间")
                return
        print("未找到该学生，修改失败")


    # 删除学生成绩
    def delete_student(self):
        name = input("请输入要删除的学生的姓名：")

        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("未找到该学生，删除失败")


    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生的姓名：")

        for s in self.student_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return
        print("未找到该学生，删除失败")


    # 展示全部学生成绩
    def show_student(self):
        for s in self.student_list:
            print(s)

    # 运行系统的方法
    def run(self):
        print(f"欢迎使用教务系统v{EduManagement.system_version}")

        while True:
            print()
            print("-" * 70)
            print("1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5.查询所有学生 6.退出系统")
            print("-" * 70)


            choice = input("请选择要执行的操作(1-6)：")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.query_student()
                case "5":
                    self.show_student()
                case "6":
                    print("拜拜")
                    break
                case _:
                    print("输入错误")



# 测试
if __name__ == "__main__":
    edu_management = EduManagement()
    edu_management.run()