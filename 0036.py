import euler_utils as eu


def get_sum_of_decimal_and_binary_palindromes_below_bound(bound):
    return sum(i for i in range(bound) if is_palindrom(i) and is_palindrom(bin(i)[2:]))


def is_palindrom(num):
    return eu.is_string_palindrome(str(num))


if __name__ == "__main__":
    n = 1000000
    print(get_sum_of_decimal_and_binary_palindromes_below_bound(n))
