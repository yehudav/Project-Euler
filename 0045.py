import math

"""
Every hexagonal number is a triangular number - no need to check if triangular
"""


def get_nth_num_that_is_triangular_pentagonal_and_hexagonal(n):
    res = 0
    hex_gen = generate_hexagonal_nums()
    while n > 0:
        cur_hex = hex_gen.__next__()
        if is_pentagonal(cur_hex):
            res = cur_hex
            n -= 1
    return res


def generate_hexagonal_nums():
    cur = 1
    add = 5
    while True:
        yield cur
        cur += add
        add += 4


def is_pentagonal(i):
    return ((math.sqrt(24 * i + 1) + 1) / 6) % 1 == 0


if __name__ == "__main__":
    n = 3  # 1, 40755 are both triangular, pentagonal and hexagonal
    print(get_nth_num_that_is_triangular_pentagonal_and_hexagonal(3))
