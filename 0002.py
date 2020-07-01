import euler_utils as eu


def sum_of_even_fibonacci_numbers(bound):
    fibonacci_sequence = eu.get_fibonacci_sequence_until_value(bound)
    return sum(i for i in fibonacci_sequence if eu.is_even_num(i))


if __name__ == "__main__":
    n = 4000000
    print(sum_of_even_fibonacci_numbers(n))
