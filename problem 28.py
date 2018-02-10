"""         problem 28           """


def diagonals_sum(bound):
    spiral_length = bound ** 2
    cur_num = 1
    sum_of_diagonals = 1
    jump = 2

    while cur_num < spiral_length:
        sum_of_diagonals += jump * 10 + cur_num * 4
        cur_num += 4 * jump
        jump += 2

    return sum_of_diagonals


print(diagonals_sum(1001))
