"""         problem 34           """


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def sum_of_factorial(n):
    factorial_sum = 0
    num = n

    while num > 0:
        factorial_sum += factorial(num % 10)
        num = int(num / 10)

    return factorial_sum


numbers = []

for i in range(100000):
    if i == sum_of_factorial(i):
        numbers.append(i)

factorial_sum = 0

for i in numbers:
    factorial_sum += i

print(factorial_sum - 3)
