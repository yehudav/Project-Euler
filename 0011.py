class MatrixMaxProductFinder:
    def __init__(self, path, product_length):
        self.matrix = []
        self.create_matrix_from_file(path)
        self.rows_num = len(self.matrix)
        self.cols_num = len(self.matrix[0])
        self.product_len = product_length
        self.max_product = -float("inf")

    def create_matrix_from_file(self, path):
        file = open(path)
        for line in file:
            str_line = line.split(" ")
            int_line = list(map(int, str_line))
            self.matrix.append(int_line)

    def get_matrix_max_product(self):
        self.matrix_max_product()
        return self.max_product

    def matrix_max_product(self):
        self.rows_max_product()
        self.cols_max_product()
        self.diagonals_max_product()
        return self.max_product

    def rows_max_product(self):
        for row in self.matrix:
            self.line_max_product(row)

    def cols_max_product(self):
        for col in range(self.cols_num):
            column = self.get_col(col)
            self.line_max_product(column)

    def get_col(self, i):
        col = []
        for row in self.matrix:
            col.append(row[i])
        return col

    def diagonals_max_product(self):
        self.down_right_diagonals_max_product()
        self.up_right_diagonals_max_product()

    def down_right_diagonals_max_product(self):
        for i in range(self.rows_num - self.product_len + 1):
            k = i
            diagonal_a = []
            diagonal_b = []

            for j in range(matrix_len - i):
                diagonal_a.append(m[k][j])
                diagonal_b.append(m[j][k])
                k += 1

            a_product = max_product(diagonal_a, adjacent_digits_number)
            b_product = max_product(diagonal_b, adjacent_digits_number)

            max_down_left_diagonals_product = max_of_three(max_down_left_diagonals_product, a_product, b_product)

    def up_right_diagonals_max_product(self):
        for i in range(matrix_len - adjacent_digits_number + 1):
            k = matrix_len - 1
            j = k - i
            diagonal_a = []
            diagonal_b = []

            for n in range(matrix_len - i):
                diagonal_a.append(m[k][n + i])
                diagonal_b.append(m[j][n])
                k -= 1
                j -= 1

            a_product = max_product(diagonal_a, adjacent_digits_number)
            b_product = max_product(diagonal_b, adjacent_digits_number)

            max_up_right_diagonals_product = max_of_three(max_up_right_diagonals_product, a_product, b_product)

    def line_max_product(self, line):
        products = len(line) - self.product_len
        for i in range(products):
            self.max_product = max(self.max_product, self.line_product(line[i:i + self.product_len]))

    def line_product(self, adjacent_nums):
        current_product = 1
        for n in adjacent_nums:
            current_product *= n
        return current_product


max_calculator = MatrixMaxProductFinder("C:\\Users\\YehudaVaknin\\PycharmProjects\\maini\\file", 4)
print(max_calculator.get_matrix_max_product())
