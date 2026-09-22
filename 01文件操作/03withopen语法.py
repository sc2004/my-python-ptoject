"""
with open() as f:

如果用这种语法，文件会自动关闭，即自动调用close

"""
with open("./test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
# 不需要写close（）
# 在python中with xxx as xxx：的写法，都可以不用写close