"""     problem 21        """
import math


def pandigital(num):
    st = str(num)
    for i in range(len(st)):
        if str(i+1) not in st:
            return False
    return True


primes = []

for p in range(10000000):
    primes.append(p)

sqr = int( math.sqrt(10000000) + 3)
for i in range(2, sqr):
    if primes[i] != 0:
        k = i + i
        while k < 10000000:
            primes[k] = 0
            k += i

maxi = 0
for j in primes:
    if j != 0:
        if pandigital(j) and j > maxi:
            maxi = j

print(maxi)