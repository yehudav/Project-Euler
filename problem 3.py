"""         problem 3           """

def divide_or_return(num):

def get_prime_factors(num):
    divisors = []
    cur_factor = 2
    cur_val = num

    while cur_val > 1:
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
