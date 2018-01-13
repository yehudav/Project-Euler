"""     problem 21        """


import math

def is_pentagonal(x):
    n = (math.sqrt(24 * x + 1) + 1 ) / 6
    return n == int(n)


pentagonals = []
D = 5000
add = 1
cur = 1

for i in range(10000):
    pentagonals.append(cur)
    add += 3
    cur += add

for pj in pentagonals:
    for pk in pentagonals:
        if pj == pk:
            continue
        diff = abs(pj - pk)
        sum = pk + pj

        if is_pentagonal(sum) and is_pentagonal(diff) and diff < D:
            D = diff

print(D)