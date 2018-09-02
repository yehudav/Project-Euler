"""         problem 47           """

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


def remove_zeros(lis):
    new_lis = []
    for i in lis:
        if i != 0:
            new_lis.append(i)
    return new_lis


def x(bound):
    prims = remove_zeros(sieve_of_eranthoses(bound))
    i = 3 * 5 * 7 * 11 - 1
    last = 0
    while True:
        last = gett(i, last)
        if last == -1:
            exit(i)
