from decimal import *


def sum_of_100(bound, precision):
    getcontext().prec = precision + 5
    return sum(get_sum(Decimal.sqrt(Decimal(i)), precision) for i in range(1, bound + 1))


def get_sum(n, precision):
    digits = str(n)[:precision + 1]
    if "." not in digits:
        return 0
    return sum(int(digit) for digit in digits if digit != ".")


# todo refactor

print(sum_of_100(100, 100))
