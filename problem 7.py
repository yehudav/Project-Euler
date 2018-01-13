"""     problem 7        """


def is_prime(num, primes_list):
    for prime in primes_list:
        if num % prime == 0:
            return False
    return True


def find_prime(index):
    primes = [2]
    cur = 3

    while len(primes) < index:
        if is_prime(cur, primes):
            primes.append(cur)

        cur += 2

    return primes[-1]


print(find_prime(10001))
