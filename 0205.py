import itertools


def X_greater_than_Y(i_sided, i_dice_num, j_sided, j_dice_num):
    X = calculate_random_variable(i_sided, i_dice_num)
    Y = calculate_random_variable(j_sided, j_dice_num)
    greater_prob = calculate_greater(X, Y)
    return greater_prob


def calculate_random_variable(values_num, power):
    var = []
# todo refactor

def calculate_greater():
    return


# print(X_greater_than_Y(4, 9, 6, 6))

a = list(itertools.combinations([1, 2, 3, 4], 9))
for i in range(10):
    print(a)
