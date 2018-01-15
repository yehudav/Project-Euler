"""         problem 2           """


def sum_of_even_fibonacci_numbers(bound):
    sum_of_even_numbers = 0
    fn_minus_2 = 0
    fn_minus_1 = 1

    while fn_minus_2 < bound:
        fn = fn_minus_1 + fn_minus_2
        fn_minus_2 = fn_minus_1
        fn_minus_1 = fn

        if fn_minus_2 % 2 == 0:
            sum_of_even_numbers += fn_minus_2

    return sum_of_even_numbers


print(sum_of_even_fibonacci_numbers(4000000))


