

num = 2520
primes = []

while num > 1:
    div = 0
    for i in range(20):
        if num % (i + 2) == 0:
            primes.append(i + 2)
            div = i + 2
            break
    num /= div

for j in range(10):
    number = j + 11
    for i in primes:
        if number % i == 0:
            number /= i

    primes.append(number)

for i in primes:
    num *= i

print(int(num))