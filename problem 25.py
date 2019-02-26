class Fibonaci_first_n_digits_term_finder:
    def __init__(self):
        self.fn_minus_2 = 1
        self.fn_minus_1 = 1
        self.index = 2
        self.length = None

    def get_first_n_digits_fibonacci(self, n=None):
        self.length = n
        while self.not_n_digits_long():
            self.update_cur_term()
        return self.index

    def not_n_digits_long(self):
        return len(str(self.fn_minus_1)) < self.length

    def update_cur_term(self):
        self.fn_minus_1 += self.fn_minus_2
        self.fn_minus_2 = self.fn_minus_1 - self.fn_minus_2
        self.index += 1


finder = Fibonaci_first_n_digits_term_finder()
print(finder.get_first_n_digits_fibonacci(1000))
