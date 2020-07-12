import euler_utils as eu  # todo refactor


def get_index_of_first_9_pandigital_edges_fibonacci_term():
    fib_gen = eu.generate_fibonacci_sequence_and_index()
    while True:
        fib_k, k = fib_gen.__next__()
        if is_9_pandigital_at_edges(fib_k):
            return k + 2  # k + 2 due to my convention of f_1 = 0, f_2 = 1


def is_9_pandigital_at_edges(n):
    digits = str(n)
    if len(digits) < 18:
        return False
    return is_9_pandigital(digits[:9]) and is_9_pandigital(digits[-9:])


def is_9_pandigital(digits):
    for i in range(1, 10):
        if str(i) not in set(str(digits)):
            return False
    return True


if __name__ == "__main__":
    print(get_index_of_first_9_pandigital_edges_fibonacci_term())
    # print(get_index_of_first_9_pandigital_edges_fibonacci_term() ==)
