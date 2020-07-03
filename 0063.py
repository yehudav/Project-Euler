def powes():
    sum = 0
    for i in range(4, 10):
        k = i
        j = 1
        while len(str(k)) == j:
            sum += 1
            j += 1
            k = k * i
    print(sum)


powes()
# todo refactor