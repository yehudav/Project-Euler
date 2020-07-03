import math


def count_sums(bound):
    sum = 0
    primes_bound = int(math.sqrt(bound)) + 1
    primes = remove_zeros(sieve_of_eratosthenes(primes_bound))
    sqrs = []
    cubes = []
    fourths = []
    for p in primes:
        a = p ** 2
        b = p ** 3
        c = p ** 4# todo refactor
        sqrs.append(a)
        cubes.append(b)
        fourths.append(c)
    s = []
    for i in sqrs:
        for j in cubes:
            for k in fourths:
                n = i + j + k
                if n < bound:
                    s.append(n)
    return len(set(s))


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


print(count_sums(50000000))
