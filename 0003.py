import math
import util


def get_max_prime_factor(n):
    if n < 2:
        raise ValueError
    factor = 2
    cur = n
    while cur > 1:
        if util.is_divisible(cur, factor):
            cur //= factor
        else:
            factor += min(factor - 1, 2)
    return factor


if __name__ == "__main__":
    n = 600851475143
    print(get_max_prime_factor(n))
