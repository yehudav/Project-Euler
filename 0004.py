import util


def get_max_palindrome_product(num_of_digits):
    max_palindrome = -1
    lower_bound, upper_bound = get_min_and_max_nums_with_n_digits(num_of_digits)
    for i in range(upper_bound, lower_bound - 1, -1):
        cur = get_max_palindrome_product_of_i_in_range(i, lower_bound * i, i ** 2)
        max_palindrome = max(max_palindrome, cur)
    return max_palindrome


def get_min_and_max_nums_with_n_digits(n):
    return 10 ** (n - 1), 10 ** n - 1


def get_max_palindrome_product_of_i_in_range(i, lower_multiple, upper_multiple):
    while upper_multiple >= lower_multiple:
        if util.is_string_palindrome(str(upper_multiple)):
            return upper_multiple
        upper_multiple -= i
    return -1


if __name__ == "__main__":
    n = 3
    print(get_max_palindrome_product(n))
