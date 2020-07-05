def get_spiral_diagonals_sum(diagonal_len):  # todo refactor
    spiral_length = diagonal_len ** 2
    cur_num = 1
    sum_of_diagonals = 1
    jump = 2

    while cur_num < spiral_length:
        sum_of_diagonals += jump * 10 + cur_num * 4
        cur_num += 4 * jump
        jump += 2

    return sum_of_diagonals


if __name__ == "__main__":
    n = 1001
    print(get_spiral_diagonals_sum(n))
    print(get_spiral_diagonals_sum(n) == 669171001)
