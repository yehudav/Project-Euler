

import math


def div(num):
    bound = int(math.floor(num / 2))
    divisor_sum = 0

    for i in range(bound):
        if num % (i + 1) == 0:
            divisor_sum += i + 1

    return divisor_sum


amicable_sum = 0

for j in range(10000):
    b = div(j + 1)
    a = div(b)

    if a == (j + 1) and a != b:
        amicable_sum += j + 1

print(amicable_sum)



