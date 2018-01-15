"""         problem 3           """


def find_max_prime_factor(num):
    divisors = {1}
    current_candidate_prime = 2
    current_unknown_factors_product = num

    while current_unknown_factors_product > 1:
        if current_unknown_factors_product % current_candidate_prime == 0:
            current_unknown_factors_product /= current_candidate_prime
            divisors.add(current_candidate_prime)

        elif current_candidate_prime > 2:
            current_candidate_prime += 2

        else:
            current_candidate_prime += 1

    return max(divisors)


print(find_max_prime_factor(600851475143))
