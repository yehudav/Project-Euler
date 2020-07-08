def get_num_of_lychrel_numbers_below_bound(bound, palindromic_bound):
    return sum(1 for i in range(bound) if is_lychrel_number(i, palindromic_bound))


def is_lychrel_number(i, palindromic_bound):
    for j in range(palindromic_bound):
        i += reverse_num(i)
        if is_palindrom(i):
            return False
    return True


def is_palindrom(i):
    return i == reverse_num(i)


def reverse_num(i):
    return int(str(i)[::-1])


if __name__ == "__main__":
    n = 10000
    k = 50
    print(get_num_of_lychrel_numbers_below_bound(n, k))
