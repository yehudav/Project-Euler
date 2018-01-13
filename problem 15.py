"""     problem 15        """


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def choose(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


print(choose(40, 20))



