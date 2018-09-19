def sum_of_squares_square_of_sum_difference(n):
    return abs(sum_of_squares(n) - square_of_sum(n))


def sum_of_squares(n):
    return (n * (n + 1)) * (2 * n + 1) // 6


def square_of_sum(n):
    return ((n * (n + 1)) // 2) ** 2


print(sum_of_squares_square_of_sum_difference(100))
