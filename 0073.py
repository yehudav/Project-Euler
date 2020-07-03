import math


def x():
    lis = set()
    for d in range(2, 12001):
        for n in range(d // 3, d // 2 + 1):
            if math.gcd(n, d) == 1:
                lis.add(n / d)
    lis = sorted(list(lis))
    print(len(lis[lis.index(1 / 3):lis.index(1 / 2) - 1]))


x()
# todo refactor