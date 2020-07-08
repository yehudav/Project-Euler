def sum_of_all_positive_nums_that_are_not_the_sum_of_two_abundant_numbers():
    return sum(i for i in range(1, 28124) if is_not_sum_of_two_abundant(i))


def is_not_sum_of_two_abundant(i):
    abundant_numbers_list = get_abundant_num_list(bound)

    abundant_numbers_sum_list = list(sums_of_abundant_numbers(abundant_numbers_list))

    for num in abundant_numbers_sum_list:
        if num < bound:
            non_abundant_sum -= num

    return non_abundant_sum


def div_sum(number):  # todo refactor
    divs_sum = 0
    bound = number // 2 + 1

    for i in range(1, bound):
        if number % i == 0:
            divs_sum += i

    return divs_sum


def get_abundant_num_list(bound):
    j = 12
    abundant_numbers = []

    while j < bound:
        if div_sum(j) > j:
            abundant_numbers.append(j)

        j += 1
    return abundant_numbers


def sums_of_abundant_numbers(abundant_numbers):
    sums_set = set()
    for num_a in abundant_numbers:
        for num_b in abundant_numbers:
            sums_set.add(num_a + num_b)

    return sums_set


if __name__ == "__main__":
    print(sum_of_all_positive_nums_that_are_not_the_sum_of_two_abundant_numbers())
    print(sum_of_all_positive_nums_that_are_not_the_sum_of_two_abundant_numbers() == 4179871)
