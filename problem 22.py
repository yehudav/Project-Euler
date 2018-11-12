def get_names_score(path):
    names = get_names(path)
    return get_names_score_by_lex_order(names)


def get_names(path):
    names = []
    file = open(path, "r")
    for line in file:
        names += get_names_in_line(line)
    return names


def get_names_in_line(line):
    names_in_line = []
    line = line.replace('"', "").split(',')
    for name in line:
        names_in_line.append(name)
    return names_in_line


def get_names_score_by_lex_order(names):
    names_score = 0
    names.sort()
    for i in range(len(names)):
        names_score += (i + 1) * name_value(names[i])
    return names_score


def name_value(name):
    val = 0
    for char in name:
        val += char_value(char)
    return val


def char_value(c):
    char = c.lower()
    return ord(char) - ord("a") + 1


print(get_names_score("C:\\Users\\YehudaVaknin\\PycharmProjects\\maini\\file"))
