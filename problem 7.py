

def is_prime(num, primes):
    for i in primes:
        if num % i == 0:
            return False
    return True

primes = [2]
cur = 3

while len(primes) < 10001:
    if is_prime(cur, primes):
        primes.append(cur)
    cur += 2

print(primes[-1])



