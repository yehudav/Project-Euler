"""         problem 10           """


import math


def remove_zeros(list):
    new_list = []

    for num in list:
        if num:
            new_list.append(num)

    return new_list


def sieve_of_eratosthenes(bound, return_primes_only):
    numbers = [0, 0]
    max_factor = int(math.sqrt(bound))

    for k in range(2, bound):
        numbers.append(k)

    for i in range(2, max_factor + 1):
        if numbers[i]:
            j = i * i
            while j < bound:
                numbers[j] = 0
                j += i

    if return_primes_only:
        return remove_zeros(numbers)

    return numbers


print(sum(sieve_of_eratosthenes(2000000, False)))









