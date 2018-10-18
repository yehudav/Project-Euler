class MatrixMaxProductFinder:
    def __init__(self, path, product_length):
        self.matrix = []
        self.create_matrix_from_file(path)
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.product_len = product_length
        self.max_product = -float("inf")

    def create_matrix_from_file(self, path):
        file = open(path)
        for line in file:
            str_line = line.split(" ")
            int_line = list(map(int, str_line))
            self.matrix.append(int_line)

    def get_matrix_max_product(self):
        self.square_matrix_max_adjacent_product()
        return self.max_product

    def matrix_max_product(self):
        self.max_product_of_rows = self.matrix_rows_max_product()
        self.max_product_of_cols = self.matrix_cols_max_product()
        self.max_product_of_diagonals = self.square_matrix_diagonals_max_product()
        return self.max_product

    def rows_max_product(self):
        for row in self.matrix:
            max_rows_product = max(self.max_product, self.max_product(row))

    def cols_max_product(self):
        for col in range(self.cols_num):
            column = []
            for row in self.matrix:
                column.append(row[col])
            self.max_product = max(self.max_product, self.max_product(column))

    def down_left_diagonals_max_product(self):

        for i in range(matrix_len - adjacent_digits_number + 1):
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


    def square_matrix_diagonals_max_product(self:
        self.square_matrix_down_left_diagonals_max_product()
        self.square_matrix_up_right_diagonals_max_product()


    def max_product(self, line):
        max_product_of_line = 0
        while len(line) >= self.product_len:
            current_product = 1
            for i in range(self.product_len):
                current_product *= line[i]
            max_product_of_line = max(current_product, max_product_of_line)
            line = line[1:]
        return max_product_of_line

    def max_of_three(a, b, c):
        return max(a, max(b, c))


max_calculator = MatrixMaxProductFinder("C:\\Users\\YehudaVaknin\\PycharmProjects\\maini\\file", 4)
print(max_calculator.get_matrix_max_product())
