VALUES = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,
            "Jack":10, "Queen":10, "King":10, "Ace":11}

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace_count = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += VALUES[card.rank]
        if card.rank == "Ace":
            self.ace_count += 1

    # Used to determine whether an ace should equal 11 or 1
    def ace_adjust(self):
        while self.value > 11 and self.ace_count:
            self.value -= 10    # If the value of the hand exceeds 11, then aces should equal 1
            self.ace_count -= 1