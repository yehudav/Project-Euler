def get_lis(bound, jump, first, first_jump):
    lis = []
    low_bound = bound // 10
    i = first
    while i < bound:
        if i >= low_bound and str(i)[2] != "0":
            lis.append(str(i))
        i += first_jump
        first_jump += jump
    return lis


def is_in(start, end, lis):
    start_with = False
    end_with = False
    for lisi in lis:
        if start_with:
            break
        for c in lisi:
            if c.startswith(start):
                start_with = True
                break
    for lisi in lis:
        if end_with:
            break
        for c in lisi:
            if c.endswith(end):
                end_with = True
                break
    return start_with and end_with


def narrow(lis, j):
    new_cur = []
    for i in lis[j]:
        if is_in(i[:2], i[2:], lis):
            new_cur.append(i)
    lis[0] = new_cur
    return lis


def find_set(bound):
    triangle = get_lis(bound, 1, 1, 2)
    squares = get_lis(bound, 2, 1, 3)
    penta = get_lis(bound, 3, 1, 4)
    hexa = get_lis(bound, 4, 1, 5)
    hepta = get_lis(bound, 5, 1, 6)
    octa = get_lis(bound, 6, 1, 7)

    lis = [triangle, squares, penta, hexa, hepta, octa]
    for i in range(6):
        lis = narrow(lis, i)
        print(lis[i])

    # print(len(triangle), len(squares), len(penta), len(hexa), len(hepta), len(octa))

    # print(8128 + 2882 + 8281 + 7326)


find_set(10000)
