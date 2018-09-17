def find_digits_sum(base, exponent):
    power = str(base ** exponent)
    digits_sum = 0

    for digit in power:
        digits_sum += int(digit)

    return digits_sum


print(find_digits_sum(2, 1000))
