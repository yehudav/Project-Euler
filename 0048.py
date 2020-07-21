def last_n_digits_of_i_pow_i_sequence(bound, n):
    return str(sum(i ** i for i in range(1, bound + 1)))[-n:]


if __name__ == "__main__":
    bound = 1000
    last_n_digits = 10
    print(last_n_digits_of_i_pow_i_sequence(bound, last_n_digits))
