

# a^2 + b^2 = c^2  ,  a + b + c = 1000  ,  a < b < c

# a + b + c = 1000  ->  c = 1000 - a - b  |^2  ->

# a^2 + b^2 + 2ab = 1000^2 + c^2 - 2000c  ->

# a^2 + b^2 + 2ab = 1000^2 + a^2 + b^2 - 2000c   | - a^2 - b^2   ->

# 2ab = 1000^2 - 2000c | / 2000 ->  ab / 1000 = 500 - (1000 - a - b) = a + b - 500



for a in range(1000):
    for b in range(1000):
        if ((a * b) / 1000) == (a + b - 500) and a != 0 and b != 0 and a < b:
            print(a * b * (1000 - a - b))
            break


