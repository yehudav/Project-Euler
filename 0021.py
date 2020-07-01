def amicable_numbers_sum(bound):
    dic = {i: sum_of_divisors(i) for i in range(bound)}
    amic = set()
    for i in range(bound):
        if i not in amic:
            if bound > dic[i] != i and dic[dic[i]] == i:
                amic.add(i)
                amic.add(dic[i])
    return sum(amic)


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
