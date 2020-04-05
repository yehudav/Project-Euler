digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def are_pandigital(sttr, digits):
    for d in digits:
        if d not in sttr:
            return False
    return True


pandigitals = []

for i in range(31434):

    for j in range(987654321):
        p = i * j
        if p > 987654321:
            break
        sttr = str(i) + str(j) + str(p)
        if len(sttr) > 9:
            break

        if are_pandigital(sttr, digits):
            pandigitals.append(p)

ls = list(set(pandigitals))

sum = 0
for k in ls:
    sum += k

print(sum)
