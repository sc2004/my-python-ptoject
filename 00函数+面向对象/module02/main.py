# 导入模块
import my_fun

# 使用模块中的功能
# my_fun.log_seperator1()
# print(my_fun.PI)

# 导入自定义模块中的功能
from my_fun import log_seperator1, log_seperator2, PI, NAME
from my_fun import *
print(NAME)
print(PI)
log_seperator2()
log_seperator1()