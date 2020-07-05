def get_num_of_distinct_powers_in_range(lower_bound, upper_bound):
    pow_range = range(lower_bound, upper_bound + 1)
    return len({a ** b for a in pow_range for b in pow_range})


if __name__ == "__main__":
    lower_bound = 2
    upper_bound = 100
    print(get_num_of_distinct_powers_in_range(lower_bound, upper_bound))
