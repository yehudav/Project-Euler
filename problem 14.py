"""         problem 14           """


def chain_length(n):
    chain_len = 0
    m = n

    while m > 1:
        if m % 2 != 0:
            m = m + m + m + 1
        else:
            m = m >> 1

        chain_len += 1

    return chain_len


def max_chain_length_head(bound):
    chains = []

    for i in range(bound):
        chains.append(chain_length(i))

    return chains.index(max(chains))


print(max_chain_length_head(1000000))
