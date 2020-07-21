import math
import euler_utils as eu


def get_sum_of_distinct_squarefree_nums_in_first_n_rows_of_pascal_triangle(n):
    values = set(i for row in get_first_n_rows_of_pascal_triangle(n) for i in row)
    bound = math.ceil(math.sqrt(max(values)))
    primes_squares = set(i ** 2 for i in eu.sieve_of_eratosthenes(bound) if i != 0)
    return sum(i for i in values if is_squarefree(i, primes_squares))


def get_first_n_rows_of_pascal_triangle(n):
    rows = [[1]]
    row = [1]
    for x in range(1, n):
        row = [l + r for l, r in zip(row + [0], [0] + row)]
        rows.append(row)
    return rows


def is_squarefree(i, primes_squares):
    for p in primes_squares:
        if i % p == 0:
            return False
    return True


if __name__ == "__main__":
    rows_num = 51
    print(get_sum_of_distinct_squarefree_nums_in_first_n_rows_of_pascal_triangle(rows_num))
