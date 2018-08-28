"""         problem 54           """


class Card:
    def __init__(self, description):
        self.value = self.val(description[0])
        self.suit = description[1]

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

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


class Hand:
    def __init__(self, cards):
        self.high_card = None
        self.one_pair = None
        self.two_pairs = None
        self.three_of_a_kind = None
        self.straight = None
        self.flush = None
        self.full_house = None
        self.four_of_a_kind = None
        self.straight_flush = None
        self.royal_flush = None
        self.values = []
        self.cards = []
        for d in cards:
            card = Card(d)
            self.cards.append(card)
            self.values.append(card.get_value())
        self.values.sort()

        self.high_card = max(self.values)
        for v in self.values:
            if self.values.count(v) == 4:
                self.four_of_a_kind = v
                break
            if self.values.count(v) == 3:
                self.four_of_a_kind = v
                break

def player1_game_score(game):
    player1_hand = Hand(game[:5])
    player2_hand = Hand(game[5:])


def poker(path):
    player1_score = 0
    file = open(path, "r")
    for line in file:
        game = line.split(" ")
        player1_score += player1_game_score(game)
    return player1_score
