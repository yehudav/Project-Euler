class MinProductFinder:
    def __init__(self):
        self.min_product = None
        self.upper_bound = None
        self.factors = None

    def get_min_product(self, bound):
        self.upper_bound = bound + 1
        self.factors = []
        self.min_product = 1
        for j in range(2, self.upper_bound):
            self.get_next_factor(j)
        return self.min_product

    def get_next_factor(self, n):
        for i in self.factors:
            if n % i == 0:
                n //= i
            if n == 1:
                break
        if n != 1:
            self.factors.append(n)
            self.min_product *= n


min_product_finder = MinProductFinder()
print(min_product_finder.get_min_product(20))
