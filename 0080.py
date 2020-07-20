from decimal import *


def sum_of_100(bound, precision):
    getcontext().prec = precision
    sum = 0
    for i in range(1, bound):
        sum += get_sum(Decimal.sqrt(Decimal(i)))
    return sum


def get_sum(d):
    print(d)
    sum = 0
    st = str(d)[2:]
    print(st)
    for c in st:
        sum += int(c)
    return sum
# todo refactor


# print(get_sum(Decimal.sqrt(Decimal(2))))
print(sum_of_100(101, 100))
