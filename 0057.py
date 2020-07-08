from fractions import *


def get_num_of_sqrt_two_expressions_with_longer_numerator(n):
    if n < 1:
        raise ValueError
    num = 0
    cur = Fraction(3, 2)
    for i in range(n):
        num, cur = update_num_of_longer_numerators_and_cur_fraction(num, cur)
    return num


def update_num_of_longer_numerators_and_cur_fraction(num, cur):
    cur = 1 + 1 / (1 + cur)
    if is_numerator_longer(cur.numerator, cur.denominator):
        num += 1
    return num, cur


def is_numerator_longer(numerator, denominator):
    return len(str(numerator)) > len(str(denominator))


if __name__ == "__main__":
    print(get_num_of_sqrt_two_expressions_with_longer_numerator(1000))
