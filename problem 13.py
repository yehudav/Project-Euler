

# copy paste the number to a txt file

import math

file = open("file.txt", "r")

number = 0

for num in file:
    number += int(num)

digits = number

while len(str(digits)) > 10:
    digits = math.floor(digits / 10)
print(digits)



