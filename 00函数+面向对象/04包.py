# 导入模块
# import utils.my_fun
#
# utils.my_fun.log_seperator1()
# utils.my_fun.log_seperator2()

# from utils import my_fun

# my_fun.log_seperator1()
# my_fun.log_seperator2()
# my_fun.log_seperator3()

# 如果要通过这种方式from utils import *导入包下所有模块，需要在__init__.py文件中添加__all__=[]
#
# from utils import *
#
# my_fun.log_seperator1()
# my_fun.log_seperator2()

# 2.导入模块的功能
# 相对路径：从当前文件所在目录开始查找
from utils.my_fun import log_seperator1, log_seperator2
log_seperator1()
log_seperator2()