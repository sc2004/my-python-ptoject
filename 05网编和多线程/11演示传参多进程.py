"""
多进程案例

目的：
    属于多任务的一种实现方式，目的是充分利用CPU资源，提高程序的执行效率。
实现方式：
    导包
    创建进程对象，关联目标函数
    启动进程
"""

# 导包
import multiprocessing
import time

# 创建进程对象，关联目标函数
def coding(name, book):
    for i in range(1, book + 1):
        time.sleep(0.1)
        print(f'{name}正在学习第{i}章')
        

def music(name, song):
    for i in range(1, song + 1):
        time.sleep(0.1)
        print(f'{name}正在听第{i}首歌。。。。。。。。。')

# 创建进程对象
# p1关联coding函数，p1抢到CPU资源
# p2关联music函数
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding, args=('张三', 10))
    p2 = multiprocessing.Process(target=music, kwargs={'name': '李四', 'song': 5})  
# 启动进程
    p1.start()
    p2.start()
