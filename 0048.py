def power(x, y):
    if y == 0:
        return 1

    d = power(x, y >> 1)

    if y & 1 == 0:
        return d * d

    else:
        return x * d * d

# todo refactor
power_sum = 0

for i in range(1, 1001):
    power_sum += power(i, i)

digits = str(power_sum)

print(digits[2991:])
