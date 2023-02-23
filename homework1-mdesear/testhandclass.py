import card, hand, random, unittest

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", 
        "Jack", "Queen", "King", "Ace"]
VALUES = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,
            "Jack":10, "Queen":10, "King":10, "Ace":11}

class TestHandClass(unittest.TestCase):
    def test_add_hand(self):
        testCard = card.Card(random.choice(SUITS), RANKS[random.randrange(12)])
        testHand = hand.Hand()

        testHand.add_card(testCard)

        self.assertEqual(testHand.value, VALUES[testCard.rank])

    def test_add_ace(self):
        testCard = card.Card(random.choice(SUITS), RANKS[12])
        testHand = hand.Hand()

        testHand.add_card(testCard)

        self.assertEqual(testHand.value, 11)
        self.assertEqual(testHand.ace_count, 1)

    def test_ace_no_adjust(self):
        testAce = card.Card(random.choice(SUITS), "Ace")
        testHand = hand.Hand()

        testHand.add_card(testAce)
        testHand.ace_adjust()

        self.assertEqual(testHand.value, 11)

    def test_ace_adjust(self):
        testAce = card.Card(random.choice(SUITS), "Ace")
        testKing = card.Card(random.choice(SUITS), "King")
        testTwo = card.Card(random.choice(SUITS), "2")
        testHand = hand.Hand()

        testHand.add_card(testAce)
        testHand.add_card(testKing)
        testHand.add_card(testTwo)
        testHand.ace_adjust()

        self.assertEqual(testHand.value, 13)

if __name__ == "__main__":
    unittest.main()