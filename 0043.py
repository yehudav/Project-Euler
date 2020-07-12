# import itertools
#
# a = list(map("".join, itertools.permutations("0123456789")))
#
# sum = 0
# for p in a:
#     a = int(p[1:4]) / 2
#     b = int(p[2:5]) / 3
#     c = int(p[3:6]) / 5
#     d = int(p[4:7]) / 7
#     e = int(p[5:8]) / 11
#     f = int(p[6:9]) / 13
#     g = int(p[7:10]) / 17
#
#     if int(a) == a and int(b) == b and int(c) == c and int(d) == d and int(e) == e and int(f) == f and int(g) == g:
#         sum += int(p)
# # todo refactor
# print(sum)
#
# a = {s for s in range(2, 1000, 2)}
# b = {s for s in range(3, 1000, 3)}
# c = {s for s in range(5, 1000, 5)}
# d = {s for s in range(7, 1000, 7)}
# e = {s for s in range(11, 1000, 11)}
# f = {s for s in range(13, 1000, 13)}
# g = {s for s in range(17, 1000, 17)}
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)


"""
constraints - using rules of divisibility

* d2d3d4 is divisible by 2 -> d4 = {0,2,4,6,8}

* d3d4d5 is divisible by 3 -> d3 + d4 + d5 = n,  n % 3 == 0

* d4d5d6 is divisible by 5 -> d6 = {0, 5}

* d5d6d7 is divisible by 7 -> d5d6 - 2 * d7 = n, n % 7 == 0

* d6d7d8 is divisible by 11 -> d6 - d7 + d8 = n, n % 11 == 0

* d7d8d9 is divisible by 13 ->

* d8d9d10 is divisible by 17 -> d8d9 - 5 * d10 = n, n % 17
"""


def get_sum_of_0_to_9_pandigital_with_sub_string_divisibility():
    aa = [str(i) for i in range(12, 1000, 2) if len(str(i)) == len(set(str(i)))]
    bb = [str(i) for i in range(12, 1000, 3) if len(str(i)) == len(set(str(i)))]
    cc = [str(i) for i in range(15, 1000, 5) if len(str(i)) == len(set(str(i)))]
    dd = [str(i) for i in range(14, 1000, 7) if len(str(i)) == len(set(str(i)))]
    ee = [str(i) for i in range(11, 1000, 11) if len(str(i)) == len(set(str(i)))]
    ff = [str(i) for i in range(13, 1000, 13) if len(str(i)) == len(set(str(i)))]
    gg = [str(i) for i in range(17, 1000, 17) if len(str(i)) == len(set(str(i)))]

    a = [i + j[-1] for i in aa for j in bb if i[-2:] == j[:-1]]

    print(a)
    print(len(a))
    # print(b)
    # print(c)
    # print(d)
    # print(e)
    # print(f)
    # print(g)
    # print(len(a) + len(b) + len(c) + len(d) + len(e) + len(f) + len(g))


if __name__ == "__main__":
    print(get_sum_of_0_to_9_pandigital_with_sub_string_divisibility())
