"""         problem 4           """


def find_max_palindrome_product(lower_bound, higher_bound):
    max_palindrome = 0
    cur = higher_bound
    while cur >= lower_bound:
        cur_palindrome = cur_multiples_max_palindrome(cur, cur ** 2, cur * lower_bound)
        max_palindrome = max(max_palindrome, cur_palindrome)
        cur -= 1
    return max_palindrome


def cur_multiples_max_palindrome(number, highest_multiple, lowest_multiple):
    current_multiple = highest_multiple
    while current_multiple >= lowest_multiple:
        if is_palindrome(current_multiple):
            return current_multiple
        current_multiple -= number
    return 0


def is_palindrome(n):
    left_to_right = str(n)
    right_to_left = left_to_right[::-1]
    return left_to_right == right_to_left


print(find_max_palindrome_product(100, 999))
