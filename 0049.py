import euler_utils as eu


def get_three_primes_with_four_digit_chained_term():
    primes = [get_key(i) for i in eu.sieve_of_eratosthenes(10000) if i > 1000]
    s = set(primes)
    dic = {p: 0 for p in s}
    for p in primes:
        dic[p] += 1
    print(len(dic))
    # for p in dic:
    #     if dic[p] == 3:
    #         print(p)

    #
    # dict = {get_key(p): [] for p in primes}
    # print(dict)
    # for p in primes:
    #     dict[get_key(p)].append(p)
    # res = []
    # for key in dict:
    #     if len(dict[key]) == 3 and "1487" not in dict[key]:
    #         dict[key].sort()
    #         # return int("".join(map(str, dict[key])))
    #         if abs(dict[key][0] - dict[key][1]) == abs(dict[key][1] - dict[key][2]):
    #             res.append(dict[key])
    # print(res)
    # return res


def get_key(p):
    return "".join(sorted(list(str(p))))


if __name__ == "__main__":
    print(get_three_primes_with_four_digit_chained_term())
    print(get_three_primes_with_four_digit_chained_term() == 296962999629)

#
# def permutations_of(num):
#     return list(map("".join, itertools.permutations(num)))
#
#
# aaaa = sorted(list(set(primes_list)))
#
# j = 0
# # todo refactor
#
# for i in range(len(aaaa)):
#     for j in range(i + 1, len(aaaa)):
#         for k in range(j + 1, len(aaaa)):
#             if aaaa[i] - aaaa[j] == aaaa[j] - aaaa[k]:
#
#                 st = str(aaaa[i]) + str(aaaa[j]) + str(aaaa[k])
#                 per = list(map("".join, itertools.permutations(str(aaaa[i]))))
#                 if str(aaaa[k]) in per and str(aaaa[j]) in per and aaaa[i] != 1487:
#                     print(st)
#                     exit(0)
