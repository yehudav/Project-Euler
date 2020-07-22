from fractions import *


def get_denominator_of_four_digit_cancelling_fractions_product():
    result = Fraction(1, 1)
    for denominator in range(10, 100):
        for numerator in range(10, denominator):
            if is_digit_cancelling_fraction(numerator, denominator):
                result *= Fraction(numerator, denominator)
    return result.denominator


def is_digit_cancelling_fraction(num, denom):
    shared, rd_num, rd_denom = get_shared_digit_and_reduced_fraction(num, denom)
    return False if shared is None else Fraction(num, denom) == Fraction(rd_num, rd_denom)


def get_shared_digit_and_reduced_fraction(num, denom):
    num_digits, denom_digits = set(str(num)), set(str(denom))
    shared = denom_digits & num_digits
    res = list(shared) + list(num_digits - shared) + list(denom_digits - shared)
    return [None, None, None] if len(res) != 3 or "0" in res else list(map(int, res))


if __name__ == "__main__":
    print(get_denominator_of_four_digit_cancelling_fractions_product())
