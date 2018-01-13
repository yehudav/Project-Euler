"""     problem 5        """


def min_product(bound):
    product = 1
    upper_bound = bound + 1
    factors = []

    for j in range(2, upper_bound):
        for i in factors:
            if j % i == 0:
                j /= i

        factors.append(j)
        product *= j

    return int(product)


print(min_product(20))






