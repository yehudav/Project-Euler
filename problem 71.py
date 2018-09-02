import math


def x(bound):
    lis = set()
    for d in range(2, bound + 1):
        for n in range(int(d / 2.5), d // 2):
            if math.gcd(n, d) == 1:
                lis.add(n / d)
    lis = sorted(list(lis))
    print(lis.index(3 / 7) - 1)


x(10 ** 7)
