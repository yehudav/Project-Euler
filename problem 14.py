class Foo:
    def __init__(self, bound):
        self.bound = bound + 1
        self.max_head = 0
        self.max_chain_length = 0
        self.cur_head = 0
        self.cur_num = 0
        self.cur_chain_length = 0

    def get_head_of_longest_chain_under_bound(self):
        for i in range(self.bound):
            self.cur_head = i
            self.get_cur_chain_length()
            self.update_max_length()
        return self.max_head

    def get_cur_chain_length(self):
        self.cur_chain_length = 0
        self.cur_num = self.cur_head
        while self.cur_num > 1:
            self.get_next_num_in_chain()
            self.cur_chain_length += 1

    def get_next_num_in_chain(self):
        if self.cur_num != ((self.cur_num >> 1) << 1):
            self.cur_num = self.cur_num << 1 + self.cur_num + 1
        else:
            self.cur_num = self.cur_num >> 1

    def update_max_length(self):
        if self.cur_chain_length > self.max_chain_length:
            self.max_chain_length = self.cur_chain_length
            self.max_head = self.cur_head


f = Foo(1000000)
print(f.get_head_of_longest_chain_under_bound())
