def get_champernowne_constant_n_digits_product(indices):
    champernowne_constant = create_n_digits_champernowne_constant(max(indices))
    product = 1
    for i in indices:
        product *= int(champernowne_constant[i])
    return product


def create_n_digits_champernowne_constant(n):
    num = ["."]
    cur_len = 0
    cur_num = 1
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
