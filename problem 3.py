"""         problem 3           """

def divide_or_return(num):

def get_prime_factors(num):
    divisors = {1}
    cur = 2
    current_unknown_factors_product = num

    while current_unknown_factors_product > 1:
        if current_unknown_factors_product % cur == 0:
            current_unknown_factors_product /= cur
            divisors.add(cur)

        else:
            cur += min(cur - 1, 2)

    return divisors


def find_max_prime_factor(num):
    divisors = get_prime_factors(num)
    return max(divisors)


print(find_max_prime_factor(600851475143))
