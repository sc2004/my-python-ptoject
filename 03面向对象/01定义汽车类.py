class Car:
    def run(self):
        print("会跑")

c1 = Car()
c1.run()
print(f"c1对象：{c1}")
print(f"c1对象的地址：{id(c1)}")
c1.run()
