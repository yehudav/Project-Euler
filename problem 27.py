"""         problem 27           """

# b most be prime
# n + a < b   or  n - a < b


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


def primes(bound):
    primes = sieve_of_eratosthenes(10000000)
    b_s = remove_zeros(sieve_of_eratosthenes(bound))
    max_num = 0
    a_s = range(1000)
    max_a = 0
    max_b = 0
    for b in b_s:
        for a in a_s:
            n = 0
            while True:
                cur = n * (n - a) + b
                if primes[abs(cur)] != 0:
                    n += 1
                else:
                    break
            if max_num < n - 1:
                max_a = a
                max_b = b
    print(max_a, max_b)
    return max_a * max_b


print(primes(1000))
# print(len(set(sieve_of_eranthoses(1000))))
