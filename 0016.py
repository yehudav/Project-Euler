def get_n_power_of_2_digits_sum(exponent):
    n_power = get_n_power_of_2_digits(exponent)
    return get_digits_sum(n_power)


def get_n_power_of_2_digits(exponent):
    return str(1 << exponent)


def get_digits_sum(n):
    digits_sum = 0
    for digit in n:
        digits_sum += int(digit)
    return digits_sum


print(get_n_power_of_2_digits_sum(1000))
