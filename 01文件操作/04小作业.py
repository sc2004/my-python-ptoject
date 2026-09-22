f = open("./word.txt", "r", encoding="utf-8")
num = 0
for line in f:
    print(line.strip())
    line = line.strip()
    line.split(" ")
    for word in line.split(" "):
        if "itheima" == word:
            num += 1
print(f"文件中有{num}个itheima")
f.close()