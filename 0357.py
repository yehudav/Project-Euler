import euler_utils as eu
import math

"""
define n to be a prime_generating_integer if for every divisor d of n:
d + n/d is prime

for every odd number o > 1, we get that 1 + o/1 = o + 1 = even -> not a prime
for every even number e = 4k we get that 2 + 4k/2 is even
so we only need to check every even number e = 4k - 2 -> 2 + (4k - 2)/2 = 2k + 1 
 
"""


def get_sum_of_prime_generating_integers_below_n(n):
    primes = set(eu.sieve_of_eratosthenes(n))
    return sum(i for i in range(2, 100000001, 4) if is_prime_generating(i, primes)) + 1


def is_prime_generating(n, p):
    for d in range(1, math.ceil(math.sqrt(n))):
        d_tag = n // d
        if n % d == 0 and (d + d_tag not in p or d_tag + n // d_tag not in p):
            return False
    return True


if __name__ == "__main__":
    n = 100000000
    print(get_sum_of_prime_generating_integers_below_n(n))
