"""         problem 2           """


def is_even(n):
    return n / 2 == n // 2

def sum_of_even_fibonacci_numbers(bound, fn_minus_2, fn_minus_1):
    sum_of_even_numbers = 0
    while fn_minus_2 < bound:
        fn = fn_minus_1 + fn_minus_2
        fn_minus_2 = fn_minus_1
        fn_minus_1 = fn
        if is_even(fn_minus_2):
            sum_of_even_numbers += fn_minus_2
    return sum_of_even_numbers


print(sum_of_even_fibonacci_numbers(4000000, 0, 1))

