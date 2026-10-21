"""
生成器案例:基于文件中的歌词生成器，生成批次歌词
"""
import math
def dataset_loader(batch_size):
    """
    自定义的歌词生成器
    batch_size: 每个批次的歌词数量
    return: 每个批次的歌词
    """
    with open('D:\\code\\python\\05网编和多线程\\data\\song.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
        total_batch = math.ceil(len(lines) / batch_size)
        for idx in range(total_batch):
            yield lines[idx * batch_size : idx * batch_size + batch_size]


# 测试
d1 = dataset_loader(10)
print(next(d1))
for batch_data in d1:
    print(batch_data)
