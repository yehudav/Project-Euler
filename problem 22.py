# """     problem 21        """
#
#
# characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
#            20, 21, 22, 23, 24, 25, 26]
#
# path = "C:\\Users\\YehudaVaknin\\Desktop\\p022_names.txt"
#
# file = open(path, "r")
#
# names = []
#
#
# def char_value(c):
#     char = c.lower()
#     index = characters.index(char)
#     return numbers[index]
#
#
# def name_value(a_name):
#     val = 0
#
#     for char in a_name:
#         val += char_value(char)
#
#     return val
#
#
# for line in file:
#     line = line.split(',')
#
#     for name in line:
#         names.append(name[1:-1])
#
# names.sort()
#
# names_score = 0
#
# for i in range(5163):
#     names_score += (i + 1) * name_value(names[i])
#
# print(names_score)
#
#
#



"""     problem 22        """

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
           20, 21, 22, 23, 24, 25, 26]


def char_value(c):
    char = c.lower()
    index = characters.index(char)
    return numbers[index]


def name_value(a_name):
    val = 0

    for char in a_name:
        val += char_value(char)

    return val


def get_names_score(path):
    names = []
    number_of_names = 0
    names_score = 0
    file = open(path, "r")

    for line in file:
        line = line.split(',')
        for name in line:
            names.append(name[1:-1])
            number_of_names += 1

    names.sort()

    for i in range(number_of_names):
        names_score += (i + 1) * name_value(names[i])

    return names_score


print(get_names_score("file.txt"))
