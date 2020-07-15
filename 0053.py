import euler_utils as eu


def choose_bigger_than_val(bound, val):
    ns = range(1, bound + 1)
    return sum(1 for n in ns for k in range(1, n) if eu.n_choose_k(n, k) > val)


if __name__ == "__main__":
    print(choose_bigger_than_val(100, 1000000))
