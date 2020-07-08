import math

maxi_list = []
for i in range(1001):
    maxi_list.append(0)

for s in range(1000):
    for t in range(1000):
        if math.gcd(s, t) == 1:
            a = 2 * s * t
            b = abs(s * s - t * t)
            c = s * s + t * t
            index = a + b + c
            if index <= 1000 and a * a + b * b == c * c:
                maxi_list[index] += 1
# todo refactor
print(max(maxi_list))
print(maxi_list.index(4))

#
# def get_max_num_of_pythagorean_triplets_for_given_parameter(p):
#     max_num = -1
#     for i in range(1, p + 1):
#         max_num = max(max_num, get_num_of_pythagorean_triplets_with_given_sum(i))
#     return max_num
#
#
# def get_num_of_pythagorean_triplets_with_given_sum(given_sum):
#     """
#     https://en.wikipedia.org/wiki/Pythagorean_triple :
#     a = m^2 - n^2, b = 2mn, c = m^2 + n^2,
#     a + b + c = 2m^2 + 2mn = 1000, m^2 + mn < x^2 = 500
#     """
#     num = 0
#     half_of_given_sum = given_sum / 2
#     bound = round(math.sqrt(half_of_given_sum)) + 1
#     for m in range(1, bound):
#         for n in range(1, bound):
#             if m ** 2 + m * n == half_of_given_sum:
#                 num += 1
#     return num
#
#
# if __name__ == "__main__":
#     p = 1000
#     print(get_max_num_of_pythagorean_triplets_for_given_parameter(p))
