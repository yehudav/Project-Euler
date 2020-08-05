let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']


def dec(path):
    file = open(path, "r")
    values = [i for line in file for i in list(map(int, line.split(",")))]
    r = range(97, 123)
    keys = [[a, b, c] for a in r for b in r for c in r]
    possible = []
    for key in keys:
        extended_key = key * (len(values) // 3 + 1)
        decripted_msg = "".join([chr(i ^ j) for (i, j) in zip(extended_key, values)])
        if w(decripted_msg, 0.7):
            possible.append(("".join(list(map(chr, key))), decripted_msg))
    with open('C:\\Users\\yehud\\PycharmProjects\\muchwow\\res', 'w') as filehandle:
        for i in possible:
            a, b = i
            filehandle.write(a + "--" + b + "\n")
    return possible


def w(msg, char_precent):
    return sum(1 for i in msg if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 93) / len(msg) >= char_precent


if __name__ == "__main__":
    path = "C:\\Users\\yehud\\PycharmProjects\\muchwow\\file"
    a = dec(path)
    print(len(a))
    print(sum(ord(i) for i in "An extract taken from the introduction of one of Euler's most celebrated papers, \"De summis serierum reciprocarum\" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers."))

#todo