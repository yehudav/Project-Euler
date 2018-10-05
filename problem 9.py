def find_pythagorean_triple_with_given_sum_product(given_sum):
    triplet = find_pythagorean_triple_with_given_sum(given_sum)
    return triplet_product(triplet)


def find_pythagorean_triple_with_given_sum(given_sum):
    M = given_sum
    bound = M + 1
    for a in range(1, bound):
        for b in range(1, bound):
            if ((a * b) / M) == (a + b - M / 2):
                return a, b, M - a - b
    exit(-1)


def triplet_product(triplet):
    product = 1
    for i in triplet:
        product *= i
    return product


print(find_pythagorean_triple_with_given_sum_product(1000))
