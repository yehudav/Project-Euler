

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


factorial_num = str(factorial(100))

sum_of_digits = 0

for digit in factorial_num:
    sum_of_digits += int(digit)

print(sum_of_digits)



