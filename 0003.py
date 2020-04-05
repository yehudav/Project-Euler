def get_max_prime_factor(num):
    factor = 2
    cur = num
    while cur > 1:
        if evenly_divisible(cur, factor):
            cur /= factor
        else:
            factor += min(factor - 1, 2)
    return factor


def evenly_divisible(n, d):
    return n % d == 0


print(get_max_prime_factor(600851475143))
