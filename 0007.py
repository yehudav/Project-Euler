import util


def get_nth_prime(n):
    if n < 2:
        raise ValueError
    primes = []
    cur = 2
    while len(primes) < n:
        if is_prime(cur, primes):
            primes.append(cur)
        cur += min(cur - 1, 2)
    return primes[-1]


def is_prime(num, primes):
    for prime in primes:
        if util.is_divisible(num, prime):
            return False
    return True


if __name__ == "__main__":
    n = 10001
    print(get_nth_prime(n))
