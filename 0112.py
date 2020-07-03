def get_bouncy_percent_num(percent):
    cur_percent = 0
    bouncy_num = 0
    i = 99
    while cur_percent != percent:
        i += 1
        if is_bouncy(i):
            bouncy_num += 1
        cur_percent = get_cur_percent(i, bouncy_num)
    return i

# todo refactor
def is_bouncy(n):
    return not is_dec(n) and not is_inc(n)


def is_dec(n):
    st = str(n)
    for j in range(len(st) - 1):
        if int(st[j]) < int(st[j + 1]):
            return False
    return True


def is_inc(n):
    st = str(n)
    for j in range(len(st) - 1):
        if int(st[j]) > int(st[j + 1]):
            return False
    return True


def get_cur_percent(number, bouncy_number):
    ratio = bouncy_number / (number)
    return ratio


print(get_bouncy_percent_num(0.99))
