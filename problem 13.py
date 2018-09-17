def find_sum_first_n_digits(path, first_digits_num):
    file = open(path)
    numbers_sum = 0

    for num in file:
        numbers_sum += int(num)

    return str(numbers_sum)[:first_digits_num]


print(find_sum_first_n_digits("file.txt", 10))
