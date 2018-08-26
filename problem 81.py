"""         problem 81           """


def load_matrix(path):
    matrix = []
    file = open(path, "r")
    for line in file:
        row = line.split(",")
        row = [int(i) for i in row]
        matrix.append(row)
    print(matrix)
    return matrix


def two_way_minimal_path_sum(path):
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
    return matrix[length - 1][length - 1]


print(two_way_minimal_path_sum("C:\\Users\\YehudaVaknin\\PycharmProjects\\untitled1\\file"))
