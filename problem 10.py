

import math

all_numbers = []

primes_to_sqrt = [2]

bound = 2000000


def is_prime(num):
    for p in primes_to_sqrt:
        if num % p == 0:
            return False
    return True


for i in range(bound + 1):
        all_numbers.append(i)

all_numbers[1] = 0

sqrt_bound = int(math.ceil(math.sqrt(bound)))

for i in range(sqrt_bound):
    if is_prime(i + 3):
        primes_to_sqrt.append(i + 3)

for i in primes_to_sqrt:
    index = i + i

    while index <= bound:
        all_numbers[index] = 0
        index += i

primes_sum = 0

for i in all_numbers:
    primes_sum += i

print(primes_sum)



