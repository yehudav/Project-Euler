# for trail in digits:
#     cur_recurring_num = recurring_cycle(trail)
#
#     if cur_recurring_num > max_recurring_cycle:
#         max_recurring_cycle = cur_recurring_num
#         d_index = digits.index(trail) + 1
#
# print(d_index)# todo refactor


def max_recurring_cycle(string):
    cycles_num = 0

    return cycles_num


def get_unit_fraction_str(n):
    return str(1 / n)[2:]


def find_longest_recurring_cycle(bound):
    cycles_num_list = []
    for i in range(1, bound):
        str_fraction = get_unit_fraction_str(i)
        cycles_num_list.append(max_recurring_cycle(str_fraction))

    return cycles_num_list.index(max(cycles_num_list))


# print(find_longest_recurring_cycle(1000))
print(1 / 7)
