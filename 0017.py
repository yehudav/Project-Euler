def get_num_of_letters_of_all_numbers_up_to_1000():
    dic = get_len_of_numbers_up_to_1000()
    return sum(get_number_len(i, dic) for i in range(1, 1001))


def get_number_len(i, dic): # todo refactor
    length = 0
    for
        if i in dic:
            return dic[i]

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


def get_len_of_numbers_up_to_1000():
    return {1: len("one"), 2: len("two"), 3: len("three"), 4: len("four"), 5: len("five"), 6: len("six"),
            7: len("seven"), 8: len("eight"), 9: len("nine"), 10: len("ten"), 11: len("eleven"), 12: len("twelve"),
            13: len("thirteen"), 14: len("fourteen"), 15: len("fifteen"), 16: len("sixteen"), 17: len("seventeen"),
            18: len("eighteen"), 19: len("nineteen"), 20: len("twenty"), 30: len("thirty"), 40: len("forty"),
            50: len("fifty"), 60: len("sixty"), 70: len("seventy"), 80: len("eighty"), 90: len("ninety"),
            100: len("hundred"), 1000: len("thousand")}


if __name__ == "__main__":
    print(get_num_of_letters_of_all_numbers_up_to_1000())
    print(get_num_of_letters_of_all_numbers_up_to_1000() == 21124)
