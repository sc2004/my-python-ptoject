"""
线程入门
"""
import threading
import time

def coding():
    for i in range(1, 11):
        print(f'正在学习第{i}章')
        time.sleep(0.1)

def music():
    for i in range(10):
        print('正在听歌')
        time.sleep(0.1)

if __name__ == '__main__':
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)
    t1.start()
    t2.start()