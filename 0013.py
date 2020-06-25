def get_sum_first_n_digits(path, n_digits):
    file = open(path)
    nums_sum = 0
    for num in file:
        nums_sum += int(num)
    return str(nums_sum)[:n_digits]


if __name__ == "__main__":
    first_n_digits = 10
    print(get_sum_first_n_digits("file", first_n_digits))
