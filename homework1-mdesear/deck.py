import card, random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", 
        "Jack", "Queen", "King", "Ace"]

class Deck:
    def __init__(self):
        self.deck = []
        self.graveyard = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(card.Card(suit, rank))

    def __str__(self):
        com_deck = ""
        for card in self.deck:
            com_deck += "\n" + card.__str__()
        return "The deck contains: " + com_deck

    def shuffle(self):
        random.shuffle(self.deck)

    # Used in the event that the deck is empty
    def reshuffle(self):
        for i in range(len(self.graveyard)):
            self.deck.append(self.graveyard[i])
        self.shuffle()
        self.graveyard = []
        print("\n===================================\nReshuffling graveyard into deck...\n===================================")

    def deal(self):
        if not self.deck:
            self.reshuffle()
        card = self.deck.pop()
        # Cards dealt out are reserved in the graveyard
        self.graveyard.append(card) 
        return card