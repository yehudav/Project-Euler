import euler_utils as eu  # todo refactor

a = set("123456789")


def get_index_of_first_9_pandigital_edges_fibonacci_term():
    fib_gen = eu.generate_fibonacci_sequence_and_index()
    while True:
        fib_k, k = fib_gen.__next__()
        if is_9_pandigital(str(fib_k)[-9:]) and is_9_pandigital(str(fib_k)[:9]):
            return k + 2  # k + 2 due to convention of f_1 = 0, f_2 = 1


def is_9_pandigital_at_edges(n):
    digits = str(n)
    if len(digits) < 18:
        return False
    return is_9_pandigital(digits[:9]) and is_9_pandigital(digits[-9:])


def is_9_pandigital(digits):

    return set(digits) == a


if __name__ == "__main__":
    print(get_index_of_first_9_pandigital_edges_fibonacci_term())
    # print(get_index_of_first_9_pandigital_edges_fibonacci_term() ==)
