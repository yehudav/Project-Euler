def calculate_nim_winnig_states(bound):
    count = 0
    for i in range(1, bound + 1):
        if is_winning_state(i) == 0:
            count += 1
    return count


def is_winning_state(n):
    return n ^ 2 * n ^ 3 * n == 0


if __name__ == "__main__":
    n = 2 ** 30
    print(calculate_nim_winnig_states(n))
# todo refactor
