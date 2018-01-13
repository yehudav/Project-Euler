"""     problem 1        """


def arithmetic_series_sum(n):
    return (n * (n + 1)) / 2


def sum_of_multiples(a, b, bound):
    a_multiples = int(bound / a)
    b_multiples = int(bound / b)
    a_times_b_multiples = int(bound / (a * b))

    a_multiples_sum = a * arithmetic_series_sum(a_multiples)
    b_multiples_sum = b * arithmetic_series_sum(b_multiples)
    a_times_b_multiples_sum = a * b * arithmetic_series_sum(a_times_b_multiples)

    return int(a_multiples_sum + b_multiples_sum - a_times_b_multiples_sum)


print(sum_of_multiples(3, 5, 999))
