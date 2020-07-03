import fractions


def e_convergent(n):
    e = fractions.Fraction(2 / 1)
    f = n + fractions.Fraction(n, n + 1)
    for i in range(n, 0, -1):
        f = n + fractions.Fraction(n, f)
        e = e + 1 / f
        print(f)
# todo refactor

def digits_sum(n):
    s = str(n)
    v = 0
    for c in s:
        v += int(c)
    return v


e_convergent(10)
