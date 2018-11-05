def find_first_n_digits_of_numbers_sum(path, first_digits_num):
    numbers_sum = get_nums_sum(path)
    return get_first_n_digits(numbers_sum, first_digits_num)


def get_nums_sum(path):
    file = open(path)
    nums_sum = 0
    for num in file:
        nums_sum += int(num)
    return nums_sum


def get_first_n_digits(num, n):
    return str(num)[:n]


print(find_first_n_digits_of_numbers_sum("file.txt", 10))
