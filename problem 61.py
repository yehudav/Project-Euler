"""         problem 61           """


def get_lis(bound, jump, first, first_jump):
    lis = []
    low_bound = bound // 10
    i = first
    while i < bound:
        if i >= low_bound:
            lis.append(str(i))
        i += first_jump
        first_jump += jump
    return lis


def narrow(cur, prev, next):
    aaa = set()
    for a in cur:
        for b in next:
            if a[2:] == b[:2]:
                aaa.add(a)
                break
    bbb = set()
    for a in prev:
        for b in aaa:
            if a[2:] == b[:2]:
                bbb.add(b)
                break
    return bbb


def find_set(bound):
    triangle = get_lis(bound, 1, 1, 2)
    squares = get_lis(bound, 2, 1, 3)
    penta = get_lis(bound, 3, 1, 4)
    hexa = get_lis(bound, 4, 1, 5)
    hepta = get_lis(bound, 5, 1, 6)
    octa = get_lis(bound, 6, 1, 7)

    # triangle = narrow(triangle, octa, squares)
    # squares = narrow(squares, triangle, penta)
    # penta = narrow(penta, squares, hexa)
    # hexa = narrow(hepta, penta, hepta)
    # # hepta = narrow(hepta, hexa, octa)
    # # octa = narrow(octa, hepta, triangle)
    #
    # print(triangle)
    # print(squares)
    # print(penta)
    # print(hexa)
    # print(hepta)
    # print(octa)
    # print(7480 + 4774 + 2147 +1521 + 5815 )


find_set(10000)
