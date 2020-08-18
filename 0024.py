import euler_utils as eu

"""

class ith_permutation_data:
    def __init__(self, elements):
        self.elements = elements
        self.n = len(elements)
        self.cur_sum = 0
        self.i_perm = ""
        self.cur_fact = eu.factorial(self.n)"""


# todo refactor
def get_ith_permutation(elements, i):
    i_perm, n, cur_sum, cur_fact = "", len(elements), 0, eu.factorial(len(elements))
    for k in range(n, 1, -1):
        cur_fact //= k
        for e in elements:
            if cur_sum + cur_fact >= i:
                i_perm += str(e)
                elements.remove(e)
                break
            cur_sum += cur_fact
    return int(i_perm + str(elements[0]))


print(get_ith_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))
print(get_ith_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000) == 2783915460)

"""
import euler_utils as eu


# todo refactor
class PermutationCounter:
    def __init__(self):
        self.used_elements = None
        self.i_permutation = ""
        self.n = None
        self.cur_sum = 0
        self.elements = None
        self.cur_factorial = None

    def reset_state(self, elements):
        self.i_permutation = ""
        self.n = len(elements)
        self.cur_sum = 0
        self.elements = elements
        self.cur_factorial = eu.factorial(self.n)
        self.used_elements = set()

    def get_ith_permutation_of_elements(self, elements, i):
        self.reset_state(elements)
        return self.build_ith_permutation(i)

    def build_ith_permutation(self, i):
        for k in range(self.n, 1, -1):
            self.cur_factorial //= k
            self.get_cur_digit_of_permutation(i)
        return self.i_permutation + str((set(self.elements) - self.used_elements).pop())

    def get_cur_digit_of_permutation(self, i):
        for e in self.elements:
            if e not in self.used_elements:
                if self.cur_sum + self.cur_factorial >= i:
                    self.i_permutation += str(e)
                    self.used_elements.add(e)
                    break
                self.cur_sum += self.cur_factorial


counter = PermutationCounter()
print(counter.get_ith_permutation_of_elements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))
print(counter.get_ith_permutation_of_elements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000) == '2783915460')
"""
