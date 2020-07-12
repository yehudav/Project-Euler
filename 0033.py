from fractions import *


def get_denominator_of_four_digit_cancelling_fractions_product():
    result = Fraction(1, 1)
    for denominator in range(10, 100):
        for numerator in range(10, denominator):
            if is_digit_cancelling_fraction(numerator, denominator):
                result *= Fraction(numerator, denominator)
    return result


def is_digit_cancelling_fraction(numerator, denominator):#todo refactor
    shared_digit = None
    for i in str(numerator):
        for j in str(denominator):
            if i == j:
                shared_digit = i
                break
    if shared_digit is None:
        return False
    reduced_numerator = str(numerator).replace(shared_digit, "")
    reduced_denominator = str(denominator).replace(shared_digit, "")
    return Fraction(numerator, denominator) == Fraction(int(reduced_numerator), int(reduced_denominator
                                                                                    ))

if __name__ == "__main__":
    print(get_denominator_of_four_digit_cancelling_fractions_product())
    # print(get_denominator_of_four_digit_cancelling_fractions_product() == 100)
