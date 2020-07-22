import math
import euler_utils as eu


def get_totient_maximum_below_bound(n):
    table = [0 for i in range(n + 1)]
    primes = [i for i in eu.sieve_of_eratosthenes(n) if i != 0]
    p_se = set(primes)
    for i in range(2, len(table)):
        table[i] = i / phi(i, primes, p_se)
    return table.index(max(table[8:]))


def phi(i, primes, p_se):
    res = i
    if i in p_se:
        return res - 1
    bound = math.ceil(math.sqrt(i))
    for p in primes:
        if p > bound:
            break
        if i % p == 0:
            res *= (1 - (1 / p))
    return res


# todo refactor


if __name__ == "__main__":
    # n = 1000000
    n = 10
    print(get_totient_maximum_below_bound(n))
    # print(get_totient_maximum_below_bound(n) == )
