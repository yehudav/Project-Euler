"""         problem 12           """



import math


def is_prime(num, primes):
    for p in primes:
        if num % p == 0:
            return False
    return True


def get_primes(primes_bound):
    primes = [2]
    current_prime = 3
    bound = int(math.sqrt(primes_bound))

    while current_prime < bound:
        if is_prime(current_prime, primes):
            primes.append(current_prime)

        current_prime += 2

    return primes


def triangle_num(n):
    return int((n * (n + 1)) / 2)


def divisors_number(n, primes):
    divs = 1
    cur = n

    for p in primes:
        if p > n:
            break

        if cur % p != 0:
            continue
        else:
            power = 1
            cur /= p

        while cur % p == 0:
            power += 1
            cur /= p

        divs *= (power + 1)

    return divs


def first_triangle_num_with_n_divisors(n, primes_bound):
    primes = get_primes(primes_bound)
    first_triangle = 0
    i = 1

    while first_triangle == 0:
        current_triangle = triangle_num(i)
        if divisors_number(current_triangle, primes) > n:
            first_triangle = current_triangle

        i += 1

    return first_triangle


print(first_triangle_num_with_n_divisors(500, 100000))
