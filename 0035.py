import euler_utils as eu


def get_num_of_circular_primes_below_bound(n):
    primes = {str(i) for i in eu.sieve_of_eratosthenes(n) if i != 0}
    return sum(1 for i in primes if is_circular_prime(i, primes))


def is_circular_prime(num, primes):
    if len(set(num) & set("02468")) != 0 and num != "2":
        return False
    circular_permutations = [num[i:] + num[:i] for i in range(len(num))]
    return len(num) == sum(1 for i in circular_permutations if i in primes)


if __name__ == "__main__":
    n = 1000000
    print(get_num_of_circular_primes_below_bound(n))
