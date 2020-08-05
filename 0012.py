import math
import euler_utils as eu


# todo improve num_of_div speed
def get_first_triangle_num_with_n_divisors(n, primes_bound):
    cur = 1
    jmp = 2
    while eu.get_num_of_divisors(cur) <= n:
        cur += jmp
        jmp += 1
    return cur


#

if __name__ == "__main__":
    print(get_first_triangle_num_with_n_divisors(500, 500))
    print(get_first_triangle_num_with_n_divisors(500, 500) == 76576500)
