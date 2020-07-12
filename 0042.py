import euler_utils as eu
import math

"""
triangle num t_n = n(n+1)/2 -> 2*t_n / n ~= n + 1 
hence given a value x, we know at what n we get t_n > x
"""


def get_num_of_triangle_words(path):
    file = open(path)
    words_values = [get_word_value(word) for line in file for word in line.split(",")]
    max_triangle_num = math.ceil(math.sqrt(max(words_values) * 2))
    triangle_numbers = set(eu.get_triangle_nums_sequence_until_value(max_triangle_num))
    return sum(1 for i in words_values if i in triangle_numbers)


def get_word_value(word):
    return sum(ord(c) - ord('a') + 1 for c in word.lower() if c != '"')


if __name__ == "__main__":
    path = "file"
    print(get_num_of_triangle_words(path))
