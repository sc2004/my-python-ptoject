"""
mode:
- r 只读
- w 写入
    - 如果文件不存在则新建
    - 如果文件存在则清空
- a 追加
"""
# 打开
f = open("./test.txt", "w", encoding="utf-8")
# 将helloworld写入文件
# write函数表示将内容写入缓冲区
f.write("Hello World")
# 将缓冲去的内容写进硬盘
f.flush()

# 关闭
f.close()
for line in open("./test.txt", "r", encoding="utf-8"):
    print(line.strip())