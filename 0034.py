import euler_utils as eu


def get_sum_of_nums_equal_to_sum_of_digits_factorial():
    factorions = []
    for i in range(3, eu.factorial(9)):
        if i == get_sum_of_digits_factorial(i):
            factorions.append(get_sum_of_digits_factorial(i))
    return sum(factorions)


def get_sum_of_digits_factorial(n):
    return sum(eu.factorial(int(d)) for d in str(n))


if __name__ == "__main__":
    print(get_sum_of_nums_equal_to_sum_of_digits_factorial())
