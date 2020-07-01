import euler_utils as eu


def sum_of_squares_square_of_sum_difference(n):
    return abs(eu.sum_of_squares_up_to_n(n) - eu.square_of_sum_up_to_n(n))


if __name__ == "__main__":
    n = 100
    print(sum_of_squares_square_of_sum_difference(n))
