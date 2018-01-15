"""         problem 52           """


def contains_the_same_digits(n):
    digits = []

    for char in str(n):
        digits.append(char)

    x2 = str(n + n)
    x3 = str(n + n + n)
    x4 = str(n + n + n + n)
    x5 = str(n + n + n + n + n)
    x6 = str(n + n + n + n + n + n)

    for char in x2:
        if char not in digits:
            return False
    for char in x3:
        if char not in digits:
            return False
    for char in x4:
        if char not in digits:
            return False
    for char in x5:
        if char not in digits:
            return False
    for char in x6:
        if char not in digits:
            return False
    return True


j = 1
num = 0

while True:
    if contains_the_same_digits(j):
        num = j
        break
    j += 1

print(num)
