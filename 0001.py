def sum_of_multiples(a, b, bound):
    a_mult_sum = a * arithmetic_series_sum(multiples_num(bound, a))
    b_mult_sum = b * arithmetic_series_sum(multiples_num(bound, b))
    a_times_b_mult_sum = a * b * arithmetic_series_sum(multiples_num(bound, a * b))
    return inclusion_exclusion(a_mult_sum, b_mult_sum, a_times_b_mult_sum)


def arithmetic_series_sum(n):
    return (n * (n + 1)) // 2


def multiples_num(M, n):
    return M // n


def inclusion_exclusion(a, b, a_b_intersection):
    return a + b - a_b_intersection


print(sum_of_multiples(3, 5, 999))
