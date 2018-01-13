"""     problem 21        """


import math

def is_palindrom(num):
    middle = math.floor(len(num))
    first_half = num[:middle:1]
    second_half = num[middle+1::-1]
    return first_half == second_half


sum_of_palidroms = 0

for i in range(1000000):
    decimal = str(i)
    binary = str(bin(i))[2:]

    if is_palindrom(decimal) and is_palindrom(binary):
        sum_of_palidroms += i

print(sum_of_palidroms)



