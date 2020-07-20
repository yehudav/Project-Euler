import math
import euler_utils as eu


def get_totient_maximum_below_bound(n):
    pass


# todo refactor

#
# def que(bound):
#     primes = eu.sieve_of_eratosthenes(bound)
#     factors = [i for i in primes if i != 0]
#     f = set(factors)
#     dic = {i: i / (i - 1) if i in f else 0 for i in range(2, bound)}
#     print(dic)
#     # for i in range(2, bound):
#     #     if primes[i] != 0:
#     #         primes[i] = geti(i)
#     #     else:
#     #         primes[i] = seti(i, factors)
#     #
#     # return primes.index(max(primes))
#
#
# def geti(prime):
#     return 1 / (1 - 1 / prime)
#
#
# def seti(n, factors):
#     ret = set()
#     for f in factors:
#         if f > n:
#             break
#         if n / f == n // f:
#             ret.add(f)
#     a = 1
#     for j in ret:
#         a *= geti(j)
#     return a
#

def que(bound):
    maxi = 0
    for i in range(1, bound):
        cur = 0
        for j in range(1, i):
            if math.gcd(i, j) == 1:
                cur += 1
        if cur > 0:
            maxi = max(maxi, i / cur)
    return maxi


if __name__ == "__main__":
    n = 1000000
    print(que(n))
