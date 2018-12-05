def choose(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(choose(40, 20))
