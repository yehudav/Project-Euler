import math
import euler_utils as eu

def get_n_consecutive_nums_with_distinct_primes_factors(n):
    return x(n)


def gett(n, primes):
    s = set()
    for p in primes:
        if p > n:
            break
        if n / p == n // p:
            s.add(p)
    if len(s) == 4:
        return 1
    return -5


def x(bound):
    prims = [i for i in eu.sieve_of_eratosthenes(bound) if i !=0]
    i = 3 * 5 * 7 * 11 - 1
    last = 0
    while True:
        last += gett(i, prims)
        if last == 4:
            exit(i - 3)
        if last < 0:
            last = 0
        i += 1


if __name__ == "__main__":
    print(get_n_consecutive_nums_with_distinct_primes_factors(4))  # todo refactor
