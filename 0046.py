import euler_utils as eu
import math


def get_smallest_odd_composite_that_is_not_the_sum_of_prime_and_twice_a_square(bound):
    primes = [i for i in eu.sieve_of_eratosthenes(bound) if i != 0]
    double_squares = [2 * i ** 2 for i in range(math.ceil(math.sqrt(bound / 2)))]
    odd_composites = {i + j for i in primes for j in double_squares}
    return min(i for i in range(3, bound, 2) if i not in odd_composites)


if __name__ == "__main__":
    bound = 10000
    print(get_smallest_odd_composite_that_is_not_the_sum_of_prime_and_twice_a_square(bound))
