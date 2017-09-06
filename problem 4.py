

def is_palindrome(num):
    num = str(num)
    half1 = num[0:3]
    half2 = num[5] + num[4] + num[3]
    return half1 == half2


numbers = []
palindromes = []

for i in range(100):
    numbers.append([999 * (999 - i), 999 - i])

for j in range(100):
    for i in numbers:
        if is_palindrome(i[0]):
            palindromes.append(i[0])
        i[0] -= i[1]

print(max(palindromes))



