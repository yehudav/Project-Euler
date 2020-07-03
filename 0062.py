def get_cubes(bound):
    lis = []
    cur = 1
    cur_jmp = 7
    next = 12
    while cur <= bound:
        lis.append(cur)
        cur += cur_jmp
        cur_jmp += next
        next += 6
    return lis


def co(n):
    lisi = [0 for i in range(10)]
    s = str(n)
    for c in s:
        lisi[int(c)] += 1
    return lisi
# todo refactor

lis = get_cubes(30000 ** 3)
new_lis = []
for i in lis:
    new_lis.append(co(i))
cube = None
for i in range(13655, len(new_lis)):
    val = 0
    for j in range(i, len(new_lis)):
        if new_lis[i] == new_lis[j]:
            val += 1
    if val == 5:
        print(i)
        exit(0)
