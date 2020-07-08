import math


def find_sqr(format):
    upper_sqr = math.ceil(math.sqrt(int(format.replace("_", "9"))))
    lower_sqr = math.floor(math.sqrt(int(format.replace("_", "0"))))
    print(upper_sqr - lower_sqr)
    for i in range(lower_sqr, upper_sqr):
        cur = str(i ** 2)
        if format[0] == cur[0] and format[2] == cur[2] and format[4] == cur[4] and format[6] == cur[6] and format[8] == \
                cur[8] and format[10] == cur[10] and format[12] == cur[12] and format[14] == cur[14] and format[16] == \
                cur[16] and format[18] == cur[18]:
            print(int(math.sqrt(int(cur))))
            exit(0)


# todo refactor

print(find_sqr("1_2_3_4_5_6_7_8_9_0"))

"""took 5 minutes - not good """  # todo
