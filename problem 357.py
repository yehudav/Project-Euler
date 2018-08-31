import math
import numpy as np


def sieve_of_eranthoses(bound):
    primes = [0, 1, 2]
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
    primes = remove_zeros(sieve_of_eranthoses(10000000))
    lis = [1]
    for i in range(10000001, bound, 2):
        flag = True
        bb = math.sqrt(i)
        for j in lis:
            if j > bb:
                break
            if i/ j != i//j:
                flag = False
                break
        if flag:
            lis.append(i)
    print(len(lis))

    print(len(primes))


x(1000000000)
