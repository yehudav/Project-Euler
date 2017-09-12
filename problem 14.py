

chains = []


def chain(n):
    chain_num = 0
    m = n

    while m > 1:
        if m % 2:
            m = 3 * m + 1
        else:
            m /= 2

        chain_num += 1
    return chain_num


for i in range(1000000):
    chains.append(chain(i))

highest = max(chains)

print(chains.index(highest))



