# 手机类 实现开机，关机，拍照
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def open(self):
        print(f'{self.brand}{self.model}开机')
    def close(self):
        print(f'{self.brand}{self.model}关机')
    def photo(self):
        print(f'{self.brand}{self.model}拍照')

p1 = Phone('小米', '14 Pro')
p1.open()
p1.close()
p1.photo()