import euler_utils as eu


def get_sum_of_min_num_where_digits_sum_is_k(iter):
    a = 0
    for i in iter:
        a += get_min_num_where_digits_sum_is_n(i)
    return a


def get_min_num_where_digits_sum_is_n(n):
    return int(str(n % 9) + "9" * (n // 9))


if __name__ == "__main__":
    summ = 0
    fib = eu.get_fibonacci_sequence_until_value(2880067194370816121)
    print(fib)

    sums = [get_min_num_where_digits_sum_is_n(i) for i in fib]
    print(sums)
    # for i in range(1, len(sums)):
    #     sums[i] += sums[i - 1]
    #     sums[i] = sums[i] % 1000000007
    # print(sum(sums))

# todo refactor
