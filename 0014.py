import euler_utils as eu


class LongestCollatzSequence:
    def __init__(self):
        self.dic = None
        self.bound = None

    def get_longest_chain_head_under_bound(self, bound):
        if bound < 2:
            raise ValueError
        self.bound = bound
        self.dic = {i: 0 for i in range(1, self.bound)}
        self.calculate_chains()
        return self.get_longest_chain_head()

    def calculate_chains(self):
        for i in range(2, self.bound):
            self.calculate_chain_length(i)

    def calculate_chain_length(self, head):
        chain, last = self.get_empty_values_in_chain(head)
        self.update_empty_values_in_chain(chain, last)
        return self.dic[head]

    def get_empty_values_in_chain(self, cur):
        chain = []
        while cur != 1 and self.dic[cur] == 0:
            chain.append(cur)
            cur = self.get_next_num_in_chain(cur)
            if cur not in self.dic:
                self.dic[cur] = 0
        return chain, cur

    def update_empty_values_in_chain(self, chain, cur):
        for i in chain[::-1]:
            self.dic[i] = self.dic[cur] + 1
            cur = i

    def get_next_num_in_chain(self, n):
        if eu.is_odd(n):
            return 3 * n + 1
        return n >> 1

    def get_longest_chain_head(self):
        max_len_head = 1
        for key in self.dic:
            if self.dic[key] > self.dic[max_len_head]:
                max_len_head = key
        return max_len_head


if __name__ == "__main__":
    n = 1000000
    longest_collatz_seq = LongestCollatzSequence()
    print(longest_collatz_seq.get_longest_chain_head_under_bound(n))
