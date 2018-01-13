"""     problem 21        """


import math


def div_sum(number):
    divs_sum = 0
    bound = int(math.floor(number / 2))

    for i in range(bound):
        if number % (i + 1) == 0:
            divs_sum += i + 1

    return divs_sum


abundant_numbers = []
abundant_numbers_sum = []
j = 12

while j < 28134:
    if div_sum(j) > j:
        abundant_numbers.append(j)

    j += 1

sum_of_non_abundant = int((28123 * 28124) / 2)

for num_a in abundant_numbers:
    for num_b in abundant_numbers:
        abundant_numbers_sum.append(num_a + num_b)

abundant_numbers_sum_no_duplicates = list(set(abundant_numbers_sum))

for num in abundant_numbers_sum_no_duplicates:
    if num < 28124:
        sum_of_non_abundant -= num

print(sum_of_non_abundant)



