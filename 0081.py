def find_two_way_minimal_path_sum(path):  # todo refactor

    matrix = load_matrix(path)
    length = len(matrix[0])
    for j in range(1, length):
        matrix[0][j] += matrix[0][j - 1]
        matrix[j][0] += matrix[j - 1][0]
    i = 1
    while i < length:
        matrix[i][i] += min(matrix[i - 1][i], matrix[i][i - 1])
        for j in range(i + 1, length):
            matrix[i][j] += min(matrix[i][j - 1], matrix[i - 1][j])
            matrix[j][i] += min(matrix[j][i - 1], matrix[j - 1][i])
        i += 1
    return matrix[- 1][- 1]


def load_matrix(path):
    file = open(path)
    return [[int(i) for i in line.split(",")] for line in file]


if __name__ == "__main__":
    path = "C:\\Users\\yehud\\PycharmProjects\\muchwow\\file"
    print(find_two_way_minimal_path_sum(path))
    print(find_two_way_minimal_path_sum(path) == 427337)
