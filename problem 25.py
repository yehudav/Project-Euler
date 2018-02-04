"""         problem 25           """


def n_digits_fibonacci(n):
    fn_minus_2 = 1
    fn_minus_1 = 1
    counter = 2

    while len(str(fn_minus_1)) < n:
        fn_minus_1 += fn_minus_2
        fn_minus_2 = fn_minus_1 - fn_minus_2
        counter += 1

    return counter


print(n_digits_fibonacci(1000))
