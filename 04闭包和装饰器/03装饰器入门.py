"""
装饰器入门
    解释：
        装饰器是指在函数外部定义的函数，该函数可以修改其他函数的行为。
    格式：
        def 装饰器函数名(形参):
            装饰器函数的(局部)变量

            def 被装饰器函数名(形参):
                被装饰器函数的(局部)变量

            return 被装饰器函数名

    写法：
        装饰后的函数名 = 装饰器函数名()
        装饰后的函数名()

        在要被装饰的函数上添加 @装饰器函数名 即可实现装饰
        
"""

def login(fn_name):
    def inner():
        print('校验登录')
        fn_name()
    return inner

def comment():
    print('评论')

def payment():
    print('支付')

commment = login(comment)
commment()
