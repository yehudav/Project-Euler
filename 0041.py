"""
Divisibility rule: a number is divisible by 3 if the sum of it's digits is divisible by 3.
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
upper bound - 7654321 - pandigital primes with 7 digits
"""
import euler_utils as eu


def get_max_n_digit_pandigital_prime():
    return max(i for i in eu.sieve_of_eratosthenes(7654322) if i != 0 and is_pandigital(i))


def is_pandigital(num):
    for i in range(1, len(str(num)) + 1):
        if str(i) not in str(num):
            return False
    return True


if __name__ == "__main__":
    print(get_max_n_digit_pandigital_prime())
    print(get_max_n_digit_pandigital_prime() == 7652413)
