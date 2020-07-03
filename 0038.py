def is_pandigital(num):
    if len(num) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in num:
            return False
    return True


lis = []
for i in range(1, 10000):
    st = ""
    a = i# todo refactor
    while len(st) < 9:
        st += str(a)
        a += i
    if is_pandigital(st):
        lis.append(int(st))

print(max(lis))
