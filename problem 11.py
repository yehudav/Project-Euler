def max_of_three(a, b, c):
    return max(a, max(b, c))


def max_product(line, adjacent_digits_num):
    max_product_of_line = 0

    while len(line) >= adjacent_digits_num:
        current_product = 1

        for i in range(adjacent_digits_num):
            current_product *= int(line[i])

        max_product_of_line = max(current_product, max_product_of_line)

        line = line[1:]

    return max_product_of_line


def create_matrix_from_file(path):
    file = open(path)
    matrix = []

    for line in file:
        str_numbers = line.split(" ")
        matrix.append(str_numbers)

    return matrix


def matrix_rows_max_product(m, adjacent_digits_number):
    max_rows_product = 0

    for row in m:
        max_rows_product = max(max_rows_product, max_product(row, adjacent_digits_number))

    return max_rows_product


def matrix_cols_max_product(m, adjacent_digits_number):
    cols_num = len(m[0])
    max_cols_product = 0

    for col in range(cols_num):
        column = []
        for row in m:
            column.append(row[col])

        max_cols_product = max(max_cols_product, max_product(column, adjacent_digits_number))

    return max_cols_product


def square_matrix_down_left_diagonals_max_product(m, adjacent_digits_number, matrix_len):
    max_down_left_diagonals_product = 0

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

    return max_down_left_diagonals_product


def square_matrix_up_right_diagonals_max_product(m, adjacent_digits_number, matrix_len):
    max_up_right_diagonals_product = 0

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

    return max_up_right_diagonals_product


def square_matrix_diagonals_max_product(m, adjacent_digits_number):
    matrix_length = len(m)

    max_down_left = square_matrix_down_left_diagonals_max_product(m, adjacent_digits_number, matrix_length)
    max_up_right = square_matrix_up_right_diagonals_max_product(m, adjacent_digits_number, matrix_length)

    return max(max_down_left, max_up_right)


def square_matrix_max_adjacent_product(matrix, adjacent_digits_number):
    max_product_of_rows = matrix_rows_max_product(matrix, adjacent_digits_number)
    max_product_of_cols = matrix_cols_max_product(matrix, adjacent_digits_number)
    max_product_of_diagonals = square_matrix_diagonals_max_product(matrix, adjacent_digits_number)

    return max_of_three(max_product_of_rows, max_product_of_cols, max_product_of_diagonals)


print(square_matrix_max_adjacent_product(create_matrix_from_file("file.txt"), 4))
