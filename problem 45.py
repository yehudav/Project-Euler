triangle = []
pentagonal = []
hexagonal = []

for i in range(80000 - 143):
    n = i + 144

    hexagonal.append(int((n * (2 * n - 1))))

for i in range(80000 - 165):
    n = i + 166
    num = int((n * (3 * n - 1)) / 2)

    if num in hexagonal:
        pentagonal.append(num)

for i in range(80000 - 285):
    n = i + 286
    num = int((n * (n + 1)) / 2)

    if num in pentagonal:
        triangle.append(num)

print(triangle)
