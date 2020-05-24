import util


# todo
def get_product_of_pythagorean_triplet_with_given_sum_(given_sum):
    triplet = find_pythagorean_triple_with_given_sum(given_sum)
    return util.get_iter_product(triplet)


def find_pythagorean_triple_with_given_sum(given_sum):
    M = given_sum
    bound = M + 1
    for a in range(1, bound):
        for b in range(1, bound):
            if ((a * b) / M) == (a + b - M / 2):
                return a, b, M - a - b
    exit(-1)


if __name__ == "__main__":
    n = 1000
    print(get_product_of_pythagorean_triplet_with_given_sum_(n))
