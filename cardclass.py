class Card():
    def __init__(self,suit,number):
        self.suit = 0
        self.number = 0 
        self.value = 0
class Deck():
    def __init__(self):
        self.Cards = []
        self.assign()
    def assign (self):
        for suit in ['heart', 'club', 'spade', 'diamond']:
            for number in range(0,12)
                self.Cards.append(Card(suit, number))

