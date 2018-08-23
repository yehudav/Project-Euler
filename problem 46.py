"""         problem 46           """

import math


def sieve_of_eranthoses(bound):
    primes = [0, 0, 0]
    i = 3
    while i < bound:
        primes.append(i)
        primes.append(0)

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


def get_odd_composites(bound, primes):
    lis = []
    i = 9
    while i <= bound:
        if primes[i] != i:
            lis.append(i)
        i += 2
    return lis


def get_squares(bound):
    lis = []
    for i in range(1, bound // 2 + 2):
        lis.append(2 * i ** 2)
    return lis


def min_odd_composite_counter(bound):
    primes_list = sieve_of_eranthoses(bound)
    odd_composits_list = get_odd_composites(bound, primes_list)
    primes_list = remove_zeros(primes_list)
    squars_list = get_squares(bound)

    options_lis = []
    for sqr in squars_list:
        for p in primes_list:
            options_lis.append(p + sqr)
    options_lis = list(set(options_lis)).sort()

    for o in odd_composits_list:
        if o not in options_lis:
            return o
    return "ohhh bound not big enough"

# print(min_odd_composite_counter(10))
print(sieve_of_eranthoses(1000))
# print(get_odd_composites(1000, sieve_of_eranthoses(1000)))