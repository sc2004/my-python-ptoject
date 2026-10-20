"""
多个装饰器装饰一个函数
    从上到下，从内到外执行
"""

def code(fn_name):
    def inner():
        print('验证验证码')
        fn_name()
    return inner

def login(fn_name):
    def inner():
        print('校验登录')
        fn_name()        
    return inner

@code
@login
def comment():
    print('评论')

comment()
