

import math


def triangle(n):
    return int((n * (n + 1)) / 2)


def is_prime(n, primes):
    for p in primes:
        if n % p == 0:
            return False
    return True


def divisors(n, primes):
    divs = 1
    cur = n

    for p in primes:
        if p > n:
            break

        if cur % p:
            continue
        else:
            power = 1
            cur /= p

        while cur % p == 0:
            power += 1
            cur /= p
        divs *= (power + 1)

    return divs


primes = [2]

j = 3

bound = int(math.sqrt(1000000)) + 5

while j < bound:
    if is_prime(j, primes):
        primes.append(j)
    j += 2

for i in range(1000000):
    t = triangle(i + 1)
    if divisors(t, primes) > 500:
        print(t)
        break



