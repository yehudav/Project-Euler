import euler_utils as eu


# todo
def get_consecutive_prime_sum_below_bound(n):
    primes_in_order = [i for i in eu.sieve_of_eratosthenes(n) if i != 0]
    return get_longest_consecutive_prime_sum(primes_in_order)


def get_longest_consecutive_prime_sum(primes_in_order):
    primes = set(primes_in_order)
    sums = [(i, 0) for i in primes_in_order]
    for i in range(1, len(sums)):
        sums[i] = sums[i][0] + sums[i - 1][0], sums[i][1] + i
    max_p, max_l = 2, 0
    while True:
        for i in sums:
            if i[0] in primes and i[1] > max_l:
                max_p = i[0]
                max_l = i[1]

    max_prime, max_len = 2, 1
    while primes_in_order is not []:
        max_prime, max_len = get_longest_consecutive_sum_in_sequance(max_prime, max_len, primes_in_order, primes)
        primes_in_order = primes_in_order[1:]
    return max_prime


def get_longest_consecutive_sum_in_sequance(max_prime, max_len, primes_in_order, primes):
    seq_sum = sum(primes_in_order)
    cur = len(primes_in_order) - 1
    cur_len = cur
    while seq_sum not in primes:
        seq_sum -= primes_in_order[cur]
        cur -= 1
        cur_len -= 1
    if cur_len > max_len:
        return seq_sum, cur_len
    return max_prime, max_len


if __name__ == "__main__":
    n = 1000000
    print(get_consecutive_prime_sum_below_bound(n))
