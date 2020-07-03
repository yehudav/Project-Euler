def remove_common_digit_frac(a, b):
    p = a[0]
    q = a[1]
    r = b[0]
    t = b[1]# todo refactor
    if p == "0":
        p = "1"
    if q == "0":
        q = "1"
    if r == "0":
        r = "1"
    if t == "0":
        t = "1"

    if p == r:
        return int(q) / int(t)
    if p == t:
        return int(q) / int(r)
    if q == r:
        return int(p) / int(t)
    if q == t:
        return int(p) / int(r)


fracs = []

for i in range(10, 100):
    for j in range(10, 100):
        a = str(i)
        b = str(j)
        new_frac = remove_common_digit_frac(a, b)
        if new_frac == i / j and i % 10 != 0 and j % 10 != 0 and i / j < 1:
            print(i, j)
