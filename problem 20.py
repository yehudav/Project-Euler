def factorial_digits_sum(num):
    factorial_result = str(factorial(num))
    return sum_of_digits(factorial_result)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def sum_of_digits(n):
    digits_sum = 0
    for digit in n:
        digits_sum += int(digit)
    return digits_sum


print(factorial_digits_sum(100))
