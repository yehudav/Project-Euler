import euler_utils as eu


def get_ith_permutation(elements, i):
    i_perm, n, cur_sum, cur_fact = "", len(elements), 0, eu.factorial(len(elements))
    for k in range(n, 1, -1):
        cur_fact, j = cur_fact // k, 0
        while cur_sum + cur_fact < i:
            cur_sum, j = cur_sum + cur_fact, j + 1
        i_perm += str(elements[j])
        elements = elements[:j] + elements[j + 1:]
    return int(i_perm + str(elements[0]))


if __name__ == "__main__":
    print(get_ith_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))
