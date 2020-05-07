import util


def get_lcm_of_range_n(n):
    cur_lcm = 1
    for i in range(1, n + 1):
        cur_lcm = i * cur_lcm // util.gcd(cur_lcm, i)
    return cur_lcm


if __name__ == "__main__":
    n = 20
    print(get_lcm_of_range_n(20))
