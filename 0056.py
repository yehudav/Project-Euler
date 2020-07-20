def get_max_power_digits_sum(n):
    max_sum = 0
    for a in range(1, n):
        for b in range(1, n):
            max_sum = max(max_sum, sum(int(digit) for digit in str(a ** b)))
    return max_sum


if __name__ == "__main__":
    n = 100
    print(get_max_power_digits_sum(n))
