def get_longest_chain_head_under_bound(bound):
    lengths_by_indexes = get_chains_lengths(bound)
    return get_longest_chain_head(lengths_by_indexes)


def get_chains_lengths(bound):
    upper_bound = bound + 1
    chains_lengths = []
    for i in range(upper_bound):
        chains_lengths.append(chain_length(i))
    return chains_lengths


def chain_length(head):
    chain_len = 0
    cur_num = head
    while cur_num > 1:
        cur_num = get_next_num_in_chain(cur_num)
        chain_len += 1
    return chain_len


def get_next_num_in_chain(n):
    if n != ((n >> 1) << 1):
        return n + n + n + 1
    else:
        return n >> 1


def get_longest_chain_head(chains_lengths):
    return chains_lengths.index(max(chains_lengths))


print(get_longest_chain_head_under_bound(1000000))
