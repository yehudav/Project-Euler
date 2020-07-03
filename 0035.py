import math


def is_circ(num, liss):
    n = str(num)
    if "2" in n or "4" in n or "6" in n or "8" in n or "0" in n:
        return False
    for i in range(len(n)):
        n = n[1:] + n[0]
        nn = int(n)
        if nn not in liss:
            return False# todo refactor
    return True


primes = []

for i in range(1000000):
    if i == 0 or i == 2:
        primes.append(i)
    elif i / 2 == int(i / 2):
        primes.append(0)
    else:
        primes.append(i)

sqrt = int(math.sqrt(1000000)) + 1

for i in range(3, sqrt):
    k = i + i
    while k < 1000000:
        primes[k] = 0
        k += i

pprimes = sorted(list(set(primes)))[2:]


counter = 0
for p in pprimes:
    if is_circ(p, pprimes):
        counter += 1

print(counter + 1)
