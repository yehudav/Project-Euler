import euler_utils as eu


def get_sum_of_truncatable_primes_below_bound(n):
    primes = {str(i) for i in eu.sieve_of_eratosthenes(n) if i != 0}
    return sum(int(p) for p in primes if is_truncatable_prime(p, primes) and int(p) >= 23)


def is_truncatable_prime(p, primes):
    left, right = p, p
    while left != "":
        if right not in primes or left not in primes:
            return False
        left, right = left[1:], right[:-1]
    return True


if __name__ == "__main__":
    n = 1000000
    print(get_sum_of_truncatable_primes_below_bound(n))
