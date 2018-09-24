import math


def sum_of_primes(bound):
    primes_sieve = sieve_of_eratosthenes(bound)
    return sum(primes_sieve)


def sieve_of_eratosthenes(bound):
    numbers = set_sieve(bound)
    primes = remove_non_primes(numbers)
    return primes


def set_sieve(bound):
    sieve = [0, 0]
    for i in range(2, bound):
        sieve.append(1)
    return sieve


def remove_non_primes(sieve):
    bound = len(sieve)
    multiples_bound = int(math.sqrt(bound)) + 1
    for i in range(2, multiples_bound):
        if sieve[i] != 0:
            prime_multiply = i * i
            while prime_multiply < bound:
                sieve[prime_multiply] = 0
                prime_multiply += i
    return sieve


print(sum_of_primes(2000000))
