def sum_of_divisors(num):
    bound = num // 2 + 1
    divisors_sum = 0

    for i in range(1, bound):
        if num % i == 0:
            divisors_sum += i

    return divisors_sum


def amicable_numbers_sum(bound):
    amicable_sum = 0

    for cur in range(1, bound):
        cur_div_sum = sum_of_divisors(cur)
        cur_tag = sum_of_divisors(cur_div_sum)

        if cur_tag == cur and cur_tag != cur_div_sum:
            amicable_sum += cur

    return amicable_sum


print(amicable_numbers_sum(10000))
