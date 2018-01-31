"""         problem 24           """

import itertools


def find_i_permutation(elements, i):
    permutation_list = list(itertools.permutations(elements))
    i_permutation = ""

    for i in permutation_list[i - 1]:
        i_permutation += str(i)

    return i_permutation


print(find_i_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def find_i_permutation_v2(elements, i):
    i_permutation = ""
    n = len(elements)
    cur_sum = 0

    for k in range(1, n):
        cur_factorial = factorial(n - k)

        for e in elements:
            cur_sum += cur_factorial

            if cur_sum >= i:
                cur_sum -= cur_factorial
                i_permutation += str(e)
                elements.remove(e)
                break

    return i_permutation + str(elements[0])


print(find_i_permutation_v2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))
