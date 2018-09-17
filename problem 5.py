def min_product(bound):
    product = 1
    upper_bound = bound + 1
    factors = []
    for j in range(2, upper_bound):
        cur_min_factor = get_min_factor(j, factors)
        factors.append(cur_min_factor)
        product *= cur_min_factor
    return product


def get_min_factor(n, factors):
    for i in factors:
        if n % i == 0:
            n //= i
    return n


print(min_product(20))
