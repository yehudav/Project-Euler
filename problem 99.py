"""         problem 99           """


def load_bases_and_exponents(path):
    file = open(path, "r")
    bases_and_exps_pairs = []
    line_num = 0
    for pair in file:
        base, exp = pair
        bases_and_exps_pairs.append((int(base), int(exp), line_num))
        line_num += 1
    return bases_and_exps_pairs


def decide(a, b):


def get_max_base(pair1, pair2):
    if pair1[0] <= pair2[0] and pair1[1] <= pair2[1]:
        return pair2
    if pair1[0] >= pair2[0] and pair1[1] >= pair2[1]:
        return pair1
    return decide(pair1, pair2)


def get_max_numeric_line_num(path):
    bases = load_bases_and_exponents(path)
    max_base = bases[0]
    for pair in bases:
        max_base = get_max_base(max_base, pair)
    return max_base[2]
