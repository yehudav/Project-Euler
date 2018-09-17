import itertools

a = list(map("".join, itertools.permutations("0123456789")))

sum = 0
for p in a:
    a = int(p[1:4]) / 2
    b = int(p[2:5]) / 3
    c = int(p[3:6]) / 5
    d = int(p[4:7]) / 7
    e = int(p[5:8]) / 11
    f = int(p[6:9]) / 13
    g = int(p[7:10]) / 17

    if int(a) == a and int(b) == b and int(c) == c and int(d) == d and int(e) == e and int(f) == f and int(g) == g:
        sum += int(p)

print(sum)
