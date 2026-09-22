"""
1. 打开
2. 读写
3. 关闭
"""
# 相对路径写法
f = open("test.txt", "r", encoding="utf-8")
# 绝对路径写法
f2 = open("D:\\code\\python\\01文件操作\\test.txt", "r", encoding="utf-8")

# content = f.read()
# print(content)

# 仅读取5个长度
# content = f.read(5)
# print(content)

#resdlines 分行读\n不会清除
# lst = f.readlines()
# print(f"{lst}, type:{type(lst)}")
# for line in f.readlines():
#     line = line.strip()  #去除收尾的空格和回车
#     print(line)

# 一次读一行
print(f.readline().strip())
print(f.readline().strip())
print(f.readline().strip())

while True:
    pass

# close
# f.close()