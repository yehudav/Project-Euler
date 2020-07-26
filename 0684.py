def get_sum_of_min_num_where_digits_sum_is_k(n):
    return sum(get_min_num_where_digits_sum_is_n(i) for i in range(1, n + 1))


def get_min_num_where_digits_sum_is_n(n):
    return int(str(n % 9) + "9" * (n // 9))


print(get_sum_of_min_num_where_digits_sum_is_k(20))
