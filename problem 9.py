# def


for a in range(1, 1001):
    for b in range(1, 1001):
        if ((a * b) / 1000) == (a + b - 500):# and a < b:
            print(a, b, 1000 - a - b)
            print(a * b * (1000 - a - b))
            # exit(0)
