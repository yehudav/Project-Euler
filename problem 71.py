import math


def x(bound):
    lis = [0.5]
    for d in range(2, bound + 1):
        for n in range(1, d):
            if math.gcd(d, n) == 1:
                lis.append(n / d)
    lis.sort()
    return lis[lis.index(3 / 7) - 1]


print(x(1000000))
