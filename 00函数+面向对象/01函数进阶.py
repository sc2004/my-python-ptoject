# 计算n的阶乘
# 一定要有终结点
"""
jc(10) = 10 * jc(9)
jc(9) = 9 * jc(8)
...
jc(3） = 3 * jc(2) = 3 * 2 = 6
jc(2) = 2 * jc(1) = 2 * 1 = 2
jc(1) = 1
"""
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n-1)
print(jc(8))