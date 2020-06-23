import util


def get_sum_of_primes_below_bound(bound):
    return sum(util.sieve_of_eratosthenes(bound))


if __name__ == "__main__":
    bound = 2000000
    print(get_sum_of_primes_below_bound(bound))
