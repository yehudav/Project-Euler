"""         problem 301           """


def calculate_nim_winnig_states(bound):
    count = 0
    for i in range(1, bound + 1):
        if state(i) == 0:
            count += 1
    return count


def state(n):
    two_n = n << 1
    three_n = n + two_n
    return n ^ two_n ^ three_n


print(calculate_nim_winnig_states(2 ** 30))
