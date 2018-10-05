class Hand:
    def __init__(self, description):
        self.hand = description
        self.values = [self.val(i[0]) for i in description]
        self.values.sort()
        self.different_values = len(set(self.values))
        self.suits = [i[1] for i in description]
        self.different_suits = len(set(self.suits))
        self.valll = sorted(self.values) + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if self.different_values == 4:
            self.valll[5] = 1
        if self.different_values == 3:
            if self.values.count(self.values[0]) == 3 or self.values.count(self.values[1]) == 3 or self.values.count(
                    self.values[2]) == 3:
                self.valll[7] = 1
            else:
                self.valll[6] = 1
        if self.different_values == 3:
            self.valll[6] = 1
        if self.straight() and self.different_suits > 1:
            self.valll[8] = 1
        if self.different_suits == 1:
            self.valll[9] = 1
        if self.different_values == 2:
            if self.values.count(self.values[0]) == 3 or self.values.count(self.values[1]) == 3 or self.values.count(
                    self.values[2]) == 3:
                self.valll[10] = 1
            else:
                self.valll[11] = 1
        if self.straight() and self.different_suits == 1:
            if self.values[0] == 10:
                self.valll[13] = 1
            else:
                self.valll[12] = 1

    def get_values(self):
        return self.values

    def get_values_num(self):
        return self.different_values

    def get_suits(self):
        return self.suits

    def get_suites_num(self):
        return self.different_suits

    def val(self, char):
        if char == "A":
            return 14
        if char == "K":
            return 13
        if char == "Q":
            return 12
        if char == "J":
            return 11
        return 10

    def straight(self):
        for i in range(4):
            if self.values[i] + 1 != self.values[i + 1]:
                return format(False)
        return True


def poker(path):
    player1_score = 0
    file = open(path, "r")
    for line in file:
        game = line.split(" ")
        player1_score += player1_game_score(game)
    return player1_score


def player1_game_score(game):
    p1 = Hand(game[:5])
    p2 = Hand(game[5:])
    return decider(p1.valll, p2.valll)


def decider(p1, p2):
    if p1 == []:
        return 0
    if p1[-1] > p2[-1]:
        return 1
    if p1[-1] < p2[-1]:
        return 0
    return decider(p1[:-1], p2[:-1])


print(poker("C:\\Users\\YehudaVaknin\\PycharmProjects\\untitled1\\file"))
