import euler_utils as eu


def get_digits_sum_of_nth_power(base, exponent):
    return eu.get_iterable_sum(str(base ** exponent))


if __name__ == "__main__":
    base = 2
    exponent = 1000
    print(get_digits_sum_of_nth_power(base, exponent))
