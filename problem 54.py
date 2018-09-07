"""         problem 54           """


class Hand:
    def __init__(self, description):
        self.hand = description
        self.values = [self.val(i[0]) for i in description]
        self.different_values = len(set(self.values))
        self.suits = [self.val(i[1]) for i in description]
        self.different_suits = len(set(self.suits))

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
            return 13
        if char == "K":
            return 12
        if char == "Q":
            return 11
        if char == "J":
            return 10
        return int(char)


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
    return decider(p1, p2)


def decider(p1, p2):
    if royal(p1, p2):
        return 1 + sf(p1, p2) + four(p1, p2) + full(p1, p2) + flush(p1, p2) + straight(p1, p2) + \
    three(p1, p2) + _2pair(p1, p2) + pair(p1, p2) + high(p1, p2)


def draw(p1, p2):
    a = sorted(p1.get_values())
    b = sorted(p2.get_values())
    for i in range(le)

def royal(p1, p2):
    is_royal_1 = p1.get_suites_num() == 1 and min(p1.get_values()) == 10 and p1.get_values_num() == 5
    is_royal_2 = p2.get_suites_num() == 1 and min(p2.get_values()) == 10 and p2.get_values_num() == 5
    if is_royal_1 and is_royal_2:
        return draw(p1, p2)
    if is_royal_1 and not is_royal_2:
        return 1
    if is_royal_1 and is_royal_2:
        return draw(p1, p2)


poker()
