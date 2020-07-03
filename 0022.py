def get_names_score(path):
    return get_names_score_by_lex_order(get_names_in_file(path))


def get_names_in_file(path):
    file = open(path)
    return [name for line in file for name in get_names_in_line(line)]


def get_names_in_line(line):
    return [name for name in line.replace('"', "").split(',')]


def get_names_score_by_lex_order(names):
    names.sort()
    return sum((i + 1) * get_name_value(names[i]) for i in range(len(names)))


def get_name_value(name):
    return sum(get_char_value(char) for char in name)


def get_char_value(c):
    return ord(c) - ord("A") + 1


if __name__ == "__main__":
    print(get_names_score("file"))
