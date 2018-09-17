def sum_of_squares(n):
    return int((n * (n + 1)) * (2 * n + 1) / 6)


def square_of_sum(n):
    return int(((n * (n + 1)) / 2)) ** 2


print(abs(sum_of_squares(100) - square_of_sum(100)))
