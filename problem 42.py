"""         problem 42           """

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
           20, 21, 22, 23, 24, 25, 26]

path = "C:\\Users\\YehudaVaknin\\Desktop\\p042_words.txt"


def char_value(c):
    char = c.lower()
    index = characters.index(char)
    return numbers[index]


def word_value(a_word):
    val = 0

    for char in a_word:
        val += char_value(char)

    return val


def triangle(n):
    return int((n * (n + 1)) / 2)


triangles = []

for i in range(45):
    triangles.append(triangle(i + 1))

file = open(path, "r")

words = []

for line in file:
    line = line.split(',')

    for word in line:
        words.append(word[1:-1])

triangles_sum = 0

for i in words:
    if word_value(i) in triangles:
        triangles_sum += 1

print(triangles_sum)
