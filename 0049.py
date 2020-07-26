import euler_utils as e
import itertools


def permutations_of(num):
    return list(map("".join, itertools.permutations(num)))


primes_list = e.sieve_of_eratosthenes(10000)

aaaa = sorted(list(set(primes_list)))

j = 0
# todo refactor
for i in aaaa:
    if i > 1000:
        j = aaaa.index(i)
        break

aaaa = aaaa[j:]

for i in range(len(aaaa)):
    for j in range(i + 1, len(aaaa)):
        for k in range(j + 1, len(aaaa)):
            if aaaa[i] - aaaa[j] == aaaa[j] - aaaa[k]:

                st = str(aaaa[i]) + str(aaaa[j]) + str(aaaa[k])
                per = list(map("".join, itertools.permutations(str(aaaa[i]))))
                if str(aaaa[k]) in per and str(aaaa[j]) in per and aaaa[i] != 1487:
                    print(st)
                    exit(0)
