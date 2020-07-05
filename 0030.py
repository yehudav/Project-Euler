def get_sum_of_digits_nth_powers(n):  # todo refactor

    powers_sum = 0
    num = n

    while num > 0:
        powers_sum += ((num % 10) ** 5)
        num = int(num / 10)

    return powers_sum

    numbers = []

    for i in range(2, 1000000):
        if i == sum_of_power(i):
            numbers.append(i)

    sum_of_nums = 0

    for i in numbers:
        sum_of_nums += i


if __name__ == "__main__":
    n = 5
    print(get_sum_of_digits_nth_powers(n))
    print(get_sum_of_digits_nth_powers(n) == 443839)
