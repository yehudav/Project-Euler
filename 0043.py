
# # todo refactor

"""
constraints - using rules of divisibility

* d2d3d4 is divisible by 2 -> d4 = {0,2,4,6,8}

* d3d4d5 is divisible by 3 -> d3 + d4 + d5 = n,  n % 3 == 0

* d4d5d6 is divisible by 5 -> d6 = {0, 5}

* d5d6d7 is divisible by 7 -> d5d6 - 2 * d7 = n, n % 7 == 0

* d6d7d8 is divisible by 11 -> d6 - d7 + d8 = n, n % 11 == 0

* d7d8d9 is divisible by 13 ->

* d8d9d10 is divisible by 17 -> d8d9 - 5 * d10 = n, n % 17
"""


def get_sum_of_0_to_9_pandigital_with_sub_string_divisibility():
    d2d3d4 = [str(i) if i >= 100 else '0' + str(i) for i in range(12, 1000, 2) if len(str(i)) == len(set(str(i)))]
    d2d3d4d5 = [i + str(d) for i in d2d3d4 for d in range(0, 10) if int(i[-2:] + str(d)) % 3 == 0]
    d2d3d4d5d6 = [i + str(d) for i in d2d3d4d5 for d in range(0, 10) if int(i[-2:] + str(d)) % 5 == 0]
    d2d3d4d5d6d7 = [i + str(d) for i in d2d3d4d5d6 for d in range(0, 10) if int(i[-2:] + str(d)) % 7 == 0]
    d2d3d4d5d6d7d8 = [i + str(d) for i in d2d3d4d5d6d7 for d in range(0, 10) if int(i[-2:] + str(d)) % 11 == 0]
    d2d3d4d5d6d7d8d9 = [i + str(d) for i in d2d3d4d5d6d7d8 for d in range(0, 10) if int(i[-2:] + str(d)) % 13 == 0]
    d2d3d4d5d6d7d8d9d10 = [i + str(d) for i in d2d3d4d5d6d7d8d9 for d in range(0, 10) if int(i[-2:] + str(d)) % 17 == 0]

    print(d2d3d4d5d6d7d8d9d10)
    print(len(d2d3d4d5d6d7d8d9d10))

if __name__ == "__main__":
    get_sum_of_0_to_9_pandigital_with_sub_string_divisibility()
