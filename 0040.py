import euler_utils as eu


def get_champernowne_constant_n_digits_product(indices):
    champernowne_constant = create_n_digits_champernowne_constant(max(indices))
    return eu.get_iterable_product([int(champernowne_constant[i]) for i in indices])


def create_n_digits_champernowne_constant(n):
    num = ["."]
    cur_len, cur_num = 0, 1
    while cur_len < n:
        num.append(str(cur_num))
        cur_len += len(str(cur_num))
        cur_num += 1
    return "".join(num)


if __name__ == "__main__":
    indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    print(get_champernowne_constant_n_digits_product(indices))
    print(get_champernowne_constant_n_digits_product(indices) == 210)
# todo refactor
