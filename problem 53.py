"""         problem 52           """


def choose_bigger_than_val(bound, val):
    num = 0
    for n in range(1, bound + 1):
        for i in range(1, n):
            if n_choose_k(n, i) > val:
                num += 1
    return num


def n_choose_k(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(choose_bigger_than_val(100, 1000000))
