
import time

def fun_a():
    print('倒计时60秒')
    for i in range(60):
        print(i)
        time.sleep(1)

def fun_b():
    print('fun_b')
    for i in range(10):
        print(i)
        time.sleep(1)

fun_a()
fun_b()