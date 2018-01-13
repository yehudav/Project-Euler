def is_palindrome(n):
    num = str(n)
    num_length = len(num)
    mid = int(num_length / 2)

    first_half = num[:mid]
    second_half = num[mid:]
    second_half = second_half[::-1]

    if mid != num_length / 2:
        second_half = second_half[:-1]

    return first_half == second_half


def find_max_palindrome_product(lower_bound, higher_bound):
    palindromes = []

    current_number = higher_bound

    while current_number >= lower_bound:
        current_product = current_number * current_number
        smallest_current_product = current_number * lower_bound

        while current_product >= smallest_current_product:
            if is_palindrome(current_product):
                palindromes.append(current_product)
            current_product -= current_number

        current_number -= 1

    return max(palindromes)


print(find_max_palindrome_product(100, 999))


