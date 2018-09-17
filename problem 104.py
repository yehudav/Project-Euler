import math


def fib():
    sq = math.sqrt(5)
    n = 1474
    f2 = (1 / sq) * (((sq + 1) / 2) ** n - ((sq - 1) / 2) ** n)
    return f2


print(fib())
