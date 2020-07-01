import math
import euler_utils as eu

#todo
def first_triangle_num_with_n_divisors(n, primes_bound):
    primes = get_primes(primes_bound)
    first_triangle = 0
    i = 1

    while first_triangle == 0:
        current_triangle = eu.get_nth_triangle_num(i)
        if get_num_of_divisors(current_triangle, primes) > n:
            first_triangle = current_triangle

        i += 1

    return first_triangle


def get_primes(primes_bound):
    primes = [2]
    current_prime = 3
    bound = int(math.sqrt(primes_bound))

    while current_prime < bound:
        if is_prime(current_prime, primes):
            primes.append(current_prime)

        current_prime += 2

    return primes


def is_prime(num, primes):
    for p in primes:
        if num % p == 0:
            return False
    return True


def get_num_of_divisors(n, primes):
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


if __name__ == "__main__":
    print(first_triangle_num_with_n_divisors(500, 500))
    print(first_triangle_num_with_n_divisors(500, 500) == 76576500)
