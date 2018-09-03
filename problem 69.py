"""         problem 69           """

import math


def sieve_of_eratosthenes(bound):
    primes = [0, 0, 2]
    i = 3
    while i < bound:
        primes.append(i)
        primes.append(0)
        i += 2

    for j in range(3, int(math.sqrt(bound))):
        k = j + j
        while k < bound:
            primes[k] = 0
            k += j
    return primes


def remove_zeros(lis):
    new_lis = []
    for i in lis:
        if i != 0:
            new_lis.append(i)
    return new_lis


def geti(prime):
    return 1 / (1 - 1 / prime)


def seti(n, factors):
    ret = set()
    for f in factors:
        if f > n:
            break
        if n / f == n // f:
            ret.add(f)
    a = 1
    for j in ret:
        a *= geti(j)
    return a


def que(bound):
    primes = sieve_of_eratosthenes(bound)
    factors = remove_zeros(primes)
    for i in range(2, bound):
        if primes[i] != 0:
            primes[i] = geti(i)
        else:
            primes[i] = seti(i, factors)

    return primes.index(max(primes))


print(que(1000000))
