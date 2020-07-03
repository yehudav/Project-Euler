import euler_utils as eu

"""
20 steps right, 20 steps down:
* each step right is the same - divide by 20! ways to place right steps in a row .
* each step down is the same - divide by 20! ways to place down steps in a row .
* for every possible placement of right steps there are 20! ways possible placement of down steps.
so 40! possible steps placements / 20! right * 20! down
"""
if __name__ == "__main__":
    print(eu.n_choose_k(40, 20))
