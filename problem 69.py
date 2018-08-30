"""         problem 69           """

import math


def sieve_of_eranthoses(bound):
    primes = [-1, -1, 2]
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
        if i > 0:
            new_lis.append(i)
    return new_lis


def get_que(n, primes, factors):
    ret = set()
    for f in factors:
        if n <= 1:
            break
        while n / f == n // f:
            n = n // f
            ret.add(f)
    a = 1
    for j in ret:
        a *= primes[j]
    return a


def que(bound):
    primes = sieve_of_eranthoses(bound)
    factors = remove_zeros(primes)
    maxi = 0
    maxxx = 0
    for i in range(bound):
        if primes[i] > 0:
            primes[i] = 1 / (i - 1)
    for i in range(bound):
        if primes[i] == 0:
            primes[i] = get_que(i, primes, factors)
            if primes[i] > maxi:
                maxi = primes[i]
                maxxx = i
    return maxxx


print(que(1000000))
