def find_prime(index):
    primes = [2]
    cur = 3
    while len(primes) < index:
        if is_prime(cur, primes):
            primes.append(cur)
        cur += 2
    return primes[-1]


def is_prime(num, primes):
    for prime in primes:
        if num % prime == 0:
            return False
    return True


print(find_prime(10001))
