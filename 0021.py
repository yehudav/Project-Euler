import math
import euler_utils as eu


def get_sum_of_all_amicable_nums_below_bound(bound):
    dic = {i: get_sum_of_divisors(i) for i in range(bound)}
    return sum(i for i in range(bound) if bound > dic[i] != i and dic[dic[i]] == i)


def get_sum_of_divisors(num):
    num_sqrt = math.ceil(math.sqrt(num)) + 1
    div_sum = sum(i + num // i for i in range(1, num_sqrt) if eu.is_divisible(num, i))
    return div_sum - num


if __name__ == "__main__":
    n = 10000
    print(get_sum_of_all_amicable_nums_below_bound(n))
