import math


def x(bound):
    lis = set()
    for d in range(2, bound + 1):
        for n in range(math.floor(d * 0.4), math.ceil(d * 0.43) + 1):
            if math.gcd(n, d) == 1:
                lis.add(n / d)
    lis = sorted(list(lis))
    print(lis.index(3 / 7) - 1) 


x(10 ** 7)
#
# import math
#
#
# def x():
#     lis = set()
#     for d in range(2, 12001):
#         for n in range(d // 3, d // 2 + 1):
#             if math.gcd(n, d) == 1:
#                 lis.add(n / d)
#     lis = sorted(list(lis))
#     print(len(lis[lis.index(1 / 3):lis.index(1 / 2) - 1]))
#
#
# x()
