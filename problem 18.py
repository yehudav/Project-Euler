

"""     problem 18      """


def create_matrix(path):
    file = open(path, "r")

    matrix = []

    for line in file:
        line = (line[:-1]).split(" ")
        new_line = []
        for str in line:
            new_line.append(int(str))
        matrix.append(new_line)

    return matrix


def calculate_max_route_sum(path):
    matrix = create_matrix(path)
    cur_row = 0

    for row in matrix:
        if cur_row != 0:
            for i in range(len(row)):
                if i == 0:
                    row[i] += matrix[cur_row - 1][0]
                elif i == len(row) - 1:
                    row[i] += matrix[cur_row - 1][len(row) - 2]
                else:
                    row[i] += max(matrix[cur_row - 1][i], matrix[cur_row - 1][i - 1])

        cur_row += 1

    return max(matrix[len(matrix) - 1])


print(calculate_max_route_sum("file.txt"))
