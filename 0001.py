import euler_utils as eu


def sum_of_multiples_of_two_nums_below_bound(a, b, bound):
    a_sum, b_sum = sum_of_multiples_below_bound(a, bound), sum_of_multiples_below_bound(b, bound)
    a_times_b_sum = sum_of_multiples_below_bound(a * b, bound)
    return inclusion_exclusion(a_sum, b_sum, a_times_b_sum)


def sum_of_multiples_below_bound(n, bound):
    return n * eu.get_arithmetic_series_sum(number_of_multiples_below_bound(n, bound))


def number_of_multiples_below_bound(num, bound):
    return bound // num


def inclusion_exclusion(a, b, a_b_intersection):
    return a + b - a_b_intersection


if __name__ == "__main__":
    a, b, bound = [3, 5, 999]
    print(sum_of_multiples_of_two_nums_below_bound(a, b, bound))
