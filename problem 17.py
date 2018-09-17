hundreds = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
singles = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
thousand = "onethousand"
str = ""

for i in range(1, 1000):
    j = i % 100

    if i > 99:
        str += hundreds[(i // 100) - 1] + "hundred"
        if j != 0:
            str += "and"

    if j > 19:
        str += tens[(j // 10) - 1]
        if (j % 10) - 1 > -1:
            str += singles[(j % 10) - 1]
    elif j == 10:
        str += tens[0]
    elif j > 10 and j < 20:
        str += teens[(j % 10) - 1]
    else:
        if j > 0:
            str += singles[j - 1]

str += thousand

print(len(str))
