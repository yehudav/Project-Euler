import math


def get_smallest_num_where_x_2x_3x_4x_5x_6x_contain_same_digits():
    a, b = 10, 100
    result = -1
    while result == -1:
        result = check_range_for_result(range(a, math.ceil(b / 6)))
        a, b = b, b * 10
    return result


def check_range_for_result(cur_range):
    for i in cur_range:
        if are_x_2x_3x_4x_5x_6x_contain_same_digits(i):
            return i
    return -1


def are_x_2x_3x_4x_5x_6x_contain_same_digits(i):
    digits = set(str(i))
    for j in range(2, 7):
        if digits != set(str(i * j)):
            return False
    return True


if __name__ == "__main__":
    print(get_smallest_num_where_x_2x_3x_4x_5x_6x_contain_same_digits())
