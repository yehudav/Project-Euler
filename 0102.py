def oa(x1, y1, x2, y2):
    k = 0.5 * (x1 * y2 - x2 * y1)

    if k < 0:
        return -1
    if k > 0:
        return 1
    return 0

# todo refactor
def mi(path):
    file = open(path, "r")
    lis = []
    sum = 0
    for line in file:
        x1, y1, x2, y2, x3, y3 = line.split(",")
        val = oa(int(x1), int(y1), int(x2), int(y2)) + oa(int(x2), int(y2), int(x3), int(y3)) + oa(int(x3), int(y3),
                                                                                                   int(x1), int(y1))
        if abs(val) == 3:
            sum += 1
    return sum


print(mi("C:\\Users\\YehudaVaknin\\PycharmProjects\\untitled1\\file"))
