class Foo:
    def __init__(self, bound):
        self.bound = bound
        self.max_head = 0
        self.max_length = 0

    def get_head_of_longest_chain_under_bound(self):
        for i in range(self.bound):
            cur_chain_len = self.get_chain_length(i)
            self.update_max_length(cur_chain_len)
        return self.max_head

    def update_max_length(self, cur_chain_len):
        if cur_chain_len > self.max_length:
            self.max_length = cur_chain_len
            self.max_head = cur_chain_len

    def get_chain_length(self, head):
        chain_len = 0
        cur_num = head
        while cur_num > 1:
            cur_num = self.get_next_num_in_chain(cur_num)
            chain_len += 1
        return chain_len

    def get_next_num_in_chain(self, n):
        if n % 2 != 0:
            return n + n + n + 1
        else:
            return n >> 1


f = Foo(1000000)
print(f.get_head_of_longest_chain_under_bound())
