import util


def sum_of_even_fibonacci_numbers(bound):
    fibonacci_sequence = util.get_fibonacci_sequence_until_value(bound)
    return sum(i for i in fibonacci_sequence if util.is_even_num(i))


if __name__ == "__main__":
    n = 4000000
    print(sum_of_even_fibonacci_numbers(n))
