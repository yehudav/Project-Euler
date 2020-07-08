import euler_utils as eu


def get_num_of_circular_primes_below_bound(n):
    primes = eu.sieve_of_eratosthenes(n)
    primes_set = {str(i) for i in primes if i != 0}
    return sum(1 for i in primes_set if is_circular_prime(i, primes_set))


def is_circular_prime(num, primes):
    if int(num) < 10:
        return True
    for digit in num:
        if int(digit) % 2 == 0:
            return False

    for i in range(len(num)):
        n = num[1:] + num[0]
        if n not in primes:
            return False  # todo refactor
    return True


if __name__ == "__main__":
    n = 1000000
    print(get_num_of_circular_primes_below_bound(n))
    print(get_num_of_circular_primes_below_bound(n) == 55)
