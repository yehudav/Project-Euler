import euler_utils as eu

import math


def get_sum_of_nums_that_are_not_sum_of_two_abundant_numbers():
    abundant_nums = set(get_abundant_numbers_below_value(28124))
    range_of = range(1, 28124)
    return sum(i for i in range_of if not is_sum_of_2_abundant_nums(i, abundant_nums))


def get_abundant_numbers_below_value(n):
    return [i for i in range(1, n) if is_abundant_number(i)]


def is_abundant_number(n):
    divisors_range = range(1, math.ceil(math.sqrt(n)) )
    divisors_sum = sum(i + n // i for i in divisors_range if eu.is_divisible(n, i)) - n
    return divisors_sum > n


def is_sum_of_2_abundant_nums(n, abundant_numbers):
    for i in abundant_numbers:
        if n - i in abundant_numbers:
            return True
    return False


if __name__ == "__main__":
    print(get_sum_of_nums_that_are_not_sum_of_two_abundant_numbers())
    print(get_sum_of_nums_that_are_not_sum_of_two_abundant_numbers() == 4179871)
# todo
