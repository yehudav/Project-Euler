from fractions import *


def square_root_longer_numerator(n):
    num = 0
    cur = Fraction(3, 2)
    for i in range(n):
        cur += 1
        cur = 1 / cur + 1
        if is_numerator_longer(cur.denominator, cur.numerator):
            num += 1
    return num


def is_numerator_longer(dd, nn):
    if len(str(nn)) > len(str(dd)):
        return True
    return False
# todo refactor

print(square_root_longer_numerator(1000))
