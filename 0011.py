# # todo refactor


def get_max_product_of_n_adjacent_numbers_in_matrix(path, n):
    matrix = build_matrix_from_file(path)
    return get_max_product_of_n_adjacent_numbers(matrix, n)


def build_matrix_from_file(path):
    file = open(path)
    return [list(map(int, line.split(" "))) for line in file]


def get_max_product_of_n_adjacent_numbers(matrix, n):
    max_of_rows = get_max_product_of_lines(matrix, n)
    max_of_cols = get_max_product_of_lines(get_cols(matrix), n)
    max_of_diagonals = get_max_product_of_lines(get_diagonals(matrix), n)
    return max(max(max_of_rows, max_of_cols), max_of_diagonals)


def get_max_product_of_lines(lines, n):
    return max(get_max_product_of_single_line(line, n) for line in lines)


def get_max_product_of_single_line(line, n):
    if len(line) < n:
        return get_max_product_of_n_numbers(line)
    return max(get_max_product_of_n_numbers(line[i:i + n]) for i in range(len(line) - n + 1))


def get_max_product_of_n_numbers(numbers):
    product = 1
    for i in numbers:
        product *= i
    return product


def get_cols(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def get_diagonals(matrix):
    return


if __name__ == "__main__":
    path = "C:\\Users\\yehud\\PycharmProjects\\muchwow\\file"
    n = 4
    print(get_max_product_of_n_adjacent_numbers_in_matrix(path, 4))
    print(get_max_product_of_n_adjacent_numbers_in_matrix(path, 4) == 3)
