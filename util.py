import math


def is_odd_num(n):
    return n & 1 == 1


def is_even_num(n):
    return n & 1 == 0


def is_divisible(n, d):
    return n % d == 0


def n_choose_k(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def factorial(n):
    if n < 0:
        raise ValueError
    mult = 1
    for i in range(2, n + 1):
        mult *= i
    return mult


def get_arithmetic_series_sum(n):
    return n * (n + 1) // 2


def sum_of_squares_up_to_n(n):
    return (n * (n + 1)) * (2 * n + 1) // 6


def square_of_sum_up_to_n(n):
    return get_arithmetic_series_sum(n) ** 2


def is_string_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True


def get_fibonacci_sequence_until_value(n):
    if n < 0:
        raise ValueError
    fibonacci_sequence = []
    f0, f1 = 0, 1
    while f0 <= n:
        fibonacci_sequence.append(f0)
        f1, f0 = f1 + f0, f1
    return fibonacci_sequence


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return abs(a * b) / gcd(a, b)


def get_num_of_digits(n):
    return len(str(n))


def get_iterable_sum(iterable):
    sum = 0
    for i in iterable:
        sum += int(i)
    return sum


def get_iterable_product(iterable):
    product = 1
    for i in iterable:
        product *= int(i)
    return product


def sieve_of_eratosthenes(n):
    if n < 2:
        raise ValueError
    sieve = create_sieve(n)
    return remove_non_primes(sieve)


def create_sieve(bound):
    numbers = [0, 0]
    upper_bound = bound + 1
    for num in range(2, upper_bound):
        numbers.append(num)
    return numbers


def remove_non_primes(sieve):
    bound = len(sieve)
    max_possible_factor = int(math.sqrt(bound)) + 1
    for i in range(2, max_possible_factor):
        if sieve[i] != 0:
            for j in range(i * i, bound, i):
                sieve[j] = 0
    return sieve


def get_nth_triangle_num(n):
    return get_arithmetic_series_sum(n)
