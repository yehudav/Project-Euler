hundreds = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
singles = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
thousand = "onethousand"
str = ""


def get_num_of_letters_of_all_numbers_below(bound):  # todo refactor
    pass


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
    elif 10 < j < 20:
        str += teens[(j % 10) - 1]
    else:
        if j > 0:
            str += singles[j - 1]

str += thousand
if __name__ == "__main__":
    print(len(str))
    print(len(str) == 21124)
