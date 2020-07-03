def num_of_integrs(bound):
    num = 0
    for i in range(1, bound + 1):
        if not_div(i, 12) and not_div(i, 30) and not_div(i, 56) and not_div(i, 40) and not_div(i, 90) \
                and not_div(i, 132) and not_div(i, 84) and not_div(i, 182) and not_div(i, 144) and not_div(i, 70) \
                and not_div(i, 126) and not_div(i, 154) and not_div(i, 198) and not_div(i, 208) and not_div(i, 176) \
                and not_div(i, 234):
            num += 1
    return num


def not_div(n, d):
    return n / d != n // d


print(num_of_integrs(1500000))
# todo refactor