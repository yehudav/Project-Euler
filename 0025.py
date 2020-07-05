import euler_utils as eu


def get_index_of_first_fibonacci_term_with_n_digits(n):
    fib_seq = eu.get_fibonacci_sequence_until_value(10 ** (n - 1))
    return len(fib_seq)


if __name__ == "__main__":
    num_of_digits = 1000
    print(get_index_of_first_fibonacci_term_with_n_digits(num_of_digits))
