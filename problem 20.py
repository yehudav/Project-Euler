"""         problem 20           """


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def factorial_digits_sum(num):
    factorial_num = str(factorial(num))
    sum_of_digits = 0

    for digit in factorial_num:
        sum_of_digits += int(digit)

    return sum_of_digits


print(factorial_digits_sum(100))
