

def multiply(div):
    num = 1
    for n in div:
        num *= n
    return num


def find_prime_factor(num, prime):
    while prime < num:
        if num / prime == 1:
            return num

        if num % prime == 0:
            return prime

        prime += 2
    return 1

divisors = [1]
number = 600851475143
p = 3
current = number

while multiply(divisors) < number:
    q = find_prime_factor(current, p)

    if q != 1:
        current /= q
        divisors.append(q)

    else:
        divisors.append(int(current))
        break

print(max(divisors))



