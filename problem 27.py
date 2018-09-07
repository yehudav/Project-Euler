"""         problem 27           """

# b most be prime
# n + a < b   or  n - a < b


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


def primes(bound):
    primess = sieve_of_eranthoses(bound)
    primes = remove_zeros(sieve_of_eranthoses(bound))
    max_num = None
    assssss = range(-999, 1000)
    max_a = -2000
    max_b = -2000
    ass_new = set()
    for b in primes:
        for a in ass:
            if  1+a+b <bound:
                if primess[1 + a + b]!=0:
                    ass_new.add(a)
    aaaa = list(ass_new)
    aaaa.sort()
    print(aaaa)
    print(len(ass_new))

    #
    #
    #     for a in range(b):
    #         n = 0
    #         while n - a < b:
    #             c = n ** 2 + a * n - b
    #             if c not in primes:
    #                 break
    #             max_num = n
    #             n += 1
    #             max_a = a
    #             max_b = b
    # print(max_b, max_a, max_num)


primes(1000)
# print(len(set(sieve_of_eranthoses(1000))))
