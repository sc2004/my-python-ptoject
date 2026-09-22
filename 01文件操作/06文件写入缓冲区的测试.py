# open
f = open("./test.txt", "w", encoding="utf-8")

f.write("Hello World\n")
f.write("Hello World\n")
f.write("Hello World\n")
f.write("Hello World\n")
f.write("Hello World\n")
f.write("Hello World\n")
f.write("Hello World\n")
f.write("Hello World\n")

f.flush()
# close之前会自动flush
f.close()
