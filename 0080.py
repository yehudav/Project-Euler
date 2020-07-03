from decimal import *


def sum_of_100(bound, precision):
    getcontext().prec = precision
    sum = Decimal(0)
    for i in range(2, bound):
        sum += get_sum(Decimal(Decimal.sqrt(Decimal(i))) - Decimal(int(Decimal.sqrt(Decimal(i)))))
    return sum


def get_sum(d):
    # getcontext().prec = 100

    sum = 0
    st = str(d)[2:]
    for c in st:
        sum += int(c)
    return sum
# todo refactor

getcontext().prec = 100

print(get_sum(Decimal.sqrt(Decimal(2))))
# print(sum_of_100(100, 100))
