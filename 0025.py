import euler_utils as eu


#
# class Fibonaci_first_n_digits_term_finder:  # todo refactor
#     def __init__(self):
#         self.fn_minus_2 = 1
#         self.fn_minus_1 = 1
#         self.index = 2
#         self.length = None
#
#     def get_first_n_digits_fibonacci(self, n=None):
#         self.length = n
#         while self.not_n_digits_long():
#             self.update_cur_term()
#         return self.index
#
#     def not_n_digits_long(self):
#         return len(str(self.fn_minus_1)) < self.length
#
#     def update_cur_term(self):
#         self.fn_minus_1 += self.fn_minus_2
#         self.fn_minus_2 = self.fn_minus_1 - self.fn_minus_2
#         self.index += 1


# finder = Fibonaci_first_n_digits_term_finder()
def get_index_of_first_fibonacci_term_with_n_digits(n):
    fib_seq = eu.get_fibonacci_sequence_until_value((10 ** n) - 1)
    return len(fib_seq)


if __name__ == "__main__":
    num_of_digits = 1000
    print(get_index_of_first_fibonacci_term_with_n_digits(num_of_digits))
    print(get_index_of_first_fibonacci_term_with_n_digits(num_of_digits) == 4782)
# print(finder.get_first_n_digits_fibonacci(1000))
