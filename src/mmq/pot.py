import math

def pow_adjustment(points: list[tuple[float, float]]):
    n = len(points)
    sum_x = float(0)
    sum_y = float(0)
    sum_xy = float(0)
    sum_x2 = float(0)

    for x, y in points:
        logy = math.log(y)
        logx = math.log(x)
        sum_x += logx
        sum_y += logy
        sum_xy += logx*logy
        sum_x2 += logx*logx

    a = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    logb = (sum_x * sum_xy - sum_y*sum_x2) / (sum_x**2 - n*sum_x2)
    b = math.exp(logb)

    return a, b