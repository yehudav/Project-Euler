def evenly_divisible(n, d):
    return n % d == 0


def get_prime_factors(num):
    divisors = set()
    factor = 2
    cur = num
    while cur > 1:
        if evenly_divisible(cur, factor):
            cur /= factor
            divisors.add(factor)
        else:
            factor += min(factor - 1, 2)
    return divisors


def find_max_prime_factor(num):
    divisors = get_prime_factors(num)
    return max(divisors)


print(find_max_prime_factor(600851475143))
