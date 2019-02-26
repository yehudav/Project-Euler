def get_distinct_powers_in_range(lower_bound, upper_bound):
    upper_bound = upper_bound + 1
    all_powers = get_all_powers(lower_bound, upper_bound)
    return get_distinct_powers_num(all_powers)


def get_all_powers(lower_bound, upper_bound):
    all_powers = []
    for a in range(lower_bound, upper_bound):
        for b in range(lower_bound, upper_bound):
            all_powers.append(a ** b)
    return all_powers


def get_distinct_powers_num(numbers):
    return len(set(numbers))


print(get_distinct_powers_in_range(2, 100))
