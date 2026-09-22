def calc_order_calc(*args, coupon = 0, score = 0, express = 0.0):
    """
    根据传入的商品（商品名，价格，数量）优惠卷，积分，运费，计算总金额
    :param args: 商品信息（商品名，价格，数量）
    :param coupon: 优惠卷
    :param score: 积分
    :param express: 运费
    :return: 总金额 = 价格 * 数量 - 优惠卷 - 积分 + 运费
    """
    total_price = [good[1] * good[2] for good in args]
    total_cost = sum(total_price)
    if total_cost >= 5000 and coupon < total_cost:
        total_cost -= coupon
    if total_cost >= 5000 and score / 100 < total_cost:
        total_cost -= score / 100
    total_cost += express
    print(total_cost)

calc_order_calc(("鼠标", 88, 100), ("键盘", 188, 10), coupon = 100000,score = 100, express=3.3)

