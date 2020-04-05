import math


def sum_of_primes_below_bound(bound):
    primes = sieve_of_eratosthenes(bound)
    return sum(primes)


def sieve_of_eratosthenes(bound):
    sieve = create_sieve(bound)
    sieved_primes = remove_non_primes(sieve)
    return sieved_primes


def create_sieve(bound):
    numbers = [0, 0]
    upper_bound = bound + 1
    for num in range(2, upper_bound):
        numbers.append(num)
    return numbers


def remove_non_primes(sieve):
    bound = len(sieve)
    max_factor = int(math.sqrt(bound)) + 1
    for i in range(2, max_factor):
        if sieve[i] != 0:
            for j in range(i * i, bound, i):
                sieve[j] = 0
    return sieve


print(sum_of_primes_below_bound(2000000))
