def get_max_palindrome_product(lower_bound, higher_bound):
    max_palindrome = -1
    for i in range(higher_bound, lower_bound - 1, -1):
        cur_max_palindrome = get_i_mults_max_palindrome_product(i, lower_bound * i)
        max_palindrome = max(max_palindrome, cur_max_palindrome)
    return max_palindrome


def get_i_mults_max_palindrome_product(cur, lower_multiple):
    higher_multiple = cur ** 2
    while higher_multiple >= lower_multiple:
        if is_palindrome(higher_multiple):
            return higher_multiple
        higher_multiple -= cur
    return 0


def is_palindrome(n):
    left_to_right = str(n)
    right_to_left = left_to_right[::-1]
    return left_to_right == right_to_left


print(get_max_palindrome_product(100, 999))
