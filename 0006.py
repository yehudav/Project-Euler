import util


def sum_of_squares_square_of_sum_difference(n):
    return abs(util.sum_of_squares_up_to_n(n) - util.square_of_sum_up_to_n(n))


if __name__ == "__main__":
    n = 100
    print(sum_of_squares_square_of_sum_difference(n))
