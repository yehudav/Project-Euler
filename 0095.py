def longest_chain_min(bound):
    cur_min = 0
    max_length = 0
    for i in range(4, bound):
        chain = get_chain(i)
        if len(chain) > max_length:
            max_length = len(chain)
            cur_min = min(chain)
    return cur_min

# todo refactor
def get_chain(n):
    i = 0
    s = set()
    cur = n
    while len(s) == i:
        s.add(cur)
        cur = div_sum(cur)
        i += 1
    # s.remove(0)
    return s


def div_sum(n):
    sum = 0
    for i in range(1, int(n / 2) + 1):
        if evenly_divisible(n, i):
            sum += i
    return sum


def evenly_divisible(n, i):
    return n / i == n // i


print(longest_chain_min(1000000))

# print(evenly_divisible(8, 2))
# print(div_sum(12))
# print(get_chain(4))