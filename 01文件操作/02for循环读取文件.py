# 方式一
f = open("./test.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())

#等同于下面的写法
# for line in f.readlines():
#     print(line.strip())

# 方式二
for line in open("./test.txt", "r", encoding="utf-8"):
    print(line.strip())
#这个方式3个步骤都集成了
#open打开文件，for循环结束自动关闭

f.close()