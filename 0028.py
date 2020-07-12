def get_spiral_diagonals_sum(diagonal_len):
    if diagonal_len < 1:
        raise ValueError
    cur_num, cur_jump = 1, 2
    sum_of_diagonals = 1
    while cur_num < diagonal_len ** 2:
        sum_of_diagonals += cur_jump * 10 + cur_num * 4
        cur_num, cur_jump = cur_num + 4 * cur_jump, cur_jump + 2
    return sum_of_diagonals


if __name__ == "__main__":
    n = 1001
    print(get_spiral_diagonals_sum(n))
