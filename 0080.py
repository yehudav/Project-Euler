from decimal import *


def get_sum_of_decimal_digits_of_irrational_square_root_until_n(n, precision):
    getcontext().prec = precision + 5  # +5 for better precision
    return sum(get_sum(Decimal.sqrt(Decimal(i)), precision) for i in range(1, n + 1))


def get_sum(n, precision):
    digits = str(n)[:precision + 1]
    if "." not in digits:
        return 0
    return sum(int(digit) for digit in digits if digit != ".")


if __name__ == "__main__":
    n = 100
    precision = 100
    print(get_sum_of_decimal_digits_of_irrational_square_root_until_n(n, precision))
