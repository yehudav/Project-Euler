def amicable_numbers_sum(bound):
    amicable_sum = 0
    for cur in range(1, bound):
        if is_amicable(cur):
            amicable_sum += cur
    return amicable_sum


def is_amicable(n):
    div_sum = sum_of_divisors(n)
    n_tag = sum_of_divisors(div_sum)
    return n_tag == n and n_tag != div_sum


def sum_of_divisors(num):
    upper_bound = num // 2 + 1
    divisors_sum = 0
    for i in range(1, upper_bound):
        if evenly_divisible(num, i):
            divisors_sum += i
    return divisors_sum


def evenly_divisible(n, d):
    return n / d == n // d


print(amicable_numbers_sum(10000))
