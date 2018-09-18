import math


def x(bound):
    enu = 2
    maxi = 3 / 7
    val = 0.4
    # for d in range(2, bound + 1):
    d = 999999
    low, high = int(math.floor(d * 0.42)), int(math.ceil(d * 0.43)) + 1
    for n in range(low, high):
        if math.gcd(n, d) == 1:
            v = n / d
            if v > val and v < maxi:
                val = v
                enu = n
    return enu


print(x(1000000))
