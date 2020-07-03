import euler_utils as eu


def amicable_numbers_sum(bound):  # todo refactor
    dic = {i: sum_of_divisors(i) for i in range(bound)}
    amic = set()
    for i in range(bound):
        if i not in amic:
            if bound > dic[i] != i and dic[dic[i]] == i:
                amic.add(i)
                amic.add(dic[i])
    return sum(amic)


def sum_of_divisors(num):
    return sum(i for i in range(1, num // 2 + 1) if eu.is_divisible(num, i))


if __name__ == "__main__":
    print(amicable_numbers_sum(10000))
    print(amicable_numbers_sum(10000) == 31626)
