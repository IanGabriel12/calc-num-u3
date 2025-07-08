import math

def logarithm_adjustment(points: list[tuple[float, float]]):
    n = len(points)
    sum_x = float(0)
    sum_y = float(0)
    sum_xy = float(0)
    sum_x2 = float(0)

    for x, y in points:
        logx = math.log(x)
        sum_x += logx
        sum_y += y
        sum_xy += logx*y
        sum_x2 += logx*logx

    a = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    b = (sum_x * sum_xy - sum_y*sum_x2) / (sum_x**2 - n*sum_x2)

    return a, b