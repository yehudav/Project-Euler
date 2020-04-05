import math

lis = []

for i in range(1000000):
    div = i / 2
    if div != int(div):
        lis.append(i)
    else:
        lis.append(0)

sqr = int(math.sqrt(1000000) + 3)

for i in range(3, sqr):
    j = lis[i]
    if j != 0:
        k = j * 2
        while k < 1000000:
            lis[k] = 0
            k += j


def truncable(pp):
    strr = str(pp)
    a = strr
    b = strr
    while len(a) > 1:
        a = a[1:]
        if lis[int(a)] == 0 and int(a) != 2:
            return False
    while len(b) > 1:
        b = b[:-1]
        if lis[int(b)] == 0 and int(b) != 2:
            return False
    return True


trunc = []
for p in lis:
    if p < 23:
        continue
    if truncable(p):
        trunc.append(p)

sum = 0
i = 1
for pp in trunc:
    stt = str(pp)
    if stt.startswith("1") == False and stt.endswith("1") == False:
        print(pp, i)
        sum += int(pp)
        i += 1
print(sum)
