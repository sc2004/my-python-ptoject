import time
s = time.time()
f = open("./test.txt","w", encoding="utf-8")
for i in range(1000000):
    f.write(str(i)+"\n")
    f.flush() #带这句话性能急剧下降

f.close()
end = time.time()
print(end-s)