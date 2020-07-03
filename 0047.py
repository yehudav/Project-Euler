import math


def sieve_of_eranthoses(bound):
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
# todo refactor

def remove_zeros(lis):
    new_lis = []
    for i in lis:
        if i != 0:
            new_lis.append(i)
    return new_lis


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
    prims = remove_zeros(sieve_of_eranthoses(bound))
    i = 3 * 5 * 7 * 11 - 1
    last = 0
    while True:
        last += gett(i, prims)
        if last == 4:
            exit(i - 3)
        if last < 0:
            last = 0
        i += 1


x(10000)
