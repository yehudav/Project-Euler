import math


# todo refactor


def x(bound):
    primes = remove_zeros(sieve_of_eranthoses(10000000))
    lis = [1]
    for i in range(10000001, bound, 2):
        flag = True
        bb = math.sqrt(i)
        for j in lis:
            if j > bb:
                break
            if i / j != i // j:
                flag = False
                break
        if flag:
            lis.append(i)
    print(len(lis))

    print(len(primes))


x(1000000000)
