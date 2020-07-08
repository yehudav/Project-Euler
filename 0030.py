def get_nth_narcissistic_numbers_sum(n, bound):
    return sum(i for i in range(2, bound) if is_nth_narcissistic(i, n))


def is_nth_narcissistic(i, n):
    return i == sum(int(digit) ** n for digit in str(i))


if __name__ == "__main__":
    n = 5
    bound = 1000000  # 354294 < 999999 = 6*9**5 -> 1000000 is upper bound
    print(get_nth_narcissistic_numbers_sum(n, bound))
