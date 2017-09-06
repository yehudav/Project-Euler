

f1 = 1
f2 = 2
next_f = 0
even_sum = 0
sup = 4000000

while next_f < sup:
    next_f = f1 + f2
    f1 = f2
    f2 = next_f

    if (f1 % 2) == 0:
        even_sum += f1

print(even_sum)



