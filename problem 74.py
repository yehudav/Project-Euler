def chain_num(bound):
    num = 0
    for n in range(2, bound):
        num += is_chain_60(n)
    return num


def is_chain_60(n):
    s = set()
    for i in range(1, 61):
        s.add(n)
        n = get_next(n)
        if len(s) != i:
            return 0
    return 1


def get_next(n):
    s = str(n)
    num = 0
    for c in s:
        num += factorial(int(c))
    return num


def factorial(n):
    num = 1
    for i in range(2, n + 1):
        num *= i
    return num


print(chain_num(1000000))
