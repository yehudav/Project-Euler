def get_max_path_sum(path):
    matrix = create_matrix_from_file(path)
    for i in range(1, len(matrix)):
        update_cur_row(matrix, i)
    return max(matrix[- 1])


def update_cur_row(matrix, cur_row):
    prev_row = cur_row - 1
    matrix[cur_row][0] += matrix[prev_row][0]
    matrix[cur_row][-1] += matrix[prev_row][- 1]
    for i in range(1, len(matrix[cur_row]) - 1):
        matrix[cur_row][i] += max(matrix[prev_row][i], matrix[prev_row][i - 1])


def create_matrix_from_file(path):
    file = open(path)
    return [[int(num) for num in line.split(" ")] for line in file]


if __name__ == "__main__":
    print(get_max_path_sum("file"))
