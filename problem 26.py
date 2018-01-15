"""         problem 26           """


# for trail in digits:
#     cur_recurring_num = recurring_cycle(trail)
#
#     if cur_recurring_num > max_recurring_cycle:
#         max_recurring_cycle = cur_recurring_num
#         d_index = digits.index(trail) + 1
#
# print(d_index)


def max_recurring_cycle(string):
    cycles_num = 0

    return cycles_num


def find_longest_recurring_cycle(bound):
    cycles_num_list = []
    for i in range(bound):
        str_of_num = str(1 / i)[2:]
        cycles_num_list.append(max_recurring_cycle(str_of_num))

    return cycles_num_list.index(max(cycles_num_list))


print(find_longest_recurring_cycle(1000))
