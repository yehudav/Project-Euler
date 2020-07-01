import euler_utils as eu
import math


def get_product_of_pythagorean_triplet_with_given_sum(given_sum):
    triplet = find_pythagorean_triple_with_given_sum(given_sum)
    return eu.get_iterable_product(triplet)


def find_pythagorean_triple_with_given_sum(given_sum):
    """
    https://en.wikipedia.org/wiki/Pythagorean_triple :
    a = m^2 - n^2, b = 2mn, c = m^2 + n^2,
    a + b + c = 2m^2 + 2mn = 1000, m^2 + mn < x^2 = 500
    """
    half_of_given_sum = given_sum / 2
    bound = round(math.sqrt(half_of_given_sum)) + 1
    for m in range(1, bound):
        for n in range(1, bound):
            if m ** 2 + m * n == half_of_given_sum:
                return m * n * 2, abs(n ** 2 - m ** 2), n ** 2 + m ** 2
    raise ValueError


if __name__ == "__main__":
    n = 1000
    print(get_product_of_pythagorean_triplet_with_given_sum(n))
