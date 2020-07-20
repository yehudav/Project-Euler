import euler_utils as eu
import math

"""
upper bound:
a**2 + b**3 + c**4 <= n -> a < sqrt(n)
"""


def num_of_sum_of_primes_square_cube_and_fourth_power_below_bound(n):
    primes = eu.sieve_of_eratosthenes(math.ceil(math.sqrt(n)))
    return get_number_of_sums_below_bound(n, [i for i in primes if i != 0])


def get_number_of_sums_below_bound(n, primes):
    squares, cubes = [i ** 2 for i in primes], [i ** 3 for i in primes]
    fourth_power, sums = [i ** 2 for i in squares], set()
    for i in squares:
        for j in cubes:
            for k in fourth_power:
                if i + j + k < n:
                    sums.add(i + j + k)
                else:
                    break
    return len(sums)


if __name__ == "__main__":
    n = 50000000
    print(num_of_sum_of_primes_square_cube_and_fourth_power_below_bound(n))
