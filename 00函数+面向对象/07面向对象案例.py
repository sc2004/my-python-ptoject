# 商品类
class Goods:
    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number

    def __str__(self):
        return f"商品名称：{self.name}, 商品价格：{self.price}, 商品数量{self.number}"

    def update_goods(self, price = None, number = None):
        if price is not None:
            self.price = price
        if number is not None:
            self.number = number
        print("修改成功")

# if __name__ == "__main__":
#     g1 = Goods("鼠标", 12, 12)
#     print(g1)
#     g1.update_goods(price = 20)

# 购物车类
class ShoppingCart:
    system_version = "1.0"
    system_name = "购物车系统"

    def __init__(self):
        self.goods = []

    # 添加购物车
    def add_goods(self):

        name = input("请输入商品名字：")
        for goods in self.goods:
            if goods.name == name:
                print("商品已存在")
                return

        price = int(input("请输入商品价格："))
        number = int(input("请输入商品数量："))
        goods = Goods(name, price, number)
        self.goods.append(goods)

    # 修改购物车
    def update_goods(self):
        name = input("请输入要修改商品名字：")
        for goods in self.goods:
            if goods.name == name:
                print(f"当前信息{goods}")
                price = int(input("请输入修改后商品价格："))
                number = int(input("请输入修改后商品数量："))
                goods.update_goods(price, number)
                print(f"修改后信息：{goods}")
                return

        print("没有这个商品")


    # 删除购物车
    def delete_goods(self):

        name = input("请删除商品名字：")
        for goods in self.goods:
            if goods.name == name:
                self.goods.remove(goods)
                print("删除成功")
                return

        print("无此商品")


    # 查询购物车
    def query_goods(self):

        name = input("请查询商品名字：")
        for goods in self.goods:
            if goods.name == name:
                print(goods)
                return

        print("无此商品")

    # 查询所有
    def show_goods(self):
        for goods in self.goods:
            print(goods)


s1 = ShoppingCart()
while 1:
    print("*" * 70)
    print("1.添加购物车 2.修改购物车 3.删除购物车 4.查询购物车 5.列出所有购物车 6.退出系统")
    print("*" * 70)
    choice = input("请输入操作(1-6):")
    match choice:
        case "1":
            s1.add_goods()
        case "2":
            s1.update_goods()
        case "3":
            s1.delete_goods()
        case "4":
            s1.query_goods()
        case "5":
            s1.show_goods()
        case "6":
             break
        case _:
            print("输入错误")





