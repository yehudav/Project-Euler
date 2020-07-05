times = 0  # todo refactor

a = b = c = d = e = f = g = 200

while a >= 0:
    b = a
    a -= 200
    while b >= 0:
        c = b
        b -= 100
        while c >= 0:
            d = c
            c -= 50
            while d >= 0:
                e = d
                d -= 20
                while e >= 0:
                    f = e
                    e -= 10
                    while f >= 0:
                        g = f
                        f -= 5
                        while g >= 0:
                            g -= 2

                            times += 1
if __name__ == "__main__":
    print(times)
