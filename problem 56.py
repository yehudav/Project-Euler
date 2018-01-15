"""         problem 56           """


def digits_sum(n):
    n_sum = 0
    while len(n):
        n_sum += int(n[0])
        n = n[1:]
    return n_sum


def power(x, y):
    if y == 0:
        return 1

    d = power(x, y >> 1)

    if y & 1 == 0:
        return d * d

    else:
        return x * d * d


max_sum = 0

for a in range(100):
    for b in range(100):
        cur_pow = power(a, b)
        cur_sum = digits_sum(str(cur_pow))

        if cur_sum > max_sum:
            max_sum = cur_sum

print(max_sum)
