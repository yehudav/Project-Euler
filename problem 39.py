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

print(max(maxi_list))
print(maxi_list.index(4))
