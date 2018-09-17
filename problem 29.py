distinct_numbers = []

for i in range(99):
    a = i + 2
    for j in range(99):
        b = j + 2
        if a ** b not in distinct_numbers:
            distinct_numbers.append(a ** b)

print(len(distinct_numbers))
